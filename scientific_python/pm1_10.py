"""Evaluate a Gaussian function"""

#pm1_10.py

from math import sqrt, exp, pi

s = 2.0
x = 1.0
m = 0.0

y = 1/(sqrt(2*pi)*s)*exp(-0.5*((x-m)/s)**2)

print y