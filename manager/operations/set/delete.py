import sys

from manager_config import data_dir_path
from util.helpers.files_helpers import remove_file, get_files_in_path


def delete_set(args):
    """
    Deletes an alias set
    """
    delete_all = args.all

    if delete_all is True:
        names = get_files_in_path(data_dir_path())
    else:
        if not args.name:
            print("Delete operation needs -a/--all flag or a name")
            sys.exit(1)
        names = args.name

    yes = args.yes
    if yes is False:
        assurance_answer = input("Are you sure you want to continue? Enter \"yes\" or \"y\" to confirm. ")
        if assurance_answer == "yes" or assurance_answer == "y":
            yes = True

    if yes is True:
        for name in names:
            try:
                remove_file(data_dir_path() + name)
                print("deleted \"%s\" successfully" % name)
            except FileNotFoundError:
                print("\"%s\" not found" % name)
                sys.exit(1)
            except Exception as e:
                print("Something went wrong: " + str(e))
                sys.exit(1)
