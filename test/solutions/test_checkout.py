import unittest

from lib.solutions.checkout import checkout


class TestSum(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout("ABC"), 100)


if __name__ == '__main__':
    unittest.main()
