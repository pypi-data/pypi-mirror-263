from dataclasses import dataclass
from datetime import datetime
from enum import Enum

DOUBLE_QUOTES_HTML_LITERAL = "&quot"


class RollingDateRange(Enum):
    TODAY = "today"
    YESTERDAY = "yesterday"
    THIS_WEEK = "this_week"
    LAST_WEEK = "last_week"  # goes back 7 days and starts from that week's Monday until that sunday
    LAST_SEVEN_DAYS = "last_seven_days"
    LAST_THIRTY_DAYS = "last_thirty_days"
    LAST_NINETY_DAYS = "last_ninety_days"
    YEAR_TO_DATE = "year_to_date"
    LAST_YEAR = "last_twelve_months"
    LAST_ONE_HOURS = "last_1_hours"
    LAST_THREE_HOURS = "last_3_hours"
    LAST_SIX_HOURS = "last_6_hours"
    LAST_NINE_HOURS = "last_9_hours"
    LAST_TWELVE_HOURS = "last_12_hours"
    LAST_TWENTY_FOUR_HOURS = "last_24_hours"
    LAST_FORTY_EIGHT_HOURS = "last_48_hours"


@dataclass
class AbsoluteDateRange:
    start_dt: datetime
    end_dt: datetime

    def to_string_tuple(self):
        """Converts datetimes to strings and returns the tuple"""
        return self.start_dt.isoformat(), self.end_dt.isoformat()

    @classmethod
    def from_strings(cls, start: str, end: str):
        """Creates a new AbsoluteDateRange from two strings"""
        return AbsoluteDateRange(
            start_dt=datetime.fromisoformat(start), end_dt=datetime.fromisoformat(end)
        )
