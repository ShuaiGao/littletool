# -*- coding: utf-8 -*-

import wx
import os
from logic import tool
class MainApp(wx.App):
	def OnInit(self):
		self.Frame = tool.HomeFrame(None)
		self.Frame.Show()
		return True

if __name__ == '__main__':
	app = MainApp()
	app.MainLoop()
