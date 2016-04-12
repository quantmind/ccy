import unittest

from . import ccytests
from . import datetests
from . import tcstests
from . import testccy


def suite():
    loader = unittest.TestLoader()
    return unittest.TestSuite([
        loader.loadTestsFromModule(ccytests),
        loader.loadTestsFromModule(datetests),
        loader.loadTestsFromModule(tcstests),
        loader.loadTestsFromModule(testccy)
        ])
