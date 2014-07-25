import wx

def main():
	app = wx.App()
	
	frame = wx.Frame(None, -1, "Icon", pos=(350,300))
	frame.SetIcon(wx.Icon('E:/Projects/Python/tipi.ico', wx.BITMAP_TYPE_ICO))
	frame.Center()
	frame.Show()
	app.MainLoop()
	
if __name__ == '__main__':
	main()