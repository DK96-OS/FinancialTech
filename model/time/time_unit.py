from enum import Enum


class TimeUnit(Enum):
    DAILY = 1
    WEEKLY = 7
    BI_WEEKLY = 14
    MONTHLY = 30
    QUARTERLY = 90
    ANNUALLY = 365
