import sys

from util.constants import TABLE_FORMAT, data_dir_path, JSON_FORMAT, SET_NAME_ATTRIBUTE, ALIAS_COLUMNS, \
    ALIAS_ATTRIBUTES_DEFAULTS, NAME_ATTRIBUTE
from util.helpers.files_helpers import path_exists
from util.helpers.filters import remove_non_valid_aliases, handle_conflict, change_name_handler, \
    delete_an_element_handler
from util.helpers.read_helpers import load_json_from_file
from util.helpers.print_helpers import print_table_in_file, print_json_in_file
from util.shell import execute_shell_command


def export_set(args):
    """
        Export aliases sets
    """
    destination = args.destination
    view_format = args.format
    names = args.name
    package = args.package
    ignore_conflict = args.ignore_conflict
    overwrite = args.overwrite
    if package is not None:
        # Export all sets into a single file
        destination_file = destination + package
        if path_exists(destination_file) and overwrite is not True:
            print("'{}' already exists in destination".format(destination_file))
        else:
            all_aliases = []
            for name in names:
                try:
                    aliases_set = load_json_from_file(name, data_dir_path)
                    for alias in aliases_set:
                        temp = {}
                        for attribute in ALIAS_ATTRIBUTES_DEFAULTS.keys():
                            temp[attribute] = alias[attribute] if attribute in alias \
                                else ALIAS_ATTRIBUTES_DEFAULTS[attribute]
                        temp[SET_NAME_ATTRIBUTE] = name
                        all_aliases.append(temp)
                except Exception as err:
                    print("Failed to export '{}': {}".format(name, str(err)))
                    continue
            try:
                # Remove invalid aliases from list
                all_aliases = remove_non_valid_aliases(all_aliases)
                if ignore_conflict is True:
                    # Set alias name to set_name + alias_name
                    all_aliases = handle_conflict(all_aliases, change_name_handler)
                else:
                    # Delete conflicted aliases
                    all_aliases = handle_conflict(all_aliases, delete_an_element_handler)
                if view_format == JSON_FORMAT:
                    print_json_in_file(all_aliases, ALIAS_COLUMNS, destination_file)
                elif view_format == TABLE_FORMAT:
                    print_table_in_file(all_aliases, ALIAS_COLUMNS, destination_file)

                print("Exported '{}' successfully".format(package))

            except Exception as err:
                print("Failed to export package '{}': {}".format(package, str(err)))
                sys.exit(1)
    else:
        # Export the sets separately
        for name in names:
            try:
                destination_file = destination + name
                data = load_json_from_file(name, data_dir_path)

                if path_exists(destination_file) and overwrite is not True:
                    raise Exception("file already exits in destination")

                if view_format == JSON_FORMAT:
                    output, err, rc = execute_shell_command("cp {} {}".format(data_dir_path + name, destination_file))
                    if rc != 0:
                        raise Exception(err)
                elif view_format == TABLE_FORMAT:
                    print_table_in_file(data, ALIAS_COLUMNS, destination_file)
                print("Exported '{}' Successfully".format(name))
            except Exception as err:
                print("Failed to export '{}': {}".format(name, str(err)))
