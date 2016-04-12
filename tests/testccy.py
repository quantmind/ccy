import unittest

import ccy


class TestInitFile(unittest.TestCase):

    def test_version(self):
        self.assertTrue(ccy.VERSION)
        self.assertTrue(ccy.__version__)
        self.assertEqual(ccy.__version__, ccy.get_version(ccy.VERSION))
        self.assertTrue(len(ccy.VERSION), 5)
