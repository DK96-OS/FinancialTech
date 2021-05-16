""" Testing for the Accounting Period Account Data structure """
# pylint: disable=protected-access
import unittest

from model.data.dollars import Dollars
from model.data.t_account import TAccount
from model.data.transaction import Transaction
from model.time.ap_calendar import APCalendar

# Test Constants
ACCOUNT_PERIOD = APCalendar(2018).get_ap(2)
OPEN_DATE = ACCOUNT_PERIOD.get_open_date()
CAPITAL = Dollars(24000)
EQUIPMENT_COST = Dollars(3000)


class TestTAccount(unittest.TestCase):
    """ AP Account initialization and operations testing """

    def setUp(self) -> None:
        self.cash_account = TAccount(101, ACCOUNT_PERIOD)
        self.equipment_account = TAccount(102, ACCOUNT_PERIOD)
        self.expense_account = TAccount(201, ACCOUNT_PERIOD)
        self.equity_account = TAccount(301, ACCOUNT_PERIOD)
        self.capital_investment = Transaction(
            1, ACCOUNT_PERIOD.get_open_date(), CAPITAL,
            'Capital investment from business owner'
        )
        self.capital_investment.post_to_accounts(
            debited=self.cash_account, credited=self.equity_account)

    def test_init(self):
        """ Initialization of T-Accounts """
        self.assertEqual(101, self.cash_account.account_id)
        self.assertEqual(102, self.equipment_account.account_id)
        self.assertEqual(201, self.expense_account.account_id)
        self.assertEqual(301, self.equity_account.account_id)
        self.assertEqual(ACCOUNT_PERIOD, self.cash_account.account_period)
        self.assertEqual(ACCOUNT_PERIOD, self.equipment_account.account_period)
        self.assertEqual(ACCOUNT_PERIOD, self.expense_account.account_period)
        self.assertEqual(ACCOUNT_PERIOD, self.equity_account.account_period)
        self.assertEqual(
            (CAPITAL, Dollars(0)), self.cash_account.get_balances())
        self.assertEqual(
            (Dollars(0), Dollars(0)), self.equipment_account.get_balances())
        self.assertEqual(
            (Dollars(0), Dollars(0)), self.expense_account.get_balances())
        self.assertEqual(
            (Dollars(0), CAPITAL), self.equity_account.get_balances())
        # Internal member check
        assert self.capital_investment in self.cash_account._debit_transactions
        assert self.capital_investment in self.equity_account._credit_transactions

    def test_posting_through_transaction(self):
        """ Post to accounts using the transaction method """
        equipment_purchase = Transaction(
            'EQUIP_1', OPEN_DATE, EQUIPMENT_COST, '2 Equipment model 4590')
        assert equipment_purchase.post_to_accounts(
            self.equipment_account, self.cash_account)
        # Check Account balances
        self.assertEqual(
            (CAPITAL, EQUIPMENT_COST), self.cash_account.get_balances())
        self.assertEqual(
            (EQUIPMENT_COST, Dollars(0)), self.equipment_account.get_balances())
        self.assertEqual(
            (Dollars(0), Dollars(0)), self.expense_account.get_balances())
        self.assertEqual(
            (Dollars(0), CAPITAL), self.equity_account.get_balances())
        # Internal member check
        self.assertEquals(
            1, len(self.cash_account._debit_transactions))
        self.assertEquals(
            1, len(self.cash_account._credit_transactions))
        self.assertEqual(
            1, len(self.equipment_account._debit_transactions))
        self.assertEqual(
            0, len(self.equipment_account._credit_transactions))
        self.assertEquals(
            0, len(self.equity_account._debit_transactions))
        self.assertEquals(
            1, len(self.equity_account._credit_transactions))

    def test_post_and_remove_transaction(self):
        """ Post and remove a transaction using the transaction """
        assert self.capital_investment.post_to_accounts(
            self.cash_account, self.equity_account)
        bad_transaction = Transaction(
            2, OPEN_DATE, CAPITAL * 0.5, 'Accidental transaction')
        assert bad_transaction.post_to_accounts(
            self.expense_account, self.equity_account)
        # Check balances
        self.assertEqual(
            (CAPITAL, Dollars(0)), self.cash_account.get_balances())
        self.assertEqual(
            (CAPITAL * 0.5, Dollars(0)), self.expense_account.get_balances())
        self.assertEqual(
            (Dollars(0), CAPITAL * 1.5), self.equity_account.get_balances())
        # That is not right, undo post transaction
        assert bad_transaction in self.expense_account._debit_transactions
        assert bad_transaction in self.equity_account._credit_transactions
        assert bad_transaction.unpost_from_accounts()
        assert bad_transaction not in self.expense_account._debit_transactions
        assert bad_transaction not in self.equity_account._credit_transactions
        # Balances have been restored
        self.assertEqual(
            (CAPITAL, Dollars(0)), self.cash_account.get_balances())
        self.assertEqual(
            (Dollars(0), Dollars(0)), self.expense_account.get_balances())
        self.assertEqual(
            (Dollars(0), CAPITAL), self.equity_account.get_balances())
        # Internal member check
        self.assertEquals(
            1, len(self.cash_account._debit_transactions))
        self.assertEquals(
            1, len(self.equity_account._credit_transactions))
