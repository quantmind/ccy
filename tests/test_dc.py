from datetime import date, timedelta

import pytest

import ccy


def test_alldc():
    assert len(ccy.alldc()) == 4


def test_getdb():
    for name in ("ACT/365", "ACT/ACT", "ACT/360", "30/360"):
        assert ccy.getdc(name).name == name
        start = date.today()
        assert ccy.getdc(name).count(start, start + timedelta(days=1)) == 1
        assert ccy.getdc(name).dcf(start, start + timedelta(days=1)) > 0

    with pytest.raises(KeyError):
        ccy.getdc("kaputt")
