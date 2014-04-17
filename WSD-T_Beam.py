
import math

solved = False
As = 0
Acon = 352.0 #inch 
t = 4.0 #inch
d = 21.0 #inch
Es = 29000.0 #ksi
Ec = 33.0*math.pow(150.0, 1.5)*math.sqrt(7000.0)/1000.0 #ksi
n = round(Es/Ec)
fs = 24.0 #ksi
fc = 2.7 #ksi
b_e = 48.0 #inch
M_service = 214.375*12 #kip-in

while not solved:
	As = As + 0.01
	rho = As/(Acon)
	k = (rho*n+1/2*math.pow((t/d),2))/(rho*n+(t/d))
	z = ((3*k*d-2*t)/(2*k*d-t))*(t/3)
	jd = d-z
	j = (6-6*(t/d)+2*math.pow((t/d),2)+math.pow((t/d),3)*(1/(2*rho*n)))/(6-3*(t/d))
	M_t = As*fs*j*d
	#fc_act = 2*M_service/(b_e*t*(d-t/2))
	fc_act = k/(n*(1-k))*fs
	M_c = fc_act*(1-(t/(2*k*d)))*b_e*t*j*d
	if abs(M_t - M_service) < 10 and M_t >= M_service:
		solved = True
		print "t = " + str(t)
		print "d = " + str(d)
		print "t/d = " + str(t/d)
		print "n = " + str(n)
		print "rho = " + str(rho)
		print "jd = " + str(j*d)
		print "M_c = " + str(M_c/12)
		print "M_t = " + str(M_t/12)
		print "k = " + str(k)
		print "kd = " + str(k*d)
		print "As = " + str(As)
		print "fc_act = " + str(fc_act)