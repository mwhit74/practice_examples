#Quick Sort; Recursive Sort
a = [45,45,45,45,45,45,45,213,54968,635,78,45,32,854,87,65,4987,65,465,654]
hi = []
lo = []



def QuickSort(array):
	middle = int((len(a))/2)
	ls = 0
	hs = len(a)
	
	for i in a:
		if i <= a[middle]:
			lo.append(i)

		elif i >= a[middle]:
			hi.append(i)

	return lo, a[middle], hi
	
print QuickSort(a)

