from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class Company(BaseModel):
    """
    Represents an entity in RavenPack's dataset.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(validation_alias="key")
    name: str
    # description: str
    category: str
    entity_type: Literal["COMP"] = Field(default="COMP", validation_alias="entityType")
    # queryType: str  # Literal['entity']
    company_type: Optional[str] = Field(validation_alias="group1", default=None)
    country: Optional[str] = Field(validation_alias="group2", default=None)
    sector: Optional[str] = Field(validation_alias="group3", default=None)
    industry_group: Optional[str] = Field(validation_alias="group4", default=None)
    industry: Optional[str] = Field(validation_alias="group5", default=None)
    ticker: Optional[str] = Field(validation_alias="metadata1", default=None)


class Product(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(validation_alias="key")
    name: str
    entity_type: Literal["PROD"] = Field(default="PROD", validation_alias="entityType")
    product_type: str = Field(validation_alias="group1")
    product_owner: str = Field(validation_alias="group2")


class ProductType(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(validation_alias="key")
    name: str
    entity_type: Literal["PRDT"] = Field(default="PRDT", validation_alias="entityType")


class Organization(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(validation_alias="key")
    name: str
    entity_type: Literal["ORGA"] = Field(default="ORGA", validation_alias="entityType")
    organization_type: Optional[str] = Field(validation_alias="group1", default=None)
    country: Optional[str] = Field(validation_alias="group2", default=None)


class OrganizationType(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(validation_alias="key")
    name: str
    entity_type: Literal["ORGT"] = Field(default="ORGT", validation_alias="entityType")


class Person(BaseModel):
    """A person"""

    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(validation_alias="key")
    name: str
    entity_type: Literal["PEOP"] = Field(default="PEOP", validation_alias="entityType")
    # Disabled but enabled for watchlists?
    position: Optional[str] = Field(validation_alias="group1", default=None)
    employer: Optional[str] = Field(validation_alias="group2", default=None)
    nationality: Optional[str] = Field(validation_alias="group3", default=None)
    gender: Optional[str] = Field(validation_alias="group4", default=None)


class Place(BaseModel):
    """A place. E.g. a country, city, etc."""

    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(validation_alias="key")
    name: str
    entity_type: Literal["PLCE"] = Field(default="PLCE", validation_alias="entityType")
    place_type: str = Field(validation_alias="group2")
    country: Optional[str] = Field(validation_alias="group4", default=None)
    region: Optional[str] = Field(validation_alias="group5", default=None)


class Facility(BaseModel):
    """A facility. E.g. a factory, a mine, etc."""

    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(validation_alias="key")
    name: str
    entity_type: Literal["FCTY"] = Field(default="FCTY", validation_alias="entityType")
    country: Optional[str] = Field(validation_alias="group4", default=None)
    region: Optional[str] = Field(validation_alias="group5", default=None)


class Landmark(BaseModel):
    """A landmark. E.g. a mountain, a lake, etc."""

    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(validation_alias="key")
    name: str
    entity_type: Literal["LAND"] = Field(default="LAND", validation_alias="entityType")
    landmark_type: str = Field(validation_alias="group2")
    country: Optional[str] = Field(validation_alias="group4", default=None)
    region: Optional[str] = Field(validation_alias="group5", default=None)


class Concept(BaseModel):
    """Basically everything else"""

    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(validation_alias="key")
    name: str
    entity_type: str = Field(
        validation_alias="entityType"
    )  # Should belong in EntityType
    entity_type_name: str = Field(validation_alias="group1")
    concept_level_2: Optional[str] = Field(validation_alias="group2", default=None)
    concept_level_3: Optional[str] = Field(validation_alias="group3", default=None)
    concept_level_4: Optional[str] = Field(validation_alias="group4", default=None)
    concept_level_5: Optional[str] = Field(validation_alias="group5", default=None)
