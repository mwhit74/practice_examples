#Compute Mean of Tuple

numbers = (1, 2, 3, 4, 6, 23, 45, 65, 42, 12, 89)

count = 0
sum = 0
for i in numbers:
	sum += i
	count += 1

print(sum/count)