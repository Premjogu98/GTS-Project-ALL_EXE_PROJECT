import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition,
                          wx.Size(350, 230),
                          wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER |
                                                      wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        # ------ Area for the user's controls
        userin = wx.Panel(self, -1, (0, 100), (200, 100))
        userin.SetBackgroundColour(wx.GREEN)
        Text = wx.StaticText(userin, -1, " F-NAME: ", pos=(20, 20))
        Text.SetForegroundColour('white')
        Text.SetBackgroundColour('black')
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        Text.SetFont(font)

        Text1 = wx.StaticText(userin, -1, "L-NAME: ", pos=(23, 47))
        Text1.SetForegroundColour('white')
        Text1.SetBackgroundColour('black')
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        Text1.SetFont(font)
        # ------ Area for user to input text

        userbox1 = wx.TextCtrl(userin, -1, "", pos=(100, 17))
        self.box1 = userbox1

        userbox = wx.TextCtrl(userin, -1, "", pos=(100, 45))
        self.box2 = userbox

        # ------ Button to take text from userbox and place it in textarea
        Press = wx.Button(userin, -1, "Print", (45, 100))

        Press.Bind(wx.EVT_BUTTON, self.inserttext)
        Press.SetBackgroundColour(wx.Colour(255, 0, 0)) # Change Button Color

        Close = wx.Button(userin, -1, "Close", (45, 130))

        Close.Bind(wx.EVT_BUTTON, self.onClose)

    def inserttext(self, event):
        Number_Of_Links2 = self.box1.GetLineText(1)
        print("First Name is: ", Number_Of_Links2)
        Number_Of_Links = self.box2.GetLineText(1)
        print("Last Name is: ", Number_Of_Links)

    def mouseclick(self, event):
        self.box1.Clear()
        self.box2.Clear()

    def onClose(self, event):
        self.Close()


class MainApp(wx.App):
    def OnInit(self):
        myWindow = MainWindow(None, -1, "sberbank")
        myWindow.Show(True)
        self.SetTopWindow(myWindow)
        return (True)


AppStart = MainApp(0)
AppStart.MainLoop()
