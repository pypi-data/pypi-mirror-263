from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class Topic(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(validation_alias="key")
    name: str
    # Disabled, but enabled for watchlists?
    topic: Optional[str] = Field(validation_alias="group1", default=None)
    topic_group: str = Field(validation_alias="group2")
    entity_type: Literal["TOPC"] = Field(
        default="TOPC", validation_alias="entityType"
    )  # TODO: we could also use queryType
    # Disabled fields.
    # topic_type: str = Field(validation_alias="group3")
    # topic_subtype: str = Field(validation_alias="group4")
    # topic_role: str = Field(validation_alias="group5")
