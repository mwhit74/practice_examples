#Standard Deviation
import math

numbers = ( 2, 3, 4, 6, 23, 45, 65, 42, 12, 89)


sum = 0
for i in numbers:
	sum += i
	count += 1

mean = sum/count

d = 0
count_2 = 0
for i in numbers:
	d = i - mean
	s = sum + d**2
	variance = s/(i-1)
	print(math.sqrt(abs(variance)))