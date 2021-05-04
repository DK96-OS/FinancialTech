import datetime
import unittest

from model.time.ap_calendar import APCalendar, days_in_month, net_days


class TestAPCalendar(unittest.TestCase):

    def setUp(self) -> None:
        self.cal = APCalendar(year=2018)
        self.c_leap = APCalendar(year=2020)

    def test_init(self):
        self.assertEqual(False, self.cal.is_leap)
        self.assertEqual(True, self.c_leap.is_leap)

    def test_start_date_monthly(self):
        for i in range(1, 13):
            date = self.cal.start_date(i)
            print(date)
            self.assertEqual('01', str(date)[-2:])
        self.cal.update_year(1955)
        for i in range(1, 13):
            self.assertEqual('01', str(self.cal.start_date(i))[-2:])

    def test_start_date_monthly_leap(self):
        for i in range(1, 13):
            date = self.c_leap.start_date(i)
            print(date)
            self.assertEqual('01', str(date)[-2:])
        self.c_leap.update_year(2024)
        for i in range(1, 13):
            self.assertEqual('01', str(self.c_leap.start_date(i))[-2:])

    def test_end_date_monthly(self):
        for i in range(1, 13):
            date = self.cal.end_date(i)
            print(date)
            self.assertEqual(str(days_in_month[i]), str(date)[-2:])
        self.cal.update_year(2029)
        for i in range(1, 13):
            date = self.cal.end_date(i)
            print(date)
            self.assertEqual(str(days_in_month[i]), str(date)[-2:])

    def test_end_date_monthly_leap(self):
        self.assertEqual(str(31), str(self.c_leap.end_date(1))[-2:])
        self.assertEqual(str(29), str(self.c_leap.end_date(2))[-2:])
        for i in range(3, 13):
            date = self.c_leap.end_date(i)
            print(date)
            self.assertEqual(str(days_in_month[i]), str(date)[-2:])
        self.c_leap.update_year(2024)
        self.assertEqual(str(31), str(self.c_leap.end_date(1))[-2:])
        self.assertEqual(str(29), str(self.c_leap.end_date(2))[-2:])
        for i in range(3, 13):
            date = self.c_leap.end_date(i)
            print(date)
            self.assertEqual(str(days_in_month[i]), str(date)[-2:])

    def test_net_days(self):
        """ Check net 30 days due date calculations """
        self.assertEqual(datetime.date(2018, 1, 31),
                         net_days(datetime.date(2018, 1, 1), 30)
                         )
        self.assertEqual(datetime.date(2018, 3, 2),
                         net_days(datetime.date(2018, 1, 31), 30)
                         )
        self.assertEqual(datetime.date(2020, 3, 1),
                         net_days(datetime.date(2020, 1, 31), 30)
                         )
        self.assertEqual(datetime.date(2020, 3, 21),
                         net_days(datetime.date(2020, 2, 20), 30)
                         )


if __name__ == '__main__':
    unittest.main()
