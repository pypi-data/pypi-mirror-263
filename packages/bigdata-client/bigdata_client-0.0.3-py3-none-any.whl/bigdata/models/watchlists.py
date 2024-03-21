from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Watchlist(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(validation_alias="key")
    name: str
    query_type: Literal["watchlist"] = Field(
        default="watchlist", validation_alias="queryType"
    )
