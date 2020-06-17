import wx


def GetText_From_textFile():
    global Website_List
    File_Location = open("D:\\PycharmProjects\\All Python Examples\\Website List.txt", "r")  # Read The Text Form Website List Text File
    Website_List = File_Location.read()

    Website_List = [int(e) if e.isdigit() else e for e in Website_List.split('\n')]
    # print('You Select This website:',Website_Text)


GetText_From_textFile()


class Website:

    def __init__(self, model):

        self.model = model


class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Web Site List", wx.DefaultPosition, wx.Size(650, 130),
                          wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER |
                                                      wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        Text = wx.StaticText(panel, -1, "Select Website To Navigate :", pos=(6, 33))
        # sizer = wx.BoxSizer(wx.VERTICAL)
        self.cb = wx.ComboBox(panel)
        sizer = wx.GridBagSizer(5, 5)
        sizer.Add(self.cb,pos=(1, 12), span=(2, 22),
                  flag=wx.TOP | wx.EXPAND, border=5)

        self.widgetMaker(self.cb, Website_List)
        panel.SetSizer(sizer)
        Press = wx.Button(panel, -1, "Go", (510, 29))
        Press.Bind(wx.EVT_BUTTON, self.insert_text)

        panel.SetBackgroundColour(wx.GREEN)
        Text.SetForegroundColour('white')
        Text.SetBackgroundColour('black')
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        Text.SetFont(font)
        Press.SetBackgroundColour(wx.Colour(255, 0, 0))

    def insert_text(self, event):
        print(self.cb.GetStringSelection())

    def widgetMaker(self, widget, objects):
        """"""
        for obj in objects:
            widget.Append(obj)
        widget.Bind(wx.EVT_COMBOBOX, self.onSelect)

    def onSelect(self, event):
        Selected_Website = self.cb.GetStringSelection()
        print("You selected Website : " + Selected_Website)

# Run the program


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
