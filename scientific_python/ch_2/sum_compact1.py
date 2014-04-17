"""Condense computer a mathematical sum - list comp with range"""
#sum of list of 1/k elements from 1 to M

#sum_compact1.py

import time

M = 10000000

print sum([1.0/k for k in range(1, M + 1, 1)])

print time.clock()