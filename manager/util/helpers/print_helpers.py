import json
from texttable import Texttable
import os


def print_table_in_file(data, headers, file_path):
    table = prepare_table(data, 160, *headers)
    f = open(file_path, "w+")
    f.write(table)
    f.close()


def print_table_in_console(data, headers):
    table = prepare_table(data, None, *headers)
    print(table)


def print_json_in_file(raw_data, keys, file_path):
    data = prepare_json(raw_data, *keys)
    f = open(file_path, "w+")
    f.write(json.dumps(data, indent=4, sort_keys=True))
    f.close()


def print_json_in_console(raw_data, keys):
    data = prepare_json(raw_data, *keys)
    print(json.dumps(data, indent=4, sort_keys=True))


def prepare_table(data, width=None, *headers):
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
    f = open(file_path, "w+")
    f.write(raw_data)
    f.close()


def prepare_json(raw_data, *keys):
    data = []
    for raw_object in raw_data:
        new_object = {}
        for key in keys:
            new_object[key] = raw_object[key]
        data.append(new_object)
    return data


def print_divider(divider_text="="):
    columns = get_console_width()
    times = max(columns // len(divider_text), 1)
    print(divider_text * times)


def get_console_width():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(columns)