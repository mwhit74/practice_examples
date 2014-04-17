#simple generator practice

def primes():
	seq = range(50)
	for x in seq:
		if x % 2 == 0:
			yield x
	
def print_primes():
	for x in primes():
		print x
		
print_primes()