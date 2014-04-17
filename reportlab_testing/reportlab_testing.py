"""Testing reportlab module"""

#reportlab_testing.py

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

ifile = open(r'E:\Projects\Python\python_entry.txt', 'r')

def hello(c):
	textobject = c.beginText()
	textobject.setTextOrigin(0.5*inch, 11*inch)
	textobject.setFont("Courier", 8)
	for line in ifile:
		textobject.textLine(line)
	c.drawText(textobject)
c = canvas.Canvas("test.pdf")
hello(c)
c.showPage()
c.save()
