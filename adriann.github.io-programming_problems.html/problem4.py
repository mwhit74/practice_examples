number = raw_input("Sum numbers between 1 and ?: ")

sum = 0
for x in range(int(number) + 1):
	sum = sum + int(x)
	
print sum