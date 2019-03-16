
def make_ccys(db):
    '''
    Create the currency dictionary
    '''
    dfr = 4
    dollar = r'\u0024'
    peso = r'\u20b1'
    kr = r'kr'
    insert = db.insert

    # G10 & SCANDI
    insert('EUR', '978', 'EU', 1,
           'Euro', dfr, 'EU', '30/360', 'ACT/360',
           future='FE', symbol=r'\u20ac', html='&#x20ac;')
    insert('GBP', '826', 'BP', 2,
           'British Pound', dfr, 'GB', 'ACT/365', 'ACT/365',
           symbol=r'\u00a3', html='&#xa3;')
    insert('AUD', '036', 'AD', 3,
           'Australian Dollar', dfr, 'AU', 'ACT/365', 'ACT/365',
           symbol=dollar, html='&#x24;')
    insert('NZD', '554', 'ND', 4,
           'New-Zealand Dollar', dfr, 'NZ', 'ACT/365', 'ACT/365',
           symbol=dollar, html='&#x24;')
    insert('USD', '840', 'UD', 5,
           'US Dollar', 0, 'US', '30/360', 'ACT/360',
           future='ED', symbol=dollar, html='&#x24;')
    insert('CAD', '124', 'CD', 6,
           'Canadian Dollar', dfr, 'CA', 'ACT/365', 'ACT/365',
           symbol=dollar, html='&#x24;')
    insert('CHF', '756', 'SF', 7,
           'Swiss Franc', dfr, 'CH', '30/360', 'ACT/360',
           symbol=r'Fr', html='&#x20a3;')
    insert('NOK', '578', 'NK', 8,
           'Norwegian Krona', dfr, 'NO', '30/360', 'ACT/360',
           symbol=kr, html=kr)
    insert('SEK', '752', 'SK', 9,
           'Swedish Krona', dfr, 'SE', '30/360', 'ACT/360',
           symbol=kr, html=kr)
    insert('DKK', '208', 'DK', 10,
           'Danish Krona', dfr, 'DK', '30/360', 'ACT/360',
           symbol=kr, html=kr)
    insert('JPY', '392', 'JY', 10000,
           'Japanese Yen', 2,  'JP', 'ACT/365', 'ACT/360',
           symbol=r'\u00a5', html='&#xa5;')

    # ASIA
    insert('CNY', '156', 'CY', 680,
           'Chinese Renminbi', dfr, 'CN', 'ACT/365', 'ACT/365',
           symbol=r'\u00a5', html='&#xa5;')
    insert('KRW', '410', 'KW', 110000,
           'South Korean won', 2, 'KR', 'ACT/365', 'ACT/365',
           symbol=r'\u20a9', html='&#x20a9;')
    insert('SGD', '702', 'SD', 15,
           'Singapore Dollar', dfr, 'SG', 'ACT/365', 'ACT/365',
           symbol=dollar, html='&#x24;')
    insert('IDR', '360', 'IH', 970000,
           'Indonesian Rupiah', 0, 'ID', 'ACT/360', 'ACT/360',
           symbol=r'Rp', html='Rp')
    insert('THB', '764', 'TB', 3300,
           'Thai Baht', 2, 'TH', 'ACT/365', 'ACT/365',
           symbol=r'\u0e3f', html='&#xe3f;')
    insert('TWD', '901', 'TD', 18,
           'Taiwan Dollar', dfr, 'TW', 'ACT/365', 'ACT/365',
           symbol=dollar, html='&#x24;')
    insert('HKD', '344', 'HD', 19,
           'Hong Kong Dollar', dfr, 'HK', 'ACT/365', 'ACT/365',
           symbol=r'\u5713', html='HK&#x24;')
    insert('PHP', '608', 'PP', 4770,
           'Philippines Peso', dfr, 'PH', 'ACT/360', 'ACT/360',
           symbol=peso, html='&#x20b1;')
    insert('INR', '356', 'IR', 4500,
           'Indian Rupee', dfr, 'IN', 'ACT/365', 'ACT/365',
           symbol=r'\u20a8', html='&#x20a8;')
    insert('MYR', '458', 'MR', 345,
           'Malaysian Ringgit', dfr, 'MY', 'ACT/365', 'ACT/365')
    insert('VND', '704', 'VD', 1700000,
           'Vietnamese Dong', 0,  'VN', 'ACT/365', 'ACT/365',
           symbol=r'\u20ab', html='&#x20ab;')

    # LATIN AMERICA
    insert('BRL', '986', 'BC', 200,
           'Brazilian Real', dfr, 'BR', 'BUS/252', 'BUS/252',
           symbol=r'R$')
    insert('PEN', '604', 'PS', 220,
           'Peruvian New Sol', dfr, 'PE', 'ACT/360', 'ACT/360',
           symbol=r'S/.')
    insert('ARS', '032', 'AP', 301,
           'Argentine Peso', dfr, 'AR', '30/360', 'ACT/360',
           symbol=dollar, html='&#x24;')
    insert('MXN', '484', 'MP', 1330,
           'Mexican Peso', dfr, 'MX', 'ACT/360', 'ACT/360',
           symbol=dollar, html='&#x24;')
    insert('CLP', '152', 'CH', 54500,
           'Chilean Peso', 2,  'CL', 'ACT/360', 'ACT/360',
           symbol=dollar, html='&#x24;')
    insert('COP', '170', 'CL', 190000,
           'Colombian Peso', 2,  'CO', 'ACT/360', 'ACT/360',
           symbol=dollar, html='&#x24;')
    # TODO: Check towletters code and position
    insert('JMD', '388', 'JD', 410,
           'Jamaican Dollar', dfr, 'JM', 'ACT/360', 'ACT/360',
           symbol=dollar, html='&#x24;')
    # TODO: Check towletters code and position
    insert('TTD', '780', 'TT', 410,
           'Trinidad and Tobago Dollar', dfr, 'TT', 'ACT/360', 'ACT/360',
           symbol=dollar, html='&#x24;')
    # TODO: Check towletters code and position
    insert('BMD', '060', 'BD', 410,
           'Bermudian Dollar', dfr, 'BM',
           symbol=dollar, html='&#x24;')

    # EASTERN EUROPE
    insert('CZK', '203', 'CK', 28,
           'Czech Koruna', dfr, 'CZ', 'ACT/360', 'ACT/360',
           symbol=r'\u004b\u010d')
    insert('PLN', '985', 'PZ', 29,
           'Polish Zloty', dfr, 'PL', 'ACT/ACT', 'ACT/365',
           symbol=r'\u0050\u0142')
    insert('TRY', '949', 'TY', 30,
           'Turkish Lira', dfr, 'TR', 'ACT/360', 'ACT/360',
           symbol=r'\u0054\u004c')
    insert('HUF', '348', 'HF', 32,
           'Hungarian Forint', dfr, 'HU', 'ACT/365', 'ACT/360',
           symbol=r'Ft', html='Ft')
    insert('RON', '946', 'RN', 34,
           'Romanian Leu', dfr, 'RO', 'ACT/360', 'ACT/360')
    insert('RUB', '643', 'RR', 36,
           'Russian Ruble', dfr, 'RU', 'ACT/ACT', 'ACT/ACT',
           symbol=r'\u0440\u0443\u0431')
    # TODO: Check towletters code and position
    insert('HRK', '191', 'HK', 410,
           'Croatian kuna', dfr, 'HR',
           symbol=r'kn')
    # TODO: Check towletters code and position
    insert('KZT', '398', 'KT', 410,
           'Tenge',  dfr, 'KZ',
           symbol=r'\u20b8', html='&#x20b8;')
    # TODO: Check towletters code and position
    insert('BGN', '975', 'BN', 410,
           'Bulgarian Lev', dfr, 'BG',
           symbol=r'\u043b\u0432.', html='&#1083;&#1074;')

    # MIDDLE EAST & AFRICA
    insert('ILS', '376', 'IS', 410,
           'Israeli Shekel', dfr, 'IL', 'ACT/365', 'ACT/365',
           symbol=r'\u20aa', html='&#x20aa;')
    # TODO: Check towletters code and position
    insert('AED', '784', 'AE', 410,
           'United Arab Emirates Dirham', dfr, 'AE')
    # TODO: Check towletters code and position
    insert('QAR', '634', 'QA', 410,
           'Qatari Riyal', dfr, 'QA',
           symbol=r'\ufdfc', html='&#xfdfc;')
    # TODO: Check towletters code and position
    insert('SAR', '682', 'SR', 410,
           'Saudi Riyal', dfr, 'SA',
           symbol=r'\ufdfc', html='&#xfdfc;')
    insert('EGP', '818', 'EP', 550,
           'Egyptian Pound', dfr, 'EG',
           symbol=r'\u00a3', html='&#xa3;')
    insert('ZAR', '710', 'SA', 750,
           'South African Rand', dfr, 'ZA', 'ACT/365', 'ACT/365',
           symbol=r'R', html='R')

    # BITCOIN
    insert('XBT', '000', 'BT', -1,
           'Bitcoin', 8, 'WW',
           symbol=r'\u0e3f', html='&#xe3f;')
