#User_Input_Function.py


class UserQuit(Exception): pass
class InvalidInput(Exception): pass

def input():
	valid = False
	while not valid:
			user_input = raw_input("\nWhat would you like to do? (q=quit, ?=help): \nckdate\nckint\nckitem\nckkeywd\nckpath\nckrange\nckstr\ncktime\nckyorn\n\nINPUT: ")
			ck_user_input = user_input.lower()
			
			if ck_user_input == "?":
				print "This is a helpful message"
				valid = False			
			elif ck_user_input == "q":
				ex = UserQuit("The user has left the building")
				raise ex
			else: 
				valid_input(ck_user_input)
		
		
def valid_input(ck_user_input):
		if ck_user_input == "ckdate":
			print "Check date"
			date = raw_input("Enter a date [m/d/yy]: ")
		elif ck_user_input == "ckint":
			print "Check integer"
			interger = raw_input("Enter a number: ")
			if type(interger) != int:
				invalidInput()
			else:
				print "You input is valid"
		elif ck_user_input == "ckitem":
			print "Check item"
			choice = int(raw_input("Pick an option:\n1. Good day\n2. Bad Day\n3. Good morning\n4. Good night\n\nINPUT: "))
			choose(choice)
		elif ck_user_input == "ckkeywd":
			print "Check keyword"
		elif ck_user_input == "ckpath":
			print "Check path"
		elif ck_user_input == "ckrange":
			print "Check range"
		elif ck_user_input == "ckstr":
			print "Check string"
		elif ck_user_input == "cktime":
			print "Check time"
		elif ck_user_input == "ckyorn":
			print "Check yes or no"
		else:
			invalidInput()
			
def choose(choice):
	if choice == 1:
		print "I am glad you had a good day."
	elif choice == 2:
		print "I hope your day improves."
	elif choice == 3:
		print "Good morning to you too."
	elif choice == 4:
		print "Sleep tight."
	else:
		invalidInput()
		
def invalidInput():
	ex = InvalidInput("Your input did no match any known choices.")
	raise ex
	
def validReport():
	try: 
		input()
	except UserQuit, ex:
		print ex
	except InvalidInput, ex:
		print ex
		validReport()
		
validReport()