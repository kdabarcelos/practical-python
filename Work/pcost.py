# pcost.py
#
# Exercise 1.27

import report
def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    
    return sum ([s['shares']*s['price'] for s in portfolio])
            

total =  portfolio_cost('Data/portfolio.csv')

print ("Total cost is", total)