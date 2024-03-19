import uuid

import pandas as pd

from tk_core.common.dictionary import subset_dict
from tk_core.common.hasher import hash_from_dict
from tk_core.core.models import TerakeetRequestModel, TerakeetResponseMetadata
from tk_core.core.request_id import PostInitMetaclass
from tk_core.snowkeet import Snowkeet


class TerakeetRequest(metaclass=PostInitMetaclass):
    def __init__(self, params: TerakeetRequestModel) -> None:
        # set the parameters
        self.params = params
        # extract metadata
        self.metadata = params.tk_metadata
        # build request hash from params
        self.request_hash = self.make_request_hash(f"tk_core.{type(self).__name__}", self.params.model_dump())

    def __post_init__(self) -> None:
        """
        because of the metaclass, this is called after __init__
        This is used incase a future class needs to override the __init__ method
        We still need these things to take place
        """
        # make ID each request should have one
        self.request_id = str(uuid.uuid1())
        # get time
        self.request_time = pd.Timestamp.now()
        # set results for cached/needed to None
        self.cached_results_count = None
        self.needed_results_count = None
        # add request_id to my metadata
        self.add_request_id_to_metadata()
        # clean up the tags in metadata making sure they are lists
        self.clean_up_metadata_tags()
        # define the output metadata as Pydantic model
        self.define_output_metadata()

    @staticmethod
    def make_request_hash(request_service: str, request_parameters: dict) -> str:
        """
        Generates a hash from the request parameters
        Does not consider the metadata an important parameter
        """
        if "tk_metadata" in request_parameters:
            important_parameters = subset_dict(request_parameters, ["tk_metadata"])
        else:
            important_parameters = request_parameters
        # add the service as an element to cache (we don't want to match on different services)
        request_parameters["request_service"] = request_service
        return hash_from_dict(important_parameters)

    def clean_up_metadata_tags(self) -> None:
        """
        Makes all request tags (from metadata) as lists
        """
        self.metadata.tags = {k: v if isinstance(v, list) else [v] for k, v in self.metadata.tags.items()}

    def write_request_response_to_snowflake(
        self,
        data: dict,
        request_parameters: dict,
    ) -> None:
        """
        Writes the request response to Snowflake this only happens for
        non-cached results
        """
        # create the df
        df = pd.DataFrame(
            [
                {
                    "tk_metadata": self.get_tags_as_lists(),
                    "request_id": self.request_id,
                    "request_time": self.request_time,
                    "request_hash": self.request_hash,
                    "request_parameters": request_parameters,
                    "raw_json": data,
                    "update_time": self.request_time,
                }
            ]
        )
        with Snowkeet() as snow:
            snow.write_to_snowflake(df, "REQUEST_CACHE")

    def write_audit_table(self) -> None:
        with Snowkeet() as snow:
            snow.write_to_snowflake(self.output_metadata_dataframe(), "request_audit")

    def write_api_response_table(self, raw_response: dict) -> None:
        """
        write the results for long term storage
        """
        pass

    def define_output_metadata(self) -> None:
        """
        Adds/alters created_by to metadata
        """
        self.output_metadata = TerakeetResponseMetadata(
            requesting_application=self.metadata.application,
            request_tags=self.metadata.tags,
            request_id=self.request_id,
            processing_application=f"tk_core.{type(self).__name__}",
            request_time=self.request_time,
            cached_results=self.cached_results_count,
            needed_results=self.needed_results_count,
        )
        return self.output_metadata

    def end_user_formatted_output_metadata(self, status: str, table_name: str) -> dict:
        """
        format the output metadata for end users

        This is designed to let the user know where their data can be found once
        the request is complete
        """
        md = self.output_metadata.model_dump()
        message = f"Batch Request complete for {type(self).__name__}"
        return {
            "status": status,
            "request_id": md["request_id"],
            "message": message,
            "cached_results": md["cached_results"],
            "pulled_results": md["needed_results"],
            "tags": md["request_tags"],
            "snowflake_location": table_name,
        }

    def output_metadata_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame([self.output_metadata.model_dump()])

    def add_request_id_to_metadata(self) -> None:
        self.metadata.tags["request_id"] = [self.request_id]

    def get_tags_as_lists(self) -> None:
        """
        Makes all request tags (from metadata) as lists
        """
        return {k: v if isinstance(v, list) else [v] for k, v in self.output_metadata.model_dump()["request_tags"].items()}
