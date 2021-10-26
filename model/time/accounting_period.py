""" Accounting events are divided into an accounting period """
import datetime
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class AccountingPeriod:
    """ An accounting period data structure with helpful methods """
    opening_date: datetime.date
    closing_date: datetime.date

    def get_open_date(self) -> datetime.date:
        """ Obtain the opening date for this accounting cycle """
        return self.opening_date

    def get_close_date(self) -> datetime.date:
        """ Obtain the closing date for this accounting cycle """
        return self.closing_date

    def contains_date(self, date: datetime.date) -> bool:
        """ Whether a date belongs in this account cycle """
        return self.opening_date <= date <= self.closing_date

    def get_date_range(self) -> tuple:
        """ Returns a tuple of opening and closing dates """
        return self.opening_date, self.closing_date
