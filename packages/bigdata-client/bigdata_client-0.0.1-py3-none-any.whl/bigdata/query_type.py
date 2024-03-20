from enum import Enum


class QueryType(str, Enum):
    # SAVED_SEARCH = "savedSearch"
    # WATCHLIST = "watchlist"
    entity = "entity"
    topic = "rp_topic"
    source = "source"
    language = "language"
    # KEYWORD = "keyword"  # TODO: check
