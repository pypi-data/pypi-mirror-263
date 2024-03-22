# SPDX-FileCopyrightText: 2023 German Aerospace Center <fame@dlr.de>
#
# SPDX-License-Identifier: Apache-2.0

from fameio.source.tools import ensure_is_list, keys_to_lower


class Test:
    def test_convert_keys_to_lower(self):
        input_dict = {"all_lower_int": 5, "ALL_UPPER_DICT": {}, "MiXedCaPS_LiSt": []}
        result = keys_to_lower(input_dict)
        assert result["all_lower_int"] == 5
        assert result["all_upper_dict"] == {}
        assert result["mixedcaps_list"] == []  # noqa

    def test_ensure_is_list_no_list(self):
        assert ensure_is_list(5) == [5]
        assert ensure_is_list("Ninety") == ["Ninety"]
        assert ensure_is_list({"A": 5}) == [{"A": 5}]
        assert ensure_is_list(5.8) == [5.8]

    @staticmethod
    def _assert_input_is_returned(input_list: list) -> None:
        """Asserts that given list is returned by ensure_is_list"""
        assert input_list == ensure_is_list(input_list)

    def test_ensure_is_list_is_list(self):
        Test._assert_input_is_returned([5, 7])
        Test._assert_input_is_returned(["5", "6"])
        Test._assert_input_is_returned([{21: 42, "a": "b"}])
        Test._assert_input_is_returned([5.6, 7.8])
