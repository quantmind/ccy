import json
from unittest import TestCase

import ccy
from ccy import (currencydb, countryccy, set_new_country, CountryError,
                 ccypair, currency)
from ccy.utils import ispy3k

if ispy3k:
    import pickle
else:
    import cPickle as pickle


class CcyTest(TestCase):

    def testdefaultcountry(self):
        ccys = currencydb()
        for ccy in ccys.values():
            if ccy.code != 'XBT':
                self.assertEqual(ccy.code[:2], ccy.default_country)

    def testiso(self):
        ccys = currencydb()
        iso = {}
        for ccy in ccys.values():
            self.assertFalse(ccy.isonumber in iso)
            iso[ccy.isonumber] = ccy

    def test2letters(self):
        ccys = currencydb()
        twol = {}
        for ccy in ccys.values():
            self.assertFalse(ccy.twoletterscode in twol)
            twol[ccy.twoletterscode] = ccy

    def testNewCountry(self):
        try:
            set_new_country('EU', 'EUR', 'Eurozone')
        except CountryError:
            return
        self.assertTrue(False)

    def testCountryCcy(self):
        self.assertEqual('AUD', countryccy('au'))
        self.assertEqual('EUR', countryccy('eu'))

    def test_ccy_pair(self):
        p = ccypair('usdchf')
        self.assertEqual(str(p), 'USDCHF')
        p = p.over()
        self.assertEqual(str(p), 'CHFUSD')
        p = ccypair('EURUSD')
        self.assertEqual(p, p.over())

    def test_pickle(self):
        c = currency('eur')
        cd = pickle.dumps(c)
        c2 = pickle.loads(cd)
        self.assertEqual(c, c2)
        self.assertNotEqual(c, 'EUR')

    def test_json(self):
        c = currency('eur')
        info = c.info()
        s = json.dumps(info)

    def test_swap(self):
        c1 = currency('eur')
        c2 = currency('chf')
        inv, a1, a2 = c1.swap(c2)
        self.assertFalse(inv)
        self.assertEqual(c1, a1)
        self.assertEqual(c2, a2)
        inv, a1, a2 = c2.swap(c1)
        self.assertTrue(inv)
        self.assertEqual(c1, a1)
        self.assertEqual(c2, a2)

    def test_as_cross(self):
        c1 = currency('eur')
        c2 = currency('chf')
        self.assertEqual(c1.as_cross(), 'EURUSD')
        self.assertEqual(c2.as_cross(), 'USDCHF')
        self.assertEqual(c1.as_cross('/'), 'EUR/USD')
        self.assertEqual(c2.as_cross('/'), 'USD/CHF')
