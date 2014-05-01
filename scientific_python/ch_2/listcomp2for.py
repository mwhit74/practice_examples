"""Convert nested list comprehensions to nested standard loops"""

#listcomp2for.py

#list comprehension to convert:
# q = [r**2 for r in [10**i for i in range(5)]]

q = []
n = []

for i in range(5):
		n.append(10**i)
for r in n:
	q.append(r**2)
		
j = [r**2 for r in [10**i for i in range(5)]]

print q
print j