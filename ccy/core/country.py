#
# Requires pytz 2008i or higher
#
from .currency import currencydb

# Eurozone countries (officially the euro area)
# see http://en.wikipedia.org/wiki/Eurozone
# using ISO 3166-1 alpha-2 country codes
# see http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
#
eurozone = tuple(('AT BE CY DE EE ES FI FR GR IE IT LU LV LT MT '
                  'NL PT SI SK').split(' '))


def print_eurozone():
    for c in sorted(map(country, eurozone)):
        print(c)


_countries = None
_country_ccys = None
_country_maps = {}


class CountryError(Exception):
    pass


def country(code):
    cdb = countries()
    code = country_map(code)
    return cdb.get(code, '')


def countryccy(code):
    cdb = countryccys()
    code = str(code).upper()
    return cdb.get(code, None)


def countries():
    '''
    get country dictionar from pytz and add some extra.
    '''
    global _countries
    if not _countries:
        v = {}
        _countries = v
        try:
            from pytz import country_names
            for k, n in country_names.items():
                v[k.upper()] = n
        except Exception:
            pass
    return _countries


def countryccys():
    '''
    Create a dictionary with keys given by countries ISO codes and values
    given by their currencies
    '''
    global _country_ccys
    if not _country_ccys:
        v = {}
        _country_ccys = v
        ccys = currencydb()
        for c in eurozone:
            v[c] = 'EUR'
        for c in ccys.values():
            if c.default_country:
                v[c.default_country] = c.code
    return _country_ccys


def set_country_map(cfrom, cto, name=None, replace=True):
    '''
    Set a mapping between a country code to another code
    '''
    global _country_maps
    cdb = countries()
    cfrom = str(cfrom).upper()
    c = cdb.get(cfrom)
    if c:
        if name:
            c = name
        cto = str(cto).upper()
        if cto in cdb:
            raise CountryError('Country %s already in database' % cto)
        cdb[cto] = c
        _country_maps[cfrom] = cto
        ccys = currencydb()
        cccys = countryccys()
        ccy = cccys[cfrom]
        cccys[cto] = ccy

        # If set, remove cfrom from database
        if replace:
            ccy = ccys.get(ccy)
            ccy.default_country = cto
            cdb.pop(cfrom)
            cccys.pop(cfrom)
    else:
        raise CountryError('Country %s not in database' % c)


def set_new_country(code, ccy, name):
    '''
    Add new country code to database
    '''
    code = str(code).upper()
    cdb = countries()
    if code in cdb:
        raise CountryError('Country %s already in database' % code)
    ccys = currencydb()
    ccy = str(ccy).upper()
    if ccy not in ccys:
        raise CountryError('Currency %s not in database' % ccy)
    cdb[code] = str(name)
    cccys = countryccys()
    cccys[code] = ccy


def country_map(code):
    '''
    Country mapping
    '''
    code = str(code).upper()
    global _country_maps
    return _country_maps.get(code, code)


# Add eurozone to list of Countries
set_new_country('EU', 'EUR', 'Eurozone')
