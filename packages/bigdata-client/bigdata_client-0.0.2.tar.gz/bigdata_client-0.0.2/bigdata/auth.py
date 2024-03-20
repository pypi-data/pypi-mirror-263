from http import HTTPStatus
from typing import Optional

import requests

from bigdata.clerk.models import SignInStrategyType
from bigdata.clerk.token_manager import ClerkTokenManager
from bigdata.clerk.token_manager_factory import token_manager_factory
from bigdata.settings import ClerkInstanceType, settings
from bigdata.user_agent import get_user_agent


class Auth:
    """
    Class that performs the authentication logic, and wraps all the http calls
    so that it can handle the token autorefresh when needed.
    """

    def __init__(self, token_manager: ClerkTokenManager):
        self._session = requests.session()
        self._token_manager = token_manager

    @classmethod
    def from_username_and_password(
        cls,
        username: str,
        password: str,
        instance_type: Optional[ClerkInstanceType] = None,
    ) -> "Auth":
        if instance_type is None:
            instance_type = settings.CLERK_INSTANCE_TYPE
        # A token manager handles the authentication flow and stores a jwt. It contains methods for refreshing it.
        token_manager = token_manager_factory(
            instance_type,  # FIXME OLD AUTH
            SignInStrategyType.PASSWORD,
            email=username,
            password=password,
        )
        token_manager.refresh_session_token()
        auth = Auth(token_manager=token_manager)
        return auth

    def request(
        self,
        method,
        url,
        params=None,
        data=None,
        headers=None,
        json=None,
    ):
        """Makes an HTTP request, handling the token refresh if needed"""
        headers = headers or {}
        headers["origin"] = f"{settings.BIGDATA_API_URL}"
        headers["referer"] = f"{settings.BIGDATA_API_URL}"
        # if "content-type" not in headers:
        # We may have to conditionally set the content type when uploading files
        headers["content-type"] = "application/json"
        headers["accept"] = "application/json"
        headers["user-agent"] = get_user_agent(settings.PACKAGE_NAME)
        headers["Authorization"] = f"Bearer {self._token_manager.get_session_token()}"

        # The request method has other arguments but we are not using them currently
        response = self._session.request(
            method=method, url=url, params=params, data=data, headers=headers, json=json
        )
        if response.status_code == HTTPStatus.UNAUTHORIZED:
            headers = headers.copy()
            headers["Authorization"] = (
                f"Bearer {self._token_manager.refresh_session_token()}"
            )
            # Retry the request
            response = self._session.request(
                method=method,
                url=url,
                params=params,
                data=data,
                headers=headers,
                json=json,
            )
        return response
