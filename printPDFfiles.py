import win32api
import win32print
import time

path = "Y:\\MLW\\"

filename = "Y:\\MLW\\test.txt"

tempPrinter = "Adobe PDF"
currentPrinter = win32print.GetDefaultPrinter()

win32print.SetDefaultPrinter(tempPrinter)
win32api.ShellExecute(0, "print", filename, None, ".", 0)
time.sleep(5)
win32print.SetDefaultPrinter(currentPrinter)