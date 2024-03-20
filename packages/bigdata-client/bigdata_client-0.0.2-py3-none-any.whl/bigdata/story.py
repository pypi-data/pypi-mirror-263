import datetime
from dataclasses import dataclass

from bigdata.api.search import StoryResponse
from bigdata.models.story import (
    StorySentence,
    StorySentenceEntity,
    StorySource,
    StoryType,
)


@dataclass
class Story:
    """A story object"""

    id: str
    headline: str
    sentiment: float
    story_type: StoryType
    source: StorySource
    timestamp: datetime.datetime
    sentences: list[StorySentence]

    @classmethod
    def from_response(cls, response: StoryResponse) -> "Story":
        source = StorySource(
            key=response.source_key,
            name=response.source_name,
            rank=response.source_rank,
        )
        sentences = [
            StorySentence(
                s.text,
                s.pnum,
                s.snum,
                [
                    StorySentenceEntity(e.key, e.start, e.end, e.queryType)
                    for e in s.entities
                ],
            )
            for s in response.sentences
        ]
        story = cls(
            id=response.id,
            headline=response.headline,
            sentiment=response.sentiment,
            story_type=response.story_type,
            source=source,
            timestamp=response.timestamp,
            sentences=sentences,
        )
        return story
