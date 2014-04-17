#E:\Project\Python\Practice_Examples\GUI_Practice

#texteditormenu.pyw

import wx

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title = title, size = (800, 500))
		self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
		self.CreateStatusBar() #a status bar in the bottom of the window
		
		filemenu = wx.Menu()
		helpmenu = wx.Menu()
		
		#filemenu.AppendSeparator()
		filemenu.Append(wx.ID_EXIT, "&Exit", "Terminate the program")
		
		helpmenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
		
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "&File")
		menuBar.Append(helpmenu, "&Help")
		self.SetMenuBar(menuBar)
		self.Show(True)
		
app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()