import datetime
from unittest import TestCase

from ccy.tradingcentres import nextbizday, prevbizday, centres


class TradingCentresTests(TestCase):

    def setUp(self):
        self.d1 = datetime.date(2010, 4, 1)  # Thu
        self.d2 = datetime.date(2010, 4, 2)  # Fri
        self.d3 = datetime.date(2010, 4, 3)  # Sat
        self.d4 = datetime.date(2010, 4, 5)  # Mon
        self.d5 = datetime.date(2010, 4, 6)  # Tue

    def testNextBizDay(self):
        self.assertEqual(self.d2, nextbizday(self.d1))
        self.assertEqual(self.d5, nextbizday(self.d2, 2))

    def testNextBizDay0(self):
        self.assertEqual(self.d1, nextbizday(self.d1, 0))
        self.assertEqual(self.d4, nextbizday(self.d3, 0))

    def testPrevBizDay(self):
        self.assertEqual(self.d1, prevbizday(self.d2))
        self.assertEqual(self.d2, prevbizday(self.d4))
        self.assertEqual(self.d2, prevbizday(self.d5, 2))
        self.assertEqual(self.d1, prevbizday(self.d5, 3))

    def testTGT(self):
        tcs = centres('TGT')
        self.assertFalse(tcs.isbizday(datetime.date(2009, 12, 25)))
        self.assertFalse(tcs.isbizday(datetime.date(2010, 1, 1)))
