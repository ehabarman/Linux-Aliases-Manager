from manager_config import data_dir_path
from util.helpers.print_helpers import print_json_in_console, print_table_in_console
from util.constants import TABLE_FORMAT, JSON_FORMAT
from util.helpers.files_helpers import get_files_in_path
from util.helpers.read_helpers import load_json_from_file

__NAME__ = "Name"
__STATUS__ = "Status"
__VALID_STATUS__ = "Valid"
__INVALID_STATUS__ = "Invalid"


def list_sets(args):
    """
    Lists all aliases sets
    """
    view_format = args.format
    show_validity = args.validity
    json_files = get_files_in_path(data_dir_path())
    headers = [__NAME__]
    view_data = [{__NAME__: json_file, __STATUS__: None} for json_file in json_files]
    if show_validity is True:
        headers.append(__STATUS__)
        for json_data in view_data:
            try:
                load_json_from_file(json_data[__NAME__], data_dir_path())
                json_data[__STATUS__] = __VALID_STATUS__
            except Exception:
                json_data[__STATUS__] = __INVALID_STATUS__
    if view_format == JSON_FORMAT:
        print_json_in_console(view_data, headers)
    elif view_format == TABLE_FORMAT:
        print_table_in_console(view_data, headers)
