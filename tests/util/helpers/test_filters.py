import unittest

from tests.test_config import tests_data_dir
from manager.util.helpers.filters import remove_non_valid_aliases, handle_conflict, delete_an_element_handler, \
    change_name_handler
from manager.util.helpers.read_helpers import load_json_from_file


class TestFiltersHelpers(unittest.TestCase):
    data_path = tests_data_dir() + "util/helpers/test_filters/"

    def test_remove_non_valid_aliases(self):
        raw_data = load_json_from_file("remove_non_valid_aliases/raw_data.json", self.data_path)
        expected_data = load_json_from_file("remove_non_valid_aliases/expected.json", self.data_path)
        actual_result = remove_non_valid_aliases(raw_data)
        self.assertEqual(expected_data, actual_result)

    def test_handle_conflict(self):
        raw_data = load_json_from_file("handle_conflict/raw_data.json", self.data_path)
        expected_delete_handler = load_json_from_file("handle_conflict/delete_handler.json", self.data_path)
        expected_change_name_handler = load_json_from_file("handle_conflict/change_name.json", self.data_path)
        actual_delete_handler = handle_conflict(raw_data, delete_an_element_handler)
        actual_change_name_handler = handle_conflict(raw_data, change_name_handler)
        self.assertEqual(expected_change_name_handler, actual_change_name_handler)
        self.assertEqual(expected_delete_handler, actual_delete_handler)

