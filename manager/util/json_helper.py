import json
import sys
from json import JSONDecodeError
from pathlib import Path


def load_json_from_file(json_file_name, json_file_path):
    """ Method to read json file content """
    file = join_file_and_path(json_file_name, json_file_path)
    if path_exits(file):
        try:
            with open(file) as json_file:
                return json.load(json_file)
        except JSONDecodeError:
            sys.exit("The file {} does not have a valid json format".format(file))
        except Exception:
            sys.exit("Something went wrong while reading {}".format(file))
    else:
        sys.exit("Couldn't find the file: %s" % file)


def save_json_to_file(data, json_file_name, json_file_path, overwrite=True):
    """Method that will write json data to a file"""
    if path_exits(json_file_path):
        file = join_file_and_path(json_file_name, json_file_path)
        if overwrite is False and path_exits(file):
            sys.exit("File %s exits and overwrite option is False" % file)
        else:
            try:
                with open(file, 'w') as outfile:
                    json.dump(data, outfile)
            except Exception:
                sys.exit("Failed to write json data to file %s. Make sure you are passing a json data" % file)
    else:
        sys.exit("Invalid path: %s" % json_file_path)


def path_exits(file):
    path = Path(file)
    return path.exists()


def join_file_and_path(file, path):
    # Add / to the end of the path file if not added
    if path[-1] != "/":
        return path + "/" + file
    else:
        return path + file
