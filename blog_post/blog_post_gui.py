#Blog Post GUI

import wx

class MyMenu(wx.Frame):

	def __init__(self, parent, id, title):
		wx.Frame.__init__(self,parent,id,title,wx.DefaultPosition,wx.Size(600, 400))

		menubar = wx.MenuBar()
		
		fileMenu = wx.Menu()
		editMenu = wx.Menu()
		helpMenu = wx.Menu()
		
		fileMenu.Append(101,'&Open', 'Open a new document')
		quit = wx.MenuItem(fileMenu, 105, '&Close\tCtrl+Q', 'Close the program')
		fileMenu.AppendItem(quit)
		
		menubar.Append(fileMenu, '&File')
		menubar.Append(editMenu, '&Edit')
		menubar.Append(helpMenu, '&Help')
		
		self.SetMenuBar(menubar)
		self.CreateStatusBar()

class MyApp(wx.App):
	def OnInit(self):
		frame = MyMenu(None, -1, 'Blog Post')
		frame.Show()
		return True
		
app = MyApp(False)
app.MainLoop()