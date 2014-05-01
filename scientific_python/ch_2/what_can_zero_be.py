"""Explore what zero can be on a computer"""

#this exercise was completed in live session of python
# on the command prompt

eps = 1.0
while 1.0 != 1.0 + eps:
	print "................", eps
	eps = eps/2.0
print "final eps", eps

#Apparently, somewhere between 1 + 1.11022302463E-16 and 
# 1 + 2.22044604925-16 my computer determined that this was
# close enough to consider equal to 1.0