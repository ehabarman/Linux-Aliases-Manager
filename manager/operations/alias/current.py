import sys

from util.constants import SOURCE_FORMAT, JSON_FORMAT, TABLE_FORMAT, NAME_ATTRIBUTE, COMMAND_ATTRIBUTE, \
    DESCRIPTION_ATTRIBUTE, TAGS_ATTRIBUTE, IS_ACTIVE_ATTRIBUTE, ALIAS_COLUMNS
from util.helpers.print_helpers import print_table_in_console, print_json_in_console, print_raw_data_in_file, \
    print_table_in_file, print_json_in_file
from util.shell import execute_shell_command


def current_aliases(args):
    """
    Shows aliases sourced by the current user
    """
    format_view = args.format
    stdout = args.stdout

    output, err, rc = execute_shell_command("/bin/bash -i -c alias")
    if rc != 0:
        print("Error: {}".format(err))
        sys.exit(1)

    if format_view == SOURCE_FORMAT:
        data_view = output
    else:
        aliases = output.split("\n")
        data_view = []
        if aliases:
            for alias in aliases:
                temp = alias[6:]
                equality_index = temp.index("=")
                name = temp[: equality_index]
                command = temp[equality_index + 1:]
                data_view.append({
                    NAME_ATTRIBUTE: name,
                    COMMAND_ATTRIBUTE: command,
                    DESCRIPTION_ATTRIBUTE: "",
                    TAGS_ATTRIBUTE: "",
                    IS_ACTIVE_ATTRIBUTE: True
                })

    if stdout is None:
        if format_view == SOURCE_FORMAT:
            print(data_view)
        elif format_view == TABLE_FORMAT:
            print_table_in_console(data_view, [NAME_ATTRIBUTE, COMMAND_ATTRIBUTE])
        elif format_view == JSON_FORMAT:
            print_json_in_console(data_view, ALIAS_COLUMNS)
    else:
        if format_view == SOURCE_FORMAT:
            print_raw_data_in_file(data_view, stdout)
        elif format_view == TABLE_FORMAT:
            print_table_in_file(data_view, [NAME_ATTRIBUTE, COMMAND_ATTRIBUTE], stdout)
        elif format_view == JSON_FORMAT:
            print_json_in_file(data_view, ALIAS_COLUMNS, stdout)
        print("Result redirected to '{}'".format(stdout))
