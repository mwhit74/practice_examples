#E:\Project\Python\Practice_Examples\GUI_Practice

#simplemenu.py

import wx

class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		
		self.InitUI()
	
	def InitUI(self):
		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')
		menubar.Append(fileMenu, '&File')
		self.SetMenuBar(menubar)
		
		self.Bind(wx.EVT_MENU, self.OnQuit, fitem)
		
		self.SetSize((800,500))
		self.SetTitle('Simple Menu')
		self.Centre()
		self.Show()
		
	def OnQuit(self, e):
		self.Close()
		
def main():
	app = wx.App()
	Example(None)
	app.MainLoop()
	
if __name__ == '__main__':
	main()
