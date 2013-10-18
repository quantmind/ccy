#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import unittest

import tests


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite  = loader.loadTestsFromModule(tests)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    sys.exit(int(not result.wasSuccessful()))
