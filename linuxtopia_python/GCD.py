def input_var():
	p = int(input("First number: "))
	q = int(input("Second number: "))
	return range(p,q)
	
def GCD(a, b):
	while a != b:
		if a < b:
			a,b = b,a
		if b < a:
			a = a - b
			return a

def range(p,q):
	if p == q:
		print(p)
	elif p < q:
		print(GCD(q,p))
	elif p > q:
		print(GCD(p,p-q))

input_var()