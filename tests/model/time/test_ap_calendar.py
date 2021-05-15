""" Testing for accounting calendar operations """
import datetime
import unittest

from model.time import net_days
from model.time.ap_calendar import APCalendar, DAYS_IN_MONTH


class TestAPCalendar(unittest.TestCase):
    """ Test the initialization and usage of APCalendar objects """

    def setUp(self) -> None:
        self.cal = APCalendar(year=2018)
        self.c_leap = APCalendar(year=2020)

    def test_init(self):
        """ Initialization works """
        self.assertEqual(False, self.cal.is_leap)
        self.assertEqual(True, self.c_leap.is_leap)

    def test_start_date_monthly(self):
        """ Start date of the month """
        for i in range(1, 13):
            date = self.cal.start_date(i)
            print(date)
            self.assertEqual('01', str(date)[-2:])
        self.cal.update_year(1955)
        for i in range(1, 13):
            self.assertEqual('01', str(self.cal.start_date(i))[-2:])

    def test_start_date_monthly_leap(self):
        """ Start date of the month in leap years """
        for i in range(1, 13):
            date = self.c_leap.start_date(i)
            print(date)
            self.assertEqual('01', str(date)[-2:])
        self.c_leap.update_year(2024)
        for i in range(1, 13):
            self.assertEqual('01', str(self.c_leap.start_date(i))[-2:])

    def test_end_date_monthly(self):
        """ Check end of the month dates in non-leap years"""
        for i in range(1, 13):
            date = self.cal.end_date(i)
            print(date)
            self.assertEqual(str(DAYS_IN_MONTH[i]), str(date)[-2:])
        self.cal.update_year(2029)
        for i in range(1, 13):
            date = self.cal.end_date(i)
            print(date)
            self.assertEqual(str(DAYS_IN_MONTH[i]), str(date)[-2:])

    def test_end_date_monthly_leap(self):
        """ Check the end of the month dates in leap years """
        self.assertEqual(str(31), str(self.c_leap.end_date(1))[-2:])
        self.assertEqual(str(29), str(self.c_leap.end_date(2))[-2:])
        for i in range(3, 13):
            date = self.c_leap.end_date(i)
            print(date)
            self.assertEqual(str(DAYS_IN_MONTH[i]), str(date)[-2:])
        self.c_leap.update_year(2024)
        self.assertEqual(str(31), str(self.c_leap.end_date(1))[-2:])
        self.assertEqual(str(29), str(self.c_leap.end_date(2))[-2:])
        for i in range(3, 13):
            date = self.c_leap.end_date(i)
            print(date)
            self.assertEqual(str(DAYS_IN_MONTH[i]), str(date)[-2:])

    def test_net_days(self):
        """ Check net 30 days due date calculations """
        self.assertEqual(
            datetime.date(2018, 1, 31),
            net_days(datetime.date(2018, 1, 1), 30)
        )
        self.assertEqual(
            datetime.date(2018, 3, 2),
            net_days(datetime.date(2018, 1, 31), 30)
        )
        self.assertEqual(
            datetime.date(2020, 3, 1),
            net_days(datetime.date(2020, 1, 31), 30)
        )
        self.assertEqual(
            datetime.date(2020, 3, 21),
            net_days(datetime.date(2020, 2, 20), 30)
        )

    def test_ap_date_range(self):
        """ Check the Accounting Period date range method """
        feb_2018_range = self.cal.get_ap_date_range(2)
        self.assertEqual(
            datetime.date(2018, 2, 1), feb_2018_range[0])
        self.assertEqual(
            datetime.date(2018, 2, 28), feb_2018_range[1])
        feb_2020_range = self.c_leap.get_ap_date_range(2)
        self.assertEqual(
            datetime.date(2020, 2, 1), feb_2020_range[0])
        self.assertEqual(
            datetime.date(2020, 2, 29), feb_2020_range[1])

    def test_ap_date_range_invalid(self):
        """ Invalid inputs to the date range method """
        with self.assertRaises(ValueError):
            self.cal.get_ap_date_range(0)
        with self.assertRaises(ValueError):
            self.cal.get_ap_date_range(13)


if __name__ == '__main__':
    unittest.main()
