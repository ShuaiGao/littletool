# -*- coding: utf-8 -*-

import os
import wx
from gui.tool_gui import setting as SettingFrameBase
from validators import email as checkEmail
import logic.libs as libs



# basepath = os.path.dirname(os.getcwd())
basepath = os.getcwd()
resourceDir = basepath + os.sep + "resources" + os.sep

class SettingFrame(SettingFrameBase):
	def __init__(self, HomeFrame, accountData):
		SettingFrameBase.__init__(self, HomeFrame)
		self.home = HomeFrame
		self.m_sendermail.SetValue(accountData.get("sendermail",""))
		self.m_senderpwd.SetValue(accountData.get("senderpwd",""))
		self.m_receiver.SetValue(";".join(accountData.get("receivermaillist",())))

		# img1 = wx.Image(resourceDir + "qqmail_1.png", wx.BITMAP_TYPE_ANY)
		# self.m_help1.SetBitmap(wx.Bitmap(img1))
		# img2 = wx.Image(resourceDir + "qqmail_2.png", wx.BITMAP_TYPE_ANY)
		# self.m_help2.SetBitmap(wx.Bitmap(img2))

		helpImg = wx.Image(resourceDir + "help.png", wx.BITMAP_TYPE_ANY)
		self.m_helpBtn.SetBitmap(wx.Bitmap(helpImg))

	def OnOk( self, event ):
		senderMail = self.m_sendermail.GetValue()
		receiverMailList = []
		if checkEmail(senderMail) is not True:
			self.home.warning("您输入的发件人邮箱格式不正确")
			return

		receiverStr = self.m_receiver.GetValue()
		if len(receiverStr)  > 0:
			receiverMailList = receiverStr.split(";")
			for tmpMail in receiverMailList:
				if tmpMail == "":
					receiverMailList.pop()
					break
				if checkEmail(tmpMail) is not True:
					self.home.warning("您输入的收件人邮箱格式不正确")
					return

		senderPWD = libs.xor_encrypt(self.m_senderpwd.GetValue())
		if not senderPWD or senderPWD == "":
			return

		dataTbl = {"sendermail": senderMail,"receivermaillist": receiverMailList,"senderpwd": senderPWD,"key":libs.getKey()}
		libs.w_json(dataTbl, "account_data", encrypt = True)

		self.home.RefeshData(dataTbl)
		self.home.m_sender.SetValue(senderMail)
		self.home.m_receiver.SetValue(";".join(receiverMailList))
		self.Close(True)


	def OnCancel( self, event ):
		self.Close(True)
	def OnLeave( self, event ):
		self.Close(True)
	def OnHelpButton(self, event):
		os.startfile(resourceDir + "qqmail_help.html")
		
