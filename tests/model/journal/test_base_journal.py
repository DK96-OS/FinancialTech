""" Testing for the Journal data structure """
# pylint: disable=protected-access
import datetime
import unittest

from model.data.dollars import Dollars
from model.journal.base_journal import BaseJournal
from model.journal.journal_entry import JournalEntry
from model.time.accounting_period import AccountingPeriod

AP = AccountingPeriod(
    datetime.date(2018, 2, 1), datetime.date(2018, 2, 28))


class TestBaseJournal(unittest.TestCase):
    """ Journal Initialization and operation testing """

    def setUp(self) -> None:
        self.test_journal = BaseJournal(
            name='General',
            opening_date=AP.get_open_date(),
            closing_date=AP.get_close_date()
        )

    def test_init(self):
        """ Journal Initial state """
        self.assertEqual(
            'General', self.test_journal.name)
        self.assertEqual(
            AP.get_open_date(), self.test_journal.get_open_date())
        self.assertEqual(
            AP.get_close_date(), self.test_journal.get_close_date())

    def test_add_entry(self):
        """ Journal Entry Insertion """
        new_entry = JournalEntry(
            date=datetime.date(2018, 2, 1),
            dollars=Dollars(9, 99),
            description="Monthly Tech News Subscription 1"
        )
        was_inserted = self.test_journal.insert_entry(new_entry)
        self.assertEqual(True, was_inserted)

    def test_invalid_entry_date(self):
        """ Journal Entry rejected because of date"""
        new_entry = JournalEntry(
            date=datetime.date(2018, 3, 1),
            dollars=Dollars(9, 99),
            description="Monthly Tech News Subscription 2"
        )
        was_inserted = self.test_journal.insert_entry(new_entry)
        self.assertEqual(False, was_inserted)


if __name__ == '__main__':
    unittest.main()
