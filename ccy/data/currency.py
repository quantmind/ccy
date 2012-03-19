
_tatd ='Trinidad and Tobago Dollar'
_uaed = 'United Arab Emirates Dirham'

def make_ccys(db):
    '''
    Create the currency dictionary 
    '''
    dfr = 4
    dollar = '\u0024'
    peso   = '\u20b1'
    kr     = 'kr'
    yen    = '\xa5'
    
    db.insert('EUR','978','EU',1,       'Euro',                 dfr,'EU', '30/360', 'ACT/360', symbol='\u20ac')
    db.insert('GBP','826','BP',2,       'British Pound',        dfr,'GB', 'ACT/365','ACT/365', symbol='\xa3')
    db.insert('AUD','036','AD',3,       'Australian Dollar',    dfr,'AU', 'ACT/365','ACT/365', symbol=dollar)
    db.insert('NZD','554','ND',4,       'New-Zealand Dollar',   dfr,'NZ', 'ACT/365','ACT/365', symbol=dollar)
    db.insert('USD','840','UD',5,       'US Dollar',            0,  'US', '30/360', 'ACT/360', symbol=dollar)
    db.insert('CAD','124','CD',6,       'Canadian Dollar',      dfr,'CA', 'ACT/365','ACT/365', symbol=dollar)
    db.insert('CHF','756','SF',7,       'Swiss Franc',          dfr,'CH', '30/360', 'ACT/360', symbol='Fr')
    db.insert('NOK','578','NK',8,       'Norwegian Krona',      dfr,'NO', '30/360', 'ACT/360', symbol=kr)
    db.insert('SEK','752','SK',9,       'Swedish Krona',        dfr,'SE', '30/360', 'ACT/360', symbol=kr)
    db.insert('DKK','208','DK',10,      'Danish Krona',         dfr,'DK', '30/360', 'ACT/360', symbol=kr)
    db.insert('JPY','392','JY',10000,   'Japanese Yen',         2,  'JP', 'ACT/365','ACT/360', symbol=yen)
    
    db.insert('CNY','156','CY',680,     'Chinese Renminbi',     dfr,'CN', 'ACT/365','ACT/365', symbol=yen)
    db.insert('KRW','410','KW',110000,  'South Korean won',     2,  'KR', 'ACT/365','ACT/365', symbol='\u20a9')
    db.insert('SGD','702','SD',15,      'Singapore Dollar',     dfr,'SG', 'ACT/365','ACT/365')
    db.insert('IDR','360','IH',970000,  'Indonesian Rupiah',    0,  'ID', 'ACT/360','ACT/360')
    db.insert('THB','764','TB',3300,    'Thai Baht',            2,  'TH', 'ACT/365','ACT/365', symbol='\u0e3f')
    db.insert('TWD','901','TD',18,      'Taiwan Dollar',        dfr,'TW', 'ACT/365','ACT/365')
    db.insert('HKD','344','HD',19,      'Hong Kong Dollar',     dfr,'HK', 'ACT/365','ACT/365', symbol='\u5713')
    db.insert('PHP','608','PP',4770,    'Philippines Peso',     dfr,'PH', 'ACT/360','ACT/360')
    db.insert('INR','356','IR',4500,    'Indian Rupee',         dfr,'IN', 'ACT/365','ACT/365', symbol='\u20a8')
    db.insert('MYR','458','MR',345,     'Malaysian Ringgit',    dfr,'MY', 'ACT/365','ACT/365')
    db.insert('VND','704','VD',1700000, 'Vietnamese Dong',      0,  'VN', 'ACT/365','ACT/365', symbol='\u20ab')
    
    db.insert('BRL','986','BC',200,     'Brazilian Real',       dfr,'BR', 'BUS/252','BUS/252', symbol='R$')
    db.insert('PEN','604','PS',220,     'Peruvian New Sol',     dfr,'PE', 'ACT/360','ACT/360', symbol='S/.')
    db.insert('ARS','032','AP',301,     'Argentine Peso',       dfr,'AR', '30/360', 'ACT/360', symbol=dollar)
    db.insert('MXN','484','MP',1330,    'Mexican Peso',         dfr,'MX', 'ACT/360','ACT/360', symbol=dollar)
    db.insert('CLP','152','CH',54500,   'Chilean Peso',         2,  'CL', 'ACT/360','ACT/360', symbol=dollar)
    db.insert('COP','170','CL',190000,  'Colombian Peso',       2,  'CO', 'ACT/360','ACT/360', symbol=dollar)
    db.insert('JMD','388','JD',410,     'Jamaican Dollar',      dfr,'JM', 'ACT/360','ACT/360', symbol=dollar)   ### TODO: Check towletters code and position
    db.insert('TTD','780','TT',410,     _tatd,                  dfr,'TT', 'ACT/360','ACT/360', symbol=dollar)   ### TODO: Check towletters code and position
    db.insert('BMD','060','BD',410,     'BermudIan Dollar',     dfr,'BM', symbol=dollar)   ### TODO: Check towletters code and position
    
    db.insert('CZK','203','CK',28,      'Czech Koruna',         dfr,'CZ', 'ACT/360','ACT/360')
    db.insert('PLN','985','PZ',29,      'Polish Zloty',         dfr,'PL', 'ACT/ACT','ACT/365')
    db.insert('TRY','949','TY',30,      'Turkish Lira',         dfr,'TR', 'ACT/360','ACT/360', symbol='YTL')
    db.insert('HUF','348','HF',32,      'Hungarian Forint',     dfr,'HU', 'ACT/365','ACT/360', symbol='Ft')
    db.insert('RON','946','RN',34,      'Romanian Leu',         dfr,'RO', 'ACT/360','ACT/360')
    db.insert('RUB','643','RR',36,      'Russian Ruble',        dfr,'RU', 'ACT/ACT','ACT/ACT', symbol='\u0440\u0443\u0431')
    db.insert('HRK','191','HK',410,     'Croatian kuna',        dfr,'HR')                 ### TODO: Check towletters code and position.
    db.insert('EEK','233','EK',410,     'Estonia Kroon',        dfr,'EE')                 ### TODO: Check towletters code and position
    db.insert('KZT','398','KT',410,     'Tenge',                dfr,'KZ')                         ### TODO: Check towletters code and position
    
    db.insert('ILS','376','IS',410,     'Israeli Shekel',       dfr,'IL', 'ACT/365','ACT/365', symbol='\u20aa')
    db.insert('AED','784','AE',410,     _uaed,                  dfr,'AE')   ### TODO: Check towletters code and position
    db.insert('QAR','634','QA',410,     'Qatari Riyal',         dfr,'QA')                   ### TODO: Check towletters code and position
    db.insert('SAR','682','SR',410,     'Saudi Riyal',          dfr,'SA')                    ### TODO: Check towletters code and position
    db.insert('EGP','818','EP',550,     'Egyptian Pound',       dfr,'EG')
    db.insert('ZAR','710','SA',750,     'South African Rand',   dfr,'ZA', 'ACT/365','ACT/365', symbol='R')
    

