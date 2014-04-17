# COCOMO How much effort to produce software

r = int(input("Hourly billing rate? ($): "))

print("\nLines of \nSource\t\tEffort\tDuration\tCost\tStaff Size")

for k in range(8, 65, 8):
	#development effort; effort in staff-months
	e = int(2.4*k**1.05)

	#cost in dollars; assuming r $/hr and 152 working hours per staff month
	c = int(e*r*152)

	#duration in calendar months
	d = int(2.5*e**0.38)

	#staffing
	s = int(e/d)
	
	print("%r\t\t%r\t%r\t\t%r\t%r" % (k, e, d, c, s))