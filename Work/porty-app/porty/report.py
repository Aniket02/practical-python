# report.py
#
# Exercise 2.4
from .fileparse import parse_csv
from . import tableformat
from .portfolio import Portfolio


def read_portfolio(filename, **opts):
    '''Create a list of dictionaries from a portfolio file'''
    with open(filename) as f:
        port = Portfolio.from_csv(f)
        return port

def read_prices(filename):
    '''Create a dictionary of prices from a price file'''
    with open(filename) as f:
        records = parse_csv(f, types=[str, float], has_headers=False)
        prices = {symbol: price for symbol, price in records}
        return prices

def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        report.append((holding.name, holding.shares, prices[holding.name], prices[holding.name] - holding.price))
    return report

def print_report(reportdata, formatter):
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
    # headers = ('Name', 'Shares', 'Price', 'Change')
    # table_header = f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}\n"
    # table = table_header + '---------- ---------- ---------- -----------\n'
    # for row in report:
    #     leading_dollar_sign = f"${row[2]:.2f}"
    #     table += f"{row[0]:>10s} {row[1]:>10d} {leading_dollar_sign:>10s} {row[3]:>10.2f}\n"
    # print(table)

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    if len(argv) == 4:
        portfolio_report(argv[1], argv[2], argv[3])
    elif len(argv) == 3:
        portfolio_report(argv[1], argv[2])
    else:
        print(f"Usage: {argv[0]} <portfolio_file> <prices_file>")

if __name__ == '__main__':
    import sys
    import logging
    logging.basicConfig(
        filename = 'app.log',            # Name of the log file (omit to use stderr)
        filemode = 'w',                  # File mode (use 'a' to append)
        level    = logging.DEBUG,      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL) 
    )
    main(sys.argv)

# portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

