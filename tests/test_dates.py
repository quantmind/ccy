from datetime import date, datetime

import pytest
from dateutil.relativedelta import relativedelta
from pydantic import BaseModel, Field

from ccy import (
    Period,
    date2juldate,
    date2yyyymmdd,
    juldate2date,
    period,
    todate,
    yyyymmdd2date,
)


class RateModel(BaseModel):
    rate: float = Field(..., description="Interest rate")
    period: Period = Field(
        default_factory=lambda: period("3m"),
        description="Compounding period",
    )


@pytest.fixture()
def dates():
    return [
        (date(2010, 6, 11), 40340, 20100611, 1276210800),
        (date(2009, 4, 2), 39905, 20090402, 1238626800),
        (date(1996, 2, 29), 35124, 19960229, 825552000),
        (date(1970, 1, 1), 25569, 19700101, 0),
        (date(1900, 1, 1), 1, 19000101, None),
    ]


def test_period():
    a = period("5Y")
    assert a.years == 5
    b = period("1y3m")
    assert b.years == 1
    assert b.months_remaining == 3
    c = period("3m")
    assert c.years == 0
    assert c.months_remaining == 3


def test_add_period():
    a = period("4Y")
    b = period("1Y3M")
    c = a + b
    assert c.years == 5
    assert c.months_remaining == 3


def test_add_string():
    a = period("4y")
    assert a + "3m" == period("4y3m")
    assert "3m" + a == period("4y3m")


def test_compare():
    a = period("4Y")
    b = period("4Y")
    c = period("1Y2M")
    assert a == b
    assert a != c
    assert (c == a) is False


def test_week():
    p = period("7d")
    assert p.weeks == 1
    assert p.days_remaining == 0
    assert p.to_str() == "1W"
    p.add_weeks(3)
    assert p.weeks == 4
    assert p.to_str() == "4W"
    assert not p.isempty()
    p = period("3w2d")
    assert not p.isempty()
    assert p.weeks == 3
    assert p.to_str() == "3W2D"


def test_empty():
    assert not period("3y").isempty()
    assert not period("1m").isempty()
    assert not period("3d").isempty()
    assert period().isempty()


def test_addperiod():
    p = period("3m")
    a = period("6m")
    assert a.add_period(p) is a
    assert a.to_str() == "9M"


def test_error():
    with pytest.raises(ValueError):
        period("5y6g")


def test_make_from_period_instance():
    p = period("3M")
    assert Period.make(p) is p


def test_make_from_relativedelta():
    rd = relativedelta(years=1, months=3, days=5, hours=2)
    p = Period.make(rd)
    assert p.months == 15
    assert p.days == 5
    assert p.hours == 2


def test_make_type_error():
    with pytest.raises(TypeError):
        Period.make(42)


def test_hours():
    p = period("2H")
    assert p.hours == 2
    assert p.isempty() is False
    assert p.to_str() == "2H"


def test_add_hours_overflow():
    p = period("22H")
    p.add_hours(4)
    assert p.days == 1
    assert p.hours == 2
    assert p.to_str() == "1D2H"


def test_add_hours_negative():
    p = period("1H")
    with pytest.raises(ValueError):
        p.add_hours(-1)


def test_add_days_negative():
    p = period("1D")
    with pytest.raises(ValueError):
        p.add_days(-1)


def test_add_weeks_negative():
    p = period("1W")
    with pytest.raises(ValueError):
        p.add_weeks(-1)


def test_add_months_negative():
    p = period("1M")
    with pytest.raises(ValueError):
        p.add_months(-1)


def test_add_years_negative():
    p = period("1Y")
    with pytest.raises(ValueError):
        p.add_years(-1)


def test_to_str_full():
    p = Period(months=14, days=10, hours=3)
    assert p.to_str() == "1Y2M1W3D3H"


def test_to_relativedelta():
    p = Period(months=14, days=10, hours=3)
    rd = p.to_relativedelta()
    assert rd.years == 1
    assert rd.months == 2
    assert rd.days == 10  # dateutil normalizes weeks into days
    assert rd.hours == 3


def test_radd():
    a = period("1Y")
    c = "6M" + a
    assert c == period("1Y6M")


def test_add_period_with_period_instance():
    a = period("1Y")
    b = period("3M")
    a.add_period(b)
    assert a == period("1Y3M")


def test_equality_with_hours():
    a = Period(months=3, days=0, hours=2)
    b = Period(months=3, days=0, hours=2)
    c = Period(months=3, days=0, hours=1)
    assert a == b
    assert a != c


def test_date2JulDate(dates):
    for d, jd, y, ts in dates:
        assert jd == date2juldate(d)


def test_JulDate2Date(dates):
    for d, jd, y, ts in dates:
        assert d == juldate2date(jd)


def test_Date2YyyyMmDd(dates):
    for d, jd, y, ts in dates:
        assert y == date2yyyymmdd(d)


def test_YyyyMmDd2Date(dates):
    for d, jd, y, ts in dates:
        assert d == yyyymmdd2date(y)


def test_datetime2Juldate():
    jd = date2juldate(datetime(2013, 3, 8, 11, 20, 45))
    assert jd == 41341.47274305556


def test_Juldate2datetime():
    dt = juldate2date(41341.47274305556)
    dt2 = datetime(2013, 3, 8, 11, 20, 45)
    assert dt == dt2


def test_string():
    target = date(2014, 1, 5)
    assert todate("2014 Jan 05") == target


def test_todate_nothing():
    with pytest.raises(ValueError):
        todate("")
    with pytest.raises(ValueError):
        todate(None)


def test_todate_datetime():
    assert todate(datetime.now()) == date.today()
    assert todate(date.today()) == date.today()


# def testDate2Timestamp():
#     for d,jd,y,ts in .dates:
#         if ts is not None:
#             .assertEqual(ts,date2timestamp(d))

# def testTimestamp2Date():
#     for d,jd,y,ts in .dates:
#         if ts is not None:
#             .assertEqual(d,timestamp2date(ts))
