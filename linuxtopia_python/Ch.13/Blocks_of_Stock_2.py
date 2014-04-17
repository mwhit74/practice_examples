#Blocks of Stock

#(Purchase Date, Purchase Price, Shares, Symbol, Current Price)
portfolio = [ ("25-Jan-2001", 43.50, 25, 'CAT', 92.45), ("25-Jan-2001", 42.80, 50, 'DD', 51.19), ("25-Jan-2001", 42.10, 75, 'EK', 34.87), ("25-Jan-2001", 37.58, 100, 'GM', 37.58)]

i=0
total_purchase_price, total_current_price = 0, 0
for stock in portfolio:
	individ_total_purchase_price = portfolio[i][1]*portfolio[i][2]
	individ_total_current_price = portfolio[i][2]*portfolio[i][4]
	
	total_purchase_price += individ_total_purchase_price
	total_current_price += individ_total_current_price
	
	i += 1
	
current_worth = total_purchase_price + total_current_price
print("Current worth is $ %r" % current_worth)