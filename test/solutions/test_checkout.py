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
        self.assertEqual(checkout("EEBBB"), 40*2+45)
        self.assertEqual(checkout("EEEEBBB"), 40*4+30)
        self.assertEqual(checkout("FF"), 20)
        self.assertEqual(checkout("FFF"), 20)
        self.assertEqual(checkout("FFFFF"), 40)
        self.assertEqual(checkout("FFFFFF"), 40)

    def test_group_buy(self):
        self.assertEqual(checkout("ZZTSR"), 50+20+45)

if __name__ == '__main__':
    unittest.main()
