'''Day Counter for Counting time between 2 dates.
Implemented::

    * Actual 360
    * Actual 365
    * 30 / 360
    * Actual Actual
'''
from copy import copy
from datetime import date


__all__ = ['getdc', 'ActActYears', 'alldc']


def getdc(name):
    dc = _day_counters.get(name)
    if dc:
        return dc()
    else:
        return None


def alldc():
    global _day_counters
    return copy(_day_counters)


def ActActYears(dt):
    y = dt.year
    r = y % 4
    a = 0.0
    if r > 0:
        a = 1.0
    dd = (dt - date(y, 1, 1)).days
    return y + dd/(365.0 + a)


class DayCounterMeta(type):

    def __new__(cls, name, bases, attrs):
        new_class = super(DayCounterMeta, cls).__new__(cls, name, bases, attrs)
        if new_class.name:
            _day_counters[new_class.name] = new_class
        return new_class


_day_counters = {}


class DayCounter(object):
    name = None
    __metaclass__ = DayCounterMeta

    def count(self, start, end):
        return (end-start).days

    def dcf(self, start, end):
        return self.count(start, end)/360.0


class act360(DayCounter):
    name = 'ACT/360'


class act365(DayCounter):
    name = 'ACT/365'

    def dcf(self, start, end):
        return self.count(start, end)/365.0


class thirty360(DayCounter):
    name = '30/360'

    def count(self, start, end):
        d1 = min(start.day, 30)
        d2 = min(end.day, 30)
        return 360*(end.year - start.year) + 30*(end.month -
                                                 start.month) + d2 - d1


class actact(DayCounter):
    name = 'ACT/ACT'

    def dcf(self, start, end):
        return ActActYears(end) - ActActYears(start)
