""" Calendar Management for Accounting Periods """
import calendar
import datetime

from model.time.accounting_period import AccountingPeriod

DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}


class APCalendar:
    """ Accounting Period Calendar """

    def __init__(self, year: int):
        self.year = year
        self.is_leap = calendar.isleap(year)

    def update_year(self, year: int):
        """ Set the year of this calendar """
        self.year = year
        self.is_leap = calendar.isleap(year)

    def start_date(self, month: int):
        """ Find the start date of the given month """
        return datetime.date(self.year, month, 1)

    def end_date(self, month: int):
        """ Find the end date of the given month """
        if month == 2 and self.is_leap:
            return datetime.date(self.year, month, 29)
        return datetime.date(self.year, month, DAYS_IN_MONTH[month])

    def get_ap_date_range(self, month: int) -> tuple:
        """ Get the date range for a monthly accounting cycle """
        return self.start_date(month), self.end_date(month)

    def get_ap(self, month: int) -> AccountingPeriod:
        """ Get an Accounting Period for the given month """
        return AccountingPeriod(
            self.start_date(month), self.end_date(month))
