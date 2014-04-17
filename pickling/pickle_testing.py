import pickle

#test list for pickling
test_list_in = [1, 2, 3, 4, 5, "one", "two", "three" , "four", "five"]

#print test list
print "test_list_in items \n"
for item in test_list_in:
	print item
	
#printing item 4 of test_list_in, should be '5'
print '\n'
print "print test list in item 4"
print test_list_in[4]

#pickling input
#opening file
picklefile_in = open('pickle_test_file.txt', 'r+')
#pickling, dumping pickled list to file
pickle.dump(test_list_in, picklefile_in)
#closing file
picklefile_in.close()


#pickling output
picklefile_out = open('pickle_test_file.txt', 'r+')
#unpickling, loading pickled list from file
test_list_out = pickle.load(picklefile_out)
#closing file
picklefile_out.close()


#printing unpickled list
print "test_list_out items \n"
for item in test_list_out:
	print item
	
#printing item 4 from unpickled list, should be '5' as above
print "\nprinting test list out item 4"
print test_list_out[4]

