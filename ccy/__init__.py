"""Python currencies"""

__version__ = '1.0.0'


from .core.currency import (
    currency, currencydb, ccypair, currency_pair,
    dump_currency_table
)
from .core.country import (
    country, countryccy, set_new_country,
    countries, set_country_map, country_map,
    CountryError, eurozone, print_eurozone
)
from .core.daycounter import getdc, ActActYears, alldc
from .dates.converters import (
    todate, date2timestamp, timestamp2date, yyyymmdd2date,
    date2yyyymmdd, juldate2date, date2juldate, date_from_string,
    jstimestamp
)
from .dates.futures import future_date_to_code, future_month_dict
from .dates.period import period, Period


__all__ = [
    'currency', 'currencydb', 'ccypair', 'currency_pair',
    'dump_currency_table',
    #
    'getdc', 'ActActYears', 'alldc',
    #
    'country', 'countryccy', 'set_new_country',
    'countries', 'set_country_map', 'country_map',
    'CountryError', 'eurozone', 'print_eurozone',
    'future_date_to_code', 'future_month_dict',
    'period', 'Period',
    'todate', 'date2timestamp', 'timestamp2date',
    'yyyymmdd2date', 'date2yyyymmdd', 'juldate2date',
    'date2juldate', 'date_from_string', 'jstimestamp'
]


# Shortcuts
def cross(code):
    return currency(code).as_cross()


def crossover(code):
    return currency(code).as_cross('/')


def all():
    return currencydb().keys()


def g7():
    return ['EUR', 'GBP', 'USD', 'CAD']


def g10():
    return g7() + ['CHF', 'SEK', 'JPY']


def g10m():
    """modified g10 = G10 + AUD, NZD, NOK
    """
    return g10() + ['AUD', 'NZD', 'NOK']
