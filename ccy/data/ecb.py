import os
from urllib import urlopen
import StringIO
import csv
import zipfile
from datetime import date

from ccy import currency

__all__ = ['ecbccy','ecbzipccy']


usdobj  = currency('USD')


def ecbdate(dstr):
    '''
    convert ecb string date into python date
    '''
    bits  = dstr.split('-')
    year  = int(bits[0])
    month = int(bits[1])
    day   = int(bits[2])
    return date(year,month,day)


class ecbccy(object):
    url = 'http://www.ecb.int/stats/eurofxref'
    filename = 'eurofxref'
    
    def __init__(self, usdbase = True, handler = None):
        '''Constructor
        @param usdbase: if True convert currency to USD base,
        @param handler: hook to post-process currency data
        handler(ccy,dt,value)'''
        self.handler = handler
        zfile = self.filename + '.zip'
        ecsv  = self.filename + '.csv' 
        urlz = os.path.join(self.url,zfile)
        try:
            res = urlopen(urlz)
            tf  = open(zfile,'wb')
            tf.write(res.read())
            tf.close()
        except:
            return
        zfile  = zipfile.ZipFile(zfile)
        data   = StringIO.StringIO(zfile.read(ecsv))
        self.reader = csv.DictReader(data)
        
        if usdbase:
            self.data = self.usdbase()
        else:
            self.data = self.vanilla()
            
    def usdbase(self):
        pass
        
    def vanilla(self):
        pass
    
    def handle(self, ccy, dt, val):
        pass
    

class ecbzipccy(ecbccy):
    '''Read the ECB zip file containing currencies historical values'''
    filename = 'eurofxref-hist'
    
    def __init__(self, start = None, end = None, **kwargs):
        if not start:
            self.start = date.min
        else:
            self.start = start
        
        if not end:
            self.end = date.today()
        else:
            self.end = end
            
        super(ecbzipccy,self).__init__(**kwargs)
        
    
    def usdbase(self):
        reader  = self.reader
        handler = self.handler or self.handle
        usdobj  = currency('USD')
        for d in reader:
            dt = ecbdate(d['Date'])
            if self.start > dt:
                continue
            if self.end < dt:
                break
            usd = float(d[usdobj.code])
            handler('EUR', dt, usd)
            for ccy,v in d.items():
                if ccy == usdobj.code or len(ccy) != 3:
                    continue
                try:
                    cobj = currency(ccy)
                    cu = float(v)/usd
                    if cobj.order < usdobj.order:
                        cu = 1./cu
                except:
                    continue
                handler(ccy, dt, cu)
                
    
    
if __name__ == "__main__":
    f = ecbzipccy()
    
    