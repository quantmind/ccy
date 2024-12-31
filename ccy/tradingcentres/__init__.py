from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
import holidays
import holidays.countries
import holidays.financial

isoweekend = frozenset((6, 7))
oneday = timedelta(days=1)

trading_centres: dict[str, TradingCentre] = {}


def prevbizday(dte: date, nd: int = 1, tcs: str | None = None) -> date:
    return centres(tcs).prevbizday(dte, nd)


def nextbizday(dte: date, nd: int = 1, tcs: str | None = None) -> date:
    return centres(tcs).nextbizday(dte, nd)


def centres(codes: str | None = None) -> TradingCentres:
    tcs = TradingCentres()
    if codes:
        lcs = codes.upper().replace(" ", "").split(",")
        for code in lcs:
            tc = trading_centres.get(code)
            if tc:
                tcs.centres[tc.code] = tc
    return tcs


@dataclass
class TradingCentre:
    code: str
    calendar: holidays.HolidayBase

    def isholiday(self, dte: date) -> bool:
        return dte in self.calendar


@dataclass
class TradingCentres:
    centres: dict[str, TradingCentre] = field(default_factory=dict)

    @property
    def code(self) -> str:
        return ",".join(sorted(self.centres))

    def isbizday(self, dte: date) -> bool:
        if dte.isoweekday() in isoweekend:
            return False
        for c in self.centres.values():
            if c.isholiday(dte):
                return False
        return True

    def nextbizday(self, dte: date, nd: int = 1) -> date:
        n = 0
        while not self.isbizday(dte):
            dte += oneday
        while n < nd:
            dte += oneday
            if self.isbizday(dte):
                n += 1
        return dte

    def prevbizday(self, dte: date, nd: int = 1) -> date:
        n = 0
        if nd < 0:
            return self.nextbizday(dte, -nd)
        else:
            while not self.isbizday(dte):
                dte -= oneday
            n = 0
            while n < nd:
                dte -= oneday
                if self.isbizday(dte):
                    n += 1
        return dte


trading_centres.update(
    (tc.code, tc)
    for tc in (
        TradingCentre(
            code="TGT",
            calendar=holidays.financial.european_central_bank.EuropeanCentralBank(),  # type: ignore [no-untyped-call]
        ),
        TradingCentre(
            code="LON",
            calendar=holidays.countries.united_kingdom.UnitedKingdom(),  # type: ignore [no-untyped-call]
        ),
        TradingCentre(
            code="NY",
            calendar=holidays.countries.united_states.UnitedStates(),  # type: ignore [no-untyped-call]
        ),
    )
)
