"""Condense computer a mathematical sum - sum with xrange"""
#sum of list of 1/k elements from 1 to M

#sum_compact1.py

import time

M = 100000000

print sum(1.0/k for k in xrange(1, M + 1, 1))

print time.clock()