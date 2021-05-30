# report.py

# read datafile
import csv

def read_portfolio(filename):
    '''Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.'''
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

def read_prices(filename):
    '''Read a stock prices file into a dictionarie with keys name and price data'''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

def make_report(portfolio, prices):
    '''Make a list (name, shares, price, and change) of tuples'''
    list = []
    for s in portfolio:
        price_now = prices[s['name']]
        diff = price_now - s['price']
        s_tuples = (s['name'], s['shares'], price_now, diff) #create tuples
        list.append(s_tuples)
    return list

def print_report(report, prices):
    '''Print out the total cost (shares*price) of a portfolio file'''
    #headers
    header_1 = ('Name', 'Shares', 'Price', 'Change')
    print ('%10s %10s %10s %10s' % header_1)
    print (('-' *10 + ' ')* len(header_1))

    #better looking loop
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
    return (report)


def portfolio_report (portfoliofile,pricefile):
    '''Stock report of the portfokio and price files'''
    
    portfolio =  read_portfolio(portfoliofile)
    prices =  read_prices(pricefile)
    report = make_report(portfolio,prices)
    report_print = print_report(report, prices)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
