import json
from texttable import Texttable
import os


def print_table_in_file(data, headers, file_path):
    """
    Builds a table from dictionary of aliases with cols headers then print it in a file

    @param data: The dictionary containing the data
    @param headers: Cols name
    @param file_path: The path to print the table in
    """
    table = prepare_table(data, 160, *headers)
    f = open(file_path, "w+")
    f.write(table)
    f.close()


def print_table_in_console(data, headers):
    """
    Builds a table from dictionary of aliases with cols headers then print it in the console

    @param data: The dictionary containing the data
    @param headers: Cols name
    """
    table = prepare_table(data, None, *headers)
    print(table)


def print_json_in_file(raw_data, keys, file_path):
    """
    Print json data in a file with the specific keys

    @param raw_data: The dictionary containing the data
    @param keys: keys to be used
    @param file_path: The path to print dictionary in
    """
    data = prepare_json(raw_data, *keys)
    f = open(file_path, "w+")
    f.write(json.dumps(data, indent=4, sort_keys=True))
    f.close()


def print_json_in_console(raw_data, keys):
    """
    Print json data in the console with the specific keys

    @param raw_data: The dictionary containing the data
    @param keys: keys to be used
    """
    data = prepare_json(raw_data, *keys)
    print(json.dumps(data, indent=4, sort_keys=True))


def prepare_table(data, width=None, *headers):
    """
    Draws a table using a list of dictionaries

    @param data: list of data representing rows
    @param width: table width (minimum 80)
    @param headers: tables headers
    @return: String containing the table
    """
    raw_table = []
    for row_data in data:
        row = []
        for index in range(len(headers)):
            header = headers[index]
            if header in row_data:
                row.append(str(row_data[header]))
            else:
                row.append(None)
        raw_table.append(row)
    if width is None:
        width = get_console_width()
    table = Texttable(max(80, width))
    table.header(headers)
    table.add_rows(raw_table, header=False)
    return table.draw()


def print_raw_data_in_file(raw_data, file_path):
    """
    Print data in a given file
    """
    f = open(file_path, "w+")
    f.write(raw_data)
    f.close()


def prepare_json(raw_data, *keys):
    """
    Returns json list after extracting the keys values from a json list

    @param raw_data: list of objects
    @param keys: keys to be extracted
    @return: filter json list
    """
    data = []
    for raw_object in raw_data:
        new_object = {}
        for key in keys:
            new_object[key] = raw_object[key] if key in raw_object.keys() else None
        data.append(new_object)
    return data


def print_divider(divider_text="="):
    """
    Will print a dividing line on the screen
    """
    columns = get_console_width()
    times = max(columns // len(divider_text), 1)
    print(divider_text * times)


def get_console_width():
    """
    Get the current console session width using stty command

    @return: console width as integer
    """
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(columns)
