#Fast Exponentiation

n = int(input("Input base number: "))
p = int(input("Input exponent: "))

def fastExp(n,x=1):
	return n**x

def odd(n, p):
	if p == 0:
		return 1
	elif p%2 == 1:
		return n*fastExp(n, p-1)
	elif p%2 == 0:
		t = fastExp(n, p/2)
		return t**2
		
print(odd(n, p))