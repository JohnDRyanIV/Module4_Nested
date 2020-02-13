import unittest
from store import coupon_calculations as topic2


class MyTestCase(unittest.TestCase):
    def test_under_10(self):
        assert topic2.calculate_price(5, 5, 0) == 5.95
        assert topic2.calculate_price(7, 5, 20) == 7.65
        assert topic2.calculate_price(9, 2, 20) == 11.89
        assert topic2.calculate_price(8, 5, 15) == 8.65
        assert topic2.calculate_price(9, 0, 0) == 15.49
    def test_between_10_and_under_30(self):
        assert topic2.calculate_price(15, 5, 20) == 14.43
        assert topic2.calculate_price(25, 0, 15) == 30.48
        assert topic2.calculate_price(12, 10, 20) == 7.65
        assert topic2.calculate_price(29.99, 0, 0) == 39.74
        assert topic2.calculate_price(20, 5, 15) == 21.47
        assert topic2.calculate_price(18.76, 10, 10) == 14.31
    def test_between_30_and_under_50(self):
        assert topic2.calculate_price(45.87, 10, 20) == 38.37
        assert topic2.calculate_price(37.43, 0, 15) == 45.67
        assert topic2.calculate_price(49.99, 0, 0) == 64.94
        assert topic2.calculate_price(30, 10, 20) == 24.91
        assert topic2.calculate_price(35.55, 5, 15) == 35.48
        assert topic2.calculate_price(40, 5, 10) == 45.34




if __name__ == '__main__':
    unittest.main()
