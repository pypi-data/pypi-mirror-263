from typing import Annotated, Any, Optional, Union

from pydantic import BaseModel, Discriminator, Tag, ValidationError

from bigdata.models.entities import (
    Company,
    Concept,
    Facility,
    Landmark,
    Organization,
    OrganizationType,
    Person,
    Place,
    Product,
    ProductType,
)
from bigdata.models.languages import Language
from bigdata.models.search import AutosuggestedSearch
from bigdata.models.sources import Source
from bigdata.models.topics import Topic
from bigdata.models.watchlists import Watchlist


def get_discriminator_domain_value(v: Any) -> Optional[str]:
    if isinstance(v, dict):
        return v.get(
            "entityType", v.get("entity_type", v.get("queryType", v.get("query_type")))
        )
    return getattr(v, "entity_type", getattr(v, "query_type", None))


EntityTypes = Union[
    Company,
    Facility,
    Landmark,
    Organization,
    OrganizationType,
    Person,
    Place,
    Product,
    ProductType,
    Concept,
]

DomainTypes = Union[
    EntityTypes, Topic, Source, Language, AutosuggestedSearch, Watchlist
]


class Domain(BaseModel):
    root: Annotated[
        Union[
            Annotated[Company, Tag(Company.model_fields["entity_type"].default)],
            Annotated[Facility, Tag(Facility.model_fields["entity_type"].default)],
            Annotated[Landmark, Tag(Landmark.model_fields["entity_type"].default)],
            Annotated[
                Organization, Tag(Organization.model_fields["entity_type"].default)
            ],
            Annotated[
                OrganizationType,
                Tag(OrganizationType.model_fields["entity_type"].default),
            ],
            Annotated[Person, Tag(Person.model_fields["entity_type"].default)],
            Annotated[Place, Tag(Place.model_fields["entity_type"].default)],
            Annotated[Product, Tag(Product.model_fields["entity_type"].default)],
            Annotated[
                ProductType, Tag(ProductType.model_fields["entity_type"].default)
            ],
            Annotated[Source, Tag(Source.model_fields["entity_type"].default)],
            Annotated[Topic, Tag(Topic.model_fields["entity_type"].default)],
            Annotated[Language, Tag(Language.model_fields["query_type"].default)],
            Annotated[
                AutosuggestedSearch,
                Tag(AutosuggestedSearch.model_fields["query_type"].default),
            ],
            Annotated[Watchlist, Tag(Watchlist.model_fields["query_type"].default)],
        ],
        Discriminator(get_discriminator_domain_value),
    ]


def parse_domain_object(domain_obj: dict) -> DomainTypes:
    try:
        return Domain.model_validate({"root": domain_obj}).root
    except ValidationError:
        return Concept.model_validate(domain_obj)


# TODO: could somehow unify domain_types and Annotated[Union] in a single list?
# we have mypy to help. `poetry run task pre-commit`
