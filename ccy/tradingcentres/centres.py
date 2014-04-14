import datetime
# from dateutil import rrule

from .holiday import BaseHoliday, PartialDate


# weekdays = (rrule.MO,rrule.TU,rrule.WE,rrule.TH,rrule.FR)
# weekend  = (rrule.SA,rrule.SU)
isoweekend = (6, 7)
oneday = datetime.timedelta(days=1)

_tcs = {}


def centres(codes=None):
    tcs = TradingCentres()
    if codes:
        lcs = codes.upper().replace(' ', '').split(',')
        for code in lcs:
            tc = _tcs.get(code)
            if tc:
                tcs.add(tc)
    return tcs


def get_declared_holidays(bases, attrs):
    _attrs = attrs.copy()
    holidays = [(field_name, attrs.pop(field_name)) for field_name, obj in
                _attrs.items() if isinstance(obj, BaseHoliday)]

    for base in bases[::-1]:
        if hasattr(base, 'holidays'):
            holidays = base.holidays.items() + holidays

    return dict(holidays)


class TradingCentreMeta(type):

    def __new__(cls, name, bases, attrs):
        global _tcs
        abstract = attrs.pop('abstract', False)
        if abstract:
            return super(TradingCentreMeta, cls).__new__(cls, name,
                                                         bases, attrs)
        else:
            attrs['holidays'] = get_declared_holidays(bases, attrs)
            new_class = super(TradingCentreMeta, cls).__new__(cls, name,
                                                              bases, attrs)
            if not getattr(new_class, 'abstract', False):
                cl = new_class()
                _tcs[cl.code] = cl
            return new_class


TradingCentreBase = TradingCentreMeta('TradingCentreBase',
                                      (object, ),
                                      {'abstract': True})


class TradingCentre(TradingCentreBase):
    abstract = True
    onedaydelta = datetime.timedelta(days=1)

    def __new__(cls):
        obj = super(TradingCentre, cls).__new__(cls)
        obj._start = None
        obj._end = None
        obj._cache = {}
        return obj

    def __get_code(self):
        return self.__class__.__name__
    code = property(__get_code)

    def isbizday(self, dte):
        if dte.isoweekday() in isoweekend:
            return False
        else:
            return self._isholiday(dte) is False

    def _isholiday(self, dte):
        year = dte.year
        if self._start:
            if year >= self._start and year <= self._end:
                return self._cache.get(dte, False)
            elif year < self._start:
                start = year
                end = self._start - 1
            else:
                start = self._end + 1
                end = year
        else:
            start = year
            end = year
        for year in range(start, end+1):
            self.build_dates(year)
        return self._cache.get(dte, False)

    def build_dates(self, year):
        for holiday in self.holidays.values():
            days = holiday.allholidays(year)
            for day in days:
                self._cache[day] = True


class TradingCentres(object):
    onedaydelta = datetime.timedelta(days=1)

    def __init__(self):
        self._centres = {}

    def __len__(self):
        return len(self._centres)

    def add(self, tc):
        self._centres[tc.code] = tc

    def _isbizday(self, dte):
        for c in self._centres.values():
            if c._isholiday(dte):
                return False
        return True

    def isbizday(self, dte):
        if dte.isoweekday() in isoweekend:
            return False
        return self._isbizday(dte)

    def nextbizday(self, dte, nd=1):
        n = 0
        isbz = self.isbizday
        while not isbz(dte):
            dte += oneday
        while n < nd:
            dte += oneday
            if isbz(dte):
                n += 1
        return dte

    def prevbizday(self, dte, nd=1):
        n = 0
        if nd < 0:
            return self.nextbizday(dte, -nd)
        else:
            while not self.isbizday(dte):
                dte -= self.onedaydelta
            n = 0
            while n < nd:
                dte -= self.onedaydelta
                if self.isbizday(dte):
                    n += 1
        return dte


#
# TRADING CENTRES
class TGT(TradingCentre):
    '''Target'''
    new_years_day = PartialDate(1, 1)
    labor_day = PartialDate(5, 1)
    christmas_day = PartialDate(12, 25)
    december_26 = PartialDate(12, 26)


class LON(TradingCentre):
    '''London'''
    christmas_day = PartialDate(12, 25)
