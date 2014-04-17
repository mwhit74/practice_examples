#Sort Three Numbers

a = input("First number: ")
b = input("Second number: ")
c = input("Third number: ")


if a < c and b < c:
	x = c
	if a < b:
		y = b
		z = a
	if b < a:
		y = a
		z = b
if c < a and b < a:
	x = a
	if c < b:
		y = b
		z = c
	if b < c:
		y = c
		z = b
if a < b and c < b:
	x = b
	if a < c:
		y = c
		z = a
	if c < a:
		y = a
		z = c


print("x =", x)
print("y =", y)
print("z =", z)