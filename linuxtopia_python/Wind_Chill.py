#~~Wind Chill~~

from math import *
import sys
sys.path.append('E:\Projects\Python\Practice_Examples\linuxtopia_python\Class')
from loop_functions import cont

x = True
while x == True:
	wind_speed = int(input("What is the wind speed in mph?: "))
	temp = int(input("What is the temperature in degrees F?: "))
	
	if wind_speed > 40:
		wind_speed = 40
		
	if temp > 0:
		w = 91.4-(0.474677-0.020425*wind_speed+0.303170*sqrt(wind_speed))*(91.4*temp)
		
		answer = "It feels like %d degrees F." % w
		print(answer)
		
		x = cont()

	elif temp < 0:
		w = 91.4+(0.474677-0.020425*wind_speed+0.303170*sqrt(wind_speed))*(91.4*temp)
		
		answer = "It feels like %d degrees F." % w
		print(answer)
		
		x = cont()
	else:
		print("You entered a non-numeric value please try again")
		
		x=1