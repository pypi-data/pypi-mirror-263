from dataclasses import dataclass
from datetime import datetime
from enum import Enum

DOUBLE_QUOTES_HTML_LITERAL = "&quot"


class RollingDateRange(Enum):
    today = "today"
    yesterday = "yesterday"
    this_week = "this_week"
    last_week = "last_week"  # goes back 7 days and starts from that week's Monday until that sunday
    last_seven_days = "last_seven_days"
    last_thirty_days = "last_thirty_days"
    last_ninety_days = "last_ninety_days"
    year_to_date = "year_to_date"
    last_year = "last_twelve_months"
    last_one_hours = "last_1_hours"
    last_three_hours = "last_3_hours"
    last_six_hours = "last_6_hours"
    last_nine_hours = "last_9_hours"
    last_twelve_hours = "last_12_hours"
    last_twenty_four_hours = "last_24_hours"
    last_fourty_eight_hours = "last_48_hours"


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
