""" Dollar Data structure """
import math
from dataclasses import dataclass

from model.data.currencies import DEFAULT_CURRENCY, VERIFIED_CURRENCIES
from model.data import CurrencyException


@dataclass(frozen=True)
class Dollars:
    """ Represents an amount of money in dollars and cents.
        100 cents are in a dollar.
    """
    dollars: int
    cents: int = 0
    currency: str = DEFAULT_CURRENCY

    def __post_init__(self):
        # Validate currency
        if len(self.currency) != 3 or \
                self.currency not in VERIFIED_CURRENCIES:
            raise CurrencyException()
        # Validate dollar and cent values
        if not isinstance(self.dollars, int):
            raise TypeError('Dollars must be an integer')
        if not isinstance(self.cents, int):
            raise TypeError('Cents must be an integer')
        if self.dollars < 0 or self.cents < 0:
            raise ValueError('Negative dollars not allowed')
        if self.cents >= 100:
            # todo: support currencies with 1000 cents
            raise ValueError("Cents should be rounded into dollars")

    def __add__(self, other):
        """ Returns the Sum of two Dollar Amounts """
        self.check_compatible(other)
        dollars = self.dollars + other.dollars
        cents = self.cents + other.cents
        if cents >= 100:
            dollars += cents // 100     # Update Dollars first
            cents = cents % 100
        return Dollars(
            dollars=dollars,
            cents=cents,
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
            if other < 0:
                raise ValueError('Cannot multiply dollars by a negative')
            elif other == 0:
                return Dollars(0, 0, self.currency)
            d_raw = self.dollars * other
            d_overflow = math.floor((d_raw - math.floor(d_raw)) * 100)
            cents = round(self.cents * other + d_overflow)
            if cents >= 100:
                d_raw += cents // 100  # Update Dollars first
                cents = cents % 100
            return Dollars(
                round(d_raw), cents, self.currency
            )
        if isinstance(other, int):
            if other < 0:
                raise ValueError('Cannot multiply dollars by a negative')
            elif other == 0:
                return Dollars(0, 0, self.currency)
            d_raw = self.dollars * other
            cents = round(self.cents * other)
            if cents >= 100:
                d_raw += cents // 100  # Update Dollars first
                cents = cents % 100
            return Dollars(
                d_raw, cents, self.currency
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
