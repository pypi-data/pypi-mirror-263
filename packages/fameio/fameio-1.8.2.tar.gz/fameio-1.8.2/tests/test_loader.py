# SPDX-FileCopyrightText: 2023 German Aerospace Center <fame@dlr.de>
#
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

import pytest
from fameio.source.loader import PathResolver, load_yaml, check_for_yaml_file_type


class Test:
    def test_load_yaml_plain(self):
        expected = {"ToBe": "ThatIs", "OrNot": "TheQuestion"}
        loaded = load_yaml(Path("tests/yaml/simple.yaml"))
        assert expected == loaded

    def test_load_yaml_with_simple_include(self):
        expected = {"Is": {"ToBe": "ThatIs", "OrNot": "TheQuestion"}}
        loaded = load_yaml(Path("tests/yaml/simple_include.yaml"))
        assert expected == loaded

    def test_load_yaml_with_nested_include(self):
        expected = {
            "ToBe": {"ThatIs": {"Or": "maybe"}, "TheQuestion": {"not": "?"}},
            "OrNot": {"not": "?"},
        }
        loaded = load_yaml(Path("tests/yaml/a.yaml"))
        assert expected == loaded

    def test_with_custom_path_resolver(self):
        class CustomPathResolver(PathResolver):
            def __init__(self):
                super().__init__()
                self.last_file_pattern = ""

            def resolve_yaml_imported_file_pattern(self, root_path: str, file_pattern: str):
                self.last_file_pattern = file_pattern
                return super().resolve_yaml_imported_file_pattern(root_path, file_pattern)

        path_resolver = CustomPathResolver()
        load_yaml(Path("tests/yaml/simple_include.yaml"), path_resolver)
        assert path_resolver.last_file_pattern.endswith("simple.yaml")

    def test_with_failed_path_resolver(self):
        class BadPathResolver(PathResolver):
            def resolve_yaml_imported_file_pattern(self, root_path: str, file_pattern: str):
                return []

        with pytest.raises(Exception):
            load_yaml(Path("tests/yaml/simple_include.yaml"), BadPathResolver())

    @pytest.mark.parametrize("file_name", ["my/non_yaml/file.csv", "my/non_yaml/file", "file.", "file.xml"])
    def test_check_for_yaml_file_type_invalid(self, file_name):
        with pytest.raises(Exception):
            check_for_yaml_file_type(Path(file_name))

    @pytest.mark.parametrize("file_name", ["my/file.yml", "file.Yml", "my/file.yaml", "file.YAML", "file.yAmL"])
    def test_check_for_yaml_file_type_valid(self, file_name):
        check_for_yaml_file_type(Path(file_name))
