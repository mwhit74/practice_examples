#Extracting the Square Root
from sys import argv
script, num = argv

g1 = 0
g2 = float(num)
n = 1

target = open("F:\Projects\output1.txt", 'w')

if g1*g1-n <= 0 <= g2*g2-n:
	target.write("move to iteration \n")
	while (abs(g1*g1-n)/n)>0.1:
		target.write("iteration %r \n" % n)
		mid = float((g1+g2))/2
		target.write("mid %r \n" % mid)
		sqrt_mid = mid*mid - n
		target.write("sqrt mid %r \n" % sqrt_mid)
		
		if sqrt_mid <= 0:
			g1 = mid
		if sqrt_mid >= g2:
			g2 = mid
		if sqrt_mid == 0:
			target.write("if mid %r \n" % mid)
			break
		target.write("g2 %r \n" % g2)
		target.write("g1 %r \n\n" % g1)
		n += 1
target.write("Square root of %r is %r" % (num, g1))
target.close()
			