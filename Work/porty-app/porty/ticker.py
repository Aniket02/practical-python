# ticker.py

from .follow import follow
import csv
from . import report
from . import tableformat


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, str, str])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def select_columns(rows, indices):
    return (
        [row[index] for index in indices]
        for row in rows
    )

def convert_types(rows, types):
    return (
        [func(val) for func, val in zip(types, row)]
        for row in rows
    )

def filter_symbols(rows, names):
    # for row in rows: 
    #     if row['name'] in names:
    #         yield row
    return (row for row in rows if row['name'] in names)

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def print_rows(rows):
    for row in rows:
        rowdata = [row['name'], row['price'], row['change']]
        yield rowdata

def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = filter_symbols(rows, portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name','Price','Change'])
    for row in print_rows(rows):
        formatter.row(row)

if __name__ == '__main__':
    portfolio = report.read_portfolio('Data/portfolio.csv')
    rows = parse_stock_data(follow('Data/stocklog.csv'))
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)