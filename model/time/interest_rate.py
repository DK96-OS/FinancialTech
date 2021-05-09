""" Interest Rate Calculations """
import math
import string

from model.data.dollars import Dollars
from model.time import convert_time, TimeConversionException
from model.time.time_unit import TimeUnit


class InterestRate:
    """ Represents an Interest Rate """

    def __init__(
            self, rate, rate_cycle: TimeUnit = TimeUnit.ANNUALLY,
    ):
        """ Create new Interest Rate
         :param rate Provide the interest rate as an int, float or string
            integer rates are assumed to be a percent, converted to decimal.
            float rates are assumed to be in decimal format.
            string rates must be in percent format, including the % sign.
         """
        if isinstance(rate, float): # Check and decode rate
            if not 0 < rate <= 1:
                raise ValueError('Rate must be a between 0 and 100%')
            self.rate = rate
        elif isinstance(rate, int):
            if not 0 < rate <= 100:
                raise ValueError('Rate must be between 0 and 100%')
            self.rate = round(float(rate) / 100, 3)
        elif isinstance(rate, str):
            if not rate.__contains__('%'):
                raise ValueError('Missing % in interest rate string')
            r_numerical = float(rate.strip('% '+string.ascii_letters))
            if r_numerical <= 0:
                raise ValueError('Interest rate must be positive')
            self.rate = round(r_numerical / 100, 3)
        else:
            raise TypeError('Interest rate must be int, float, or string')
        if not isinstance(rate_cycle, TimeUnit):
            raise TypeError('A TimeUnit is required')
        self.rate_cycle = rate_cycle

    def simple_interest(
            self, principal: Dollars,
            time: float, unit: TimeUnit,
    ) -> Dollars:
        """ Compute the interest during the given time """
        rate_time_product = math.fabs(self.rate * time)
        if self.rate_cycle == unit:
            return principal * rate_time_product
        try:
            time_convert_factor = convert_time(unit, self.rate_cycle)
            return principal * rate_time_product * time_convert_factor
        except TimeConversionException:
            print("Time Conversion Failed")
            raise ValueError('Provided time unit is incompatible')

    def __str__(self) -> str:
        num = round(self.rate * 100, 3) # Max 3 decimal points
        if num.is_integer():
            num = int(num)
        return str(num) + '% ' + str(self.rate_cycle.name).lower()
