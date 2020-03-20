import unittest

from tests.test_config import tests_data_dir
from manager.util.helpers.files_helpers import *


class TestFilesHelpers(unittest.TestCase):
    data_path = tests_data_dir() + "util/helpers/test_files_helpers/"

    def test_path_exists(self):
        self.assertTrue(path_exists(self.data_path + "test_file_exists"))
        self.assertFalse(path_exists(self.data_path + "test_file_exists2"))

    def test_remove_file(self):
        file_name = "test_remove_file"
        file_path = self.data_path + file_name
        if path_exists(file_path) is False:
            open(file_path, 'a').close()
        remove_file(file_path)
        self.assertFalse(path_exists(file_path), "The file '{}' should have been removed".format(file_name))

    def test_join_file_and_path(self):
        files_names = ["test1", "test2", "", "", ""]
        paths = ["/path1", "/path2/", "/path3", "/path4/"]
        expected_results = ["/path1/test1", "/path2/test2", "/path3/", "/path4/"]
        for file_name, path, expected_result in zip(files_names, paths, expected_results):
            self.assertEqual(expected_result, join_file_and_path(file_name, path))

    def test_get_files_in_path(self):
        path = self.data_path + "test_get_files_in_path"
        files = get_files_in_path(path)
        self.assertEqual(len(files), 3)
        for index in range(1, 4):
            self.assertTrue("file{}".format(index) in files)

    def test_separate_file_from_path(self):
        test_cases = ["/test1", "/test2/", "/test3/test4", "test5", ""]
        expected_paths = ["/", "/test2/", "/test3/", "", ""]
        expected_files = ["test1", "", "test4", "test5", ""]
        for case, expected_path, expected_file in zip(test_cases, expected_paths, expected_files):
            path, file = separate_file_from_path(case)
            self.assertEqual(expected_path, path)
            self.assertEqual(expected_file, file)

    def test_is_file(self):
        file_path = self.data_path + "test_is_file"
        directory_path = self.data_path + "test_is_directory"
        self.assertTrue(is_file(file_path))
        self.assertFalse(is_file(directory_path))

    def test_is_directory(self):
        file_path = self.data_path + "test_is_file"
        directory_path = self.data_path + "test_is_directory"
        self.assertFalse(is_directory(file_path))
        self.assertTrue(is_directory(directory_path))
