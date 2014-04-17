#Sieve of Eratosthenes

target = open("E:/Projects/Python/Practice_Examples/linuxtopia_python/Ch.18/junk.txt", 'w')

prime = 5000*[True]
p = 2

#print prime[p]
while 2 <= p < 5000:
	while 2 <= p < 5000 and prime[p]:
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
p = 2
target.write( "awesome")
while 2 <= p <5000:
	if prime[p]:
		print p
		target.write("primes: %r\n" % p)
	p += 1