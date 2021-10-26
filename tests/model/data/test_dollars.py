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

    def test_init_bad_cents(self):
        """ Invalid Cents value """
        with self.assertRaises(ValueError):
            Dollars(10, 100)
        with self.assertRaises(ValueError):
            Dollars(10, 510)
        with self.assertRaises(ValueError):
            Dollars(10, -5)
        with self.assertRaises(TypeError):
            Dollars(10, 1.5)

    def test_init_bad_dollars(self):
        """ Invalid dollar value """
        with self.assertRaises(ValueError):
            Dollars(-1, 1)
        with self.assertRaises(TypeError):
            Dollars(1.1, 1)

    def test_init_bad_currency(self):
        """ Invalid currency """
        with self.assertRaises(CurrencyException):
            Dollars(1, 1, 'ji3')
        with self.assertRaises(CurrencyException):
            Dollars(1, 1, 'ABC')
        with self.assertRaises(CurrencyException):
            Dollars(1, 1, 'jik9njk')

    def test_addition(self):
        """ Perform basic addition of two simple Dollar amounts """
        d_sum = Dollars(150, 20) + Dollars(300, 50)
        self.assertEqual(450, d_sum.dollars)
        self.assertEqual(70, d_sum.cents)
        # Test another set of numbers
        d_sum = Dollars(150000, 41) + Dollars(3000, 42)
        self.assertEqual(153000, d_sum.dollars)
        self.assertEqual(83, d_sum.cents)

    def test_addition_carrying(self):
        """ Carrying cents into dollars when adding """
        d_sum = self.d_1 + self.d_2
        self.assertEqual(18, d_sum.dollars)
        self.assertEqual(19, d_sum.cents)
        # Check another set of numbers
        d_sum = Dollars(60, 65) + Dollars(60, 50)
        self.assertEqual(121, d_sum.dollars)
        self.assertEqual(15, d_sum.cents)

    def test_addition_bad(self):
        """ Adding different currencies fails """
        alt_currency = Dollars(10, 9, VERIFIED_CURRENCIES[3])
        with self.assertRaises(CurrencyException):
            self.d_1 + alt_currency

    def test_addition_bad_non_dollar_object(self):
        """ Adding a non-dollar object fails """
        with self.assertRaises(TypeError):
            self.d_1 + 6   # Adding a non-Dollars object

    def test_subtraction(self):
        """ Simple subtraction operation """
        d_diff = self.d_2 - self.d_1    # 10.20 - 7.99
        self.assertEqual(2, d_diff.dollars)
        self.assertEqual(21, d_diff.cents)
        # Test another set of numbers
        d_diff = Dollars(100, 80) - Dollars(10, 5)
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
        d_3 = Dollars(7, 99)
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
        self.assertEqual(Dollars(9, 18), self.d_2 * (9 / 10))

    def test_multiplication_rounding(self):
        """ Test specific rounding outcomes """
        amount_1 = Dollars(45, 80)
        t1 = amount_1 * 90
        t1_float = amount_1 * 90.0
        t1_expected = Dollars(4122)
        self.assertEqual(t1_expected, t1)
        self.assertEqual(t1_expected, t1_float)

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
