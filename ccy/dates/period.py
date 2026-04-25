from __future__ import annotations

from typing import Any, Self

from dateutil.relativedelta import relativedelta
from pydantic import BaseModel, Field


def period(pstr: str = "") -> Period:
    """Create a period object from a period string"""
    return Period.make(pstr)


def find_first_of(st: str, possible: str) -> int:
    lowi = -1
    for p in tuple(possible):
        i = st.find(p)
        if i != -1 and (i < lowi or lowi == -1):
            lowi = i
    return lowi


class Period(BaseModel):
    months: int = Field(default=0, ge=0, description="Number of months in the period")
    days: int = Field(default=0, ge=0, description="Number of days in the period")
    hours: int = Field(default=0, ge=0, description="Number of hours in the period")

    @classmethod
    def make(cls, data: Any) -> Self:
        if isinstance(data, cls):
            return data
        elif isinstance(data, str):
            return cls().add_period(data)
        elif isinstance(data, relativedelta):
            return cls(
                months=data.years * 12 + data.months,
                days=data.days,
                hours=data.hours,
            )
        else:
            raise TypeError("Cannot convert %s to Period" % data)

    def isempty(self) -> bool:
        return self.months == 0 and self.days == 0 and self.hours == 0

    def add_days(self, days: int) -> None:
        if days < 0:
            raise ValueError("Negative days are not supported")
        self.days += days

    def add_weeks(self, weeks: int) -> None:
        if weeks < 0:
            raise ValueError("Negative weeks are not supported")
        self.days += int(7 * weeks)

    def add_months(self, months: int) -> None:
        if months < 0:
            raise ValueError("Negative months are not supported")
        self.months += months

    def add_years(self, years: int) -> None:
        if years < 0:
            raise ValueError("Negative years are not supported")
        self.months += int(12 * years)

    def add_hours(self, hours: int) -> None:
        if hours < 0:
            raise ValueError("Negative hours are not supported")
        self.hours += hours
        if self.hours >= 24:
            self.days += self.hours // 24
            self.hours = self.hours % 24

    @property
    def years(self) -> int:
        return self.months // 12

    @property
    def months_remaining(self) -> int:
        """Months remaining after extracting years from the period"""
        return self.months % 12

    @property
    def weeks(self) -> int:
        """Weeks in the period after extracting months and years from the period"""
        return self.days // 7

    @property
    def days_remaining(self) -> int:
        """Days remaining after extracting weeks from the period"""
        return self.days % 7

    def to_str(self) -> str:
        """The period string"""
        p = ""
        y = self.years
        m = self.months
        w = self.weeks
        d = self.days
        if y := self.years:
            p = "%sY" % y
        if m := self.months_remaining:
            p = "%s%sM" % (p, m)
        if w := self.weeks:
            p = "%s%sW" % (p, w)
        if d := self.days_remaining:
            p = "%s%sD" % (p, d)
        if h := self.hours:
            p = "%s%sH" % (p, h)
        return p

    def to_relativedelta(self) -> relativedelta:
        """Convert the period to a dateutil.relativedelta object"""
        return relativedelta(
            years=self.years,
            months=self.months_remaining,
            weeks=self.weeks,
            days=self.days_remaining,
            hours=self.hours,
        )

    def add_period(self, pstr: str | Self) -> Self:
        if isinstance(pstr, Period):
            self.add_days(pstr.days)
            self.add_months(pstr.months)
            self.add_hours(pstr.hours)
            return self
        st = str(pstr).upper()
        while st:
            ip = find_first_of(st, "HDWMY")
            if ip == -1:
                raise ValueError("Unknown period %s" % pstr)
            p = st[ip]
            v = int(st[:ip])
            if v < 0:
                raise ValueError("Negative values are not supported")
            if p == "D":
                self.add_days(v)
            elif p == "W":
                self.add_weeks(v)
            elif p == "M":
                self.add_months(v)
            elif p == "H":
                self.add_hours(v)
            elif p == "Y":
                self.add_years(v)
            ip += 1
            st = st[ip:]
        return self

    def __add__(self, other: Any) -> Self:
        p = self.make(other)
        period = self.model_copy()
        period.add_days(p.days)
        period.add_months(p.months)
        period.add_hours(p.hours)
        return period

    def __radd__(self, other: Any) -> Self:
        return self + other

    def __eq__(self, other: Any) -> bool:
        period = self.make(other)
        return (
            self.months == period.months
            and self.days == period.days
            and self.hours == period.hours
        )
