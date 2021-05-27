# pcost.py
#
# Exercise 1.27

import csv
def portfolio_cost(filename):
    total = 0

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for rowno, row in enumerate (rows, start=1):
            record = dict(zip(headers, row))
            try:
                stock_shares_1 = record['shares']
                stock_price_1 = record['price']
                stock_shares = int(stock_shares_1)
                stock_price = float(stock_price_1)
                shares_prices = stock_shares * stock_price
                total = total + shares_prices
            except ValueError:
                print (f'Row {rowno}: Bad row {row}')
        return total
            
total =  portfolio_cost('Data/portfoliodate.csv')

print ("Total cost is", total)