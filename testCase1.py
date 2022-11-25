import unittest

from multiplication import multiply

class TestCase(unittest.TestCase):
    def testCase1(self):
        result = multiply(20, 30)
        self.assertEqual(result, 600)


if __name__ == '__main__':
    unittest.main()