from dataclasses import dataclass
from enum import Enum

from bigdata.query_type import QueryType


@dataclass
class StorySource:
    """The source of a story"""

    key: str
    name: str
    rank: int


class StoryType(Enum):
    """
    The type of the story. A news, a transcript or an uploaded file.
    """

    NEWS = "news"
    TRANSCRIPTS = "transcripts"
    FILES = "files"


@dataclass
class StorySentenceEntity:
    """
    A detection instance of an entity in a sentence
    """

    key: str
    start: int
    end: int
    query_type: QueryType


@dataclass
class StorySentence:
    """
    A sentence in a story
    """

    text: str
    paragraph: int
    sentence: int
    entities: list[StorySentenceEntity]
