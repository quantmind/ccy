from ccy import currencydb, countryccy, set_new_country, CountryError
from unittest import TestCase


class CcyTest(TestCase):
        
    def testdefaultcountry(self):
        ccys = currencydb()
        for ccy in ccys.values():
            self.assertEqual(ccy.code[:2],ccy.default_country)
            
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
            self.assertFalse(ccy.twolettercode in twol)
            twol[ccy.twolettercode] = ccy
            
    def testNewCountry(self):
        try:
            set_new_country('EU','EUR','Eurozone')
        except CountryError:
            return
        self.assertTrue(False)
        
    def testCountryCcy(self):
        self.assertEqual('AUD',countryccy('au'))
        self.assertEqual('EUR',countryccy('eu'))
            
    