from datetime import date

import pytest
from ccy.tradingcentres import nextbizday, prevbizday, centres


@pytest.fixture()
def dates():
    return [
        date(2010, 4, 1),  # Thu
        date(2010, 4, 2),  # Fri
        date(2010, 4, 3),  # Sat
        date(2010, 4, 5),  # Mon
        date(2010, 4, 6),  # Tue
    ]


def test_NextBizDay(dates):
    assert dates[1] == nextbizday(dates[0])
    assert dates[4] == nextbizday(dates[1], 2)


def test_nextBizDay0(dates):
    assert dates[0] == nextbizday(dates[0], 0)
    assert dates[3] == nextbizday(dates[2], 0)


def test_prevBizDay(dates):
    assert dates[0] == prevbizday(dates[1])
    assert dates[1] == prevbizday(dates[3])
    assert dates[1] == prevbizday(dates[4], 2)
    assert dates[0] == prevbizday(dates[4], 3)


def test_TGT():
    tcs = centres("TGT")
    assert tcs.code == "TGT"
    assert not tcs.isbizday(date(2009, 12, 25))
    assert not tcs.isbizday(date(2010, 1, 1))
