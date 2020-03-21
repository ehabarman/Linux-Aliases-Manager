import sys

from manager_config import data_dir_path
from util.constants import TAGS_ATTRIBUTE, DESCRIPTION_ATTRIBUTE, COMMAND_ATTRIBUTE, NAME_ATTRIBUTE, \
    ALIAS_ATTRIBUTES_DEFAULTS, SET_NAME_ATTRIBUTE, IS_ACTIVE_ATTRIBUTE
from util.helpers.files_helpers import path_exists, is_file
from util.helpers.filters import remove_non_valid_aliases, handle_conflict, change_name_handler, \
    delete_an_element_handler
from util.helpers.print_helpers import print_raw_data_in_file
from util.helpers.read_helpers import load_json_from_file


def generate_aliases_source(args):
    """
    generate a source file from aliases sets
    """
    set_names = args.set_name
    generate_all = args.all
    destination = args.destination
    package = args.package
    ignore_conflict = args.ignore_conflict
    overwrite = args.overwrite
    keep_tags = args.keep_tags
    keep_description = args.keep_description

    if package is not None:
        # Generate the sets sources into a single file
        destination_file = destination + package

        if path_exists(destination_file) and overwrite is not True:
            print("'{}' already exists in destination".format(destination_file))
        else:
            all_aliases = []
            for set_name in set_names:
                try:
                    aliases_set = load_json_from_file(set_name, data_dir_path())
                    for alias in aliases_set:
                        temp = {}
                        for attribute in ALIAS_ATTRIBUTES_DEFAULTS.keys():
                            temp[attribute] = alias[attribute] if attribute in alias \
                                else ALIAS_ATTRIBUTES_DEFAULTS[attribute]
                        temp[SET_NAME_ATTRIBUTE] = set_name
                        all_aliases.append(temp)
                except Exception as err:
                    print("Failed to load '{}' for generation: {}".format(set_name, str(err)))
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

                generate_source(all_aliases, destination_file, generate_all, keep_description, keep_tags, package)

            except Exception as err:
                print("Failed to export package '{}': {}".format(package, str(err)))
                sys.exit(1)

    else:
        # Generate the sets sources separately
        for name in set_names:
            try:
                destination_file = destination + name
                aliases = load_json_from_file(name, data_dir_path())

                if path_exists(destination_file) and overwrite is not True:
                    raise Exception("file already exits in destination")

                generate_source(aliases, destination_file, generate_all, keep_description, keep_tags, package)

            except Exception as err:
                print("Failed to generate '{}': {}".format(name, str(err)))


def generate_source(all_aliases, destination_file, generate_all, keep_description, keep_tags, package):
    source_lines = "#!/bin/bash\n\n"
    for alias in all_aliases:
        if generate_all is not True and alias[IS_ACTIVE_ATTRIBUTE] is not True:
            continue
        if keep_tags is True:
            source_lines += "#Tags: {}\n".format(alias[TAGS_ATTRIBUTE])
        if keep_description is True:
            source_lines += "#Description: {}\n".format(alias[DESCRIPTION_ATTRIBUTE])
        source_lines += "alias {}='{}'\n\n".format(alias[NAME_ATTRIBUTE], alias[COMMAND_ATTRIBUTE])
    print_raw_data_in_file(source_lines, destination_file)
    print("Exported '{}' successfully".format(package))
