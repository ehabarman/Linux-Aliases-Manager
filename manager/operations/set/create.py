from operations.set.list import list_sets
from util.constants import DATA_DIR_PATH
from util.files_helper import path_exists
from util.json_helper import save_json_to_file


def create_set(args):
    name = args.name
    if path_exists(DATA_DIR_PATH + name) is True:
        print("\"%s\" set already exists" % name)
    else:
        try:
            save_json_to_file([], name, DATA_DIR_PATH)
            print("\"%s\" set created successfully" % name)
            args.format = "table"
            args.validity = False
            list_sets(args)
        except Exception as err:
            print("Failed to create set \"%s\"" % str(err))

