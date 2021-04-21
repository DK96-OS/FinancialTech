from model.data.Currencies import default_currency, verified_currencies
from model.data.DataExceptions import CurrencyException, NegativeDollarException


class Dollars:
    """ Represents an amount of money in dollars and cents.
    100 cents are in a dollar. """

    def __init__(self, 
                 dollars: int, cents: int = 0,
                 currency: str = default_currency):
        # Validate currency
        cur = currency.upper() # Ensure always uppercase
        if len(cur) == 3 and \
                cur in verified_currencies or cur.isalpha():
            self.currency = cur
        else:
            raise CurrencyException()
        # Validate dollar and cent values
        if dollars < 0 or cents < 0:
            raise NegativeDollarException() # Negatives not allowed
        elif cents in range(0, 100):
            self.dollars, self.cents = dollars, cents
        else:
            self.cents = cents % 100
            self.dollars = dollars + (cents / 100).__floor__()

    def __add__(self, other):
        """ Returns the Sum of two Dollar Amounts """
        self.check_compatible(other)
        return Dollars(
            dollars=self.dollars + other.dollars,
            cents=self.cents + other.cents,
            currency=self.currency
        )

    def __sub__(self, other):
        """ Returns the Difference of two Dollar Amounts """
        self.check_compatible(other)
        diff = abs(self.as_float() - other.as_float())
        dollars = diff.__floor__()
        return Dollars(
            dollars=dollars,
            cents=((diff - dollars) * 100).__round__(),
            currency=self.currency
        )

    def check_compatible(self, other):
        """ Determines whether these two arguments are compatible """
        if not type(other) is Dollars:
            raise TypeError
        if self.currency != other.currency:
            raise CurrencyException

    def as_float(self): return self.dollars + (self.cents / 100.0)
