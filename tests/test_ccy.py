import json
import pickle
from io import StringIO as StreamIO

import pytest
from ccy import (
    CountryError,
    ccypair,
    countryccy,
    currency,
    currency_pair,
    currencydb,
    dump_currency_table,
    set_new_country,
)
from ccy.core.country import eurozone


def test_defaultcountry():
    ccys = currencydb()
    for ccy in ccys.values():
        if ccy.code != "XBT":
            assert ccy.code[:2] == ccy.default_country


def test_iso():
    ccys = currencydb()
    iso = {}
    for ccy in ccys.values():
        assert ccy.isonumber not in iso
        iso[ccy.isonumber] = ccy


def test_2letters():
    ccys = currencydb()
    twol = {}
    for ccy in ccys.values():
        assert ccy.twoletterscode not in twol
        twol[ccy.twoletterscode] = ccy


def test_new_country():
    with pytest.raises(CountryError):
        set_new_country("EU", "EUR", "Eurozone")


def test_eurozone():
    assert len(eurozone) == 19
    for c in eurozone:
        assert countryccy(c) == "EUR"


def test_countryccy():
    assert "AUD" == countryccy("au")
    assert "EUR" == countryccy("eu")


def test_ccy_pair():
    p = ccypair("usdchf")
    assert str(p) == "USDCHF"
    p = p.over()
    assert str(p) == "CHFUSD"
    p = ccypair("EURUSD")
    assert p == p.over()


def test_pickle():
    c = currency("eur")
    cd = pickle.dumps(c)
    c2 = pickle.loads(cd)
    assert c == c2
    assert c != "EUR"


def test_json():
    c = currency("eur")
    info = c.info()
    json.dumps(info)


def test_swap():
    c1 = currency("eur")
    c2 = currency("chf")
    inv, a1, a2 = c1.swap(c2)
    assert not inv
    assert c1 == a1
    assert c2 == a2
    inv, a1, a2 = c2.swap(c1)
    assert inv
    assert c1 == a1
    assert c2 == a2


def test_as_cross():
    c1 = currency("eur")
    c2 = currency("chf")
    assert c1.as_cross() == "EURUSD"
    assert c2.as_cross() == "USDCHF"
    assert c1.as_cross("/") == "EUR/USD"
    assert c2.as_cross("/") == "USD/CHF"


def test_print():
    stream = StreamIO()
    c2 = currency("chf")
    c2.printinfo(stream)
    value = stream.getvalue()
    assert value


def test_dump_currency_table():
    db = currencydb()
    table = list(dump_currency_table())
    assert len(table) == len(db) + 1


def test_description():
    c = currency("eur")
    assert c.description() == "EUR / USD Spot Exchange Rate"
    c = currency("chf")
    assert c.description() == "USD / CHF Spot Exchange Rate"
    c = currency("usd")
    assert c.description() == "Dollar"


def test_spot_price():
    c1 = currency("eur")
    c2 = currency("gbp")
    assert c1.spot(c2, 1.3, 1.6) == 1.3 / 1.6
    assert c2.spot(c1, 1.6, 1.3) == 1.3 / 1.6


def test_currency_pair():
    p = currency_pair("eurgbp")
    assert p.ccy1.code == "EUR"
    assert p.ccy2.code == "GBP"
    assert p.mkt() == p
    p = currency_pair("gbpeur")
    assert p.mkt() != p
