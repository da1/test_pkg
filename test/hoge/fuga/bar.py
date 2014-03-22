#! -*- coding: utf-8 -*-
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../../../")

from hoge.fuga.bar import Bar

class BarTest(unittest.TestCase):
    def testGet(self):
        obj = Bar()
        self.assertEqual(obj.get(), 'bar')

if __name__ == '__main__':
    unittest.main()
