import re
from os import listdir
from pathlib import Path
import os
from os.path import isfile, join


def path_exists(full_path):
    """
    Returns if the file or directory path passed exists
    """
    path = Path(full_path)
    return path.exists()


def remove_file(full_path):
    """
    Remove the file or directory in the path
    """
    os.remove(full_path)


def join_file_and_path(file, path):
    """
    Join the file and path into full path
    """
    if path:
        if path[-1] != "/":
            return path + "/" + file
        else:
            return path + file
    else:
        return file


def get_files_in_path(path):
    """
    returns a list of all files in a path
    """
    if path_exists(path):
        return [file for file in listdir(path) if isfile(join(path, file))]
    else:
        return []


def separate_file_from_path(full_path):
    """
    Will separate file and path from full path
    """
    file = re.search(r"(?<=\/)[^\/\\]+$", full_path)
    path = re.search(r".*\/(?=.*)", full_path)
    file = file.group(0) if file is not None else ""
    path = path.group(0) if path is not None else ""
    file = full_path if file == "" and path == "" else file
    return path, file


def is_file(file_path):
    """
    Returns true if the passed full path is file
    """
    return os.path.isfile(file_path)


def is_directory(dir_path):
    """
    Returns true if the passed full path is directory
    """
    return os.path.isdir(dir_path)
