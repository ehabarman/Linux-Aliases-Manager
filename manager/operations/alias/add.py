import sys

from manager_config import data_dir_path
from util.constants import NAME_ATTRIBUTE, TAGS_ATTRIBUTE, IS_ACTIVE_ATTRIBUTE, DESCRIPTION_ATTRIBUTE, \
    COMMAND_ATTRIBUTE, ALIAS_COLUMNS
from util.helpers.files_helpers import path_exists
from util.helpers.print_helpers import print_json_in_file, print_table_in_console
from util.helpers.read_helpers import load_json_from_file


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
        if path_exists(data_dir_path() + set_name) is False:
            raise Exception("'{}' set does not exist".format(set_name))
        set_aliases = load_json_from_file(set_name, data_dir_path())
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
        print_json_in_file(set_aliases, ALIAS_COLUMNS, data_dir_path() + set_name)
        print_table_in_console(set_aliases, ALIAS_COLUMNS)

    except Exception as e:
        print("Operation failed: {}".format(str(e)))
        sys.exit(1)
