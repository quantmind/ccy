from __future__ import annotations

from datetime import date, timedelta
from typing_extensions import Annotated, Doc

import holidays
import holidays.countries
import holidays.financial
from pydantic import BaseModel, Field

isoweekend = frozenset((6, 7))
oneday = timedelta(days=1)

trading_centres: dict[str, TradingCentre] = {}


def prevbizday(
    dte: Annotated[date, Doc("The reference date")],
    nd: Annotated[int, Doc("Number of business days to move back")] = 1,
    tcs: Annotated[str | None, Doc("Comma-separated trading centre codes")] = None,
) -> date:
    """Return the date nd business days before dte."""
    return centres(tcs).prevbizday(dte, nd)


def nextbizday(
    dte: Annotated[date, Doc("The reference date")],
    nd: Annotated[
        int,
        Doc("Number of business days to move forward; 0 adjusts to next biz day"),
    ] = 1,
    tcs: Annotated[str | None, Doc("Comma-separated trading centre codes")] = None,
) -> date:
    """Return the date nd business days after dte."""
    return centres(tcs).nextbizday(dte, nd)


def centres(
    codes: Annotated[
        str | None, Doc("Comma-separated trading centre codes, e.g. 'LON,NY'")
    ] = None,
) -> TradingCentres:
    """Return a [TradingCentres][ccy.tradingcentres.TradingCentres] instance
    for the given centre codes."""
    tcs = TradingCentres()
    if codes:
        lcs = codes.upper().replace(" ", "").split(",")
        for code in lcs:
            tc = trading_centres.get(code)
            if tc:
                tcs.centres[tc.code] = tc
    return tcs


class TradingCentre(BaseModel, arbitrary_types_allowed=True):
    code: str = Field(description="The code of the trading centre")
    calendar: holidays.HolidayBase = Field(
        exclude=True,
        description="The holiday calendar of the trading centre",
    )

    def isholiday(self, dte: Annotated[date, Doc("The date to check")]) -> bool:
        """Return True if the date is a holiday."""
        return dte in self.calendar


class TradingCentres(BaseModel):
    centres: dict[str, TradingCentre] = Field(default_factory=dict)

    @property
    def code(self) -> str:
        """Comma-separated sorted codes of the trading centres."""
        return ",".join(sorted(self.centres))

    def isbizday(self, dte: Annotated[date, Doc("The date to check")]) -> bool:
        """Return True if the date is a business day across all centres."""
        if dte.isoweekday() in isoweekend:
            return False
        for c in self.centres.values():
            if c.isholiday(dte):
                return False
        return True

    def nextbizday(
        self,
        dte: Annotated[date, Doc("The reference date")],
        nd: Annotated[
            int,
            Doc("Number of business days to move forward; 0 adjusts to next biz day"),
        ] = 1,
    ) -> date:
        """Return the date nd business days after dte."""
        n = 0
        while not self.isbizday(dte):
            dte += oneday
        while n < nd:
            dte += oneday
            if self.isbizday(dte):
                n += 1
        return dte

    def prevbizday(
        self,
        dte: Annotated[date, Doc("The reference date")],
        nd: Annotated[int, Doc("Number of business days to move back")] = 1,
    ) -> date:
        """Return the date nd business days before dte."""
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
