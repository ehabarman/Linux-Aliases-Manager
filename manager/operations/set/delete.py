from util.constants import DATA_DIR_PATH
from util.files_helper import path_exists, remove_file


def delete_set(args):
    name = args.name
    yes = args.yes
    if path_exists(DATA_DIR_PATH + name) is True:
        if yes is False:
            assurance_answer = input("Enter \"yes\" or \"y\" if you are sure about deleting \"%s\"" % name)
            if assurance_answer == "yes" or assurance_answer == "y":
                yes = True
        if yes is True:
            remove_file(DATA_DIR_PATH + name)
    else:
        print("\"%s\" doesn't exist" % name)


