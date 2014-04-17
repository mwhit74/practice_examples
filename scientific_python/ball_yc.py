"""A program to calculate at what time, t, a ball will reach
a specific height"""

import math as m

v0 = 5.0
g = 9.81
yc = 0.2

t1 = (v0 - m.sqrt(v0**2 - 2*g*yc))/g
t2 = (v0 + m.sqrt(v0**2 - 2*g*yc))/g

print "At t=%g s and g% s, the hieght is %g m." % (t1, t2, yc)
