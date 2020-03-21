import sys

from manager_config import data_dir_path
from util.helpers.files_helpers import get_files_in_path
from util.helpers.print_helpers import print_table_in_console, print_json_in_console, print_divider
from util.constants import JSON_FORMAT, TABLE_FORMAT, ALIAS_COLUMNS
from util.helpers.read_helpers import load_json_from_file


def show_set(args):
    """
    Shows aliases stored in sets
    """
    show_all = args.all
    columns = args.columns
    view_format = args.format
    if show_all is True:
        names = get_files_in_path(data_dir_path())
    else:
        if not args.name:
            print("Show operation needs -a/--all flag or a name")
            sys.exit(1)
        names = args.name
    names_count = len(names)
    if columns is None:
        columns = ALIAS_COLUMNS
    for index, name in enumerate(names):
        try:
            if names_count > 1:
                print("%s:" % name)
            view_data = load_json_from_file(name, data_dir_path())
            if view_format == JSON_FORMAT:
                print_json_in_console(view_data, columns)
            elif view_format == TABLE_FORMAT:
                print_table_in_console(view_data, columns)
        except Exception as err:
            print("Operation failed: " + str(err))
        if index < names_count - 1:
            print_divider()
