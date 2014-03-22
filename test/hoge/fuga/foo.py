#! -*- coding: utf-8 -*-
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../../")

from hoge.fuga.foo import Foo

class FooTest(unittest.TestCase):
    def testGet(self):
        obj = Foo()
        self.assertEqual(obj.get(), 'foo')

if __name__ == '__main__':
    unittest.main()
