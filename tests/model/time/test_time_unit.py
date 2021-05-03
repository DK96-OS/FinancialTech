import unittest

from model.time.exceptions import TimeConversionException
from model.time import time_unit
from model.time.time_unit import TimeUnit, convert_time


class TestTimeUnit(unittest.TestCase):
    """ Testing for TimeUnit Enum class, developed by DK96-OS 2021 """
    
    def test_accurate_conversions_group1(self):
        """ Test the conversion factors within group 1 """
        self.assertEqual(1/7, convert_time(TimeUnit.DAILY, TimeUnit.WEEKLY))
        self.assertEqual(1/14, convert_time(TimeUnit.DAILY, TimeUnit.BI_WEEKLY))
        #
        self.assertEqual(0.5, convert_time(TimeUnit.WEEKLY, TimeUnit.BI_WEEKLY))
        self.assertEqual(7, convert_time(TimeUnit.WEEKLY, TimeUnit.DAILY))
        #
        self.assertEqual(2, convert_time(TimeUnit.BI_WEEKLY, TimeUnit.WEEKLY))
        self.assertEqual(14, convert_time(TimeUnit.BI_WEEKLY, TimeUnit.DAILY))

    def test_accurate_conversions_group2(self):
        """ Test the conversion factors within group 2 """
        self.assertEqual(1/3, convert_time(TimeUnit.MONTHLY, TimeUnit.QUARTERLY))
        self.assertEqual(1/12, convert_time(TimeUnit.MONTHLY, TimeUnit.ANNUALLY))
        #
        self.assertEqual(3, convert_time(TimeUnit.QUARTERLY, TimeUnit.MONTHLY))
        self.assertEqual(1/4, convert_time(TimeUnit.QUARTERLY, TimeUnit.ANNUALLY))
        #
        self.assertEqual(12, convert_time(TimeUnit.ANNUALLY, TimeUnit.MONTHLY))
        self.assertEqual(4, convert_time(TimeUnit.ANNUALLY, TimeUnit.QUARTERLY))

    def test_non_conversion(self):
        """ Check that when both units are equal, the factor is 1 """
        # Group 1
        self.assertEqual(1, convert_time(TimeUnit.DAILY, TimeUnit.DAILY))
        self.assertEqual(1, convert_time(TimeUnit.WEEKLY, TimeUnit.WEEKLY))
        self.assertEqual(1, convert_time(TimeUnit.BI_WEEKLY, TimeUnit.BI_WEEKLY))
        # Group 2
        self.assertEqual(1, convert_time(TimeUnit.MONTHLY, TimeUnit.MONTHLY))
        self.assertEqual(1, convert_time(TimeUnit.QUARTERLY, TimeUnit.QUARTERLY))
        self.assertEqual(1, convert_time(TimeUnit.ANNUALLY, TimeUnit.ANNUALLY))

    def test_inaccurate_conversion(self):
        """ Any conversion between the two groups is inaccurate """
        for u0 in time_unit.time_group_1:
            for u1 in time_unit.time_group_2:
                with self.assertRaises(TimeConversionException):
                    convert_time(u0, u1)
