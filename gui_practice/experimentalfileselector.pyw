#E:\Project\Python\Practice_Examples\GUI_Practice

#experimentalfileselector.pyw

import wx

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title = title, size = (800, 500))
		self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
		self.CreateStatusBar() #a status bar in the bottom of the window
		
		self.mainWindowMenu()
		
		#Showing the window
		self.Show(True)
	
	def mainWindowMenu(self):
		#Main window menu bar
		menuBar = wx.MenuBar()
		filemenu = wx.Menu()
		helpmenu = wx.Menu()
		
		#Selections from main menu bar
		open = filemenu.Append(wx.ID_OPEN, "&Open", "Select a file to open")
		#save = filemenu.Append(wx.ID_SAVE, "&Save", "Save the file")
		saveas = filemenu.Append(wx.ID_SAVEAS, "&Save As", "Save the file as ...")
		exit = filemenu.Append(wx.ID_EXIT, "&Exit", "Terminate the program")
		
		about = helpmenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
		
		#Binding events to selections
		self.Bind(wx.EVT_MENU, self.OnOpen, open)
		#self.Bind(wx.EVT_MENU, self.OnSave, save)
		self.Bind(wx.EVT_MENU, self.OnSaveAs, saveas)
		self.Bind(wx.EVT_MENU, self.OnExit, exit)
		
		self.Bind(wx.EVT_MENU, self.OnAbout, about)
		
		#Creating main menu bar
		menuBar.Append(filemenu, "&File")
		menuBar.Append(helpmenu, "&Help")
		self.SetMenuBar(menuBar)

	#Filemenu Methods------------------------------------------------
	def OnOpen(self, event):
		openFileDialog = wx.FileDialog(self, "Open", "", "", "Text file (*.txt)|*.txt", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		
		openFileDialog.ShowModal()
		path = openFileDialog.GetPath()
		
		ifile = open(path, 'r')
		contents = ifile.read()
		ifile.close()
		
		self.control.ChangeValue(contents)
		
		openFileDialog.Destroy()
		
	
	#def OnSave(self, event):

		#contents = self.control.GetValue()
		#ofile = open(path, 'w')
		#ofile.write(contents)
		#ofile.close()		
		
	def OnSaveAs(self, event):
		saveAsFileDialog = wx.FileDialog(self, "Save", "", "", "Text files (*.txt)|*.txt", wx.FD_SAVE)
		
		saveAsFileDialog.ShowModal()
		path = saveAsFileDialog.GetPath()
		
		contents = self.control.GetValue()
		ofile = open(path, 'w')
		ofile.write(contents)
		ofile.close()
		
		saveAsFileDialog.Destroy()
		
	def OnExit(self, event):
		self.Close()
		
	#Helpmenu Methods--------------------------------------------------	
	def OnAbout(self, event):
		info = wx.AboutDialogInfo()
		
		info.SetVersion("0.1")
		info.SetCopyright("License: GPL")
		info.SetDescription("Description: Testing the use of wxPython")
		info.SetName("Experimental File Selector")		
		
		wx.AboutBox(info)
		

app = wx.App(False)
frame = MainWindow(None, "Experimental File Selector")
app.MainLoop()