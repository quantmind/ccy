from datetime import date, datetime

import pytest
from ccy import date2juldate, date2yyyymmdd, juldate2date, period, todate, yyyymmdd2date


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
    assert b.months == 3
    c = period("-3m")
    assert c.years == 0
    assert c.months == -3


def test_add_period():
    a = period("4Y")
    b = period("1Y3M")
    c = a + b
    assert c.years == 5
    assert c.months == 3


def test_add_string():
    a = period("4y")
    assert a + "3m" == period("4y3m")
    assert "3m" + a == period("4y3m")


def test_subtract_period():
    a = period("4Y")
    b = period("1Y")
    c = a - b
    assert c.years == 3
    assert c.months == 0
    c = period("3Y") - period("1Y3M")
    assert c.years == 1
    assert c.months == 9
    assert str(c) == "1Y9M"


def test_subtract_string():
    a = period("4y")
    assert a - "3m" == period("3y9m")
    assert "5y" - a == period("1y")
    assert "3m" - a == period("-3y9m")


def test_compare():
    a = period("4Y")
    b = period("4Y")
    c = period("1Y2M")
    assert a == b
    assert a >= b
    assert a <= b
    assert c <= a
    assert c < a
    assert (c == a) is False
    assert (c >= b) is False
    assert c > a - b


def test_week():
    p = period("7d")
    assert p.weeks == 1
    assert str(p) == "1W"
    p.add_weeks(3)
    assert p.weeks == 4
    assert str(p) == "4W"
    assert not p.isempty()
    p = period("3w2d")
    assert not p.isempty()
    assert p.weeks == 3
    assert str(p) == "3W2D"


def test_empty():
    assert not period("3y").isempty()
    assert not period("1m").isempty()
    assert not period("3d").isempty()
    assert period().isempty()


def test_addperiod():
    p = period("3m")
    a = period("6m")
    assert a.add_tenure(p) == a
    assert str(a) == "9M"


def test_error():
    with pytest.raises(ValueError):
        period("5y6g")


def test_simple():
    assert period("3m2y").simple() == "27M"
    assert period("-3m2y").simple() == "-27M"
    assert period("3d2m").simple() == "63D"
    assert period("2y").simple() == "2Y"


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


# def testDate2Timestamp():
#     for d,jd,y,ts in .dates:
#         if ts is not None:
#             .assertEqual(ts,date2timestamp(d))

# def testTimestamp2Date():
#     for d,jd,y,ts in .dates:
#         if ts is not None:
#             .assertEqual(d,timestamp2date(ts))
