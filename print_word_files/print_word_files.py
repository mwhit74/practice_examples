from win32com import client
import time

def printPage(fileToPrint,copies):
    print(fileToPrint)
    word = client.Dispatch("Word.Application")
    word.Documents.Open(fileToPrint)
    word.ActivePrinter = "CutePDF Writer"
    x = 1
    for x in range(copies):
        word.ActiveDocument.PrintOut()
    time.sleep(2)
    word.ActiveDocument.Close()
    word.Quit()
	
file = r'E:\Projects\Clints_Bachelor_Party\Final_Invite.docx'
printPage(file, 3)