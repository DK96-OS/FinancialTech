import calendar
import datetime

days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}


def net_days(start: datetime.date, days: int):
    """ Find a future due date """
    return start + datetime.timedelta(days=days)


class APCalendar:
    """ Accounting Period Calendar """
    def __init__(self, year: int):
        self.year = year
        self.is_leap = calendar.isleap(year)

    def update_year(self, year: int):
        self.year = year
        self.is_leap = calendar.isleap(year)

    def start_date(self, month: int):
        """ Find the start date of the given month """
        return datetime.date(self.year, month, 1)

    def end_date(self, month: int):
        """ Find the end date of the given month """
        if month == 2 and self.is_leap:
            return datetime.date(self.year, month, 29)
        else:
            return datetime.date(self.year, month, days_in_month[month])
