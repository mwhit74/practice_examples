#Blocks of Stock

#(Purchase Date, Purchase Price, Shares, Symbol, Current Price)
portfolio = [ ("25-Jan-2001", 43.50, 25, 'CAT', 92.45), ("25-Jan-2001", 42.80, 50, 'DD', 51.19), ("25-Jan-2001", 42.10, 75, 'EK', 34.87), ("25-Jan-2001", 37.58, 100, 'GM', 37.58)]

i=0
total = 0
for stock in portfolio:
	individ_total = portfolio[i][1]*portfolio[i][2]
	print(individ_total)
	total += individ_total
	i += 1
	
print("Total stock purchase price is $ %r" % total)