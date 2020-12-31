import wx
from ui import ui


class App(wx.App):
    def OnInit(self):
        frame = ui.MainWindow(parent=None, title="lankerens")
        frame.Show()
        frame.Center()
        return True

app = App()
app.MainLoop()
