import logging
from functools import reduce
from operator import add

from tk_core.core.batch_request import BatchRequest
from tk_core.serp_api.models import BatchSERPAPIResponse, SERPAPIBatchRequest, SERPAPIResponse
from tk_core.serp_api.serp import get_serp_client
from tk_core.serp_api.util import extract_serpapi_params


class BatchSERPAPISerps(BatchRequest):
    SOURCE_NAME_AND_VERSION = "tk_core_serp_api_batch_initiator"

    def __init__(self, params: SERPAPIBatchRequest) -> None:
        """
        Initializes the BatchSERPAPISerps class
        Args:
            params (SERPAPIBatchRequest): The parameters for the search.
        """
        # validate params
        if not isinstance(params, SERPAPIBatchRequest):
            params = SERPAPIBatchRequest.model_validate(params)
        self.params: SERPAPIBatchRequest = params
        # call the parent class
        super().__init__(params)

        # lists to use for processing
        self.requests = []
        self.additional_requests = []
        self.results = []

    def get_serps(self) -> BatchSERPAPIResponse:
        """
        Main method to get SERP results for our list of queries
        Loops through queries and creates requests for each

        This is probably the method we want to remove from the class,
        and have the dask task call it process it concurrently

        Returns:
            a nested dictionary of results
        """
        # Define the end results
        query_results = {
            "queries": {},
            "query_params": {
                "queries": self.params["queries"],
                "search_parameters": self.params["search_parameters"],
            },
            "tk_metadata": {
                "request_id": self.request_id,
                "run_date": self.request_time,
                "requesting_application": self.params.tk_metadata["application"],
                "request_tags": self.params.tk_metadata["tags"],
                "processing_application": BatchSERPAPISerps.SOURCE_NAME_AND_VERSION,
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

    def process_one_serp(self, request_hash: str) -> SERPAPIResponse:
        """
        Main method to get SERP results
        """
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
        # we use ._make_request here as we want to only get the data
        # caching has already been handled
        response = s._make_request()

        # check for a bad response
        if response.get("serpapi_pagination") is None:
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
