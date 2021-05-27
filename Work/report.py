# report.py
# Exercise 2.4 - simpler

# Exercise 2.5 - below

import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            naming_value = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(naming_value)
   
    return portfolio

portfolio =  read_portfolio('Data/portfolio.csv')

# to see the portfolio: 2.4
#print (portfolio)

#better visualization 2.5
#from pprint import pprint
#pprint(portfolio)

# Exercise 2.6

#import csv
#f = open('Data/prices.csv', 'r')
#rows = csv.reader(f)
#for row in rows:
#    print(row)

def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

prices =  read_prices('Data/prices.csv')

#from pprint import pprint
#pprint(prices)

#compute basic total cost so far

total_before = 0 # start with 0

for sum in portfolio:
    total_before += sum['price']*sum['shares'] # multiply dic with ['key names']

# current values to compare with the prior ones

total_amount_now = 0

for sum in portfolio:
    total_amount_now += prices[sum['name']]*sum['shares']

#compute loss/gain
#print ('Value in market before was', total_before)
#print ('Value in market now is', total_amount_now)
#print ('Gain/loss at the end', total_amount_now - total_before)

def make_report(portfolio, prices):
    list = []
    for s in portfolio:
        price_now = prices[s['name']]
        diff = price_now - s['price']
        s_tuples = (s['name'], s['shares'], price_now, diff) #create tuples
        list.append(s_tuples)
    return list

report = make_report(portfolio,prices)
#basic print
#for r in report:
       # print(r)

#redo for loop
#for r in report:
       # print('%10s %10d %10.2f %10.2f' % r)

#headers
header_1 = ('Name', 'Shares', 'Price', 'Change')
print ('%10s %10s %10s %10s' % header_1)
print (('-' *10 + ' ')* len(header_1))

#better looking loop
for name, shares, price, change in report:
       print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

