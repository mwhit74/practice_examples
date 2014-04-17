#Greatest Common Denominator
a = int(input("First number: "))
b = int(input("Second number: "))


while a != b:
	if a < b:
		a,b = b,a
	if b < a:
		a = a - b
		print(a)
		

