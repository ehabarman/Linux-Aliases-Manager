import sys

from util.constants import DATA_DIR_PATH
from util.helpers.files_helper import remove_file, get_files_in_path


def delete_set(args):
    """
        Deletes an alias set
    """
    delete_all = args.all

    if delete_all is True:
        names = get_files_in_path(DATA_DIR_PATH)
    else:
        if not args.name:
            sys.exit("Delete operation needs -a/--all flag or a name")
        names = args.name

    yes = args.yes
    if yes is False:
        assurance_answer = input("Are you sure you want to continue? Enter \"yes\" or \"y\" to confirm. ")
        if assurance_answer == "yes" or assurance_answer == "y":
            yes = True

    if yes is True:
        for name in names:
            try:
                remove_file(DATA_DIR_PATH + name)
                print("deleted \"%s\" successfully" % name)
            except FileNotFoundError:
                print("\"%s\" not found" % name)
            except Exception as e:
                print("Something went wrong: " + str(e))
