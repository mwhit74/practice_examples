"""Modifiy previous exercise to store data in lists"""

#Approximate Fahrenheit-Celsius conversion table
#from f2c_approx_table.py

#f2c_approx_list.py


F = 0
dF = 5


list2 = []

while F <= 215:
	list1 = []
	list1.append(F)
	list1.append(5.0/9.0*(F - 32.0))
	list1.append((F - 30.0)/2.0)
	list2.append(list1)
	F = F + dF
	
	
print "----------------"
for con in list2:
	print "%g %.2f %.2f" % (con[0], con[1], con[2])
print "----------------"