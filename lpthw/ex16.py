from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that press CTRL+C"
print "If you would like to proceed press RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now we are going to write 3 lines to that file."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

text = line1 + "\n" + line2 + "\n" + line3 + "\n"

target.write(text)

print "and finally close the file"
target.close()