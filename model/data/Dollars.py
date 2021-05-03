import math

from model.data.currencies import default_currency, verified_currencies
from model.data.data_exceptions import CurrencyException


class Dollars:
    """ Represents an amount of money in dollars and cents.
    100 cents are in a dollar. """

    def __init__(self,
                 dollars: int, cents: int = 0,
                 currency: str = default_currency):
        # Validate currency
        cur = currency.upper()  # Ensure always uppercase
        if len(cur) == 3 and \
                cur in verified_currencies or cur.isalpha():
            self.currency = cur
        else:
            raise CurrencyException()
        # Validate dollar and cent values
        if type(dollars) is not int:
            raise TypeError('Dollars must be an integer')
        elif type(cents) is not int:
            raise TypeError('Cents must be an integer')
        if dollars < 0 or cents < 0:
            raise ValueError('Negative dollars not allowed')
        elif cents in range(0, 100):
            self.dollars, self.cents = dollars, cents
        else:
            self.cents = cents % 100
            self.dollars = dollars + math.floor(cents / 100)

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
        dollars = math.floor(diff)
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

    def as_float(self):
        return self.dollars + (self.cents / 100.0)

    def __eq__(self, other):
        return type(other) is Dollars and \
               self.currency == other.currency and \
               self.dollars == other.dollars and \
               self.cents == other.cents

    def __mul__(self, other):
        if type(other) is float:
            d = self.dollars * other
            d_over = math.floor((d - math.floor(d)) * 100)
            c = round(self.cents * other + d_over)
            return Dollars(round(d), c, self.currency)
        elif type(other) is int:
            return Dollars(
                self.dollars * other,
                self.cents * other,
                self.currency
            )
        else:
            raise TypeError('Cannot multiply by non-numerical type')

    def __lt__(self, other):
        if type(other) is not Dollars:
            raise TypeError()
        if self.currency != other.currency:
            raise CurrencyException()
        return self.dollars < other.dollars or \
               self.dollars == other.dollars and \
               self.cents < other.cents

    def __str__(self):
        return f"${self.dollars}.{self.cents}"
