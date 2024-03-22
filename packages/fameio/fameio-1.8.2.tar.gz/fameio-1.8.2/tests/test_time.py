# SPDX-FileCopyrightText: 2023 German Aerospace Center <fame@dlr.de>
#
# SPDX-License-Identifier: Apache-2.0

import time

import pytest
from mockito import when, ANY

from fameio.source.time import Constants, ConversionException, FameTime, TimeUnit, DATE_FORMAT

from tests.utils import assert_exception_contains


class Test:
    STEPS_PER_SECOND = Constants.STEPS_PER_SECOND

    @staticmethod
    def assert_datetime_matches_steps(datetime: str, expected_steps: int) -> None:
        """Asserts that the given datetime converted to FAME time steps matches the expected value"""
        assert expected_steps == FameTime.convert_datetime_to_fame_time_step(datetime)

    def test_convert_datetime_to_fame_time_step(self):
        # 1 second
        expected_value = self.STEPS_PER_SECOND
        self.assert_datetime_matches_steps("2000-01-01_00:00:01", expected_value)

        # 1 minute
        expected_value = self.STEPS_PER_SECOND * 60
        self.assert_datetime_matches_steps("2000-01-01_00:01:00", expected_value)

        # 1 hour
        expected_value = self.STEPS_PER_SECOND * 60 * 60
        self.assert_datetime_matches_steps("2000-01-01_01:00:00", expected_value)

        # 1 day
        expected_value = self.STEPS_PER_SECOND * 60 * 60 * 24
        self.assert_datetime_matches_steps("2000-01-02_00:00:00", expected_value)

        # 1 year
        expected_value = self.STEPS_PER_SECOND * 60 * 60 * 24 * 365
        self.assert_datetime_matches_steps("2001-01-01_00:00:00", expected_value)

        # Mixed
        self.assert_datetime_matches_steps("2001-01-06_02:12:17", 31975937 * self.STEPS_PER_SECOND)

    def test_convert_datetime_to_fame_time_step_invalid_format(self):
        with pytest.raises(ConversionException) as e_info:
            FameTime.convert_datetime_to_fame_time_step("This is Sparta - but not a time stamp string")
        assert_exception_contains(FameTime._FORMAT_INVALID, e_info)

    def test_convert_datetime_to_fame_time_step_invalid_timestamp(self):
        with pytest.raises(ConversionException) as e_info:
            FameTime.convert_datetime_to_fame_time_step("2001-01-35_27:77:88")
        assert_exception_contains(FameTime._INVALID_TIMESTAMP, e_info)

    def test_convert_datetime_to_fame_time_step_to_large(self):
        with pytest.raises(ConversionException) as e_info:
            FameTime.convert_datetime_to_fame_time_step("2004-12-31_15:15:15")
        assert_exception_contains(FameTime._INVALID_TOO_LARGE, e_info)

    @pytest.mark.parametrize(
        "expected, steps, date_format",
        [
            ("2000-01-01_00:00:01", 1 * STEPS_PER_SECOND, DATE_FORMAT),
            ("2000-01-01_00:01:00", 60 * STEPS_PER_SECOND, DATE_FORMAT),
            ("2000-01-01_01:00:00", 3600 * STEPS_PER_SECOND, DATE_FORMAT),
            ("2000-01-02_00:00:00", 86400 * STEPS_PER_SECOND, DATE_FORMAT),
            ("2001-01-01_00:00:00", 31536000 * STEPS_PER_SECOND, DATE_FORMAT),
            ("2001-01-06_02:12:17", 31975937 * STEPS_PER_SECOND, DATE_FORMAT),
            ("2000-01-01 00:00:01", 1 * STEPS_PER_SECOND, "%Y-%m-%d %H:%M:%S"),
            ("2000-01-01 00:01", 61 * STEPS_PER_SECOND, "%Y-%m-%d %H:%M"),
            ("2000-01-01", 3600 * STEPS_PER_SECOND, "%Y-%m-%d"),
        ],
    )
    def test_convert_fame_time_step_to_datetime(self, expected: str, steps: int, date_format: str):
        assert expected == FameTime.convert_fame_time_step_to_datetime(steps, date_format)

    def test_convert_fame_time_step_to_datetime_catch_strftime_error(self):
        with pytest.raises(ConversionException) as e_info:
            with when(time).strftime(ANY, ANY).thenRaise(ValueError):
                FameTime.convert_fame_time_step_to_datetime(86400, "abc")
        assert_exception_contains(FameTime._INVALID_DATE_FORMAT, e_info)

    def test_convert_time_span_to_fame_time_steps(self):
        for unit in TimeUnit:
            assert FameTime.convert_time_span_to_fame_time_steps(19, unit) == 19 * Constants.steps_per_unit[unit]

    def test_convert_time_span_to_fame_time_steps_invalid_unit(self):
        with pytest.raises(Exception) as e_info:
            # noinspection PyTypeChecker
            FameTime.convert_time_span_to_fame_time_steps(1, "Not a time unit")
        assert_exception_contains(FameTime._TIME_UNIT_UNKNOWN, e_info)

    def test_is_datetime(self):
        assert FameTime.is_datetime("2020-04-03_10:11:12") is True
        assert FameTime.is_datetime(" 2020-04-03_10:11:12 ") is True
        assert FameTime.is_datetime(" 2020-04-03_10:11:12") is True
        # noinspection PyTypeChecker
        assert FameTime.is_datetime(13) is False
        assert FameTime.is_datetime("other String") is False
        assert FameTime.is_datetime("2020-04-03_10:11") is False
        assert FameTime.is_datetime("2020-04-03_10:11:234") is False
        assert FameTime.is_datetime("20-04-03_10:11:234") is False
        assert FameTime.is_datetime("2020-4-03_10:11:234") is False
        assert FameTime.is_datetime("2020-04-3_10:11:234") is False

    def test_convert_string_if_is_datetime_is_datetime(self):
        steps = 55
        assert steps == FameTime.convert_string_if_is_datetime(FameTime.convert_fame_time_step_to_datetime(steps))

    def test_convert_string_if_is_datetime_is_integer(self):
        steps = 55
        assert steps == FameTime.convert_string_if_is_datetime(steps)

    def test_convert_string_if_is_datetime_is_other(self):
        with pytest.raises(ConversionException) as e_info:
            FameTime.convert_string_if_is_datetime("Not a valid date time")
        assert_exception_contains(FameTime._NO_TIMESTAMP, e_info)

    def test_convert_string_if_is_datetime_is_string_of_int(self):
        steps = "55"
        assert 55 == FameTime.convert_string_if_is_datetime(steps)

    def test_is_fame_time_compatible(self):
        assert FameTime.is_fame_time_compatible(23)
        assert FameTime.is_fame_time_compatible("42")
        assert FameTime.is_fame_time_compatible(FameTime.convert_fame_time_step_to_datetime(99))
        # noinspection PyTypeChecker
        assert not FameTime.is_fame_time_compatible(4.2)
        # noinspection PyTypeChecker
        assert not FameTime.is_fame_time_compatible({"42": 99})
        # noinspection PyTypeChecker
        assert not FameTime.is_fame_time_compatible([21, 23, 25])
