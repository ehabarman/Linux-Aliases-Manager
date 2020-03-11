import sys

from util.constants import DATA_DIR_PATH, NAME_ATTRIBUTE, TAGS_ATTRIBUTE, IS_ACTIVE_ATTRIBUTE, DESCRIPTION_ATTRIBUTE, \
    COMMAND_ATTRIBUTE, ALIAS_COLUMNS
from util.helpers.files_helper import path_exists
from util.helpers.print_helper import print_json_in_file, print_json_in_console, print_table_in_console
from util.helpers.read_helper import load_json_from_file


def add_alias(args):
    """
        add new alias to a set
    """

    set_name = args.set_name
    name = args.name
    command = args.command
    description = args.description
    tags = args.tags
    is_active = args.is_active
    try:
        if path_exists(DATA_DIR_PATH + set_name) is False:
            raise Exception("'{}' set does not exist".format(set_name))
        set_aliases = load_json_from_file(set_name, DATA_DIR_PATH)
        for alias in set_aliases:
            if NAME_ATTRIBUTE in alias.keys() and name == alias[NAME_ATTRIBUTE]:
                raise Exception("'{}' alias is already in set '{}'".format(name, set_name))
        alias = {
            NAME_ATTRIBUTE: name,
            COMMAND_ATTRIBUTE: command,
            DESCRIPTION_ATTRIBUTE: description,
            TAGS_ATTRIBUTE: tags,
            IS_ACTIVE_ATTRIBUTE: is_active,
        }
        set_aliases.append(alias)
        print_json_in_file(set_aliases, ALIAS_COLUMNS, DATA_DIR_PATH + set_name)
        print_table_in_console(set_aliases, ALIAS_COLUMNS)

    except Exception as e:
        print("Operation failed: {}".format(str(e)))
        sys.exit(1)
