from tk_core.common.dates import datecode
from tk_core.core.base_request import TerakeetRequest
from tk_core.core.models import TerakeetBatchQueryRequest
from tk_core.core.tk_redis import TKRedis


class BatchRequest(TerakeetRequest):
    """
    Diagram: https://lucid.app/lucidchart/48d77f3c-6aa4-401f-9e08-dfa9fc679d55/edit
    """

    def __init__(self, params: TerakeetBatchQueryRequest) -> None:
        self.params = params
        self.metadata = params.tk_metadata
        # validate cache_duration which would be in the tk_metadata
        if params.tk_metadata.cache_duration is None:
            self.cache_duration = 1
        elif params.tk_metadata.cache_duration not in [0, 1, 30]:
            raise ValueError("cache_duration (days) must be 0, 1, or 30")

        # set the minimum date (today - cache_duration)
        self.minimum_date = int(datecode()) - self.cache_duration

        # create redis object
        self.redis = TKRedis()

        # create a dictionary of hashes
        self.hash_to_parameters: dict | None = None

    def generate_hashes_for_parameters(self) -> tuple[list]:
        """
        Step 1
        separate hash lists into cached/needed
        """
        # TODO: make this quicker? less variables maybe?
        combined_params = self.combine_queries_and_params()
        # make a dictionary of all hashes to their parameters
        # we will need the actual params later if we need to make a request
        self._generate_request_hashes(combined_params)
        return list(self.hash_to_parameters.keys())

    def combine_queries_and_params(self) -> list:
        """
        Step 1-a
        Combines the queries and parameters into a list of dictionaries
        """
        request_parameters = []
        for query in self.params.queries:
            temp_params = self.params.search_parameters.model_dump()
            temp_params["query"] = query
            request_parameters.append(temp_params)
        return request_parameters

    def _generate_request_hashes(self, list_of_parameters: list) -> dict:
        """
        Step 1-b
        given a list of parameters, make their hashes
        """
        self.hash_to_parameters = {
            self.make_request_hash(f"tk_core.{type(self).__name__}", params): params for params in list_of_parameters
        }

    def lookup_existence_of_cache(self, list_of_hashes: list) -> tuple[list]:
        """
        Step 2
        Checks the Redis stack for cached results
        """
        keys = self.batch_check_redis_for_cache(list_of_hashes)
        return self.separate_cached_vs_needed(keys, list_of_hashes)

    def batch_check_redis_for_cache(self, list_of_hashes: list) -> list:
        """
        Step 2
        Checks the Redis stack for cached results
        """
        r = TKRedis()
        return r.get_hash_values_from_list_with_pipe("test_hash", list_of_hashes)

    def separate_cached_vs_needed(self, keys: list, list_of_hashes: list) -> tuple[list]:
        """
        Step 2-a
        Separates the cached from the needed
        """
        cached = []
        needed = []
        for h, k in zip(list_of_hashes, keys):
            if k and int(k) >= self.minimum_date:
                cached.append(h)
            else:
                needed.append(h)

    def set_cached_results_count(self, count: int) -> None:
        """
        Sets the count of cached results
        """
        self.cached_results_count = count

    def set_needed_results_count(self, count: int) -> None:
        """
        Sets the count of needed results
        """
        self.needed_results_count = count

    def process(self) -> None:
        """
        main flow for batch query jobs
        """
        # Step 1
        hashed_requests = self.generate_hashes_for_parameters()
        # Step 2
        cached, needed = self.lookup_existence_of_cache(hashed_requests)
        # Step 2-metadata add
        self.set_cached_results_count(len(cached))
        self.set_needed_results_count(len(needed))
        #
        self.process_cached(cached)
        self.process_needed(needed)
        # Final Step - save to audit table
        self.write_audit_table()

    def process_cached(self, cached_hashes: list) -> None:
        """
        Step 3
        Process the cached hashes
        """
        for hash_ in cached_hashes:
            pass

    def process_needed(self, needed_hashes: list) -> None:
        """
        Step 4
        Process the needed hashes
        """
        for hash_ in needed_hashes:
            pass
