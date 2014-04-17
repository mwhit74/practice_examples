#E:\Project\Python\Practice_Examples\GUI_Practice

#simpletexteditor.pyw

import wx

class MyFrame(wx.Frame):
	# derive a new class of Frame
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(800, 500))
		self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		self.Show(True)
		
app = wx.App(False)
frame = MyFrame(None, 'Small editor')
app.MainLoop()