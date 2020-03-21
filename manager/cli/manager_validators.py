import argparse
import os

from util.constants import DESTINATION_ARG, SOURCE_ARG, PATHS_GROUP, STDOUT_ARG
from util.helpers.files_helpers import path_exists, separate_file_from_path, is_file, is_directory


class ValidatePath(argparse.Action):
    """
    needed for import and export operations
    """

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        """
        Ensures only export and import operation using this action
        """
        if nargs is not None:
            raise ValueError("nargs not allowed")
        if dest not in PATHS_GROUP:
            raise ValueError("Used only by {} arguments".format(PATHS_GROUP))
        self.operation = dest
        super(ValidatePath, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, value, option_string=None):
        """
        Check path validity and reformat it if possible
        """

        if not value:
            raise argparse.ArgumentError(None, f"You need to pass non-empty value to {self.dest}")

        # Make relative path
        if value.startswith("/") is False:
            current_directory = os.getcwdb().decode('UTF-8')
            if value.startswith("./") is True:
                value = "{}/{}".format(current_directory, value[2:])
            elif value.startswith("~/") is True:
                home = os.environ["HOME"]
                value = "{}/{}".format(home, value[2:])
            else:
                value = "{}/{}".format(current_directory, value)

        valid_path = path_exists(value)

        if not valid_path:
            if self.operation == STDOUT_ARG:
                path, file = separate_file_from_path(value)
                if not file:
                    raise argparse.ArgumentError(None, f"You need to give a valid path and the file name")
                if path_exists(path) is False:
                    raise argparse.ArgumentError(None, f"The {self.dest} does not exist: {value}")
            else:
                raise argparse.ArgumentError(None, f"The {self.dest} does not exist: {value}")

        if self.operation == SOURCE_ARG:
            if is_file(value) is not True:
                raise argparse.ArgumentError(None, "Source must be a file")
        elif self.operation == DESTINATION_ARG:
            if is_directory(value) is not True:
                raise argparse.ArgumentError(None, "Destination must be a directory")
            if not value.endswith("/"):
                value += "/"
        elif self.operation == STDOUT_ARG:
            if is_directory(value) is True:
                raise argparse.ArgumentError(None, "Destination can't be a directory")

        print(value)
        setattr(namespace, self.dest, value)


class ValidateNotEmpty(argparse.Action):
    """
    Check if user passing an empty parameters
    note: use nargs="+" if you want to check for a list of values
    """

    def __init__(self, option_strings, dest, nargs=None, **kwargs):

        self.is_list = nargs == "+"
        super(ValidateNotEmpty, self).__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, value, option_string=None):
        """
        Check if value is empty
        """
        if self.is_list is False:
            if value.strip() == "":
                raise argparse.ArgumentError(None, f"You need to pass non-empty value to {self.dest}")
        else:
            value = list(filter(lambda x: x.strip() != "", value))
            if not value:
                raise argparse.ArgumentError(None, f"You need to pass non-empty value to {self.dest}")

        setattr(namespace, self.dest, value)


class ReduceWhiteSpacesToEmpty(argparse.Action):
    """
    If passing values contain only whitespaces then it will stored as empty
    Note: required nargs='+' to handle it as a list
    """

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        self.is_list = nargs == "+"
        super(ReduceWhiteSpacesToEmpty, self).__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, value, option_string=None):
        """
        if value is whitespaces or list of whitespaces values then it will be stored as empty
        """
        if self.is_list is False:
            if value.strip() == "":
                value = ""
        else:
            value = list(filter(lambda x: x.strip() != "", value))

        setattr(namespace, self.dest, value)
