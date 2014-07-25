"""Example problems from Chapter 3"""

#L(x, n) is a function that approximates ln(1+x)
#L(x, n) = sum (1/i)*(x/(1+x))^i from i=1 to n
#or ln(1+x) = lim L(x;n) as x -> infinity

from math import log

def L(x, n):
	s = 0
	for i in range (1, n + 1):
		s += (1.0/i)*(x/(1.0 + x))**i
	value_of_sum = s
	first_neglected_term = (1.0/(n + 1))*(x/(1.0 + x))**(n + 1)
	exact_error = log(1 + x) - value_of_sum
	return value_of_sum, first_neglected_term, exact_error

#The first neglected term is the next term in the series.
#It is a good approximation of the error because it is the next
# largest term neglected and is larger than all of the rest of the terms.
#However, it may not be larger than all of the rest of the terms combined.
#This makes it an approximation.

def table(x):
	print '\nx=%g, ln(1 + x)=%g' % (x, log(1 + x))
	for n in [1, 2, 10, 100, 500]:
		value, next, error = L(x, n)
		print 'n=%-4d %-10g (next term: %8.2e    '\
				'error: %8.2e)' % (n, value, next, error)
				
table(10)
table(1000)