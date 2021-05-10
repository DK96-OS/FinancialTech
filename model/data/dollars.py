""" Dollar Data structure """
import math

from model.data.currencies import DEFAULT_CURRENCY, VERIFIED_CURRENCIES
from model.data import CurrencyException


class Dollars:
    """ Represents an amount of money in dollars and cents.
        100 cents are in a dollar.
    """

    def __init__(self,
                 dollars: int, cents: int = 0,
                 currency: str = DEFAULT_CURRENCY
                 ):
        # Validate currency
        cur = currency.upper()  # Ensure always uppercase
        if len(cur) == 3 and \
                cur in VERIFIED_CURRENCIES or cur.isalpha():
            self.currency = cur
        else:
            raise CurrencyException()
        # Validate dollar and cent values
        if not isinstance(dollars, int):
            raise TypeError('Dollars must be an integer')
        if not isinstance(cents, int):
            raise TypeError('Cents must be an integer')
        if dollars < 0 or cents < 0:
            raise ValueError('Negative dollars not allowed')
        if cents in range(0, 100):
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
        if not isinstance(other, Dollars):
            raise TypeError
        if self.currency != other.currency:
            raise CurrencyException('Currencies do not match')

    def as_float(self):
        """ Combine Dollars and Cents to a float value """
        return self.dollars + (self.cents / 100.0)

    def __eq__(self, other):
        """ Equals comparison """
        return isinstance(other, Dollars) and \
            self.currency == other.currency and \
            self.dollars == other.dollars and \
            self.cents == other.cents

    def __mul__(self, other):
        """ Multiplication operation """
        if isinstance(other, float):
            if other <= 0:
                raise ValueError('Cannot multiply dollars by a negative')
            d_raw = self.dollars * other
            d_overflow = math.floor((d_raw - math.floor(d_raw)) * 100)
            cents = round(self.cents * other + d_overflow)
            return Dollars(round(d_raw), cents, self.currency)
        if isinstance(other, int):
            if other <= 0:
                raise ValueError('Cannot multiply dollars by a negative')
            return Dollars(
                self.dollars * other,
                self.cents * other,
                self.currency
            )
        raise TypeError('Cannot multiply by non-numerical type')

    def __lt__(self, other):
        """ Less Than Comparison """
        if not isinstance(other, Dollars):
            raise TypeError('Cannot compare to other type')
        if self.currency != other.currency:
            raise CurrencyException('Currencies do not match')
        return self.dollars < other.dollars or \
            self.dollars == other.dollars and self.cents < other.cents

    def __str__(self):
        return f"${self.dollars}.{self.cents}"
