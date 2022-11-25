#!/usr/bin/python3

import unittest

from multiplication import multiply

class TestCase(unittest.TestCase):
    def testCase4(self):
        result = multiply(9, 3)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
