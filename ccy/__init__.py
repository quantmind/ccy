"""Python currencies
"""
import os

VERSION = (0, 7, 0, 'final', 0)


def get_version(version):
    assert len(version) == 5
    assert version[3] in ('alpha', 'beta', 'rc', 'final')
    main = '.'.join(map(str, version[:3]))
    sub = '' if version[3] == 'final' else '-%s.%s' % tuple(version[3:])
    return main + sub


__version__ = get_version(VERSION)


if os.environ.get('package_info') != 'odm':

    from .core import currency as _currency
    from .data.currency import make_ccys

    _currency.ccydb.load = make_ccys

    from .core.currency import *    # noqa
    from .core.country import *     # noqa
    from .core.daycounter import *  # noqa
    from .dates import *            # noqa

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
