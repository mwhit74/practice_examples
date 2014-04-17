#Temperature Conversions
import sys
sys.path.append('E:\Projects\Python\Practice_Examples\linuxtopia_python\Class')
from loop_functions import cont


x = True 
#looping through program
while x== True:
	#ask use for type of conversion; either celcius to fahrenheit or fahrenheit to celcuis
	convert_to = input("Convert from Celcuis to Fahrenheit enter 'F' or convert from Fahrenheit to Celcius enter 'C': ")
	
	print(convert_to)
	
	#if users entered 'F' or 'f' program goes into this if statement
	if convert_to == "F" or convert_to == "f":
		#getting degrees celcuis to convert to degress fahrenheit from user
		deg_C = float(input("Enter temperature in degrees Celcius: "))
		
		#conversion equation, celcius to fahrenheit
		F = 32+(212-32)/100*deg_C
		
		#print answer in degrees fahrenheit
		answer = "%d degrees Fahrenheit" % F
		print(answer)
		
		#calling continuation function
		x = cont()
	
	#if users entered 'C' or 'c' program goes into this if statement
	elif convert_to == "C" or convert_to == "c":
		#getting degress fahrenheit to convert to degress celcius from user
		deg_F = int(input("Enter temeprature in degress Fahrenheit: "))
		
		#conversion equation, celcius to fahrenheit
		C = (deg_F -32)*100/(212-32)
		
		#print answer in degrees celcius
		answer = "%d degrees Fahrenheit" % C
		print(answer)
		
		#calling continuation function
		x = cont()
		
	#exception else statement if user didn't enter correct variable program goes into else statement
	else:
		#print error, and direction to fix it
		user = input("You didn't enter an acceptable character please try again.")
		
		#automatically loop back through program
		x = 1


