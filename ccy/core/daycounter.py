"""Day Counter for Counting time between 2 dates.
Implemented::

    * Actual 360
    * Actual 365
    * 30 / 360
    * Actual Actual
"""

from __future__ import annotations

from copy import copy
from datetime import date
from typing import Any

__all__ = ["getdc", "DayCounter", "alldc"]


def getdc(name: str) -> DayCounter:
    return _day_counters[name]()


def alldc() -> dict[str, DayCounterMeta]:
    global _day_counters
    return copy(_day_counters)


def act_act_years(dt: date) -> float:
    y = dt.year
    r = y % 4
    a = 0.0
    if r > 0:
        a = 1.0
    dd = (dt - date(y, 1, 1)).days
    return y + dd / (365.0 + a)


class DayCounterMeta(type):
    def __new__(cls, name: str, bases: Any, attrs: Any) -> DayCounterMeta:
        new_class = super(DayCounterMeta, cls).__new__(cls, name, bases, attrs)
        if name := getattr(new_class, "name", ""):
            _day_counters[name] = new_class
        return new_class


_day_counters: dict[str, DayCounterMeta] = {}


class DayCounter(metaclass=DayCounterMeta):
    name: str = ""

    def count(self, start: date, end: date) -> int:
        return (end - start).days

    def dcf(self, start: date, end: date) -> float:
        return self.count(start, end) / 360.0


class Act360(DayCounter):
    name = "ACT/360"


class Act365(DayCounter):
    name = "ACT/365"

    def dcf(self, start: date, end: date) -> float:
        return self.count(start, end) / 365.0


class Thirty360(DayCounter):
    name = "30/360"

    def dcf(self, start: date, end: date) -> float:
        d1 = min(start.day, 30)
        d2 = min(end.day, 30)
        return 360 * (end.year - start.year) + 30 * (end.month - start.month) + d2 - d1


class ActAct(DayCounter):
    name = "ACT/ACT"

    def dcf(self, start: date, end: date) -> float:
        return act_act_years(end) - act_act_years(start)
