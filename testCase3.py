#!/usr/bin/python3

import unittest

from multiplication import multiply

class TestCase(unittest.TestCase):
    def testCase3(self):
        result = multiply(1, 7)
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()
