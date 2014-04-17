#Dive Planning Table

c = int(input("What is your surface air consumption rate?: "))
s = int(input("Starting pressure of tank?: "))
f = int(input("Final pressure of tank?: "))

print("Surface air consumption rate: %r" % c)
print("Tank starting pressure: %r" % s)
print("Tank final pressure: %r" % f)
print("Time[min]\tDepth[ft]")

for d in range(30, 120, 10):
	t = int(33*(s-f)/(c*(d+33)))
	print("%r\t\t%r\t" % (t,d))