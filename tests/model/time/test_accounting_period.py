""" Testing for the Accounting Period data structure """
import datetime
import unittest

from model.time.ap_calendar import APCalendar

CAL_2021 = APCalendar(2021)


class TestAccountingPeriod(unittest.TestCase):
    """ Accounting Period Tests """

    def setUp(self) -> None:
        self.ap_1 = CAL_2021.get_ap(1)  # Jan 2021
        self.ap_2 = CAL_2021.get_ap(2)  # Feb 2021

    def test_contains_date_correct(self):
        """ Contains Date method test """
        # First AP: Jan 2021
        assert self.ap_1.contains_date(CAL_2021.start_date(1))
        assert self.ap_1.contains_date(CAL_2021.end_date(1))
        assert self.ap_1.contains_date(datetime.date(2021, 1, 15))
        # Next AP: Feb 2021
        assert self.ap_2.contains_date(CAL_2021.start_date(2))
        assert self.ap_2.contains_date(CAL_2021.end_date(2))
        assert self.ap_2.contains_date(datetime.date(2021, 2, 15))

    def test_contains_date_incorrect(self):
        """ Contains date returns false """
        # First AP: Jan 2021
        self.assertEqual(False, self.ap_1.contains_date(datetime.date(2020, 1, 15)))
        self.assertEqual(False, self.ap_1.contains_date(datetime.date(2021, 2, 15)))
        self.assertEqual(False, self.ap_1.contains_date(datetime.date(1021, 4, 24)))
        # Next AP: Feb 2021
        self.assertEqual(False, self.ap_2.contains_date(datetime.date(2020, 2, 15)))
        self.assertEqual(False, self.ap_2.contains_date(datetime.date(2021, 3, 15)))
        self.assertEqual(False, self.ap_2.contains_date(datetime.date(2020, 2, 29)))

    def test_date_range(self):
        """ Date Range tuple test """
        self.assertEqual(
            (datetime.date(2021, 1, 1), datetime.date(2021, 1, 31)),
            self.ap_1.get_date_range())
        self.assertEqual(
            (datetime.date(2021, 2, 1), datetime.date(2021, 2, 28)),
            self.ap_2.get_date_range())
