
class CurrencyException(Exception):
    """ Exception for Currency comparison errors """
    pass


class NegativeDollarException(Exception):
    """ Dollar operation or input caused negative value """
    pass
