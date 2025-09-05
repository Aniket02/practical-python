# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):

    def headings(self, headers):
        entry = ""
        for h in headers:
            entry += f"<th>{h}</th>"
        print(f"<tr>{entry}</tr>")

    def row(self, rowdata):
        entry = ""
        for d in rowdata:
            entry += f"<td>{d}</td>"
        print(f"<tr>{entry}</tr>")

class FormatError(Exception):
    pass

def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {fmt}')

def print_table(portfolio, attributes, formatter):
    formatter.headings(attributes)
    for item in portfolio:
        rowdata = [str(getattr(item, attr)) for attr in attributes]
        formatter.row(rowdata)
