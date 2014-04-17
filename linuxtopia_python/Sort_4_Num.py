#Sort four numbers 

W = int(input("Enter first number: "))
X = int(input("Enter second number: "))
Y = int(input("Enter third number: "))
Z = int(input("Enter fourth number: "))

w,x,y,z = W,X,Y,Z


print("\nw %r x %r y %r z %r \n" % (w,x,y,z))

#target = open("F:\Projects\output2.txt", 'w')
	
n = 0
while not(w<=x<=y<=z):
	print("iterating \n")
	if w > x and w != x:
		w,x,y,z = x,w,y,z
		print("w > x %r %r %r %r \n" % (w,x,y,z))
	if x > y and x != y:
		w,x,y,z = w,y,x,z
		print("x > y %r %r %r %r \n" % (w,x,y,z))
	if y >= z and y != z:
		w,x,y,z = w,x,z,y
		print("y > z %r %r %r %r \n" % (w,x,y,z))
	if w >= z and w != z:
		w,x,y,z = w,x,y,z
		print("z > w %r %r %r %r \n" % (w,x,y,z))
	n += 1
print("final %r %r %r %r \n" % (w,x,y,z))