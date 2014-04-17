#Loan Payments
import sys
sys.path.append("E:\Projects\Python\Practice_Examples\linuxtopia_python\Class")
#made my own module cause I'm lazy
from loop_functions import cont

x = True
while x == True:
	loan_type = input("What type of loan do you have 1, 2, or 3?: ")
	
	#converting input to int() data type for use in equations
	p = int(input("What is the principal due? ($): "))
	#divided by 12 for 12 months in the year; the number of payments made in a year
	r = float(input("What is the yearly interest rate? (%): "))/12
	#multiplied by 12 for 12 months in the year; the number of actualy payments for the loan
	n = int(input("What is the pay back time in years?: "))*12
	
	#standand mortage load
	if loan_type == "1":
		m = p*(r/(1-pow((1+r),-n)))
		
		answer = "%d dollars per month" % m
		print(answer)
		
		#calling module function to loop program based on user input
		x = cont()
	
	#paying at the first of the month
	elif loan_type == "2":
		m = -r*p*pow(r+1, n)/(pow(r+1,n)-1)
		
		answer = "%d dollars per month" % m
		print(answer)
		
		x = cont()
	
	#paying at the end of the month
	elif loan_type == "3":
		m = -r*p*pow(r+1, n)/((pow(r+1,n)-1)*(r+1)) 
		
		answer = "%d dollars per month" % m
		print(answer)
		
		x = cont()
		
	else:
		print("You didn't enter a defined loan type, please try again.")
		
		x = cont()
		
#critrical error with program; if user enters a letter instead of a number the int(input()) will throw a fatal program error. Need to learn error handling.
		