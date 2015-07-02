#!/usr/bin/env python

import sys
import wx
from guis import KMapGui2, KMapGui3, KMapGui4


if __name__ == '__main__':
    gui_classes = [KMapGui2, KMapGui3, KMapGui4]

    app = wx.App()

    choice_dialog = wx.SingleChoiceDialog(None,
                                          'How many variables?',
                                          'Variables',
                                          ['2 variables', '3 variables', '4 variables'])
    if choice_dialog.ShowModal() == wx.ID_CANCEL:
        sys.exit()

    selection = choice_dialog.GetSelection()
    gui_classes[selection]()
    choice_dialog.Destroy()
    app.MainLoop()
