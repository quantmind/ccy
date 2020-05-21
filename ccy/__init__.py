"""Python currencies"""

__version__ = "1.2.0"


from .core.country import (
    CountryError,
    countries,
    country,
    country_map,
    countryccy,
    eurozone,
    print_eurozone,
    set_country_map,
    set_new_country,
)
from .core.currency import (
    ccypair,
    currency,
    currency_pair,
    currencydb,
    dump_currency_table,
)
from .core.daycounter import ActActYears, alldc, getdc
from .dates.converters import (
    date2juldate,
    date2timestamp,
    date2yyyymmdd,
    date_from_string,
    jstimestamp,
    juldate2date,
    timestamp2date,
    todate,
    yyyymmdd2date,
)
from .dates.futures import future_date_to_code, future_month_dict
from .dates.period import Period, period

__all__ = [
    "currency",
    "currencydb",
    "ccypair",
    "currency_pair",
    "dump_currency_table",
    #
    "getdc",
    "ActActYears",
    "alldc",
    #
    "country",
    "countryccy",
    "set_new_country",
    "countries",
    "set_country_map",
    "country_map",
    "CountryError",
    "eurozone",
    "print_eurozone",
    "future_date_to_code",
    "future_month_dict",
    "period",
    "Period",
    "todate",
    "date2timestamp",
    "timestamp2date",
    "yyyymmdd2date",
    "date2yyyymmdd",
    "juldate2date",
    "date2juldate",
    "date_from_string",
    "jstimestamp",
]


# Shortcuts
def cross(code):
    return currency(code).as_cross()


def crossover(code):
    return currency(code).as_cross("/")


def all():
    return currencydb().keys()


def g7():
    return ["EUR", "GBP", "USD", "CAD"]


def g10():
    return g7() + ["CHF", "SEK", "JPY"]


def g10m():
    """modified g10 = G10 + AUD, NZD, NOK
    """
    return g10() + ["AUD", "NZD", "NOK"]
