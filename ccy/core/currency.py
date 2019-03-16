import sys

from .data import make_ccys


usd_order = 5


def to_string(v):
    if isinstance(v, bytes):
        return v.decode('utf-8')
    else:
        return '%s' % v


def overusdfun(v1):
    return v1


def overusdfuni(v1):
    return 1./v1


class ccy(object):
    '''
    Currency object
    '''
    def __init__(self, code, isonumber, twoletterscode, order, name,
                 roundoff=4,
                 default_country=None,
                 fixeddc=None,
                 floatdc=None,
                 fixedfreq=None,
                 floatfreq=None,
                 future=None,
                 symbol=r'\00a4',
                 html=''):
        self.code = to_string(code)
        self.id = self.code
        self.isonumber = isonumber
        self.twoletterscode = to_string(twoletterscode)
        self.order = int(order)
        self.name = to_string(name)
        self.rounding = roundoff
        self.default_country = default_country
        self.symbol_raw = symbol
        self.symbol = symbol.encode('utf-8').decode('unicode_escape')
        self.html = html or self.symbol
        self.fixeddc = fixeddc
        self.floatdc = floatdc
        self.future = ''
        if future:
            self.future = str(future)

    def __getstate__(self):
        return {'code': self.code}

    def __setstate__(self, dict):
        c = currency(dict['code'])
        self.__dict__.update(c.__dict__)

    def __eq__(self, other):
        if isinstance(other, ccy):
            return other.code == self.code
        return False

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
                'twoletterscode': self.twoletterscode,
                'symbol': self.symbol,
                'order': self.order,
                'name': self.name,
                'rounding': self.rounding,
                'default_country': self.default_country,
                'unicode symbol': self.symbol_raw}

    def printinfo(self, stream=None):
        info = self.info()
        stream = stream or sys.stdout
        for k, v in info.items():
            stream.write(to_string('%s: %s\n' % (k, v)))

    def __repr__(self):
        return '%s: %s' % (self.__class__.__name__, self.code)

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
        return inv, c1, c2

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

    def as_cross(self, delimiter=''):
        '''
        Return a cross rate representation with respect USD.
        @param delimiter: could be '' or '/' normally
        '''
        if self.order > usd_order:
            return 'USD%s%s' % (delimiter, self.code)
        else:
            return '%s%sUSD' % (self.code, delimiter)

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
        self.code = '%s%s' % (c1, c2)
        self.id = self.code

    def __repr__(self):
        return '%s: %s' % (self.__class__.__name__, self.code)

    def __str__(self):
        return self.code

    def mkt(self):
        if self.ccy1.order > self.ccy2.order:
            return ccy_pair(self.ccy2, self.ccy1)
        else:
            return self

    def over(self, name='usd'):
        '''Returns a new currency pair with the *over* currency as
        second part of the pair (Foreign currency).'''
        name = name.upper()
        if self.ccy1.code == name.upper():
            return ccy_pair(self.ccy2, self.ccy1)
        else:
            return self


class ccydb(dict):

    def insert(self, *args, **kwargs):
        c = ccy(*args, **kwargs)
        self[c.code] = c


def currencydb():
    global _ccys
    if not _ccys:
        _ccys = ccydb()
        make_ccys(_ccys)
    return _ccys


def ccypairsdb():
    global _ccypairs
    if not _ccypairs:
        _ccypairs = make_ccypairs()
    return _ccypairs


def currency(code):
    c = currencydb()
    return c.get(str(code).upper())


def ccypair(code):
    c = ccypairsdb()
    return c.get(str(code).upper())


def currency_pair(code):
    '''Construct a :class:`ccy_pair` from a six letter string.'''
    c = str(code)
    c1 = currency(c[:3])
    c2 = currency(c[3:])
    return ccy_pair(c1, c2)


def make_ccypairs():
    ccys = currencydb()
    db = {}

    for ccy1 in ccys.values():
        od = ccy1.order
        for ccy2 in ccys.values():
            if ccy2.order <= od:
                continue
            p = ccy_pair(ccy1, ccy2)
            db[p.code] = p
    return db


def dump_currency_table():
    headers = ['code',
               'name',
               ('isonumber', 'iso'),
               ('html', 'symbol'),
               ('default_country', 'country'),
               'order',
               'rounding']
    all = []
    data = []
    all.append(data)
    for h in headers:
        if isinstance(h, tuple):
            h = h[1]
        data.append(h)
    for c in sorted(currencydb().values(), key=lambda x: x.order):
        data = []
        all.append(data)
        for h in headers:
            if isinstance(h, tuple):
                h = h[0]
            data.append(getattr(c, h))
    return all


_ccys = None
_ccypairs = None
