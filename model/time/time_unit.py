from enum import IntEnum

from model.time.exceptions import TimeConversionException


class TimeUnit(IntEnum):
    DAILY = 1
    WEEKLY = 7
    BI_WEEKLY = 14
    MONTHLY = 30
    QUARTERLY = 90
    ANNUALLY = 360


# Units can be converted accurately within their group
time_group_1 = [1, 7, 14]
time_group_2 = [30, 90, 360]


def convert_time(from_t: TimeUnit, to_t: TimeUnit) -> float:
    """ Determines the conversion factor to use between given time units.
     Provides accurate conversion for:
        group 1: | daily <-> weekly <-> bi-weekly
        group 2: | monthly <-> annually <-> quarterly
     Inaccuracy is present between groups, due to variations in month length.
        In proper accounting, the specific time of the calendar year must be known.
     """
    if from_t in time_group_1 and to_t in time_group_1 or \
            from_t in time_group_2 and to_t in time_group_2:
        return from_t / to_t
    else:
        raise TimeConversionException()
