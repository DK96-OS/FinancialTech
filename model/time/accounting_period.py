""" Accounting events are divided into an accounting period """
import datetime


class AccountingPeriod:
    """ An accounting period data structure with helpful methods """

    def __init__(self,
                 opening_date: datetime.date,
                 closing_date: datetime.date
                 ):
        self._opening_date = opening_date
        self._closing_date = closing_date

    def get_open_date(self) -> datetime.date:
        """ Obtain the opening date for this accounting cycle """
        return self._opening_date

    def get_close_date(self) -> datetime.date:
        """ Obtain the closing date for this accounting cycle """
        return self._closing_date

    def contains_date(self, date: datetime.date) -> bool:
        """ Whether a date belongs in this account cycle """
        return self._opening_date <= date <= self._closing_date

    def get_date_range(self) -> tuple:
        """ Returns a tuple of opening and closing dates """
        return self._opening_date, self._closing_date
