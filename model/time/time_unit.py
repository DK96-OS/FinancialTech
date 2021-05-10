""" Time Units provide definition to time values """
from enum import IntEnum


class TimeUnit(IntEnum):
    """ Represents a unit of time """
    DAILY = 1
    WEEKLY = 7
    BI_WEEKLY = 14
    MONTHLY = 30
    QUARTERLY = 90
    ANNUALLY = 360


# Units can be converted accurately within these groups
TIME_GROUP_1 = [1, 7, 14]
TIME_GROUP_2 = [30, 90, 360]
