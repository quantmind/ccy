'''Python currencies'''
VERSION = (0, 5, 3)
 
def get_version():
    if len(VERSION) == 3:
        v = '%s.%s.%s' % VERSION
    else:
        v = '%s.%s' % VERSION[:2]
    return v
 
__version__  = get_version()
__license__  = "BSD"
__author__   = "Luca Sbardella"
__contact__  = "luca@quantmind.com"
__homepage__ = "http://code.google.com/p/ccy/"


from .core import currency as _currency

from .data.currency import make_ccys
_currency.ccydb.load = make_ccys

from .core.currency import *
from .core.country import *
from .core.daycounter import *
from .dates import *

# Shortcuts
cross     = lambda code : currency(code).as_cross()
crossover = lambda code : currency(code).as_cross('/')

def all():
    return currencydb().keys()

def g7():
    return ['EUR','GBP','USD','CAD']

def g10():
    return g7() + ['CHF','SEK','JPY']

def g10m():
    '''modified g10. G10 + AUD,NZD,NOK'''
    return g10() + ['AUD','NZD','NOK']

