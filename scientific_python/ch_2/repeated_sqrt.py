"""Explore round-off errors from a large number of inverse operations"""

# repeated_sqr.py

from math import sqrt

#functions have not been introduced in the text yet but
# I feel the need to use them here so that two different
# 'chuncks' of code can be ran

def func1():
	for n in range (1, 60):
		r = 2.0
		#taking the sqrt of the number n times for example, n = 3
		#sqrt(sqrt(sqrt(r)))
		for i in range(n):
			r = sqrt(r)
		#squaring the number n times times for example, n = 3
		#(((r)^2)^2)^2)
		#this should essentially 'undo' what the first loop did
		for i in range(n):
			r = r**2
		#print the result after taking the sqrt and squaring the number
		# an equal number of times
		print "%d times sqrt and **2: %.16f" % (n, r)

def func2(num_of_loops):
	n = num_of_loops
	r = 2.0
	#taking the sqrt of the number n times for example, n = 3
	#sqrt(sqrt(sqrt(r)))
	for i in range(n):
		r = sqrt(r)
		print r
	#squaring the number n times times for example, n = 3
	#(((r)^2)^2)^2)
	#this should essentially 'undo' what the first loop did
	for i in range(n):
		r = r**2
		print r
	#print the result after taking the sqrt and squaring the number
	# an equal number of times
	print "%d times sqrt and **2: %.16f" % (n, r)
	
func1()
#func2(51)

#The seemingly magic number where using an equivalent 
# mathematical operation n times no longer works is 52.
# What actually is happening is a limitation of the computer's
# memory. It can only hold so many points after the decimal
# before it runs out of allowable space for the float type and
# truncates all the points.