# report.py
#
# Exercise 2.4

import csv
from types import DynamicClassAttribute

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            naming_value = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(naming_value)
   
    return portfolio

portfolio =  read_portfolio('Data/portfolio.csv')

# to see the portfolio: 
#print (portfolio)

from pprint import pprint
pprint(portfolio)
