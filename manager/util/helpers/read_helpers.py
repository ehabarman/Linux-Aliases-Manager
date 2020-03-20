import json
from json import JSONDecodeError
from util.helpers.files_helpers import join_file_and_path, path_exists


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
