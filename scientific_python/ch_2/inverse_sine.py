"""Explore the Python Libaray Reference
	specifically the documentation of the math module
	concerning the inverse sine function"""
	
#inverse_sine.py

from math import sin, asin

n = 10
x = 0

for c in xrange(n + 1, 1, -1):
	x += 1.0/n
	print x
	print asin(x)
	print sin(asin(x))