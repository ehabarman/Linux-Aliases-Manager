import unittest

from manager.util.helpers.print_helpers import *


class TestFilesHelpers(unittest.TestCase):

    def test_prepare_json(self):
        test_data = [
            {
                "key1": 1,
                "key2": 2,
                "key3": 3,
            },
            {
                "key1": 1,
                "key2": 2,
            },
            {
                "key3": 3,
                "key4": 4,
            },
        ]
        expected_data = [
            {
                "key1": 1,
                "key2": 2,
                "key3": 3,
            },
            {
                "key1": 1,
                "key2": 2,
                "key3": None,
            },
            {
                "key1": None,
                "key2": None,
                "key3": 3,
            },
        ]
        self.assertEqual(expected_data, prepare_json(test_data, "key1", "key2", "key3"))