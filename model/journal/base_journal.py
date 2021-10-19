""" Basic Journal functionality """

from model.journal.journal_attributes import JournalAttributes
from model.journal.journal_entry import JournalEntry


class BaseJournal:
    """ The basic Journal functionality """

    def __init__(self,
                 attributes: JournalAttributes,
                 ):
        self.attributes = attributes
        self._entries = []

    def insert_entry(self, event: JournalEntry) -> bool:
        """ Insert a new Journal Entry
        Verifies that the Entry date is within the Accounting Period
        :return Whether the Entry belongs in this journal
        """
        if self.attributes.contains_date(event.date):
            self._entries.append(event)
            return True
        else:
            return False
