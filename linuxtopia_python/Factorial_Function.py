#Factorial Function
import math

def var_input():
	n = int(input("Input number: "))
	return range(n)

def range(n):
	if n == 0:
		print(1)
	if n > 0:
		print(n*math.factorial(n-1))
		
var_input()
