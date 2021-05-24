# pcost.py
#
# Exercise 1.27

f = open('Data/portfolio.csv', 'rt')
headers = next(f)
total = 0

for line in f:
    list = line.split(',')
    stock_shares_1 = list[1]
    stock_price_1 = list[2]
    stock_shares = int(stock_shares_1)
    stock_price = float(stock_price_1)
    
    shares_prices = stock_shares * stock_price
    total = total + shares_prices

f.close()

print('Total cost', total)







#calculates how much it cost to purchase 
# all of the shares in the portfolio. Hint: 
# to convert a string to an integer, use int(s). 
# To convert a string to a floating point, 
# use float(s).

