from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Language(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(validation_alias="key")
    name: str
    query_type: Literal["language"] = Field(
        default="language", validation_alias="queryType"
    )
