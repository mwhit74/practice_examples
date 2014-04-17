"""Approximate Fahrenheit-Celsius conversion table"""

#f2c_approx_table.py

print "----------------"
F = 0
dF = 5

while F <= 215:
	C = 5.0/9.0*(F - 32.0)
	C_approx = (F - 30.0)/2.0
	print "%g %.2f %.2f" % (F, C, C_approx)
	F = F + dF
print "----------------"