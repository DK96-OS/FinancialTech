""" Testing for the Transaction Data structure
    Transaction is coupled with the T Account class
"""
import datetime
import unittest

from model.data.dollars import Dollars
from model.data.transaction import Transaction
from model.time.accounting_period import AccountingPeriod
from model.data.t_account import TAccount


# Test constants
DATE_RANGE = (datetime.date(2018, 2, 1), datetime.date(2018, 2, 28))
ACCOUNT_PERIOD = AccountingPeriod(DATE_RANGE[0], DATE_RANGE[1])
PRICE = Dollars(10, 50)
DESCRIBE = 'A proper description of a transaction is important'


class TestTransaction(unittest.TestCase):
    """ Transaction initialization and operations testing """

    def setUp(self) -> None:
        """ Create Key Examples """
        self.rent_paid = Transaction(
            'RENT_PREPAID_3', DATE_RANGE[0], PRICE, 'Rent Payment for Feb 2018')
        self.rent_used = Transaction(
            'RENT_USED_3', DATE_RANGE[1], PRICE, 'Rent Used for Feb 2018')
        self.accounts = {
            'Cash': 101, 101: TAccount(101, ACCOUNT_PERIOD),
            'Prepaid Rent': 111, 111: TAccount(111, ACCOUNT_PERIOD),
            'Rent Expense': 211, 211: TAccount(211, ACCOUNT_PERIOD),
        }

    def test_init_values(self):
        """ Check initialization of Transaction instances """
        transfer_0 = Transaction(0, DATE_RANGE[0], PRICE, DESCRIBE)
        self.assertEqual(0, transfer_0.reference_id)
        self.assertEqual(DATE_RANGE[0], transfer_0.date)
        self.assertEqual(PRICE, transfer_0.dollars)
        self.assertEqual(DESCRIBE, transfer_0.description)
        # Check numerical string conversion to integer
        transfer_1 = Transaction('1', DATE_RANGE[0], PRICE, DESCRIBE)
        transfer_2 = Transaction('2.5', DATE_RANGE[0], PRICE, DESCRIBE)
        self.assertEqual(1, transfer_1.reference_id)
        self.assertEqual('2.5', transfer_2.reference_id)

    def test_init_bad_reference(self):
        """ Reference Id must be positive int or non-blank string """
        with self.assertRaises(ValueError):
            Transaction('', DATE_RANGE[0], PRICE, '')
        with self.assertRaises(ValueError):
            Transaction('   ', DATE_RANGE[0], PRICE, '')
        with self.assertRaises(ValueError):
            Transaction(-1, DATE_RANGE[0], PRICE, DESCRIBE)
        with self.assertRaises(TypeError):
            Transaction([2], DATE_RANGE[0], PRICE, DESCRIBE)

    def test_init_bad_values(self):
        """ Additional bad initialization parameters """
        # Dollars cannot be zero or negative
        with self.assertRaises(ValueError):
            Transaction(1, DATE_RANGE[0], Dollars(0), DESCRIBE)
        with self.assertRaises(ValueError):
            bad_price = Dollars(1)
            bad_price.dollars -= 20
            Transaction(1, DATE_RANGE[0], bad_price, DESCRIBE)
        # Description must be greater than 4 non-space characters
        with self.assertRaises(ValueError):
            Transaction(1, DATE_RANGE[0], PRICE, '')
        with self.assertRaises(ValueError):
            description = DESCRIBE[:4]
            print(description)
            Transaction(1, DATE_RANGE[0], PRICE, DESCRIBE[:4])

    def test_account_methods_before_posting(self):
        """ Check values returned by methods before posting """
        self.assertEqual((), self.rent_paid.get_affected_accounts())
        self.assertEqual((), self.rent_used.get_affected_accounts())
        # Unpost returns True
        self.assertEqual(True, self.rent_paid.unpost_from_accounts())
        self.assertEqual(True, self.rent_used.unpost_from_accounts())

    def test_posting(self):
        """ Transaction saves account references after posting """
        self.assertEqual(True, self.rent_paid.post_to_accounts(
            debited=self.accounts[self.accounts['Prepaid Rent']],
            credited=self.accounts[self.accounts['Cash']]
        ))
        self.assertEqual(True, self.rent_used.post_to_accounts(
            debited=self.accounts[211], credited=self.accounts[111]
        ))
        self.assertEqual(
            (111, 101), self.rent_paid.get_affected_accounts())
        self.assertEqual(
            (211, 111), self.rent_used.get_affected_accounts())
        # Internal member check
        self.assertEqual(111, self.rent_paid._debited_account.account_id)
        self.assertEqual(101, self.rent_paid._credited_account.account_id)

    def test_undo_posting(self):
        """ Transaction clears all account references after undo posting """
        self.rent_paid.post_to_accounts(
            self.accounts[101], self.accounts[111])
        self.assertEqual(
            (101, 111), self.rent_paid.get_affected_accounts()
        )
        # That's the wrong direction for this transaction, undo it!
        self.assertEqual(
            True, self.rent_paid.unpost_from_accounts()
        )   # Undo succeeded
        self.assertEqual((), self.rent_paid.get_affected_accounts())
        # Internal member check
        self.assertEqual(None, self.rent_paid._debited_account)
        self.assertEqual(None, self.rent_paid._credited_account)


if __name__ == '__main__':
    unittest.main()
