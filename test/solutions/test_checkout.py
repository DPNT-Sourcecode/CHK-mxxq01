import unittest

from lib.solutions.checkout import checkout


class TestSum(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout("ABC"), 50+30+20)
        self.assertEqual(checkout("ABCCCD"), 50+30+20*3+15)
        self.assertEqual(checkout("AAA"), 130)
        self.assertEqual(checkout("AAAAB"), 130+50+30)
        self.assertEqual(checkout("AAAAAAAAB"), 130+200+30)
        self.assertEqual(checkout("EEBB"), 40*2+30)


if __name__ == '__main__':
    unittest.main()
