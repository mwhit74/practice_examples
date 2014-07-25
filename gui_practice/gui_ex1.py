import wx

app = wx.App()

window = wx.Frame(None, 20,'Blog Post', style= wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
window.Show(True)

app.MainLoop()