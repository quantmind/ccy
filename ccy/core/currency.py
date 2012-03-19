from ccy.utils import string_type

__all__ = ['currency','ccypair','ccydb','currencydb','ccypairsdb','currencypair']

usd_order = 5


def overusdfun(v1):
    return v1
def overusdfuni(v1):
    return 1./v1


class ccy(object):
    '''
    Currency object
    '''
    def __init__(self, code, isonumber, twolettercode, order, name, 
                 roundoff  = 4,
                 default_country = None,
                 fixeddc   = None,
                 floatdc   = None,
                 fixedfreq = None,
                 floatfreq = None,
                 future    = None,
                 symbol    = '\u00a4'):
        #from qmpy.finance.dates import get_daycount
        self.code          = string_type(code)
        self.id            = self.code
        self.isonumber     = isonumber
        self.twolettercode = string_type(twolettercode)
        self.order         = int(order)
        self.name          = string_type(name)
        self.raundoff      = roundoff
        self.default_country = default_country
        self.symbol        = symbol
        self.fixeddc       = fixeddc    
        self.floatdc       = floatdc
        #self.fixedfreq     = str(fixedfreq)
        #self.floatfreq     = str(floatfreq)
        self.future        = ''
        if future:
            self.future    = str(future)
    
    def __getstate__(self):
        return {'code':self.code}
    
    def __setstate__(self, dict):
        c = currency(dict['code'])
        self.__dict__.update(c.__dict__)
            
    def description(self):
        if self.order > usd_order:
            v = 'USD / %s' % self.code
        else:
            v = '%s / USD' % self.code
        if self.order != usd_order:
            return '%s Spot Exchange Rate' % v
        else:
            return 'Dollar'
            
    def info(self):
        return {'code': self.code,
                'isonumber': self.isonumber,
                'twolettercode': self.twolettercode,
                'order':self.order,
                'name':self.name,
                'raundoff':self.raundoff,
                'default_country': self.default_country}
        
    def printinfo(self):
        info = self.info()
        for k,v in info.items():
            print('%s: %s' % (k,v))
        
        
    def __repr__(self):
        return '%s: %s' % (self.__class__.__name__,self.code)
    
    def __str__(self):
        return self.code
    
    def swap(self, c2):
        '''
        put the order of currencies as market standard
        '''
        inv = False
        c1 = self
        if c1.order > c2.order:
            ct = c1
            c1 = c2
            c2 = ct
            inv = True
        return inv,c1,c2
    
    def overusdfunc(self):
        if self.order > usd_order:
            return overusdfuni
        else:
            return overusdfun
    
    def usdoverfunc(self):
        if self.order > usd_order:
            return overusdfun
        else:
            return overusdfuni
    
    def as_cross(self, delimiter = ''):
        '''
        Return a cross rate representation with respect USD.
        @param delimiter: could be '' or '/' normally
        '''
        if self.order > usd_order:
            return 'USD%s%s' % (delimiter,self.code)
        else:
            return '%s%sUSD' % (self.code,delimiter)
        
    def spot(self, c2, v1, v2):
        if self.order > c2.order:
            vt = v1
            v1 = v2
            v2 = vt
        return v1/v2
    
    
class ccy_pair(object):
    '''
    Currency pair such as EURUSD, USDCHF
    
    XXXYYY - XXX is the foreign currency, while YYY is the base currency
    
    XXXYYY means 1 unit of of XXX cost XXXYYY units of YYY
    '''
    def __init__(self, c1, c2):
        self.ccy1 = c1
        self.ccy2 = c2
        self.code = '%s%s' % (c1,c2)
        self.id   = self.code
    
    def __repr__(self):
        return '%s: %s' % (self.__class__.__name__,self.code)
    
    def __str__(self):
        return self.code
    
    def mkt(self):
        if self.ccy1.order > self.ccy2.order:
            return ccy_pair(self.ccy2,self.ccy1)
        else:
            return self
    


class ccydb(dict):
    load = None
    
    def __init__(self, name):
        self.name = name
        self.__class__.load(self)
        
    def insert(self, *args, **kwargs):
        c = ccy(*args, **kwargs)
        self[c.code] = c


def currencydb():
    global _ccys
    if not _ccys:
        _ccys = ccydb('currencydb')
    return _ccys

def ccypairsdb():
    global _ccypairs
    if not _ccypairs:
        _ccypairs = make_ccypairs()
    return _ccypairs


def currency(code):
    c = currencydb()
    return c.get(str(code).upper(),None)

def ccypair(code):
    c = ccypairsdb()
    return c.get(str(code).upper(),None)

def currencypair(code):
    c = str(code)
    c1 = currency(c[:3])
    c2 = currency(c[3:])
    return ccy_pair(c1,c2)


def make_ccypairs():
    ccys = currencydb()
    db   = {}
    
    for ccy1 in ccys.values():
        od = ccy1.order
        for ccy2 in ccys.values():
            if ccy2.order <= od:
                continue
            p = ccy_pair(ccy1,ccy2)
            db[p.code] = p
    return db


_ccys = None
_ccypairs = None