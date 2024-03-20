from urllib.parse import urljoin

from pydantic import ValidationError

from bigdata.api.search import (
    DiscoveryPanelRequest,
    DiscoveryPanelResponse,
    ListSavedSearchesResponse,
    QueryClustersRequest,
    QueryClustersResponse,
    SavedSearchResponse,
    SaveSearchRequest,
    UpdateSearchRequest,
)
from bigdata.auth import Auth


class BigdataConnection:
    """
    The connection to the API.

    Contains the Auth object with the JWT and abstracts all the calls to the API,
    receiving and returning dicts to/from the caller.
    For internal use only.
    """

    def __init__(self, auth: Auth, api_url: str):
        self.auth = auth
        self.api_url = api_url

    # Autosuggest

    def autosuggest(self, q: str) -> list[dict]:
        """Calls GET /autosuggest"""
        result = self._get("autosuggest", params={"query": q})
        return result["results"]

    # Search

    def query_clusters(self, request: QueryClustersRequest) -> QueryClustersResponse:
        """Calls POST /cqs/query-clusters"""
        json_request = request.model_dump(exclude_none=True, by_alias=True)
        json_response = self._post("cqs/query-clusters", json=json_request)
        return QueryClustersResponse(**json_response)

    def get_search(self, id: str) -> SavedSearchResponse:
        """Calls GET /user-data/queries/{id}"""
        json_response = self._get(f"user-data/queries/{id}")
        try:
            return SavedSearchResponse(**json_response)
        except ValidationError as e:
            raise NotImplementedError(
                "Query expression may have unsupported expression types"
            ) from e

    def list_searches(
        self, saved: bool = True, owned: bool = True
    ) -> ListSavedSearchesResponse:
        """Calls GET /user-data/queries"""
        params = {}
        if saved:
            params["save_status"] = "saved"
        if owned:
            params["owned"] = "true"
        json_response = self._get("user-data/queries", params=params)
        return ListSavedSearchesResponse(**json_response)

    def save_search(self, request: SaveSearchRequest) -> dict:
        """Calls POST /user-data/queries"""
        json_request = request.model_dump(exclude_none=True, by_alias=True)
        return self._post("user-data/queries", json=json_request)

    def update_search(self, request: UpdateSearchRequest, search_id: str) -> dict:
        """Calls PATCH /user-data/queries/{id}"""
        json_request = request.model_dump(exclude_none=True, by_alias=True)
        return self._patch(f"user-data/queries/{search_id}", json=json_request)

    def delete_search(self, id: str) -> dict:
        """Calls DELETE /user-data/queries/{id}"""
        return self._delete(f"user-data/queries/{id}")

    def query_discovery_panel(
        self, request: DiscoveryPanelRequest
    ) -> DiscoveryPanelResponse:
        """Calls POST /cqs/discovery-panel"""
        json_request = request.model_dump(exclude_none=True, by_alias=True)
        json_response = self._post("cqs/discovery-panel", json=json_request)
        return DiscoveryPanelResponse(**json_response)

    # Wrappers for HTTP methods

    def _get(self, endpoint: str, params: dict = {}) -> dict:
        url = self._get_url(endpoint)
        response = self.auth.request("GET", url, params=params)
        response.raise_for_status()
        return response.json()

    def _post(self, endpoint: str, json: dict) -> dict:
        url = self._get_url(endpoint)
        response = self.auth.request("POST", url, json=json)
        response.raise_for_status()
        return response.json()

    def _patch(self, endpoint: str, json: dict) -> dict:
        url = self._get_url(endpoint)
        response = self.auth.request("PATCH", url, json=json)
        response.raise_for_status()
        return response.json()

    def _delete(self, endpoint: str) -> dict:
        url = self._get_url(endpoint)
        response = self.auth.request("DELETE", url)
        response.raise_for_status()
        return response.json()

    # Other helpers

    def _get_url(self, endpoint: str) -> str:
        return urljoin(str(self.api_url), str(endpoint))
