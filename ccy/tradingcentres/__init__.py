from .centres import centres, TradingCentre

__all__ = ['centres', 'TradingCentre', 'prevbizday', 'nextbizday']


def prevbizday(dte=None, nd=1, tcs=None):
    tcs = centres(tcs)
    return tcs.prevbizday(dte, nd)


def nextbizday(dte=None, nd=1, tcs=None):
    tcs = centres(tcs)
    return tcs.nextbizday(dte, nd)
