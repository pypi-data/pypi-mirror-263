"""Access the Google SERPAPI API via SERP API.
"""

import contextlib
import datetime
import logging
import uuid

from tk_core.common.de_service import DeService
from tk_core.common.hasher import hash_from_dict, uri_string_from_dict
from tk_core.core.models import TerakeetMetadata
from tk_core.serp_api.models import SERPAPITrends
from tk_core.serp_api.serp import SERPAPI


def get_trend_client(params: SERPAPITrends | dict, request_metadata: TerakeetMetadata | dict | None = None) -> SERPAPI:
    """Creates a new instance of the SERPAPI class"""
    # convert to pydantic model if dict
    if isinstance(params, dict):
        params = SERPAPITrends.model_validate(params)

    # convert to pydantic model if dict
    if isinstance(request_metadata, dict):
        request_metadata = TerakeetMetadata.model_validate(request_metadata)

    return SERPAPI(engine="google_trends", params=params, metadata=request_metadata)


class Trends:
    def __init__(self, params: SERPAPITrends, engine: str = "google") -> None:
        self.params = params
        self.params.engine = engine
        self.run_date = f"{datetime.datetime.now():%Y-%m-%d}"
        self.executed_at = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"
        self.results = {}
        self.de = DeService("serpapi_trend")

    def prepare_hash_and_metadata(self) -> None:
        to_hash = self.params.model_dump()
        self.uri = uri_string_from_dict(to_hash)
        self.query_hash = hash_from_dict(to_hash)
        self.execution_id = f"{self.query_hash}/{self.run_date}"
        self.metadata = {
            "application": self.params.tk_metadata.application,
            "processed_by": "tk_core_serp_api_trend",
            "request_id": str(uuid.uuid1()),
        }
        # if there are tags in the request, add them to the metadata
        with contextlib.suppress(AttributeError):
            self.metadata["tags"] = self.params.tags

    def get_data(self) -> dict:
        self.prepare_hash_and_metadata()
        if self.de.execution_cache_exists(self.query_hash):
            logging.info(f"cache hit for {self.query_hash}")
            self.results = self.de.load_execution_cache(self.query_hash)
        else:
            logging.info(f"cache miss for {self.execution_id}")
            trends_client = SERPAPI(engine="google_trends", params=self.params.model_dump(), metadata=self.metadata)
            self.results = trends_client.make_request()
            self.results["execution_id"] = self.execution_id
            self.results["run_date"] = self.run_date
            self.results["query_hash"] = self.query_hash
            self.results["uri"] = self.uri
            self.results["metadata"] = self.metadata

            self.de.store_execution_s3_cache(self.results)
            self.de.store_response_for_snowpipe(self.results)

        return self.results
