import sys

from util.constants import DATA_DIR_PATH, TAGS_ATTRIBUTE, DESCRIPTION_ATTRIBUTE, COMMAND_ATTRIBUTE, NAME_ATTRIBUTE
from util.helpers.files_helper import path_exists
from util.helpers.print_helper import print_raw_data_in_file
from util.helpers.read_helper import load_json_from_file


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
        pass

    else:
        # Generate the sets sources separately
        for name in set_names:
            try:
                destination_file = destination + name
                aliases = load_json_from_file(name, DATA_DIR_PATH)

                if path_exists(destination_file) and overwrite is not True:
                    raise Exception("file already exits in destination")

                source_lines = "#!/bin/bash\n\n"

                for alias in aliases:
                    if keep_tags is True:
                        source_lines += "#Tags: {}\n".format(alias[TAGS_ATTRIBUTE])
                    if keep_description is True:
                        source_lines += "#Description: {}\n".format(alias[DESCRIPTION_ATTRIBUTE])
                    source_lines += "alias {}='{}'\n\n".format(alias[NAME_ATTRIBUTE], alias[COMMAND_ATTRIBUTE])

                print_raw_data_in_file(source_lines, destination_file)
                print("Generated '{}' Successfully".format(name))
            except Exception as err:
                print("Failed to generate '{}': {}".format(name, str(err)))

    # try:
    #
    #     pass
    #
    # except Exception as e:
    #     print("Operation failed: {}".format(str(e)))
    #     sys.exit(1)


