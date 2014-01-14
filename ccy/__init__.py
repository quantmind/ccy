'''Python currencies'''
VERSION = (0, 6, 0, 'final', 0)


def get_version(version):
    assert len(version) == 5
    assert version[3] in ('alpha', 'beta', 'rc', 'final')
    main = '.'.join(map(str, version[:3]))
    sub = '' if version[3] == 'final' else '-%s.%s' % tuple(version[3:])
    return main + sub


__version__ = get_version(VERSION)
__license__ = "BSD"
__author__ = "Luca Sbardella"
__contact__ = "luca@quantmind.com"
__homepage__ = "http://code.google.com/p/ccy/"


import os

if os.environ.get('ccy_setup_running') != 'yes':

    from .core import currency as _currency
    from .data.currency import make_ccys

    _currency.ccydb.load = make_ccys

    from .core.currency import *
    from .core.country import *
    from .core.daycounter import *
    from .dates import *

    # Shortcuts
    cross = lambda code: currency(code).as_cross()
    crossover = lambda code: currency(code).as_cross('/')

    def all():
        return currencydb().keys()

    def g7():
        return ['EUR', 'GBP', 'USD', 'CAD']

    def g10():
        return g7() + ['CHF', 'SEK', 'JPY']

    def g10m():
        '''modified g10. G10 + AUD, NZD, NOK'''
        return g10() + ['AUD', 'NZD', 'NOK']
