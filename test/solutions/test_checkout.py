import unittest

from lib.solutions.checkout import checkout


class TestSum(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout("ABC"), 100)
        self.assertEqual(checkout("ABCCCD"), 155)
        self.assertEqual(checkout("AAA"), 130)
        self.assertEqual(checkout("AAAAB"), 210)


if __name__ == '__main__':
    unittest.main()
