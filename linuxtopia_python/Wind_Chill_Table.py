#Wind Chill Table
#I seriously don't think this equation for wind chill works the values make no sense
from math import *

for v in range(0, 40, 5):
	print("\nv = %r mph" % v)
	print("Actual Temp\tWind Chill")
	for t in range(-10, 40, 5):
		w = int(91.4-(0.474677-0.020425*v+0.303107*sqrt(v))*91.4*t)
		print("%r\t\t%r" % (t, w))
		
		