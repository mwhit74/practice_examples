#Computing Pi

increment_sum = 0
count = 1
for i in range(1, 5000, 2):	
	if count%2 == 1:
		sign = 1
	else:
		sign = -1
	print(sign)
	increment = sign*1/i
	increment_sum = increment_sum + increment
	pi = 1 + increment_sum
	count += 1 
	
print(pi*2)
