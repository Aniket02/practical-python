# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a file like object into a list of records
    '''
    # with open(filename) as f:
    #     rows = csv.reader(f, delimiter=delimiter)
    rows = [[field.strip().strip('"') for field in line.strip().split(delimiter)] for line in lines if line.strip() != '']

    # Read the file headers
    if has_headers:
        headers = rows[0]
        rows = rows[1:]

    if select and not has_headers:
        raise RuntimeError("select requires column headers")
        
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = []
    for index, row in enumerate(rows, start=1):
        if not row:    # Skip rows with no data
            continue
        if indices:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if silence_errors:
                    continue
                else:
                    print(f"Row {index}: Couldn't convert {row}")
                    print(f"Row {index}: Reason {e}")

        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records