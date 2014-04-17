#Binary Search

tgt = int(input("Enter a number to search for"))

#target = open("F:\Projects\Python\Experiments\junk.txt", 'w')

seq = sorted([1,2,3,56,87,98,54,12,45,56,98,45,52,85,96,74,85,96,525,54,56,85])
print("seq: %r" % seq)

l = 0
print("l = 0")
h = len(seq)-1
print("h = %r" % h)
m = int((l+h)/2)
print("m = %r" % m)
print("target = 45")
print("(%r, %r)" % (h,m))

while l<h and seq[m] != tgt:
	if tgt < seq[m]:
		m = h
		h -= 1
		print("h: %r" % h)
	elif tgt > seq[m]:
		m = l
		l += 1
		print("l: %r" % l)
	else:
		m = int((l+h)/2)
		print("m: %r" % m)
	print("l += 1 is: %r" % l)
 
if tgt == seq[m]:
	print("Found it: %r" % seq[m])
elif tgt != seq[m]:
	print("Failed: Target doesn't exist in the sequence.")