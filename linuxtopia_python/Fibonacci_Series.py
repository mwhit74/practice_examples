#Fibonacci Series
#no fibonacci library downloaded so the script won't run 
import fib

def var_input():
	n = int(input("Input n: "))
	return range(n)
	
def range(n):
	if n == 0:
		print(0)
	elif n == 1:
		print(1)
	elif n > 2:
		fib = fib.fibonacci(n-1) + fib.fibonacci(n-2)
		
var_input()