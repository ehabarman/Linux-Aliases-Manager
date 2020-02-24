from util.printing.console_printing import json_printing, table_printing
from util.constants import DATA_DIR_PATH, TABLE_FORMAT, JSON_FORMAT
from util.files_helper import get_files_in_path
from util.json_helper import load_json_from_file

__NAME__ = "Name"
__STATUS__ = "Status"
__VALID_STATUS__ = "Valid"
__INVALID_STATUS__ = "Invalid"


def list_sets(args):
    view_format = args.format
    show_validity = args.validity
    json_files = get_files_in_path(DATA_DIR_PATH)
    view_data = [{__NAME__: json_file, __STATUS__: None} for json_file in json_files]
    if show_validity is True:
        for json_data in view_data:
            try:
                load_json_from_file(json_data[__NAME__], DATA_DIR_PATH)
                json_data[__STATUS__] = __VALID_STATUS__
            except Exception:
                json_data[__STATUS__] = __INVALID_STATUS__
    if view_format == JSON_FORMAT:
        json_printing(view_data)
    elif view_format == TABLE_FORMAT:
        if show_validity is True:
            table_printing(view_data, __NAME__, __STATUS__)
        else:
            table_printing(view_data, __NAME__)
