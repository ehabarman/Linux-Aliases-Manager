import unittest
import os
from tests.test_config import tests_data_dir
from manager.util.helpers.read_helpers import load_json_from_file


class TestReadHelpers(unittest.TestCase):
    data_path = tests_data_dir() + "util/helpers/test_read_helpers/"

    def test_load_json_from_file(self):
        files_names = ["valid", "invalid", "nonexistent"]
        have_exceptions = [False, True, True]
        msg_exceptions = [None,
                          "The file '{}' does not have a valid json format".format(
                              os.path.abspath(self.data_path + "invalid")),
                          "Couldn't find the file: {}/nonexistent".format(os.path.abspath(self.data_path))]
        for file_name, have_exception, msg_exception in zip(files_names, have_exceptions, msg_exceptions):
            try:
                load_json_from_file(file_name, self.data_path)
                self.assertFalse(have_exception)
            except Exception as err:
                self.assertEqual(msg_exception, str(err))
