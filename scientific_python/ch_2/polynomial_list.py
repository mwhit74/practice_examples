"""Compute a polynomial via a product"""

#polynomial_prod.py

root_list = [-1, 1, 2]
#initial value; not needed in mathematical expression but
# need for program execution
p_x = 1 
x = 5

for r in root_list:
	p_x = (x - r)*p_x
	print p_x
	
print p_x