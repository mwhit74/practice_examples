#Sieve of Eratosthenes utilizing a generator and the yield statement


target = open("E:/Projects/Python/Practice_Examples/linuxtopia_python/Ch.18/junk2.txt", 'w')




#print prime[p]
def prime_nums():
	prime = 5000*[True]
	p = 2
	while 2 <= p < 5000:
		while 2 <= p < 5000 and prime[p]:
			yield p
			#print "p: %d" % p
			#target.write("p: %d\n" % p)
					
			k = p+p
			#print "k: %d" % k
			#target.write("k: %d\n" % k)
					
					
			while k < 5000:
				prime[k] = False
				#print "prime[k]: %r" % prime[k]
				#target.write("prime[k]: %r\n" % prime[k])
							
				k += p
				#print "new k: %d" % k
				#target.write("new k: %d\n" % k)
					
			p += 1
		p += 1
	

for x in prime_nums():
	print x
	target.write("primes: %r\n" % x)
