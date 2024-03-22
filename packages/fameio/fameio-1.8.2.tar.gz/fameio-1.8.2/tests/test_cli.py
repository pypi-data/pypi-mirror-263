# SPDX-FileCopyrightText: 2023 German Aerospace Center <fame@dlr.de>
#
# SPDX-License-Identifier: Apache-2.0
import argparse
from pathlib import Path
from typing import List

import pytest

from fameio.source.cli import (
    update_default_config,
    non_negative_int,
    ERR_NEGATIVE_INT,
    add_file_argument,
    add_select_agents_argument,
    add_logfile_argument,
    add_output_argument,
    add_log_level_argument,
    add_single_export_argument,
    add_memory_saving_argument,
    add_resolve_complex_argument,
    ResolveOptions,
    add_time_argument,
    TimeOptions,
    add_focal_point_argument,
    add_steps_before_argument,
    add_steps_after_argument,
    add_merge_time_parser,
    get_merging_args,
    MergingOptions,
)
from tests.utils import assert_exception_contains


class TestParser:
    @pytest.fixture
    def parser(self):
        return argparse.ArgumentParser()

    def test_add_file_argument_exit_on_missing_argument(self, parser):
        add_file_argument(parser, "")
        with pytest.raises(SystemExit):
            parser.parse_args([])

    def test_add_file_argument_exit_on_missing_value(self, parser):
        add_file_argument(parser, "")
        with pytest.raises(SystemExit):
            parser.parse_args(["-f"])

    @pytest.mark.parametrize("value", ["a", "file.x", "path/to/file", "./rel/path.x", "/abs/path/file.b"])
    def test_add_file_argument_creates_path_for_any_value(self, parser, value: str):
        add_file_argument(parser, "")
        result = parser.parse_args(["-f", value])
        assert result.file == Path(value)

    def test_add_select_agents_argument_missing_argument_yields_none(self, parser):
        add_select_agents_argument(parser)
        result = parser.parse_args([])
        assert result.agents is None

    def test_add_select_agents_value_missing_yields_empty_list(self, parser):
        add_select_agents_argument(parser)
        result = parser.parse_args(["-a"])
        assert result.agents == []

    @pytest.mark.parametrize("values", [["a"], ["x", "b"], ["some", "names", "of", "agents"]])
    def test_add_select_agents_values_added_to_list(self, parser, values: List[str]):
        add_select_agents_argument(parser)
        args = ["-a", *values]
        result = parser.parse_args(args)
        assert len(result.agents) == len(values)
        assert set(result.agents).issubset(values)

    def test_add_logfile_argument_missing_yields_none(self, parser):
        add_logfile_argument(parser)
        result = parser.parse_args([])
        assert result.logfile is None

    def test_add_logfile_argument_value_missing_raises(self, parser):
        add_logfile_argument(parser)
        with pytest.raises(SystemExit):
            parser.parse_args(["-lf"])

    @pytest.mark.parametrize("value", ["a", "file.x", "path/to/file", "./rel/path.x", "/abs/path/file.b"])
    def test_add_logfile_argument_creates_path_from_any_value(self, parser, value):
        add_logfile_argument(parser)
        result = parser.parse_args(["-lf", value])
        assert result.logfile == Path(value)

    @pytest.mark.parametrize("default", ["some", "/path/to/a", "./default/output.file"])
    def test_add_output_argument_missing_yields_default(self, parser, default):
        add_output_argument(parser, default, "")
        result = parser.parse_args([])
        assert result.output == Path(default)

    def test_add_output_argument_missing_value_raises(self, parser):
        add_output_argument(parser, "default", "")
        with pytest.raises(SystemExit):
            parser.parse_args(["-o"])

    @pytest.mark.parametrize("value", ["a", "file.x", "path/to/file", "./rel/path.x", "/abs/path/file.b"])
    def test_add_output_argument_value_overrides_default(self, parser, value):
        add_output_argument(parser, "default", "")
        result = parser.parse_args(["-o", value])
        assert result.output == Path(value)

    @pytest.mark.parametrize("default", ["ERROR", "DEBUG", "INFO"])
    def test_add_log_level_argument_missing_argument_yields_default(self, parser, default):
        add_log_level_argument(parser, default)
        result = parser.parse_args([])
        assert result.log == default.lower()

    def test_add_log_level_argument_missing_value_raises(self, parser):
        add_log_level_argument(parser, "ERROR")
        with pytest.raises(SystemExit):
            parser.parse_args(["-l"])

    def test_add_log_level_argument_unknown_level_raises(self, parser):
        add_log_level_argument(parser, "ERROR")
        with pytest.raises(SystemExit):
            parser.parse_args(["-l", "'not-an-error-level'"])

    @pytest.mark.parametrize("value", ["error", "ERROR", "eRRoR", "Critical", "WARN", "inFo", "dEbUg"])
    def test_add_log_level_argument_overrides_default_with_valid_value(self, parser, value):
        add_log_level_argument(parser, "warning")
        result = parser.parse_args(["-l", value])
        assert result.log == value.lower()

    @pytest.mark.parametrize("default", [True, False])
    def test_add_single_export_argument_missing_yields_default(self, parser, default):
        add_single_export_argument(parser, default)
        result = parser.parse_args([])
        assert result.single_export == default

    def test_add_single_export_argument_present_yields_true(self, parser):
        add_single_export_argument(parser, False)
        result = parser.parse_args(["-se"])
        assert result.single_export

    @pytest.mark.parametrize("default", [True, False])
    def test_add_memory_saving_argument_missing_yields_default(self, parser, default):
        add_memory_saving_argument(parser, default)
        result = parser.parse_args([])
        assert result.memory_saving == default

    def test_add_memory_saving_argument_present_yields_true(self, parser):
        add_memory_saving_argument(parser, False)
        result = parser.parse_args(["-m"])
        assert result.memory_saving

    @pytest.mark.parametrize("default", [e.name for e in ResolveOptions])
    def test_add_resolve_complex_argument_missing_yields_default(self, parser, default: str):
        add_resolve_complex_argument(parser, default)
        result = parser.parse_args([])
        assert result.complex_column == default.upper()

    def test_add_resolve_complex_argument_missing_value_raises(self, parser):
        add_resolve_complex_argument(parser, ResolveOptions.IGNORE.name)
        with pytest.raises(SystemExit):
            parser.parse_args(["-cc"])

    def test_add_resolve_complex_argument_invalid_value_raises(self, parser):
        add_resolve_complex_argument(parser, ResolveOptions.IGNORE.name)
        with pytest.raises(SystemExit):
            parser.parse_args(["-cc", "not_a_valid_value"])

    @pytest.mark.parametrize("value", [e.name for e in ResolveOptions])
    def test_add_resolve_complex_argument_override_default_on_valid_values(self, parser, value: str):
        add_resolve_complex_argument(parser, ResolveOptions.IGNORE.name)
        result = parser.parse_args(["-cc", value])
        assert result.complex_column == value.upper()

    @pytest.mark.parametrize("default", [e.name for e in TimeOptions])
    def test_add_time_argument_missing_yields_default(self, parser, default):
        add_time_argument(parser, default)
        result = parser.parse_args([])
        assert result.time == default.upper()

    def test_add_time_argument_missing_value_raises(self, parser):
        add_time_argument(parser, TimeOptions.INT.name)
        with pytest.raises(SystemExit):
            parser.parse_args(["-t"])

    def test_add_time_argument_invalid_value_raises(self, parser):
        add_time_argument(parser, TimeOptions.INT.name)
        with pytest.raises(SystemExit):
            parser.parse_args(["-t", "not_a_valid_value"])

    @pytest.mark.parametrize("value", [e.name for e in TimeOptions])
    def test_add_time_argument_valid_value_overrides_default(self, parser, value: str):
        add_time_argument(parser, TimeOptions.INT.name)
        result = parser.parse_args(["-t", value])
        assert result.time == value.upper()

    def test_add_focal_point_argument_missing_raises(self, parser):
        add_focal_point_argument(parser)
        with pytest.raises(SystemExit):
            parser.parse_args([])

    def test_add_focal_point_argument_value_missing_raises(self, parser):
        add_focal_point_argument(parser)
        with pytest.raises(SystemExit):
            parser.parse_args(["-fp"])

    @pytest.mark.parametrize("value", ["", "not_an_int", "(5,8)", "[88]"])
    def test_add_focal_point_argument_non_int_raises(self, parser, value: str):
        add_focal_point_argument(parser)
        with pytest.raises(SystemExit):
            parser.parse_args(["-fp", value])

    @pytest.mark.parametrize("value", ["-10", "0", "1", "10000"])
    def test_add_focal_point_argument_valid_values(self, parser, value: str):
        add_focal_point_argument(parser)
        result = parser.parse_args(["-fp", value])
        assert result.focal_point == int(value)

    def test_add_steps_before_argument_missing_raises(self, parser):
        add_steps_before_argument(parser)
        with pytest.raises(SystemExit):
            parser.parse_args([])

    def test_add_steps_before_argument_missing_value_raises(self, parser):
        add_steps_before_argument(parser)
        with pytest.raises(SystemExit):
            parser.parse_args(["-sb"])

    @pytest.mark.parametrize("value", ["", "not_an_int", "(5)", "[8]", "-2"])
    def test_add_steps_before_argument_invalid_value_raises(self, parser, value):
        add_steps_before_argument(parser)
        with pytest.raises(SystemExit):
            parser.parse_args(["-sb", value])

    @pytest.mark.parametrize("value", ["0", "1", "15", "12123123"])
    def test_add_steps_before_argument_valid_values(self, parser, value):
        add_steps_before_argument(parser)
        result = parser.parse_args(["-sb", value])
        assert result.steps_before == int(value)

    def test_add_steps_after_argument_missing_raises(self, parser):
        add_steps_after_argument(parser)
        with pytest.raises(SystemExit):
            parser.parse_args([])

    def test_add_steps_after_argument_missing_value_raises(self, parser):
        add_steps_after_argument(parser)
        with pytest.raises(SystemExit):
            parser.parse_args(["-sa"])

    @pytest.mark.parametrize("value", ["", "not_an_int", "(5)", "[8]", "-2"])
    def test_add_steps_after_argument_invalid_values_raise(self, parser, value: str):
        add_steps_after_argument(parser)
        with pytest.raises(SystemExit):
            parser.parse_args(["-sa", value])

    @pytest.mark.parametrize("value", ["0", "1", "15", "12123123"])
    def test_add_steps_after_argument_valid_values(self, parser, value: str):
        add_steps_after_argument(parser)
        result = parser.parse_args(["-sa", value])
        assert result.steps_after == int(value)

    @pytest.mark.parametrize("args", [["-sa", "0", "-sb", "0"], ["-fp", "0", "-sb", "0"], ["-fp", "0", "-sa", "0"]])
    def test_add_merge_time_parser_argument_missing_raises(self, parser, args):
        add_merge_time_parser(parser)
        with pytest.raises(SystemExit):
            parser.parse_args(["merge-times", *args])

    def test_get_merging_args_missing_key_returns_empty_dict(self):
        assert get_merging_args(argparse.Namespace()) == {}

    def test_get_merging_args_no_merge_times(self):
        args = argparse.Namespace(**{"time_merging": None})
        assert get_merging_args(args) == {}

    @pytest.mark.parametrize("args", [["-fp", "-1", "-sb", "0", "-sa", "20"], ["-fp", "5", "-sb", "10", "-sa", "5"]])
    def test_add_merge_time_parser_and_get_merging_args(self, parser, args):
        add_merge_time_parser(parser)
        parsed = parser.parse_args(["merge-times", *args])
        result = get_merging_args(parsed)
        assert result[MergingOptions.FOCAL_POINT] == int(args[1])
        assert result[MergingOptions.STEPS_BEFORE] == int(args[3])
        assert result[MergingOptions.STEPS_AFTER] == int(args[5])


