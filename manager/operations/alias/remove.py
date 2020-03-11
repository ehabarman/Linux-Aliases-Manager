import sys

from util.constants import DATA_DIR_PATH, NAME_ATTRIBUTE, ALIAS_COLUMNS
from util.helpers.files_helper import path_exists
from util.helpers.print_helper import print_json_in_file, print_table_in_console
from util.helpers.read_helper import load_json_from_file


def remove_aliases(args):
    """
        remove aliases from a set
    """

    aliases_names = args.name
    confirmation = args.yes
    set_name = args.set_name

    try:
        if path_exists(DATA_DIR_PATH + set_name) is False:
            raise Exception("'{}' set does not exist".format(set_name))
        set_aliases = load_json_from_file(set_name, DATA_DIR_PATH)

        set_names_list = [alias[NAME_ATTRIBUTE] for alias in set_aliases]

        found_aliases = []
        not_found_aliases = []

        for alias_name in aliases_names:
            if alias_name in set_names_list:
                found_aliases.append(alias_name)
            else:
                not_found_aliases.append(alias_name)

        if not_found_aliases:
            print("{} not found in the set".format(not_found_aliases))

        if not found_aliases:
            raise Exception("You didn't pass a valid existing aliases' names")

        print("{} found in the set".format(found_aliases))
        if confirmation is False:
            assurance_answer = input("Are you sure you want to continue? Enter \"yes\" or \"y\" to confirm. ")
            if assurance_answer == "yes" or assurance_answer == "y":
                confirmation = True

        if confirmation is True:
            remaining_aliases = list(filter(lambda alias: alias[NAME_ATTRIBUTE] not in found_aliases, set_aliases))
            print_json_in_file(remaining_aliases, ALIAS_COLUMNS, DATA_DIR_PATH + set_name)
            print_table_in_console(remaining_aliases, ALIAS_COLUMNS)

    except Exception as e:
        print("Operation failed: {}".format(str(e)))
        sys.exit(1)
