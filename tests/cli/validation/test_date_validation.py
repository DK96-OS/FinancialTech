""" Testing for the CLI Date Validation functions """
import datetime
import unittest

from cli.validation.date_validation import is_valid_date


class TestDateValidation(unittest.TestCase):
    """ Testing Date Validation """

    def test_correct_iso_strings(self):
        """ Test some iso strings """
        self.assertEquals(
            True, is_valid_date("1999-01-25")
        )
        self.assertEquals(
            True, is_valid_date("2099-12-20")
        )

    def test_proper_date_string(self):
        """ Test strings provided by datetime """
        date1 = datetime.date(2000, 1, 31)
        self.assertEquals(
            True, is_valid_date(date1.isoformat())
        )
        date1 = datetime.date(2100, 4, 30)
        self.assertEquals(
            True, is_valid_date(date1.isoformat())
        )

    def test_bad_iso_strings_month(self):
        """ Iso format with invalid months """
        self.assertEquals(
            False, is_valid_date("2030-20-01")
        )
        self.assertEquals(
            False, is_valid_date("2030-00-01")
        )

    def test_bad_iso_strings_year(self):
        """ Iso format with invalid year """
        self.assertEquals(
            False, is_valid_date("0000-01-01")
        )
        self.assertEquals(
            False, is_valid_date("9999-01-01")
        )

    def test_bad_iso_strings_day(self):
        """ Iso format with invalid day """
        self.assertEquals(
            False, is_valid_date("2000-02-61")
        )
        self.assertEquals(
            False, is_valid_date("2000-02-00")
        )
        self.assertEquals(
            False, is_valid_date("2000-02-30")
        )
        self.assertEquals(
            False, is_valid_date("2000-04-31")
        )

    def test_non_iso_string(self):
        """ Non-iso but the same length, containing two dashes """
        self.assertEquals(
            False, is_valid_date("768-769-12")
        )
        self.assertEquals(
            False, is_valid_date("7-68769-12")
        )
        self.assertEquals(
            False, is_valid_date("7-6876912-")
        )

    def test_non_iso_string2(self):
        """ Non-iso does not pass length check """
        self.assertEquals(
            False, is_valid_date("768769")
        )
        self.assertEquals(
            False, is_valid_date("768-769-1322")
        )

    def test_non_string(self):
        """ Test an object that is not a string - does not raise error """
        self.assertEquals(
            False, is_valid_date(datetime.date(2, 2, 1))
        )
