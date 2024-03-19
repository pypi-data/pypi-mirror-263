"""General functions for the initiator"""


from tk_core.serp_api.models import SERPAPIProperRequestParameters


def extract_serpapi_params(params: dict, per_page: int, offset: int) -> SERPAPIProperRequestParameters:
    """Create a param dict the executor expects as "query_params"

    Args:
        params (dict): Incoming params to convert

    Returns:
        dict: Executor-ready params
    """
    return SERPAPIProperRequestParameters.model_validate(
        {
            "q": params["query"],
            "engine": params["engine"],
            "google_domain": params["google_domain"],
            "hl": params["language"],
            "gl": params["country"],
            "location": params["location"],
            "device": params["device"],
            "num": per_page,
            "start": offset,
            "tk_metadata": params["tk_metadata"],
        }
    )
