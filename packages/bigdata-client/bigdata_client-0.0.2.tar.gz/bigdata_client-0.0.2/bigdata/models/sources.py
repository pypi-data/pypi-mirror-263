from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Source(BaseModel):
    """A source of news and information for RavenPack"""

    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(validation_alias="key")
    name: str
    entity_type: Literal["SRCE"] = Field(default="SRCE", validation_alias="entityType")
    publication_type: str = Field(validation_alias="group1")
    language: str = Field(validation_alias="group2")
    country: str = Field(validation_alias="group3")
    source_rank: str = Field(validation_alias="group4")
    provider_id: str = Field(validation_alias="metadata1")
    url: str = Field(validation_alias="metadata2")
