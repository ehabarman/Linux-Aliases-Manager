from util.constants import DATA_DIR_PATH, NAME_ATTRIBUTE, ALIAS_COLUMNS
from util.helpers.files_helper import path_exists, separate_file_from_path
from util.helpers.filters import remove_non_valid_aliases, handle_conflict
from util.helpers.print_helper import print_json_in_file
from util.helpers.read_helper import load_json_from_file


def import_set(args):
    """
        Import set operation
    """
    name = args.name
    source = args.source
    overwrite = args.overwrite
    replace = args.replace
    path, file = separate_file_from_path(source)
    try:
        imported_data = pre_process_set_data(file, path)
        if path_exists(DATA_DIR_PATH + name) is not True or overwrite is True:
            # If set is new or overwrite is true then put data directly
            print_json_in_file(imported_data, ALIAS_COLUMNS, DATA_DIR_PATH + name)
        else:
            try:
                set_data = pre_process_set_data(name, DATA_DIR_PATH)

                if replace is True:
                    result = append_aliases_with_replacing_repetitive(imported_data, set_data)
                else:
                    result = handle_conflict(set_data + imported_data, attach_index_to_name)

                print_json_in_file(result, ALIAS_COLUMNS, DATA_DIR_PATH + name)

            except Exception as err:
                raise Exception(str(err))
                sys.exit(1)

    except Exception as err:
        print("Importing '{}' into '{}' failed: {}".format(file, name, str(err)))
        sys.exit(1)


def pre_process_set_data(file, path):
    imported_data = load_json_from_file(file, path)
    # Remove invalid aliases from list
    imported_data = remove_non_valid_aliases(imported_data)
    # Fix repeated aliases
    imported_data = handle_conflict(imported_data, attach_index_to_name)
    return imported_data


def attach_index_to_name(imported_data, index):
    alias = imported_data[index]
    imported_data[index][NAME_ATTRIBUTE] = "{}-{}".format(alias[NAME_ATTRIBUTE], index)


def append_aliases_with_replacing_repetitive(source_list, target_list):
    """
        Will append the passed list into a single one without alias repetition
        source_list values will be taken when conflicts occurs
        The method assumes each list had no duplicates
    """
    source_list = sorted(source_list, key=lambda alias: (alias[NAME_ATTRIBUTE]))
    target_list = sorted(target_list, key=lambda alias: (alias[NAME_ATTRIBUTE]))

    i = 0
    j = 0
    result_list = []

    while i < len(source_list) and j < len(target_list):
        if source_list[i][NAME_ATTRIBUTE] == target_list[j][NAME_ATTRIBUTE]:
            result_list.append(source_list[i])
            i += 1
            j += 1
        elif source_list[i][NAME_ATTRIBUTE] < target_list[j][NAME_ATTRIBUTE]:
            result_list.append(source_list[i])
            i += 1
        else:
            result_list.append(target_list[j])
            j += 1

    while i < len(source_list):
        result_list.append(source_list[i])
        i += 1

    while j < len(target_list):
        result_list.append(target_list[j])
        j += 1

    return result_list
