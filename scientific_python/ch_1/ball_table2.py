"""Store number in lists"""

#ball_table2.py

v_0 = 1.0
g = 9.81
n = 11.0
t = 0
dt = (2*v_0/g)/n

t_list = []
y_list = []

while t <= 2*v_0/g:
	t_list.append(t)
	y_list.append(v_0*t + 0.5*g*t**2)
	t += dt

print " t    y"
print "____ ____"
for t, y in zip(t_list, y_list):
	print "%.2f %.2f" % (t, y)