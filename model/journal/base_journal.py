""" Basic Journal functionality """
import datetime

from model.journal.journal_entry import JournalEntry
from model.time.accounting_period import AccountingPeriod


class BaseJournal(AccountingPeriod):
    """ A Journal for one accounting period """

    def __init__(self,
                 name: str,
                 opening_date: datetime.date,
                 closing_date: datetime.date,
                 ):
        super().__init__(opening_date, closing_date)
        self.name = name
        self._entries = []

    def insert_entry(self, event: JournalEntry) -> bool:
        """ Insert a new Journal Entry
        Verifies that the Entry date is within the Accounting Period
        :return Whether the Entry belongs in this journal
        """
        if self.contains_date(event.date):
            self._entries.append(event)
            return True
        else:
            return False
