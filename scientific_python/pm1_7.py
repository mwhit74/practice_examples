"""Find errors in a program"""

#pm1_7.py

x=1; print "sin(%g)=%g" % (x, sin(x))

#The problem is that the sin() function is not defined in the 
#current scope. To fix the problem the sin() function must be defined.
#The easist way to define the sin() function is to import the function
#from the math module.

#from math import sin