import sys

from util.helpers.files_helper import get_files_in_path
from util.helpers.print_helper import print_table_in_console, print_json_in_console, print_divider
from util.constants import DATA_DIR_PATH, JSON_FORMAT, TABLE_FORMAT, ALIAS_COLUMNS
from util.helpers.json_helper import load_json_from_file


def show_set(args):
    """
        Shows aliases stored in sets
    """
    show_all = args.all
    columns = args.columns
    view_format = args.format
    if show_all is True:
        names = get_files_in_path(DATA_DIR_PATH)
    else:
        if not args.name:
            sys.exit("Show operation needs -a/--all flag or a name")
        names = args.name
    names_count = len(names)
    if columns is None:
        columns = ALIAS_COLUMNS
    for index, name in enumerate(names):
        try:
            if names_count > 1:
                print("%s:" % name)
            view_data = load_json_from_file(name, DATA_DIR_PATH)
            if view_format == JSON_FORMAT:
                print_json_in_console(view_data, *columns)
            elif view_format == TABLE_FORMAT:
                print_table_in_console(view_data, *columns)
        except Exception as err:
            print("Operation failed: " + str(err))
        if index < names_count - 1:
            print_divider()
