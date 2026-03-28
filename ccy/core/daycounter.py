from __future__ import annotations

from datetime import date
from enum import StrEnum

from ..dates.utils import date_diff

__all__ = ["DayCounter"]


class DayCounter(StrEnum):
    """Day count convention types"""

    ACT360 = "ACT/360"
    ACT365 = "ACT/365"
    THIRTY360 = "30/360"
    THIRTYE360 = "30E/360"
    ACTACT = "ACT/ACT"
    BUS252 = "BUS/252"

    def dcf(self, start: date, end: date) -> float:
        """Day count fraction between 2 dates"""
        match self:
            case DayCounter.ACT360:
                return count_days(start, end) / 360.0
            case DayCounter.ACT365:
                return count_days(start, end) / 365.0
            case DayCounter.THIRTY360:
                return _thirty_360(start, end)
            case DayCounter.THIRTYE360:
                return _thirty_e360(start, end)
            case DayCounter.ACTACT:
                return _act_act_years(end) - _act_act_years(start)
            case DayCounter.BUS252:
                return count_days(start, end) / 252.0
            case _:
                raise ValueError(f"Unknown day counter: {self}")


def count_days(start: date, end: date) -> float:
    """Count the number of days between 2 dates"""
    return date_diff(end, start).total_seconds() / 86400


def _thirty_e360(start: date, end: date) -> float:
    d1 = min(start.day, 30)
    d2 = min(end.day, 30)
    return 360 * (end.year - start.year) + 30 * (end.month - start.month) + d2 - d1


def _thirty_360(start: date, end: date) -> float:
    d1 = min(start.day, 30)
    d2 = min(end.day, 30) if d1 == 30 else end.day
    return 360 * (end.year - start.year) + 30 * (end.month - start.month) + d2 - d1


def _act_act_years(dt: date) -> float:
    y = dt.year
    days_in_year = 365 if y % 4 else 366
    dd = date_diff(dt, date(y, 1, 1)).total_seconds() / 86400
    return y + dd / days_in_year
