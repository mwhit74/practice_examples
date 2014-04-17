"""Approximate Fahrenheit-Celsius conversion table"""

#f2c_approx_table.py

print "----------------"
F = 0
dF = 5

while F <= 215:
	C = (F - 30.0)/2.0
	print "%g %.2f" % (F, C)
	F = F + dF
print "----------------"