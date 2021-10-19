""" The essential attributes of a Journal """
import datetime

from model.time.accounting_period import AccountingPeriod


class JournalAttributes(AccountingPeriod):
    """ Contains the basic attributes of a Journal """

    def __init__(
            self,
            journal_name: str,
            opening_date: datetime.date,
            closing_date: datetime.date
    ):
        super().__init__(opening_date, closing_date)
        self.journal_name = journal_name
