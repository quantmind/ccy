import unittest

import ccy


class TestInitFile(unittest.TestCase):

    def test_version(self):
        self.assertTrue(ccy.VERSION)
        self.assertTrue(ccy.__version__)
        self.assertEqual(ccy.__version__,ccy.get_version())
        self.assertTrue(len(ccy.VERSION) >= 2)

    def test_meta(self):
        for m in ("__author__", "__contact__", "__homepage__", "__doc__"):
            self.assertTrue(getattr(ccy, m, None))