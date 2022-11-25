import unittest

from multiplication import multiply

class TestCase(unittest.TestCase):
    def testCase5(self):
        result = multiply(2, 0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()