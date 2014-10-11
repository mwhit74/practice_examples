#checkmenuitem.pyw

import wx

class Example(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		
		self.InitUI()
		
	def InitUI(self):
		#Main menu bar
		menubar = wx.MenuBar()
		#Selections in the Main menu bar
		fileMenu = wx.Menu()
		viewMenu = wx.Menu()
		
		#MenuItems that are under the 'View' menu
		#check toggle for the status bar
		self.shst = viewMenu.Append(wx.ID_ANY, 'Show statusbar',
			'Show Statusbar', kind = wx.ITEM_CHECK)
		#check toggle for the tool bar
		self.shsl = viewMenu.Append(wx.ID_ANY, 'Hide toolbar',
			'Hide Statusbar', kind = wx.ITEM_CHECK)
		
		#setting both the status bar and the tool bar
		# to True (checked)
		viewMenu.Check(self.shst.GetId(), True)
		viewMenu.Check(self.shsl.GetId(), True)
		
		#binding the two View MenuItems to methods in the class
		self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
		self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shsl)
		
		#appending the File and View menu to the Main menu bar
		menubar.Append(fileMenu, '&File')
		menubar.Append(viewMenu, '&View')
		self.SetMenuBar(menubar)
		
		#creating the tool bar
		self.toolbar = self.CreateToolBar()
		#setting an icon to the tool bar
		self.toolbar.AddLabelTool(1, '', wx.Bitmap('texit.png'))
		self.toolbar.Realize()
		
		#creates a status bar at the bottom of the window
		self.statusbar = self.CreateStatusBar()
		#sets default text to status bar
		self.statusbar.SetStatusText('Ready')
		
		#parameters for the main window
		self.SetSize((350, 250))
		self.SetTitle('Check menu item')
		self.Centre(0)
		self.Show(True)
		
	#toggles the status bar on and off based on the
	# checked/not checked status of the MenuItem
	def ToggleStatusBar(self, e):
		if self.shst.IsChecked():
			self.statusbar.Show()
		else:
			self.statusbar.Hide()
	
	#toggles the tool bar on and off based on the 
	# check/not checked status of the MenuItem
	def ToggleToolBar(self, e):
		if self.shsl.IsChecked():
			self.toolbar.Show()
		else:
			self.toolbar.Hide()
			
def main():
	#general execution
	ex = wx.App()
	Example(None)
	ex.MainLoop()
	
if __name__ == '__main__':
	main()
			