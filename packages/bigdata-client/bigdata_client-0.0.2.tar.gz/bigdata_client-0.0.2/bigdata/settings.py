from enum import Enum

from pydantic import HttpUrl
from pydantic_settings import BaseSettings


class ClerkInstanceType(str, Enum):
    DEV = "DEV"
    PROD = "PROD"


class BigdataAuthType(str, Enum):
    CLERK = "CLERK"
    OLD = "OLD"


class Settings(
    BaseSettings
):  # FIXME OLD AUTH remove Clerk config when old auth is removed
    PACKAGE_NAME: str = "bigdata-client"  # The name of the python package
    BIGDATA_API_URL: HttpUrl = "https://api.bigdata.com"
    BIGDATA_AUTH_TYPE: BigdataAuthType = BigdataAuthType.OLD
    CLERK_INSTANCE_TYPE: ClerkInstanceType = ClerkInstanceType.DEV
    # TODO: Change to another endpoint as we need the refresh token
    AUTH_LOGIN_FORM_ENDPOINT: HttpUrl = "https://auth.ravenpack.com/2.0/login"
    CLERK_FRONTEND_URL: HttpUrl = "https://touched-haddock-13.clerk.accounts.dev/v1"


settings = Settings()
