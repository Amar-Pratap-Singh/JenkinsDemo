#!/usr/bin/python3

import unittest

from multiplication import multiply

class TestCase(unittest.TestCase):
    def testCase1(self):
        result = multiply(20, 30)
        self.assertEqual(result, 600)
    
    def testCase2(self):
        result = multiply(2, 9)
        self.assertEqual(result, 18)

    def testCase3(self):
        result = multiply(7, 3)
        self.assertEqual(result, 1)

    def testCase4(self):
        result = multiply(9, 0)
        self.assertEqual(result, 0)

    def testCase5(self):
        result = multiply(9, 0)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()