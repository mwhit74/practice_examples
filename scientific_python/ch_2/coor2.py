"""Generate equally spaced coordinates with a list comprehension"""

#coor2.py

h = 0.01

coor = [1 + i*h for i in range(1, 101)]

for c in coor:
	print c