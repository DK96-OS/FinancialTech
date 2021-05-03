from model.data.dollars import Dollars
from model.time.time_unit import TimeUnit


class SimpleInterestRate:
    """ Represents a Simple Interest Rate """
    def __init__(self,
                 rate: float,
                 time_unit: TimeUnit,
                 ):
        # todo: Error check
        self.rate = rate
        self.time_unit = time_unit

    def calculate_interest(self,
                           principal: Dollars,
                           time: float,
                           unit: TimeUnit,
                           ) -> Dollars:
        """ Compute the interest gained """
        if self.time_unit == unit:
            d = principal.dollars * self.rate
            c = principal.cents * self.rate
            return Dollars(d, c)
        else:
            # todo: Convert Time Units
            raise Exception('Incompatible time units')
