#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import tests
    
if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite  = loader.loadTestsFromModule(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)