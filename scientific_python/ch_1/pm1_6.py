"""Compute the growth of money in a bank"""

#pm1_6.py

p = 5.0 #interest rate per year in percent
A = 1000.0 #principle investement
n = 3.0 #number of years

total = A*(1 + p/100)**n

print total