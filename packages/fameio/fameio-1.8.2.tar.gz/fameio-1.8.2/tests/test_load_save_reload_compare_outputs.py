# SPDX-FileCopyrightText: 2023 German Aerospace Center <fame@dlr.de>
#
# SPDX-License-Identifier: Apache-2.0

import os
import shutil
from pathlib import Path
from typing import Optional

import pytest
import yaml
from fameprotobuf import DataStorage_pb2
from google.protobuf import text_format

from fameio.source.loader import load_yaml
from fameio.source.path_resolver import PathResolver
from fameio.source.scenario import Scenario
from fameio.source.validator import SchemaValidator
from fameio.source.writer import ProtoWriter


class CustomPathResolver(PathResolver):
    def __init__(self, root_dir: str):
        super().__init__()
        self._root_dir = root_dir

    def resolve_series_file_path(self, file_name: str) -> Optional[str]:
        if not os.path.isabs(file_name):
            file_path = os.path.join(self._root_dir, file_name)
            if os.path.exists(file_path):
                return file_path
        return super().resolve_series_file_path(file_name)


def _load_and_validate_yaml_file(file_path: str, path_resolver: PathResolver) -> Scenario:
    """Returns validated scenario parsed in `file_path`"""
    scenario = Scenario.from_dict(load_yaml(Path(file_path), path_resolver))
    SchemaValidator.ensure_is_valid_scenario(scenario)
    return scenario


def _write_protobuf_file(scenario: Scenario, path_resolver: PathResolver, output_file_name: str) -> None:
    """Writes `scenario` using `path_resolver` as given `output_file_name`"""
    writer = ProtoWriter(Path(output_file_name), path_resolver)
    writer.write_validated_scenario(scenario)


def _convert_protobuf_to_text(file_path: Path) -> str:
    """Returns protobuf file in `file_path` as str"""
    file_path = str(file_path)
    msg = DataStorage_pb2.DataStorage()
    with open(file_path, "rb") as file:
        protobuf_data = file.read()
        msg.ParseFromString(protobuf_data)
    text = text_format.MessageToString(msg)
    return text


class TestLoadSaveReload:
    scenario_name = "scenario.yaml"
    protobuf_name = "scenario.pb"
    scenario_copy_name = "scenario_copy.yaml"
    protobuf_copy_name = "scenario_copy.pb"
    path_to_examples = "../examples/Germany2019"

    @pytest.fixture(scope="session")
    def _cache_dir(self, tmp_path_factory):
        """Creates temporary directory where files for all tests in this Class are written to"""
        return tmp_path_factory.mktemp("cache")

    def test_load_dump_reload_compare(self, _cache_dir):
        work_dir = self._setup_workdir_with_protobuf_from_original_and_reloaded_scenario(_cache_dir)
        ref_text = _convert_protobuf_to_text(work_dir / self.protobuf_name)
        copy_text = _convert_protobuf_to_text(work_dir / self.protobuf_copy_name)

        # we can't convert the protobuf text directly because the order of the field can vary,
        # so we do something simple here: sort the output text lines and check they are similar
        ref_lines = ref_text.splitlines()
        copy_lines = copy_text.splitlines()
        ref_lines.sort()
        copy_lines.sort()
        # compare line by line to help spot the difference on a large output
        for i, line_ref in enumerate(ref_lines):
            assert i < len(copy_lines)
            line_copy = copy_lines[i]
            # the generated series id are likely to be different, so we ignore them
            if "seriesId:" in line_ref:
                assert "seriesId:" in line_copy
            else:
                assert line_ref == line_copy
        # ensure the copy has no extra lines
        assert len(ref_lines) == len(copy_lines)

    def _setup_workdir_with_protobuf_from_original_and_reloaded_scenario(self, cache_dir) -> Path:
        this_script_dir = os.path.dirname(os.path.realpath(__file__))
        example_dir = os.path.join(this_script_dir, self.path_to_examples)
        work_dir = shutil.copytree(example_dir, cache_dir / "examples/Germany2019")
        path_resolver = CustomPathResolver(work_dir)

        original_scenario = _load_and_validate_yaml_file(work_dir / self.scenario_name, path_resolver)
        _write_protobuf_file(original_scenario, path_resolver, work_dir / self.protobuf_name)

        with open(work_dir / self.scenario_copy_name, "w") as f:
            yaml.dump(original_scenario.to_dict(), f)
        copied_scenario = _load_and_validate_yaml_file(work_dir / self.scenario_copy_name, path_resolver)
        _write_protobuf_file(copied_scenario, path_resolver, work_dir / self.protobuf_copy_name)
        return work_dir
