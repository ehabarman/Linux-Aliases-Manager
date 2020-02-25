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
