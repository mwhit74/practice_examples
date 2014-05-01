"""Store data from Pb. 2.7 in a nested list"""

#file for Pb. 2.7 ball_table2.py

#ball_table3.py

v_0 = 1.0
g = 9.81
n = 11.0
t = 0.0
dt = (2*v_0/g)/n

t_list = []
y_list = []

ty1 = []
ty2 = []

while t <= 2*v_0/g:
	t_list.append(t)
	y_list.append(v_0*t + 0.5*g*t**2)
	t += dt

ty1.append(t_list)
ty1.append(y_list)

for t, y in zip(ty1[0], ty1[1]):
	print "{:>5.2f}{:>5.2f}".format(t, y, )
	
for t, y in zip(t_list, y_list):
	ty2.append([t, y])

print '\n\n'
for x in ty2:
	print "{:>5.2f}{:>5.2f}".format(x[0], x[1])
	
