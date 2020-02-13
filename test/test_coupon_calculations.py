import unittest
from store import coupon_calculations as topic2


class MyTestCase(unittest.TestCase):
    def test_under_10(self):
        assert topic2.calculate_price(5, 5, 0) == 5.95
        assert topic2.calculate_price(7, 5, 20) == 7.65
        assert topic2.calculate_price(9, 2, 20) == 11.89
        assert topic2.calculate_price(8, 5, 15) == 8.65
        assert topic2.calculate_price(9, 0, 0) == 15.49


if __name__ == '__main__':
    unittest.main()
