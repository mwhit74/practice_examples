#Temperature Converstion Table

print("Celcius\tFahrenheit")

for c in range(-20, 30, 5):
	f = 32+(212-32)/100*c
	print("%r\t%r" % (c,f))