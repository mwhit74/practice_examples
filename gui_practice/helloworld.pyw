#E:\Project\Python\Practice_Examples\GUI_Practice

#helloworld.pyw

import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
frame.Show()
app.MainLoop()