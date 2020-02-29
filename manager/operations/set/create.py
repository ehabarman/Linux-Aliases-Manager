from operations.set.list import list_sets
from util.constants import DATA_DIR_PATH, ALIAS_COLUMNS
from util.helpers.files_helper import path_exists
from util.helpers.print_helper import print_json_in_file


def create_set(args):
    """
        Creates a new aliases set
    """
    name = args.name

    if path_exists(DATA_DIR_PATH + name) is True:
        print("'%s' set already exists" % name)
    else:
        try:
            print_json_in_file([], ALIAS_COLUMNS, DATA_DIR_PATH + name)
            print("'%s' set created successfully" % name)
            args.format = "table"
            args.validity = False
            list_sets(args)
        except Exception as err:
            print("Failed to create set '%s'" % str(err))
