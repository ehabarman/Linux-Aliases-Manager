import sys

from util.constants import DATA_DIR_PATH, NAME_ATTRIBUTE, IS_ACTIVE_ATTRIBUTE, TAGS_ATTRIBUTE, DESCRIPTION_ATTRIBUTE, \
    COMMAND_ATTRIBUTE, ALIAS_COLUMNS
from util.helpers.files_helper import path_exists
from util.helpers.print_helper import print_json_in_file, print_table_in_console
from util.helpers.read_helper import load_json_from_file


def edit_alias(args):
    """
        edit alias in a set
    """
    set_name = args.set_name
    alias_name = args.alias_name
    new_name = args.name
    new_command = args.command
    new_description = args.description
    new_tags = args.tags
    new_is_active = args.is_active

    try:
        if path_exists(DATA_DIR_PATH + set_name) is False:
            raise Exception("'{}' set does not exist".format(set_name))
        set_aliases = load_json_from_file(set_name, DATA_DIR_PATH)

        target_alias = None
        for alias in set_aliases:
            if alias_name == alias_name[NAME_ATTRIBUTE]:
                target_alias = alias
                break

        if target_alias is None:
            raise Exception("'{}' is not a valid alias name".format(alias_name))

        if new_name != alias_name:
            for alias in set_aliases:
                if new_name == alias[NAME_ATTRIBUTE]:
                    raise Exception("'{}' new alias name already used".format(new_name))

        target_alias[NAME_ATTRIBUTE] = new_name if new_name is not None else target_alias[NAME_ATTRIBUTE]
        target_alias[COMMAND_ATTRIBUTE] = new_command if new_command is not None else target_alias[COMMAND_ATTRIBUTE]
        target_alias[DESCRIPTION_ATTRIBUTE] = new_description if new_description is not None \
            else target_alias[DESCRIPTION_ATTRIBUTE]
        target_alias[TAGS_ATTRIBUTE] = new_tags if new_tags is not None else target_alias[TAGS_ATTRIBUTE]
        target_alias[IS_ACTIVE_ATTRIBUTE] = new_is_active if new_is_active is not None \
            else target_alias[IS_ACTIVE_ATTRIBUTE]

        print_json_in_file(set_aliases, ALIAS_COLUMNS, DATA_DIR_PATH + set_name)
        print_table_in_console(set_aliases, ALIAS_COLUMNS)

    except Exception as e:
        print("Operation failed: {}".format(str(e)))
        sys.exit(1)
