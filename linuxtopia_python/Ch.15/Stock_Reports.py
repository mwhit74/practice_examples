#Stock Reports

stockDict = { 'GM' : "General Motors", 'CAT' : "Caterpillar", 'EK' : "Eastman Kodak", "GE" : "General Electric"}

purchases = [('GE', 100, '10-SEPT-2001', 48), ('CAT', 100, '1-APR-1999', 24), ('GE', 200, '1-JUL-1998', 56)]

print "\nPurchase Summary 1"
print "Name\t\t\tPrice"

for i in purchases:
	price = i[1]*i[3]
	symbol = i[0]
	print "%r\t%r" %(stockDict.get(symbol, "No stock bought"),price)