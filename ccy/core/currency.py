from __future__ import annotations

import sys
from typing import Any, Callable, NamedTuple

from .data import make_ccys

usd_order = 5


def to_string(v: Any) -> str:
    if isinstance(v, bytes):
        return v.decode("utf-8")
    else:
        return "%s" % v


def overusdfun(v1: float) -> float:
    return v1


def overusdfuni(v1: float) -> float:
    return 1.0 / v1


class ccy(NamedTuple):
    code: str
    isonumber: str
    twoletterscode: str
    order: int
    name: str
    rounding: int
    default_country: str
    fixeddc: str = "Act/365"
    floatdc: str = "Act/365"
    fixedfreq: str = ""
    floatfreq: str = ""
    future: str = ""
    symbol_raw: str = r"\00a4"
    html: str = ""

    @property
    def symbol(self) -> str:
        return self.symbol_raw.encode("utf-8").decode("unicode_escape")

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ccy):
            return other.code == self.code
        return False

    def description(self) -> str:
        if self.order > usd_order:
            v = "USD / %s" % self.code
        else:
            v = "%s / USD" % self.code
        if self.order != usd_order:
            return "%s Spot Exchange Rate" % v
        else:
            return "Dollar"

    def info(self) -> dict[str, Any]:
        data = self._asdict()
        data["symbol"] = self.symbol
        return data

    def printinfo(self, stream: Any | None = None) -> None:
        info = self.info()
        stream = stream or sys.stdout
        for k, v in info.items():
            stream.write(to_string("%s: %s\n" % (k, v)))

    def __str__(self) -> str:
        return self.code

    def swap(self, c2: ccy) -> tuple[bool, ccy, ccy]:
        """
        put the order of currencies as market standard
        """
        inv = False
        c1 = self
        if c1.order > c2.order:
            ct = c1
            c1 = c2
            c2 = ct
            inv = True
        return inv, c1, c2

    def overusdfunc(self) -> Callable[[float], float]:
        if self.order > usd_order:
            return overusdfuni
        else:
            return overusdfun

    def usdoverfunc(self) -> Callable[[float], float]:
        if self.order > usd_order:
            return overusdfun
        else:
            return overusdfuni

    def as_cross(self, delimiter: str = "") -> str:
        """
        Return a cross rate representation with respect USD.
        @param delimiter: could be '' or '/' normally
        """
        if self.order > usd_order:
            return "USD%s%s" % (delimiter, self.code)
        else:
            return "%s%sUSD" % (self.code, delimiter)

    def spot(self, c2: ccy, v1: float, v2: float) -> float:
        if self.order > c2.order:
            vt = v1
            v1 = v2
            v2 = vt
        return v1 / v2


class ccy_pair(NamedTuple):
    """
    Currency pair such as EURUSD, USDCHF

    XXXYYY - XXX is the foreign currency, while YYY is the base currency

    XXXYYY means 1 unit of of XXX cost XXXYYY units of YYY
    """

    ccy1: ccy
    ccy2: ccy

    @property
    def code(self) -> str:
        return "%s%s" % (self.ccy1, self.ccy2)

    def __repr__(self) -> str:
        return "%s: %s" % (self.__class__.__name__, self.code)

    def __str__(self) -> str:
        return self.code

    def mkt(self) -> ccy_pair:
        if self.ccy1.order > self.ccy2.order:
            return ccy_pair(self.ccy2, self.ccy1)
        else:
            return self

    def over(self, name: str = "usd") -> ccy_pair:
        """Returns a new currency pair with the *over* currency as
        second part of the pair (Foreign currency)."""
        name = name.upper()
        if self.ccy1.code == name.upper():
            return ccy_pair(self.ccy2, self.ccy1)
        else:
            return self


class ccydb(dict[str, ccy]):
    def insert(self, *args: Any, **kwargs: Any) -> None:
        c = ccy(*args, **kwargs)
        self[c.code] = c


def currencydb() -> ccydb:
    global _ccys
    if not _ccys:
        _ccys = ccydb()
        make_ccys(_ccys)
    return _ccys


def ccypairsdb() -> dict[str, ccy_pair]:
    global _ccypairs
    if not _ccypairs:
        _ccypairs = make_ccypairs()
    return _ccypairs


def currency(code: str | ccy) -> ccy:
    c = currencydb()
    return c[str(code).upper()]


def ccypair(code: str | ccy_pair) -> ccy_pair:
    c = ccypairsdb()
    return c[str(code).upper()]


def currency_pair(code: str | ccy_pair) -> ccy_pair:
    """Construct a :class:`ccy_pair` from a six letter string."""
    c = str(code)
    c1 = currency(c[:3])
    c2 = currency(c[3:])
    return ccy_pair(c1, c2)


def make_ccypairs() -> dict[str, ccy_pair]:
    ccys = currencydb()
    db = {}

    for ccy1 in ccys.values():
        od = ccy1.order
        for ccy2 in ccys.values():
            if ccy2.order <= od:
                continue
            p = ccy_pair(ccy1, ccy2)
            db[p.code] = p
    return db


def dump_currency_table() -> list:
    return [c.info() for c in sorted(currencydb().values(), key=lambda x: x.order)]


_ccys: ccydb = ccydb()
_ccypairs: dict[str, ccy_pair] = {}
