from datetime import date, timedelta

import pytest

from ccy.dates.utils import utcnow
from ccy import DayCounter


def test_alldc():
    assert len(DayCounter) == 6


def test_dcf():
    for dc in DayCounter:
        assert dc.value == str(dc)
        start = date.today()
        assert dc.dcf(start, start + timedelta(days=1)) > 0


def test_invalid_dc():
    with pytest.raises(ValueError):
        DayCounter("kaputt")


def test_with_datetime():
    for dc in DayCounter:
        start = utcnow()
        dc1 = dc.dcf(start, start.date() + timedelta(days=1))
        dc2 = dc.dcf(start, start + timedelta(days=1))
        assert dc1 > 0
        assert dc2 > 0
        if dc not in (DayCounter.THIRTY360, DayCounter.THIRTYE360):
            assert dc1 < dc2, f"{dc}"
