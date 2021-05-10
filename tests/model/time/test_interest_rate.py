""" Interest Rate Class Testing """
import unittest

from model.data.dollars import Dollars
from model.time.interest_rate import InterestRate
from model.time.time_unit import TimeUnit


class TestInterestRate(unittest.TestCase):
    """ Test the creation and usage of Interest Rate objects """

    def setUp(self) -> None:
        self.init_amount = Dollars(100)

    def test_init_integers(self):
        """ Initialization using Integers """
        test_rate = InterestRate(3)
        self.assertEqual(test_rate.rate, 0.03)
        self.assertEqual(test_rate.rate_cycle, TimeUnit.ANNUALLY)
        test_rate = InterestRate(20)
        self.assertEqual(test_rate.rate, 0.2)
        with self.assertRaises(ValueError):
            InterestRate(120)
        with self.assertRaises(ValueError):
            InterestRate(-10)

    def test_init_strings(self):
        """ Initialization using rate percentages from strings """
        test_rate = InterestRate('4%')
        self.assertEqual(0.04, test_rate.rate)
        test_rate = InterestRate('4.5%')
        self.assertEqual(0.045, test_rate.rate)
        with self.assertRaises(ValueError):
            InterestRate('1')
        with self.assertRaises(ValueError):
            InterestRate('-10%')

    def test_simple_interest(self):
        """ Check the accuracy of simple interest calculations """
        rate = InterestRate(2)  # 2% annually
        init = self.init_amount
        self.assertEqual(
            Dollars(1),
            rate.simple_interest(init, 6, TimeUnit.MONTHLY)
        )
        self.assertEqual(
            Dollars(2),
            rate.simple_interest(init, 12, TimeUnit.MONTHLY)
        )
        self.assertEqual(
            Dollars(1),
            rate.simple_interest(init, 2, TimeUnit.QUARTERLY)
        )
        self.assertEqual(
            Dollars(2 * 5),     # 2% per year for 5 years
            rate.simple_interest(init, 5, TimeUnit.ANNUALLY)
        )

    def test_simple_interest_exceptions(self):
        """ Exceptions in simple interest calculations """
        rate = InterestRate(5, TimeUnit.ANNUALLY)
        with self.assertRaises(ValueError):
            rate.simple_interest(self.init_amount, 30, TimeUnit.DAILY)
        with self.assertRaises(ValueError):
            rate.simple_interest(self.init_amount, 30, TimeUnit.WEEKLY)
        rate.rate_cycle = TimeUnit.WEEKLY
        with self.assertRaises(ValueError):
            rate.simple_interest(self.init_amount, 10, TimeUnit.MONTHLY)
        with self.assertRaises(ValueError):
            rate.simple_interest(self.init_amount, 10, TimeUnit.ANNUALLY)

    def test_string_method(self):
        """ Displaying Interest Rate as a string """
        rate_1 = InterestRate(4)
        self.assertEqual('4% annually', str(rate_1))
        rate_2 = InterestRate(0.045, TimeUnit.MONTHLY)
        self.assertEqual('4.5% monthly', str(rate_2))
        rate_2 = InterestRate(0.145, TimeUnit.QUARTERLY)
        self.assertEqual('14.5% quarterly', str(rate_2))


if __name__ == '__main__':
    unittest.main()
