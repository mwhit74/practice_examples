#function for continuing or terminating the program
def cont():
	cont = input("To continue press '1' to exit press '0': ")
	if cont == "1":
		x = True
	else:
		x = False
	return x