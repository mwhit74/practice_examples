"""Compute the air resistance on a football."""

#pm1_11.py

from math import pi

#Drag equation variables
C_d = 0.2 #drag coefficient
rho = 1.2 #density of medium [kg/m^3]
a = 0.011 #radius of ball [m]
A = pi*a**2 #cross-sectional area [m^2]
V_120 = 120 #velocity [km/h]
V_10 = 10 #velocity [km/h]
conversion = 0.277777778 #km/h to m/s

#Force equation variables
g = 9.81 #acceleration due to gravity [m/s^2]
m = 0.43 #mass [kg]

F_g = m*g 
F_d_120 = 0.5*C_d*rho*A*(V_120*conversion)**2
F_d_10 = 0.5*C_d*rho*A*(V_10*conversion)**2

print "Gravity force %.1f [N]" % F_g
print "Drag force at 120 [km/h] %.1f [N]" % F_d_120
print "Drag force at 10 [km/h] %.1f [N]" % F_d_10
print "Drag force at 120 [km/h] to gravity force ratio %.3f" % (F_d_120/F_g)
print "Drag force at 10 [km/h] to gravity force ratio %.3f" % (F_d_10/F_g)