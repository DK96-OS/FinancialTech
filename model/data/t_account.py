""" T-Accounts organize Account activity for one accounting cycle """
from model.data.dollars import Dollars
from model.data.transaction import Transaction
from model.time.accounting_period import AccountingPeriod


class TAccount:
    """ An Account that is available for one Accounting Period """

    def __init__(
            self, number: int,
            accounting_period: AccountingPeriod,
    ):
        self.account_id = number
        self.account_period = accounting_period
        self._debit_transactions, self._debit_balance = list(), Dollars(0)
        self._credit_transactions, self._credit_balance = list(), Dollars(0)

    def debit(self, transaction: Transaction) -> bool:
        """ Add a debit transaction, update balance.
        :returns True if succeeded, false if date is incorrect
        """
        if not self.account_period.contains_date(transaction.date):
            return False
        self._debit_balance += transaction.dollars
        self._debit_transactions.append(transaction)
        return True

    def credit(self, transaction: Transaction) -> bool:
        """ Add a credit transaction, update balance.
        :returns True if succeeded, false if date is incorrect
        """
        if not self.account_period.contains_date(transaction.date):
            return False
        self._credit_balance += transaction.dollars
        self._credit_transactions.append(transaction)
        return True

    def remove_transaction(self, transaction: Transaction) -> bool:
        """ Remove transaction, recalculate balance.
        :returns True if succeeded, false if transaction not found
        """
        if transaction in self._debit_transactions:
            self._debit_transactions.remove(transaction)
            self._debit_balance -= transaction.dollars
            return True
        if transaction in self._credit_transactions:
            self._credit_transactions.remove(transaction)
            self._credit_balance -= transaction.dollars
            return True
        return False
