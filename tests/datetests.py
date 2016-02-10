from datetime import date, datetime
from unittest import TestCase

from ccy import period, date2juldate, juldate2date, todate
from ccy import date2yyyymmdd, yyyymmdd2date


class PeriodTests(TestCase):

    def testPeriod(self):
        a = period('5Y')
        self.assertEqual(a.years, 5)
        b = period('1y3m')
        self.assertEqual(b.years, 1)
        self.assertEqual(b.months, 3)
        c = period('-3m')
        self.assertEqual(c.years, 0)
        self.assertEqual(c.months, -3)

    def testAdd(self):
        a = period('4Y')
        b = period('1Y3M')
        c = a + b
        self.assertEqual(c.years, 5)
        self.assertEqual(c.months, 3)

    def testAddString(self):
        a = period('4y')
        self.assertEqual(a+'3m', period('4y3m'))
        self.assertEqual('3m'+a, period('4y3m'))

    def testSubtract(self):
        a = period('4Y')
        b = period('1Y')
        c = a - b
        self.assertEqual(c.years, 3)
        self.assertEqual(c.months, 0)
        c = period('3Y') - period('1Y3M')
        self.assertEqual(c.years, 1)
        self.assertEqual(c.months, 9)
        self.assertEqual(str(c), '1Y9M')

    def testSubtractString(self):
        a = period('4y')
        self.assertEqual(a-'3m', period('3y9m'))
        self.assertEqual('5y'-a, period('1y'))
        self.assertEqual('3m'-a, period('-3y9m'))

    def testCompare(self):
        a = period('4Y')
        b = period('4Y')
        c = period('1Y2M')
        self.assertTrue(a == b)
        self.assertTrue(a >= b)
        self.assertTrue(a <= b)
        self.assertTrue(c <= a)
        self.assertTrue(c < a)
        self.assertFalse(c == a)
        self.assertFalse(c >= b)
        self.assertTrue(c > a-b)

    def testWeek(self):
        p = period('7d')
        self.assertEqual(p.weeks, 1)
        self.assertEqual(str(p), '1W')
        p.add_weeks(3)
        self.assertEqual(p.weeks, 4)
        self.assertEqual(str(p), '4W')
        self.assertFalse(p.isempty())
        p = period('3w2d')
        self.assertFalse(p.isempty())
        self.assertEqual(p.weeks, 3)
        self.assertEqual(str(p), '3W2D')

    def testEmpty(self):
        self.assertFalse(period('3y').isempty())
        self.assertFalse(period('1m').isempty())
        self.assertFalse(period('3d').isempty())
        self.assertTrue(period().isempty())

    def testAddperiod(self):
        p = period('3m')
        a = period('6m')
        self.assertEqual(a.add_tenure(p), a)
        self.assertEqual(str(a), '9M')

    def testError(self):
        self.assertRaises(ValueError, period, '5y6g')

    def testSimple(self):
        self.assertEqual(period('3m2y').simple(), '27M')
        self.assertEqual(period('-3m2y').simple(), '-27M')
        self.assertEqual(period('3d2m').simple(), '63D')
        self.assertEqual(period('2y').simple(), '2Y')


class DateConverterTest(TestCase):

    def setUp(self):
        self.dates = [(date(2010, 6, 11), 40340, 20100611, 1276210800),
                      (date(2009, 4, 2), 39905, 20090402, 1238626800),
                      (date(1996, 2, 29), 35124, 19960229, 825552000),
                      (date(1970, 1, 1), 25569, 19700101, 0),
                      (date(1900, 1, 1), 1, 19000101, None)]

    def testdate2JulDate(self):
        for d, jd, y, ts in self.dates:
            self.assertEqual(jd, date2juldate(d))

    def testJulDate2Date(self):
        for d, jd, y, ts in self.dates:
            self.assertEqual(d, juldate2date(jd))

    def testDate2YyyyMmDd(self):
        for d, jd, y, ts in self.dates:
            self.assertEqual(y, date2yyyymmdd(d))

    def testYyyyMmDd2Date(self):
        for d, jd, y, ts in self.dates:
            self.assertEqual(d, yyyymmdd2date(y))

    def test_datetime2Juldate(self):
        jd = date2juldate(datetime(2013, 3, 8, 11, 20, 45))
        self.assertAlmostEqual(jd, 41341.47274305556)

    def test_Juldate2datetime(self):
        dt = juldate2date(41341.47274305556)
        dt2 = datetime(2013, 3, 8, 11, 20, 45)
        self.assertEqual(dt, dt2)

    def test_string(self):
        target = date(2014, 1, 5)
        self.assertEqual(todate('2014 Jan 05'), target)

    # def testDate2Timestamp(self):
    #     for d,jd,y,ts in self.dates:
    #         if ts is not None:
    #             self.assertEqual(ts,date2timestamp(d))

    # def testTimestamp2Date(self):
    #     for d,jd,y,ts in self.dates:
    #         if ts is not None:
    #             self.assertEqual(d,timestamp2date(ts))
