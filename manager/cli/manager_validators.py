import argparse
from pathlib import Path

from util.constants import DESTINATION_ARG, SOURCE_ARG


class ValidatePath(argparse.Action):
    """needed for import and export operations"""

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        if not (dest == DESTINATION_ARG or dest == SOURCE_ARG):
            raise ValueError("Used only by destination and source arguments")
        super(ValidatePath, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, value, option_string=None):

        path = Path(value)
        if not path.exists():
            raise argparse.ArgumentError(None, f"The {self.dest} does not exist: {value}")
        setattr(namespace, self.dest, path)

    def __separate_file_from_path(self, value):
        pass