#border.py

import wx

class Example(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		
		self.InitUI()
		self.Centre()
		self.Show()
		
	def InitUI(self):
		
		panel = wx.Panel(self)
		
		panel.SetBackgroundColour('#4f5049')
		vbox = wx.BoxSizer(wx.VERTICAL)
		
		midPan = wx.Panel(panel)
		midPan.SetBackgroundColour('#ededed')
		
		vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20)
		panel.SetSizer(vbox)
		
if __name__ == "__main__":
	app = wx.App()
	Example(None, title = "Border", size = (260, 280))
	app.MainLoop()