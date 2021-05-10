""" Time Operations and Management """
import datetime

from model.time.time_unit import TimeUnit, TIME_GROUP_1, TIME_GROUP_2


def net_days(start: datetime.date, days: int):
    """ Find a future due date """
    return start + datetime.timedelta(days=days)


class TimeConversionException(Exception):
    """ There are incompatible Time Units being compared """


def check_time_conversion(from_t: TimeUnit, to_t: TimeUnit):
    """ Checks that a time unit can be accurately converted
        Provides accurate conversion for:
            group 1: | daily <-> weekly <-> bi-weekly
            group 2: | monthly <-> annually <-> quarterly
    """
    return from_t in TIME_GROUP_1 and to_t in TIME_GROUP_1 or \
        from_t in TIME_GROUP_2 and to_t in TIME_GROUP_2


def convert_time(from_t: TimeUnit, to_t: TimeUnit) -> float:
    """ Determines the conversion factor to use between given time units. """
    if check_time_conversion(from_t, to_t):
        return from_t / to_t
    raise TimeConversionException(
        'Incompatible time units: '+str(from_t)+' and '+str(to_t))
