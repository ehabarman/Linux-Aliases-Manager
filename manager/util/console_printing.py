import json
from texttable import Texttable
import os


def table_printing(data, *headers):
    raw_table = []
    for row_data in data:
        row = []
        for index in range(len(headers)):
            header = headers[index]
            if header in row_data:
                row.append(row_data[header])
            else:
                row.append(None)
        raw_table.append(row)
    rows, columns = os.popen('stty size', 'r').read().split()
    table = Texttable(max(80, int(columns)))
    table.header(headers)
    table.add_rows(raw_table, header=False)
    print(table.draw())


def json_printing(data):
    print(data)
    print(json.dumps(data, indent=4, sort_keys=True))
