from __future__ import annotations

from typing import Any


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


def safediv(x: int, d: int) -> int:
    return x // d if x >= 0 else -(-x // d)


def safemod(x: int, d: int) -> int:
    return x % d if x >= 0 else -(-x % d)


class Period:
    def __init__(self, months: int = 0, days: int = 0) -> None:
        self._months = months
        self._days = days

    @classmethod
    def make(cls, data: Any) -> Period:
        if isinstance(data, cls):
            return data
        elif isinstance(data, str):
            return cls().add_tenure(data)
        else:
            raise TypeError("Cannot convert %s to Period" % data)

    def isempty(self) -> bool:
        return self._months == 0 and self._days == 0

    def add_days(self, days: int) -> None:
        self._days += days

    def add_weeks(self, weeks: int) -> None:
        self._days += int(7 * weeks)

    def add_months(self, months: int) -> None:
        self._months += months

    def add_years(self, years: int) -> None:
        self._months += int(12 * years)

    @property
    def years(self) -> int:
        return safediv(self._months, 12)

    @property
    def months(self) -> int:
        return safemod(self._months, 12)

    @property
    def weeks(self) -> int:
        return safediv(self._days, 7)

    @property
    def days(self) -> int:
        return safemod(self._days, 7)

    @property
    def totaldays(self) -> int:
        return 30 * self._months + self._days

    def __repr__(self) -> str:
        """The period string"""
        return self.components()

    def __str__(self) -> str:
        return self.__repr__()

    def components(self) -> str:
        """The period string"""
        p = ""
        neg = self.totaldays < 0
        y = self.years
        m = self.months
        w = self.weeks
        d = self.days
        if y:
            p = "%sY" % abs(y)
        if m:
            p = "%s%sM" % (p, abs(m))
        if w:
            p = "%s%sW" % (p, abs(w))
        if d:
            p = "%s%sD" % (p, abs(d))
        return "-" + p if neg else p

    def simple(self) -> str:
        """A string representation with only one period delimiter."""
        if self._days:
            return "%sD" % self.totaldays
        elif self.months:
            return "%sM" % self._months
        elif self.years:
            return "%sY" % self.years
        else:
            return ""

    def add_tenure(self, pstr: str) -> Period:
        if isinstance(pstr, self.__class__):
            self._months += pstr._months
            self._days += pstr._days
            return self
        st = str(pstr).upper()
        done = False
        sign = 1
        while not done:
            if not st:
                done = True
            else:
                ip = find_first_of(st, "DWMY")
                if ip == -1:
                    raise ValueError("Unknown period %s" % pstr)
                p = st[ip]
                v = int(st[:ip])
                sign = sign if v > 0 else -sign
                v = sign * abs(v)
                if p == "D":
                    self.add_days(v)
                elif p == "W":
                    self.add_weeks(v)
                elif p == "M":
                    self.add_months(v)
                elif p == "Y":
                    self.add_years(v)
                ip += 1
                st = st[ip:]
        return self

    def __add__(self, other: Any) -> Period:
        p = self.make(other)
        return self.__class__(self._months + p._months, self._days + p._days)

    def __radd__(self, other: Any) -> Period:
        return self + other

    def __sub__(self, other: Any) -> Period:
        p = self.make(other)
        return self.__class__(self._months - p._months, self._days - p._days)

    def __rsub__(self, other: Any) -> Period:
        return self.make(other) - self

    def __gt__(self, other: Any) -> bool:
        return self.totaldays > self.make(other).totaldays

    def __lt__(self, other: Any) -> bool:
        return self.totaldays < self.make(other).totaldays

    def __ge__(self, other: Any) -> bool:
        return self.totaldays >= self.make(other).totaldays

    def __le__(self, other: Any) -> bool:
        return self.totaldays <= self.make(other).totaldays

    def __eq__(self, other: Any) -> bool:
        return self.totaldays == self.make(other).totaldays
