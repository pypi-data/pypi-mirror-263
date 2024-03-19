import ujson as json

from tk_core.common.dates import datecode
from tk_core.core.base_request import TerakeetRequest
from tk_core.core.models import TerakeetBatchQueryRequest
from tk_core.core.tk_redis import TKRedis
from tk_core.snowkeet import Snowkeet


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
        return list(self.hash_to_query.keys())

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
        given a list of parameters, make their hashes and assign to a dictionary
        mapping the hash to the query
        """
        self.hash_to_query = {
            self.make_request_hash(f"tk_core.{type(self).__name__}", params): params["query"] for params in list_of_parameters
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
        Step 2-a
        Checks the Redis stack for cached results
        """
        return self.redis.get_hash_values_from_list_with_pipe(f"{type(self).__name__}_cache", list_of_hashes)

    def separate_cached_vs_needed(self, keys: list, list_of_hashes: list) -> tuple[list]:
        """
        Step 2-b
        Separates the cached from the needed
        """
        cached = []
        needed = []
        for h, k in zip(list_of_hashes, keys):
            if k and self.cache_duration > 0 and int(k) >= self.minimum_date:
                cached.append({h: k})
            else:
                needed.append(h)

        return cached, needed

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

    def process_cache_checks(self) -> None:
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

        return cached, needed

    def batch_update_snowflake(self, cached_hashes: list[dict], table_name: str, filter_var: str = "EXECUTION_ID") -> None:
        """
        Given the hashes and the table, batch update the tags
        """
        # TODO: Figure out this query to merge on variant data
        # INSTEAD OF MERGE TRY UPDATE
        # query = "MERGE NEW_TAGS N INTO REQUEST_CACHE C ON C.REQUEST_HASH = N.REQUEST_HASH"

        with Snowkeet() as snow:
            for combo in cached_hashes:
                # TODO: this seems weird? is there a better way?
                indv_hash, date_to_find = [x for x in combo.items()][0]
                # get current tags
                tags = snow.get_top_result_filtered(table_name, filter_var, f"{indv_hash}/{date_to_find}", "METADATA")
                # update the tags with new metadata
                new_tags = self.update_tags(json.loads(tags))
                # update snowflake
                update_results = snow.session.sql(
                    f"""  
                    UPDATE {table_name}
                    SET METADATA = {new_tags}, UPDATED_AT = CURRENT_TIMESTAMP()
                    WHERE {filter_var} = '{indv_hash}/{date_to_find}'
                    """  # noqa: S608
                ).collect()
                print(update_results[0].as_dict())

    def send_raw_response_to_redis(self, request_hash: str, service_name: str, response: dict) -> None:
        """
        Send the raw response to redis
        """
        self.redis.set_hash_from_dict(service_name, {request_hash: response})

    def update_tags(self, tags: dict) -> list:
        """
        Update the tags
        """
        # if the tags are the same, just return
        # if they are different, we will need to update them
        if tags != self.metadata.tags:
            for key, value in self.metadata.tags.items():
                if key in tags and value not in tags[key]:
                    if isinstance(value, list):
                        tags[key].extend(value)
                    else:
                        tags[key].append(value)
                elif isinstance(value, list):
                    tags[key] = value
                else:
                    tags[key] = [value]
                # make sure the tags are unique
                tags[key] = list(set(tags[key]))

        return tags
