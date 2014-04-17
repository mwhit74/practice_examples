"""Store odd numbers in a list"""

#odd_list1.py

n = 50
x = 1
odd_list = []

while x <= n:
	if x%2 != 0:
		odd_list.append(x)
	x += 1
	
print odd_list
		