class TestHelpers:
    _default = {"a": 1, "b": 2, "c": 3}

    def test_get_config_or_default_update_a(self):
        config = {"a": 42}
        expected = {"a": 42, "b": 2, "c": 3}
        assert update_default_config(config, self._default) == expected

    def test_get_config_or_default_update_abc(self):
        config = {"a": 42, "b": 42, "c": 42}
        expected = {"a": 42, "b": 42, "c": 42}
        assert update_default_config(config, self._default) == expected

    def test_get_config_or_default_update_abcd(self):
        config = {"d": 42}
        expected = {"a": 1, "b": 2, "c": 3, "d": 42}
        assert update_default_config(config, self._default) == expected

    def test_get_config_or_default_none(self):
        config = None
        expected = {"a": 1, "b": 2, "c": 3}
        assert update_default_config(config, self._default) == expected

    def test_non_negative_int_positive(self):
        assert non_negative_int(1) == 1

    def test_non_negative_int_zero(self):
        assert non_negative_int(0) == 0

    def test_non_negative_int_err_on_negative_arg(self):
        with pytest.raises(argparse.ArgumentTypeError) as e_info:
            non_negative_int(-1)
        assert_exception_contains(ERR_NEGATIVE_INT, e_info)

    def test_non_negative_int_err_on_none(self):
        with pytest.raises(TypeError):
            non_negative_int(None)

    def test_non_negative_int_err_on_string(self):
        with pytest.raises(ValueError):
            non_negative_int("Test")
