import sys

from util.console_printing import table_printing, json_printing
from util.constants import DATA_DIR_PATH, JSON_FORMAT, TABLE_FORMAT, ALIAS_COLUMNS
from util.json_helper import load_json_from_file


def show_aliases(args):
    name = args.name
    columns = args.columns
    view_format = args.format
    try:
        view_data = load_json_from_file(name, DATA_DIR_PATH)
        if view_format == JSON_FORMAT:
            json_printing(view_data)
        elif view_format == TABLE_FORMAT:
            if columns is None:
                table_printing(view_data, *ALIAS_COLUMNS)
            else:
                table_printing(view_data, *columns)
    except Exception as err:
        print("Operation failed: " + str(err))
