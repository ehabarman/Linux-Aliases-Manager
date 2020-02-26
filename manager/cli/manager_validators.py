import argparse
import os

from util.constants import DESTINATION_ARG, SOURCE_ARG
from util.helpers.files_helper import path_exists, separate_file_from_path


class ValidatePath(argparse.Action):
    """needed for import and export operations"""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        """Ensures only export and import operation using this action"""
        if nargs is not None:
            raise ValueError("nargs not allowed")
        if not (dest == DESTINATION_ARG or dest == SOURCE_ARG):
            raise ValueError("Used only by destination and source arguments")
        self.operation = dest
        super(ValidatePath, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, value, option_string=None):
        """Check path validity and reformat it if possible"""
        print(self.dest)
        # Make relative path
        if value.startswith("/") is False:
            current_directory = os.getcwdb().decode('UTF-8')
            if value.startswith("./") is True:
                value = "{}/{}".format(current_directory, value[2:])
            else:
                value = "{}/{}".format(current_directory, value)

        path, file = separate_file_from_path(value)
        valid_path = path_exists(path)

        if self.operation == SOURCE_ARG:
            if file == "":
                raise argparse.ArgumentError(None, "Source must be a file")
            valid_path = valid_path and path_exists(path+file)
        if not valid_path:
            raise argparse.ArgumentError(None, f"The {self.dest} does not exist: {value}")

        setattr(namespace, self.dest, valid_path)
