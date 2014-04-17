"""Compute a mathematical sum - for loop"""

#sum_for.py

s = 0
M = 101

for k in range(1, M):
	s += 1.0/k
	
print s