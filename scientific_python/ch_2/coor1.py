"""Generate equally spaced coordinates with a for loop"""

#coor1.py

h = 0.01

coor = []

for i in range(1, 101):
	coor.append(1 + i*h)

for c in coor:
	print c