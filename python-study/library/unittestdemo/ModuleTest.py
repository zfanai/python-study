#!usr/bin/env python
#encoding:utf-8

import unittest
import ModuleToTest

class mytest(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def testsum(self):
        self.assertEqual(ModuleToTest.sum(1, 2), 3, 'test sum fail')
    
    def testsub(self):
        self.assertEqual(ModuleToTest.sub(2,1), 1, 'test sub fail')

if __name__ == '__main__':
    unittest.main()