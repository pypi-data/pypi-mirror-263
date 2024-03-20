from enum import StrEnum
from typing import Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field


class AutosuggestedSearch(BaseModel):
    """Class used only to parse the output from the Autosuggestion"""

    # TODO: Move this to bigdata.api.autosuggest?

    model_config = ConfigDict(populate_by_name=True)
    id: Optional[str] = Field(validation_alias="key", default=None)
    name: Optional[str] = Field(default=None)
    query_type: Literal["savedSearch"] = Field(
        default="savedSearch", validation_alias="queryType"
    )


class ExpressionOperation(StrEnum):
    IN = "in"


class ExpressionTypes(StrEnum):
    AND = "and"
    KEYWORD = "keyword"
    ENTITY = "entity"
    SOURCE = "source"
    TOPIC = "rp_topic"
    LANGUAGE = "language"
    WATCHLIST = "watchlist"
    DATE = "date"


class Expression(BaseModel):
    type: ExpressionTypes
    value: Union[list[Union[str, "Expression"]], str]
    operation: Optional[ExpressionOperation] = None

    @classmethod
    def new(cls, etype: ExpressionTypes, values: Optional[list[str]]) -> "Expression":
        if not values:
            return None
        return cls(type=etype, operation=ExpressionOperation.IN, value=values)


class FileType(StrEnum):
    all = "all"
    filings = "filings"
    transcripts = "transcripts"
    news = "news"
    files = "files"


class SortBy(StrEnum):
    """Defines the order of the search results"""

    relevance = "relevance"
    date = "date"


class Ranking(StrEnum):
    stable = "stable"
    experimental = "experimental"
    similarity = "similarity"


class SearchChain(StrEnum):
    deduplication = "deduplication"
    enricher = "enricher"  # NO LONGER USED
    default = "default"  # NO LONGER USED?
    clustering = "clustering"


class SearchPagination(BaseModel):
    limit: int = Field(default=100, gt=0, lt=1001)
    cursor: int = Field(default=1, gt=0)
