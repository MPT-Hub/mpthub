# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class analysisWindow
###########################################################################


class analysisWindow (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY,
                           title=u"Analysis configuration",
                           pos=wx.DefaultPosition, size=wx.Size(378, 235),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        main_diff_sizer = wx.BoxSizer(wx.VERTICAL)

        main_diff_sizer.Add((0, 0), 1, wx.EXPAND, 5)

        sz_config_1 = wx.BoxSizer(wx.HORIZONTAL)

        sz_config_1.Add((0, 0), 1, wx.EXPAND, 5)

        self.lbl_size = wx.StaticText(
            self, wx.ID_ANY, u"Size",
            wx.DefaultPosition, wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_size.Wrap(-1)

        sz_config_1.Add(
            self.lbl_size, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt_size = wx.TextCtrl(
            self, wx.ID_ANY, u"200",
            wx.DefaultPosition, wx.Size(43, -1), wx.TE_CENTER)
        sz_config_1.Add(self.txt_size, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sz_config_1.Add((0, 0), 1, wx.EXPAND, 5)

        self.lbl_filter = wx.StaticText(
            self, wx.ID_ANY, u"Filter",
            wx.DefaultPosition, wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_filter.Wrap(-1)

        sz_config_1.Add(
            self.lbl_filter, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt_filter = wx.TextCtrl(
            self, wx.ID_ANY, u"590",
            wx.DefaultPosition, wx.Size(43, -1), wx.TE_CENTER)
        sz_config_1.Add(
            self.txt_filter, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sz_config_1.Add((0, 0), 1, wx.EXPAND, 5)

        main_diff_sizer.Add(sz_config_1, 1, wx.EXPAND, 5)

        sz_config_2 = wx.BoxSizer(wx.HORIZONTAL)

        sz_config_2.Add((0, 0), 1, wx.EXPAND, 5)

        self.lbl_fps = wx.StaticText(
            self, wx.ID_ANY, u"FPS",
            wx.DefaultPosition, wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_fps.Wrap(-1)

        sz_config_2.Add(
            self.lbl_fps, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt_fps = wx.TextCtrl(
            self, wx.ID_ANY, u"30",
            wx.DefaultPosition, wx.Size(43, -1), wx.TE_CENTER)
        sz_config_2.Add(
            self.txt_fps, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sz_config_2.Add((0, 0), 1, wx.EXPAND, 5)

        self.lbl_frames = wx.StaticText(
            self, wx.ID_ANY, u"Frames",
            wx.DefaultPosition, wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_frames.Wrap(-1)

        sz_config_2.Add(
            self.lbl_frames, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt_frames = wx.TextCtrl(
            self, wx.ID_ANY, u"606",
            wx.DefaultPosition, wx.Size(43, -1), wx.TE_CENTER)
        sz_config_2.Add(
            self.txt_frames, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sz_config_2.Add((0, 0), 1, wx.EXPAND, 5)

        main_diff_sizer.Add(sz_config_2, 1, wx.EXPAND, 5)

        sz_config_3 = wx.BoxSizer(wx.HORIZONTAL)

        sz_config_3.Add((0, 0), 1, wx.EXPAND, 5)

        self.lbl_width_px = wx.StaticText(
            self, wx.ID_ANY, u"Width (px)",
            wx.DefaultPosition, wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_width_px.Wrap(-1)

        sz_config_3.Add(
            self.lbl_width_px, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt_width_px = wx.TextCtrl(
            self, wx.ID_ANY, u"512",
            wx.DefaultPosition, wx.Size(43, -1), wx.TE_CENTER)
        sz_config_3.Add(
            self.txt_width_px, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sz_config_3.Add((0, 0), 1, wx.EXPAND, 5)

        self.lbl_width_si = wx.StaticText(
            self, wx.ID_ANY, u"Width (um)",
            wx.DefaultPosition, wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_width_si.Wrap(-1)

        sz_config_3.Add(
            self.lbl_width_si, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.txt_width_si = wx.TextCtrl(
            self, wx.ID_ANY, u"160",
            wx.DefaultPosition, wx.Size(43, -1), wx.TE_CENTER)
        sz_config_3.Add(
            self.txt_width_si, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sz_config_3.Add((0, 0), 1, wx.EXPAND, 5)

        main_diff_sizer.Add(sz_config_3, 1, wx.EXPAND, 5)

        main_diff_sizer.Add((0, 0), 1, wx.EXPAND, 5)

        ctrl_button = wx.StdDialogButtonSizer()
        self.ctrl_buttonSave = wx.Button(self, wx.ID_SAVE)
        ctrl_button.AddButton(self.ctrl_buttonSave)
        self.ctrl_buttonCancel = wx.Button(self, wx.ID_CANCEL)
        ctrl_button.AddButton(self.ctrl_buttonCancel)
        ctrl_button.Realize()

        main_diff_sizer.Add(ctrl_button, 1, wx.EXPAND, 5)

        self.SetSizer(main_diff_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.ctrl_buttonSave.Bind(wx.EVT_BUTTON, self.on_save_analysis)
        self.ctrl_buttonCancel.Bind(wx.EVT_BUTTON, self.on_cancel_analysis)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_save_analysis(self, event):
        print("Saving changes...")
        self.Destroy()
        event.Skip()

    def on_cancel_analysis(self, event):
        print("Aborting changes...")
        self.Destroy()
        event.Skip()