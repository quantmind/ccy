import datetime

#from dateutil.rrule import rrule, YEARLY


class BaseHoliday(object):
    
    def __init__(self, description = ''):
        self.description = description
    
    def extended(self):
        return None
    
    def allholidays(self, year):
        return []
    
    def __repr__(self):
        d = self.extended()
        if d:
            return '%s: %s' % (self.__class__.__name__,d)
        else:
            return self.__class__.__name__


class PartialDate(BaseHoliday):
    
    def __init__(self, month, day):
        self.month = month
        self.day   = day
    
    def allholidays(self, year):
        return (datetime.date(year,self.month,self.day),)
        