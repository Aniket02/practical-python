# pcost.py
#
# Exercise 1.27

import sys
import report
def portfolio_cost(filename):
    records = report.read_portfolio(filename)
    pcost = 0
    for record in records:
        pcost += record.cost
    # for rowno, row in enumerate(rows, start=1):
    #     try:
    #         shares = int(row[1])
    #         price = float(row[2])
    #         pcost += (shares * price)
    #     except ValueError:
    #         print(f'Row {rowno}: Bad row: {row}')
    return pcost

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
        cost = portfolio_cost(filename)
    else:
        print(f"Usage: {argv[0]} <portfolio_file>")
    print(f"Total cost {round(cost, 2)}")

if __name__ == '__main__':
    import sys
    main(sys.argv)
    
