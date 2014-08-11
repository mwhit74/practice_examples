import win32api
import win32print
import time

path = "Y:\\MLW\\"

filename = "C:\Users\mwhitten\Desktop\output.txt"

tempPrinter = "Bluebeam PDF"
currentPrinter = win32print.GetDefaultPrinter()

win32print.SetDefaultPrinter(tempPrinter)
print '/d:"%s"' % win32print.GetDefaultPrinter()
try:
	win32api.ShellExecute(0, "print", filename, '/d:LPT1', ".", 0)
except win32api.error, info:
	print info
time.sleep(5)
win32print.SetDefaultPrinter(currentPrinter)