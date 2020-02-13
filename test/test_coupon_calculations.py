import unittest
from store import coupon_calculations as topic2



class MyTestCase(unittest.TestCase):
    def test_under_10(self):
        assert topic2.calculate_price(5, 2, 50) == 2.5
        assert topic2.calculate_price(4, 0, 90) == .4
        assert topic2.calculate_price(3, 1, 40) == 1.2
        assert topic2.calculate_price(9, 2, 73) == 1.89
        assert topic2.calculate_price(8, 4, 50) == 2
        assert topic2.calculate_price(1, 1, 0) == 0
        assert topic2.calculate_price(1, 0, 100) == 0


if __name__ == '__main__':
    unittest.main()
