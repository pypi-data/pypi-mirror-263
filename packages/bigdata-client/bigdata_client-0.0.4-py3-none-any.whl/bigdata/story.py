import datetime
from dataclasses import dataclass

from bigdata.api.search import ChunkedStoryResponse
from bigdata.models.story import StoryChunk, StorySentenceEntity, StorySource, StoryType


@dataclass
class Story:
    """A story object"""

    id: str
    headline: str
    sentiment: float
    story_type: StoryType
    source: StorySource
    timestamp: datetime.datetime
    sentences: list[StoryChunk]
    language: str

    @classmethod
    def from_response(cls, response: ChunkedStoryResponse) -> "Story":
        source = StorySource(
            key=response.source_key,
            name=response.source_name,
            rank=response.source_rank,
        )
        sentences = [
            StoryChunk(
                s.text,
                s.cnum,
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
            language=response.language,
        )
        return story

    def __str__(self) -> str:
        """
        Returns a string representation of the story.
        """
        sentences_repr = "\n".join(f"* {sentence.text}" for sentence in self.sentences)
        return (
            f"Story ID:  {self.id}\n"
            f"Timestamp: {self.timestamp}\n"
            f"Doc type:  {self.story_type}\n"
            f"Source:    {self.source.name} ({self.source.rank})\n"
            f"Title:     {self.headline}\n"
            f"Language:  {self.language}\n\n"
            f"Sentence matches:\n{sentences_repr}"
        )
