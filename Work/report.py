# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    total = 0.0

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
        
        for name, shares, price in portfolio:
            total += shares*price

        print("Total is", total)
    
    return portfolio

portfolio =  read_portfolio('Data/portfolio.csv')

# to see the portfolio: print (portfolio)
