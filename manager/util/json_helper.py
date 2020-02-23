import json
import sys
from json import JSONDecodeError
from pathlib import Path


def load_json_from_file(json_file_name, json_file_path):
    """ Method to read json file content """
    file = join_file_and_path(json_file_name, json_file_path)
    if file_exits(file):
        try:
            with open(file) as json_file:
                return json.load(json_file)
        except JSONDecodeError:
            sys.exit("The file {} does not have a valid json format".format(file))
        except Exception:
            sys.exit("Something went wrong while reading {}".format(file))
    else:
        sys.exit("Couldn't find the file: %s" % file)


def save_json_to_file(json, json_file_name, json_file_path, should_over_write=False):
    """Method that will write json data to a file"""
    pass


def file_exits(file):
    path = Path(file)
    return path.exists()


def join_file_and_path(file, path):
    # Add / to the end of the path file if not added
    if path[-1] != "/":
        return path + "/" + file
    else:
        return path + file


print(load_json_from_file("aliases.json", "../data/"))