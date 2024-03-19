"""_summary_
"""

import datetime
import logging
import uuid
from functools import reduce
from operator import add

from rich import print

from tk_core.common.de_service import DeService
from tk_core.common.dictionary import subset_dict
from tk_core.common.hasher import hash_from_dict, uri_string_from_dict
from tk_core.serp_api.models import BatchSERPAPIResponse, SERPAPIBatchRequest, SERPAPIResponse
from tk_core.serp_api.serp import get_serp_client
from tk_core.serp_api.util import extract_serpapi_params


class BatchSERPAPISerps:
    SOURCE_NAME_AND_VERSION = "tk_core_serp_api_batch_initiator"

    def __init__(self, params: SERPAPIBatchRequest, cache_duration: int = 1) -> None:
        # validate input params
        if not isinstance(params, SERPAPIBatchRequest):
            params = SERPAPIBatchRequest.model_validate(params)
        self.params: dict = params.model_dump()
        self.run_date = f"{datetime.datetime.now():%Y-%m-%d}"
        self.executed_at = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"
        if cache_duration not in [0, 1, 30]:
            raise ValueError("cache_duration (days) must be 0, 1, or 30")
        self.cache_duration = cache_duration
        self.query_hash = None
        self.execution_id = None
        self.uri = None
        self.requests = []
        self.additional_requests = []
        self.results = []
        self.de = DeService("serpapi")
        self.batch_execution_uuid = None
        self.tags = self.params["tk_metadata"]["tags"]
        self.application = self.params["tk_metadata"]["application"]
        self.created_by = "tk_core_serpapi_executor"

    def prepare_hash_and_metadata(self) -> None:
        """
        Prepares more hashing information and metadata for later use
        """
        to_hash = subset_dict(self.params, ["tk_metadata"])
        self.uri = uri_string_from_dict(to_hash)
        self.query_hash = hash_from_dict(to_hash)
        self.execution_id = f"{self.query_hash}/{self.run_date}"

    def get_serps(self) -> BatchSERPAPIResponse:
        """
        Main method to get SERP results for our list of queries
        Loops through queries and creates requests for each

        This is probably the method we want to remove from the class,
        and have the dask task call it process it concurrently

        Returns:
            a nested dictionary of results

            ├── queries
                ├── seo
                    └── execution_id
                    └── query_def_hash
                    ├── request_metadata
                        └── page_number
                        └── execution_uuid
                        └── query_def_hash
                        └── processed_by
                    └── page_count
                    └── pages
                    └── errors
                ├── ppc
                    └── execution_id
                    └── query_def_hash
                    ├── request_metadata
                        └── page_number
                        └── execution_uuid
                        └── query_def_hash
                        └── processed_by
                    └── page_count
                    └── pages
                    └── errors
            ├── query_params
                └── queries
                ├── search_parameters
                    └── google_domain
                    └── language
                    └── country
                    └── location
                    └── device
                    └── additional_results
                    └── per_page
                    └── page_count
                    └── engine
                    └── query
            ├── tk_metadata
                └── application
                ├── tags
                    └── example_tag
                └── processed_by
                └── request_id
                └── run_date
                └── executed_at
        """
        # Define the end results
        query_results = {
            "queries": {},
            "query_params": {
                "queries": self.params["queries"],
                "search_parameters": self.params["search_parameters"],
            },
            "tk_metadata": {
                "application": self.application,
                "tags": self.tags,
                "processed_by": BatchSERPAPISerps.SOURCE_NAME_AND_VERSION,
                # request_id is a unique identifier for this request
                "request_id": str(uuid.uuid1()),
                "run_date": self.run_date,
                "executed_at": self.executed_at,
            },
        }
        # Loop through queries and get results
        for query in self.params["queries"]:
            # reset the requests
            self.requests = []
            # Set the query
            self.params["search_parameters"]["query"] = query
            # Get the serp data
            query_results["queries"][query] = self.process_one_serp()

        return query_results

    def process_one_serp(self) -> SERPAPIResponse:
        """
        Main method to get SERP results
        """
        # Step 1 - build the hash and metadata
        self.prepare_hash_and_metadata()
        # Step 2 - check for cached results
        # if cached move to option A, if not move to option B
        if self.de.execution_cache_exists(self.execution_id, self.cache_duration):
            # Option A - return cached results if exists
            logging.info(f"Returning cached version of {self.execution_id}")
            return self.de.load_execution_cache(self.execution_id)
        # Option B - generate new version if not cached
        else:
            logging.info(f"Generating new version of {self.execution_id}")
            # Step B1 - create requests
            self.create_requests()
            # Step B2 - run the requests
            self.run_jobs()
            # Step B3 - check for additional results
            self.check_for_additional_results()
            # Step B4 - prepare the response
            response = self.prepare_response()
            # Step B5 - store the response to S3
            self.de.store_execution(response)

            return response

    def create_requests(self) -> None:
        """
        Step B1
        Determines number of requests to create, and sets up params for each one
        """
        page_count = self.params["search_parameters"]["page_count"]
        per_page = self.params["search_parameters"]["per_page"]
        for page_num in range(page_count):
            # convert params to serpapi proper params
            loaded_params = extract_serpapi_params(self.params["search_parameters"], per_page, per_page * page_num)
            # build the request JSON
            request_params = {
                "query_params": loaded_params.model_dump(),
                "request_metadata": {
                    "page_number": page_num + 1,
                },
            }
            self.requests.append(request_params)

    def run_jobs(self, request_list: list | None = None) -> None:
        """
        Step B2

        Loop through request parameters and run requests
        Assigns results to self.results

        Args:
            requests (list[dict]): List of prepared requests for execution

        Returns:
            None
        """

        request_list = request_list if request_list is not None else self.requests

        self.results = [self.run_request(x) for x in request_list]

    def run_request(self, request_params: dict) -> dict:
        """
        Run a single SERPAPI request

        Args:
            params (dict): The translates params for the executor

        Returns:
            str: The UTF-8 decoded request from the executor
        """
        s = get_serp_client(
            params=request_params["query_params"],
            request_metadata=request_params["request_metadata"],
        )
        response = s.execute_query()

        # check for a bad response
        if response["response"].get("serpapi_pagination") is None:
            print("Issue in initiator.run_request", exc_info=True)
            raise ValueError(f"Bad response from SERP Api: {response}")
        return response

    def check_for_additional_results(self) -> None:
        """
        Step B3

        Determine if we have been asked to load additional results from Google, and if so, create the requests
        """
        if self.params.get("additional_results", False) is True:
            print(f"Keys in results: {self.results[0].keys()}")
            result_lengths = [len(x["organic_results"]) for x in self.results if x.get("serpapi_pagination") is not None]
            print(f"Offset starting number for calculated position: {result_lengths}")
            offset = reduce(add, result_lengths) + 1
            # Optional Step B3-1
            self.create_requests_for_additional_results(offset)
            # Optional Step B3-2
            self.run_jobs_for_additional_results()

    def prepare_response(self) -> dict:
        """
        Step B4

        Prepare the response for the user
        """
        pages = self.sort_and_renumber_pages()
        return {
            "execution_id": self.execution_id,
            "query_def_hash": self.query_hash,
            "request_metadata": self.results[0]["request_metadata"],
            "page_count": len(pages),
            "pages": pages,
            "errors": self.extract_errors(),
        }

    def sort_and_renumber_pages(self) -> list:
        """
        Helper Function to prepare the response
        """
        sorted = self.sort_pages()
        return self.renumber_results(sorted)

    def sort_pages(self) -> list:
        """
        Request execution is asynchronous, so we need to sort the results
        """
        to_sort = [x for x in self.results if x["response"].get("serpapi_pagination") is not None]
        return sorted(to_sort, key=lambda x: x["request_metadata"]["page_number"])

    @staticmethod
    def renumber_results(sorted: list) -> list:
        """
        Helper Function
        Renumber the results to reflect the correct position
        """
        offset = 0
        for i, page in enumerate(sorted):
            raw_results = page["response"]
            if i > 0:
                for r, result in enumerate(raw_results["organic_results"]):
                    result["calculated_position"] = result["position"] + offset
                    raw_results["organic_results"][r] = result
                sorted[i] = page
            else:
                for r, result in enumerate(raw_results["organic_results"]):
                    result["calculated_position"] = result["position"]
                    raw_results["organic_results"][r] = result
                sorted[i] = raw_results
            offset = offset + raw_results["organic_results"][-1]["position"]

        return sorted

    def extract_errors(self) -> list:
        """
        Pull errors from SERP API Executor
        """
        # todo - need to get metadata for the page that failed from the executor.
        return [x for x in self.results if x["response"].get("serpapi_pagination") is None]

    def create_requests_for_additional_results(self, offset: int) -> None:
        """
        Optional Step B3-1

        Same process as create_requests above with tuning for 100-page results and some accounting for
        previously received results. Could be DRYed up, but this is a quick and dirty solution.

        TODO: Combine this with create_requests (I don't think we need both) DRY it up
        """
        message = f"Requesting additional results; using offset: {offset}"
        logging.info(message)
        start_page_number = len(self.results) - 1
        per_page = 100
        logging.info(f"Additional pages to load: {range(start_page_number, start_page_number + 5)}")
        for iterations, page_num in enumerate(range(start_page_number, start_page_number + 5)):
            loaded_params = extract_serpapi_params(self.params, per_page, offset + (per_page * iterations))
            logging.info(f"Additional page: {page_num + len(self.results)}")
            request_params = {
                "query_params": loaded_params,
                "request_metadata": {
                    "page_number": page_num + len(self.results),
                },
            }
            logging.info("Setup params for this page")
            logging.info(request_params)
            self.additional_requests.append(request_params)

    def run_jobs_for_additional_results(self) -> None:
        """
        Optional Step B3-2

        Does what it says on the tin, runs the additional requests
        """
        self.run_jobs(self.additional_requests)
