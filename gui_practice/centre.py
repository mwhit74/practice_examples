#E:\Project\Python\Practice_Examples\GUI_Practice

#centre.py

import wx

class Example(wx.Frame):

	def __init__(self, parent, title):
		super(Example, self).__init__(parent, title = title, size = (800,500))
		
		self.Centre()
		self.Show()
		
if __name__ == '__main__':

	app = wx.App()
	Example(None, title = 'Centre')
	app.MainLoop()