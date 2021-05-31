# report.py

# read datafile
import fileparse

def read_portfolio(filename):
    '''Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.'''
    #Iterables
    with open(filename) as lines:
        return fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):
    '''Read a stock prices file into a dictionarie with keys name and price data'''
    #Iterables
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str,float], has_headers=False))
    
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
    print_report(report)

#main() function that accepts a list of command 
# line options and produces the same output as 
# before. 

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    #calling portfolio_report
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)
