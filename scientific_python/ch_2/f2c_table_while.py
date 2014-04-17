"""Fahrenheit-Celsius conversion table"""

#f2c_table_while.py

print "------------------"
F = 0
dF = 5
while F <= 215:
	C = (5.0/9.0)*(F-32)
	print "%g %.2f" % (F, C)
	F = F + dF
print "------------------"