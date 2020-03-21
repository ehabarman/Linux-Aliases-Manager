import sys

from manager_config import data_dir_path
from operations.set.list import list_sets
from util.constants import ALIAS_COLUMNS
from util.helpers.files_helpers import path_exists
from util.helpers.print_helpers import print_json_in_file


def create_set(args):
    """
    Creates a new aliases set
    """
    name = args.name

    if path_exists(data_dir_path() + name) is True:
        print("'%s' set already exists" % name)
        sys.exit(1)
    else:
        try:
            print_json_in_file([], ALIAS_COLUMNS, data_dir_path() + name)
            print("'%s' set created successfully" % name)
            args.format = "table"
            args.validity = False
            list_sets(args)
        except Exception as err:
            print("Failed to create set '%s'" % str(err))
            sys.exit(1)
