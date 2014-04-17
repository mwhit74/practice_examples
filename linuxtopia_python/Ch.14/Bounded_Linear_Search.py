#Accumulation Unique Values; Bounded Linear Search

a = []


for v in [1,2,3,56,87,98,54,12,45,56,98,45,52,85,96,74,85,96,525,54,56,85]:
	a.append(v)
	i = 0
	
	print("v = ", v)
	x = 0
	while x < len(a):
		print("a = %r" % a[x])
		x += 1
	
	while a[i] != v:
		i += 1
		print("length: %r" % len(a))
		
	print("i: %r" % i)
	print("length 2: %r" % len(a))
	
	length = len(a) - 1
	
	if i == length:
		pass
	elif i != length:
		a.pop()

j = 0
while j < len(a):
	print("Array %r" % a[j])
	j += 1
	
		