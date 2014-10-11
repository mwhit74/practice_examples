#sizer.py

import wx

class Example(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		
		self.InitUI()
		self.Centre()
		self.Show()
		
	def InitUI(self):
		
		menubar = wx.MenuBar()
		filem = wx.Menu()
		editm = wx.Menu()
		helpm = wx.Menu()
		
		menubar.Append(filem, "&File")
		menubar.Append(editm, "&Edit")
		menubar.Append(helpm, "&Help")
		self.SetMenuBar(menubar)
		
		wx.TextCtrl(self)
		
if __name__ == "__main__":
	app = wx.App()
	Example(None, title = "", size = (260, 280))
	app.MainLoop()
		
		