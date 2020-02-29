import re
from os import listdir
from pathlib import Path
import os
from os.path import isfile, join


def path_exists(file):
    path = Path(file)
    return path.exists()


def remove_file(file):
    os.remove(file)


def join_file_and_path(file, path):
    # Add / to the end of the path file if not added
    if path[-1] != "/":
        return path + "/" + file
    else:
        return path + file


def get_files_in_path(path):
    if path_exists(path):
        return [file for file in listdir(path) if isfile(join(path, file))]
    else:
        return []


def separate_file_from_path(value):
    file = re.search(r"(?<=\/)[^\/\\]+$", value)
    path = re.search(r".*\/(?=.*)", value)
    file = file.group(0) if file is not None else ""
    path = path.group(0) if path is not None else ""
    return path, file


def is_file(file_path):
    return os.path.isfile(file_path)


def is_directory(dir_path):
    return os.path.isdir(dir_path)