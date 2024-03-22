# SPDX-FileCopyrightText: 2023 German Aerospace Center <fame@dlr.de>
#
# SPDX-License-Identifier: Apache-2.0

from fameio.source.series import TimeSeriesManager


class TestTimeSeriesManager:
    def test_save_get_time_series_id_same_file_same_id(self):
        manager = TimeSeriesManager()
        id1 = manager.save_get_time_series_id("FILE_NAME")
        id2 = manager.save_get_time_series_id("FILE_NAME")
        assert id1 == id2

    def test_save_get_time_series_id_different_files_different_id(self):
        manager = TimeSeriesManager()
        id1 = manager.save_get_time_series_id("FILE_NAME")
        id2 = manager.save_get_time_series_id("OTHER_FILE")
        assert id1 != id2

    def test_get_ids_of_series_by_name(self):
        manager = TimeSeriesManager()
        id1 = manager.save_get_time_series_id("FILE_NAME")
        id2 = manager.save_get_time_series_id("OTHER_FILE")
        ids_by_name = manager.get_ids_of_series_by_name()
        assert ids_by_name["FILE_NAME"] == id1
        assert ids_by_name["OTHER_FILE"] == id2
