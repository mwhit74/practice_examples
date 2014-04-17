#Check Amount Writing: converting numerial amount to text amount
from string import *

num = input("Enter amount: ")

tensCounter = 0
result = ""

while num > 0:
	digit = num % 10
	if digit == 1:
		result = "one"
	elif digit == 2:
		result = "two"
	elif digit == 3:
		result = "three"
	elif digit == 4:
		result = "four"
	elif digit == 5:
		result = "five"
