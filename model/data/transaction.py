""" A transaction represents a transfer of Dollars between Accounts """
import datetime

from model.data.t_account import TAccount
from model.data.dollars import Dollars

class Transaction:
  """ Data Structure for a Transaction """

    def __init__(self,
                 reference_id,
                 date: datetime.date,
                 dollars: Dollars,
                 description: str,
                 ):
        if isinstance(reference_id, str):
            if reference_id.strip() == '':
                raise ValueError('Reference id cannot be blank')
            if reference_id.isnumeric() and '.' not in reference_id:
                reference_id = int(reference_id)
        elif isinstance(reference_id, int):
            if reference_id < 0:
                raise ValueError('Reference id cannot be negative')
        else:
            raise TypeError('Reference id must be an integer or string')
        if dollars.as_float() <= 0:
            raise ValueError('Dollars cannot be zero')
        if len(description.strip()) < 5:
            raise ValueError('Provide a reasonable description')
        # Validation complete
        self.reference_id, self.date = reference_id, date
        self.dollars = dollars
        self.description = description
        # Private references for accounts posted
        self._debited_account, self._credited_account = None, None

    def get_affected_accounts(self) -> tuple:
        """ The ids of the accounts: debited, then credited.
             :returns an empty tuple if either account is missing
        """
        deb, cred = self._debited_account, self._credited_account
        if deb is not None and cred is not None:
            return deb.account_id, cred.account_id
        return ()

    def post_to_accounts(
            self, debited: TAccount, credited: TAccount
    ) -> bool:
        """ Connect this transaction to the given accounts
            If there were already accounts posted, reverse them
         """
        if debited == credited or debited.account_id == credited.account_id:
            raise ValueError('A transaction must involve two separate accounts')
        if self._debited_account != debited:
            if self._debited_account is not None:
                self._debited_account.remove_transaction(self)
            self._debited_account = debited
            if not debited.debit(self):
                return False
        if self._credited_account != credited:
            if self._credited_account is not None:
                self._credited_account.remove_transaction(self)
            self._credited_account = credited
            return credited.credit(self)
        return True

    def unpost_from_accounts(self) -> bool:
        """ Removes this transaction
            :returns True if transaction is not posted (now or before)
        """
        if self._debited_account is not None:
            result = self._debited_account.remove_transaction(self)
            if not result:
                return False
        if self._credited_account is not None:
            return self._credited_account.remove_transaction(self)
        return True
