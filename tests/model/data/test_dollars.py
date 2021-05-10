""" Testing for the Dollars Data structure """
import unittest

from model.data.currencies import VERIFIED_CURRENCIES
from model.data import CurrencyException
from model.data.dollars import Dollars


class TestDollars(unittest.TestCase):
    """ Testing Dollars class initialization and operations """

    def setUp(self) -> None:
        self.d_1 = Dollars(7, 99)
        self.d_2 = Dollars(10, 20)

    def test_init(self):
        """ Initialize valid Dollars instances """
        self.assertEqual(7, self.d_1.dollars)
        self.assertEqual(99, self.d_1.cents)
        self.assertEqual('USD', self.d_1.currency)
        #
        self.assertEqual(10, self.d_2.dollars)
        self.assertEqual(20, self.d_2.cents)
        self.assertEqual('USD', self.d_1.currency)

    def test_init_grouping(self):
        """ Groups initial Cents into Dollars """
        new_dollars = Dollars(110, 100)
        self.assertEqual(111, new_dollars.dollars)
        self.assertEqual(0, new_dollars.cents)
        new_dollars = Dollars(10, 510)           # More grouping
        self.assertEqual(15, new_dollars.dollars)
        self.assertEqual(10, new_dollars.cents)

    def test_init_bad(self):
        """ Initialize Dollars with a bad parameters """
        with self.assertRaises(CurrencyException):
            Dollars(1, 1, 'ji3')
        with self.assertRaises(CurrencyException):
            Dollars(1, 1, 'jik9njk')
        with self.assertRaises(ValueError):
            Dollars(1, -1)
        with self.assertRaises(ValueError):
            Dollars(-1, 1)
        with self.assertRaises(TypeError):
            Dollars(1.1, 1)
        with self.assertRaises(TypeError):
            Dollars(1, 1.1)

    def test_addition(self):
        """ Perform basic addition of two simple Dollar amounts """
        # Basic Addition
        d_0 = Dollars(10, 5)
        d_1 = Dollars(100, 80)
        d_sum = d_0 + d_1
        self.assertEqual(110, d_sum.dollars)
        self.assertEqual(85, d_sum.cents)

    def test_addition_carrying(self):
        """ Carrying cents into dollars when adding """
        # Carrying cents
        d_0 = Dollars(10, 50)
        d_sum = d_0 + Dollars(100, 80)
        self.assertEqual(111, d_sum.dollars)
        self.assertEqual(30, d_sum.cents)
        # Check another set of numbers
        d_sum = Dollars(20, 95) + Dollars(60, 85)
        self.assertEqual(81, d_sum.dollars)
        self.assertEqual(80, d_sum.cents)

    def test_addition_bad(self):
        """ Adding different currencies or non-dollar objects """
        self.d_2.currency = VERIFIED_CURRENCIES[3]
        with self.assertRaises(CurrencyException):
            print(self.d_1 + self.d_2)   # Different currencies cannot add
        with self.assertRaises(TypeError):
            print(Dollars(5, 0) + 6)   # Adding a non-Dollars object

    def test_subtraction(self):
        """ Simple subtraction operation """
        d_0 = Dollars(100, 80)
        d_1 = Dollars(10, 5)
        d_diff = d_0 - d_1
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

    def test_equals_operation(self):
        """ Equal and non-equal Dollars """
        self.assertEqual(False, self.d_1 == self.d_2)
        d_3 = Dollars(6, 199)
        self.assertEqual(False, self.d_2 == d_3)
        self.assertEqual(True, self.d_1 == d_3)
        # Compare with a different currency
        d_4 = Dollars(7, 99, currency=VERIFIED_CURRENCIES[2])
        self.assertEqual(False, self.d_1 == d_4)

    def test_comparison_operations(self):
        """ Greater than and less than Dollar comparison """
        self.assertEqual(True, self.d_1 < self.d_2)
        self.assertEqual(False, self.d_1 > self.d_2)
        #
        self.assertEqual(True, self.d_1 < Dollars(100))
        self.assertEqual(True, self.d_1 > Dollars(1, 99))

    def test_multiplication(self):
        """ The Multiplication operation """
        self.assertEqual(Dollars(79, 90), self.d_1 * 10)
        self.assertEqual(Dollars(799), self.d_1 * 100)
        self.assertEqual(Dollars(7990), self.d_1 * 1000)
        #
        self.assertEqual(Dollars(102), self.d_2 * 10)
        self.assertEqual(Dollars(1020), self.d_2 * 100)
        #
        self.assertEqual(Dollars(1, 2), self.d_2 * (1 / 10))
        self.assertEqual(Dollars(2, 4), self.d_2 * (2 / 10))
        self.assertEqual(Dollars(3, 6), self.d_2 * (3 / 10))
        self.assertEqual(Dollars(7, 14), self.d_2 * (7 / 10))

    def test_invalid_multiplication(self):
        """ Attempt bad multiplication operations """
        with self.assertRaises(TypeError):
            print(Dollars(3) * Dollars(3))
        with self.assertRaises(ValueError):
            print(Dollars(5) * -2)

    def test_string(self):
        """ Representing Dollars as a string """
        self.assertEqual('$7.99', str(self.d_1))
        self.assertEqual('$10.20', str(self.d_2))


if __name__ == '__main__':
    unittest.main()
