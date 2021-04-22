import unittest

from model.data.Currencies import verified_currencies
from model.data.DataExceptions import CurrencyException, NegativeDollarException
from model.data.Dollars import Dollars


class TestDollars(unittest.TestCase):
    """ Testing Dollars class initialization and operations """
    
    def test_init(self):
        """ Initialize valid Dollars instances """
        d = Dollars(0, 0)
        self.assertEqual(0, d.dollars)
        self.assertEqual(0, d.cents)
        d = Dollars(1, 10)
        self.assertEqual(1, d.dollars)
        self.assertEqual(10, d.cents)

    def test_init_grouping(self):
        """ Groups initial Cents into Dollars """
        d = Dollars(110, 100)
        self.assertEqual(111, d.dollars)
        self.assertEqual(0, d.cents)
        d = Dollars(10, 510)           # More grouping
        self.assertEqual(15, d.dollars)
        self.assertEqual(10, d.cents)

    def test_init_bad(self):
        """ Initialize Dollars with a bad parameters """
        with self.assertRaises(CurrencyException):
            Dollars(1, 1, 'ji3')
        with self.assertRaises(CurrencyException):
            Dollars(1, 1, 'jik9njk')
        with self.assertRaises(NegativeDollarException):
            Dollars(1, -1)
        with self.assertRaises(NegativeDollarException):
            Dollars(-1, 1)

    def test_addition(self):
        """ Perform basic addition of two simple Dollar amounts """
        # Basic Addition
        d0 = Dollars(10, 5)
        d1 = Dollars(100, 80)
        d_sum = d0 + d1
        self.assertEqual(110, d_sum.dollars)
        self.assertEqual(85, d_sum.cents)

    def test_addition_carrying(self):
        """ Carrying cents into dollars when adding """
        # Carrying cents
        d0 = Dollars(10, 50)
        d_sum = d0 + Dollars(100, 80)
        self.assertEqual(111, d_sum.dollars)
        self.assertEqual(30, d_sum.cents)
        # Check another set of numbers
        d_sum = Dollars(20, 95) + Dollars(60, 85)
        self.assertEqual(81, d_sum.dollars)
        self.assertEqual(80, d_sum.cents)

    def test_addition_bad(self):
        """ Adding different currencies or non-dollar objects """
        # Different Currencies
        d0 = Dollars(10, 5, verified_currencies[4])
        d1 = Dollars(100, 60, verified_currencies[3])
        with self.assertRaises(CurrencyException):
            d0 + d1
        # Adding a non-Dollars object
        d0 = Dollars(5, 0)
        with self.assertRaises(TypeError):
            d0 + 6

    def test_subtraction(self):
        """ Simple subtraction operation """
        d0 = Dollars(100, 80)
        d1 = Dollars(10, 5)
        d_diff = d0 - d1
        self.assertEqual(90, d_diff.dollars)
        self.assertEqual(75, d_diff.cents)

    def test_subtraction_borrowing(self):
        """ Borrow from dollars during subtraction operation """
        d_diff = Dollars(10, 80) - Dollars(0, 90)
        self.assertEqual(9, d_diff.dollars)
        self.assertEqual(90, d_diff.cents)
        # Repeat with many different numbers
        balance = Dollars(101, 0)
        for i in range(1, 100):
            diff = balance - Dollars(i, i)
            self.assertEqual(100 - i, diff.dollars)
            self.assertEqual(100 - i, diff.cents)

    def test_subtraction_negative(self):
        """ Absolute Dollar difference when 2nd argument is greater """
        d_diff = Dollars(7, 99) - Dollars(10, 50)
        self.assertEqual(2, d_diff.dollars)
        self.assertEqual(51, d_diff.cents)
        # Repeat with new numbers
        d_diff = Dollars(30, 10) - Dollars(40, 20)
        self.assertEqual(10, d_diff.dollars)
        self.assertEqual(10, d_diff.cents)
        # 
        d_diff = Dollars(1, 3) - Dollars(3, 16)
        self.assertEqual(2, d_diff.dollars)
        self.assertEqual(13, d_diff.cents)
        # 
        d_diff = Dollars(1, 34) - Dollars(3, 16)
        self.assertEqual(1, d_diff.dollars)
        self.assertEqual(82, d_diff.cents)


if __name__ == '__main__':
    unittest.main()
