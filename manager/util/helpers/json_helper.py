import json
from json import JSONDecodeError
from util.helpers.files_helper import join_file_and_path, path_exists


def load_json_from_file(json_file_name, json_file_path):
    """ Method to read json file content """
    file = join_file_and_path(json_file_name, json_file_path)
    if path_exists(file):
        try:
            with open(file) as json_file:
                return json.load(json_file)
        except JSONDecodeError:
            raise Exception("The file {} does not have a valid json format".format(file))
        except Exception:
            raise Exception("Something went wrong while reading {}".format(file))
    else:
        raise Exception("Couldn't find the file: %s" % file)


def save_json_to_file(data, json_file_name, json_file_path, overwrite=True):
    """Method that will write json data to a file"""
    if path_exists(json_file_path):
        file = join_file_and_path(json_file_name, json_file_path)
        if overwrite is False and path_exists(file):
            raise Exception("File %s exits and overwrite option is False" % file)
        else:
            try:
                with open(file, 'w') as outfile:
                    json.dump(data, outfile)
            except Exception:
                raise Exception("Failed to write json data to file %s. Make sure you are passing a json data" % file)
    else:
        raise Exception("Invalid path: %s" % json_file_path)
