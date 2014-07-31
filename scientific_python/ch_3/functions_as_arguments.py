#functions_as_arguments.py

def diff1(f, x, h = 1E-04):
	r = (f(x+h)-f(x))/h
	return r

def diff2(f, x, h = 1E-04):
	r = (f(x-h) - 2*f(x) + f(x+h))/float(h*h)
	return r
	
def g(t):
	return t**-6
	
if __name__ == "__main__":
	t = 1.2
	d1g = diff1(g, t)
	d2g = diff2(g, t)
	print "g'(%f)=%f" % (t, d1g)
	print "g''(%f)=%f" % (t, d2g)