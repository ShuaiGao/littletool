# -*- coding: utf-8 -*-

import sys
import time
import json
import wx
import smtplib
from enum import Enum
import wx.html as html
from email.mime.text import MIMEText
from email.header import Header
from gui import tool_gui as wxUI
from validators import email as checkEmail
import logic.filterlib as mylib
import logic.maillib as maillib
from logic.exception import *
import logic.libs as libs



from .SettingFrame import SettingFrame

FileName_FileContent_Html = "fileContent.html"

class LogLevel(Enum):
	LOG = 0
	WARNING = 1
	ERROR = 2
	
	
def print_param(func):
	def mylog(*args, **kwargs):
		print(func.__module__, func.__name__, *(args[1:]), kwargs)
		return func(*args, **kwargs)
	return mylog

class HomeFrame(wxUI.home):
	def __init__(self, parent):
		wxUI.home.__init__(self, None)
		data = libs.r_json("account_data", encrypt = True) or "{}"
		self.m_data_account = json.loads(data)
		self.m_framAbout = None
		self.m_framSetting = None
		self.m_data_msgTable = {}

		self.InitGUIValue()

		
		self.log("欢迎使用小工具，初始化成功...")

		# self.pannel.Refresh()
	def InitGUIValue(self):
		if self.m_data_account.get("key", "") != libs.getKey():
			self.m_data_account = {}
			return
		self.m_sender.SetValue(self.m_data_account.get("sendermail", ""))
		self.m_receiver.SetValue(";".join(self.m_data_account.get("receivermaillist", ())))

	@print_param
	def log(self, msg):
		self.__log__(msg, LogLevel.LOG)
	@print_param
	def warning(self, msg):
		self.__log__(msg, LogLevel.WARNING)
	@print_param
	def error(self, msg):
		self.__log__(msg, LogLevel.ERROR)

	def __log__(self, msg, logLevel):
		if logLevel == LogLevel.WARNING:
			self.m_textlog.SetDefaultStyle(wx.TextAttr("#DAA520"))
		elif logLevel == LogLevel.ERROR:
			self.m_textlog.SetDefaultStyle(wx.TextAttr("#8B0000"))
		else:
			self.m_textlog.SetDefaultStyle(wx.TextAttr(wx.BLACK))

		self.m_textlog.AppendText(str(time.strftime("[%Y/%m/%d %H-%M-%S] ", time.localtime())) + msg + "\n")
		
	def RefeshData(self, newdata):
		for key, item in newdata.items():
			self.m_data_account[key] = item

	def OnExit( self, event ):
		libs.r_json("account_data", encrypt = True) or "{}"
		self.Close(True)

	def OnClose( self, event ):
		if self.m_framAbout:
			self.m_framAbout.Close()
			self.m_framAbout.Destroy()
		if self.m_framSetting:
			self.m_framSetting.Close()
			self.m_framSetting.Destroy()
			
		self.Destroy()
	# @print_param
	# def OnSetFocus(self, event):
	# 	if self.m_framSetting:
	# 		self.m_framSetting.Show()
	# 		return self.m_framSetting.SetFocus()

	# @print_param
	# def OnShow(self, event):
	# 	if self.m_framSetting:
	# 		self.m_framSetting.Show()
	# 		return self.m_framSetting.SetFocus()

	# 	if self.m_framAbout:
	# 		self.m_framAbout.Show()
	# 		return self.m_framAbout.SetFocus()

	def OnSetting( self, event ):
		if self.m_framSetting:
			self.m_framSetting.Show()
			return self.m_framSetting.SetFocus()
		else:
			self.m_framSetting = SettingFrame(self, self.m_data_account)
			self.m_framSetting.Show()

	def OnAbout( self, event ):
		if self.m_framAbout:
			self.m_framAbout.Show()
			# self.m_framAbout.Maximize()
			return self.m_framAbout.SetFocus()
		else:
			self.m_framAbout = wxUI.about(self)
			self.m_framAbout.Show()
			# self.m_framAbout.Maximize()

	def OnDealMsg( self, event ):
		sendprice = None
		try:
			sendprice = float(self.m_price.GetValue())
			sendprice = '%.2f' % sendprice
		except Exception as e:
			self.warning("发单价格输入错误")
			return

		return sendprice and self.DealMsgEx(sendprice)
		
	def DealMsgEx(self, sendPrice):
		orderid = self.m_orderid.GetValue()
		if not orderid:
			return self.warning("请填写订单号...")
		if orderid.isalnum() is not True: 
			return self.error("订单号填写错误...")

		msg = self.m_sourcemessage.GetValue()
		mylib.SaveTmpFile(msg)

		self.m_data_msgTable = mylib.filterMsg(orderid, sendPrice = sendPrice)
		if self.m_data_msgTable:
			self.m_mailtitle.SetValue(self.m_data_msgTable["mailName"])

		mailContent = self.m_data_msgTable.get("mailContent", None)
		if not mailContent:
			self.warning("数据处理出错")
		self.m_price.SetValue(self.m_data_msgTable["sendPrice"])
		self.m_contenthtml.SetPage(mailContent)

		libs.wFile(mailContent, FileName_FileContent_Html)

		return True

	def OnSendMail( self, event ):
		senderMail, password = self.m_data_account.get("sendermail",None), self.m_data_account.get("senderpwd",None)
		password = libs.xor_decrypt(password)
		receiverMail = self.m_receiver.GetValue()
		senderName = "今嗨旅游"
		mailName = self.m_data_msgTable.get("mailName","") 
		content = self.m_data_msgTable.get("mailContent", None)

		try:
			maillib.CreateAndSendMail(senderMail, senderName, password, receiverMail, receiverMail, content, mailName)
		except ExceptLog as e:
			self.log(str(e))
		except ExceptWarring as e:
			self.warning(str(e))
		except ExceptError as e:
			self.error(str(e))




	def CalcutePrice(self, discout):
		totalPrice = 0
		try:
			totalPriceStr = self.m_totalprice.GetValue()
			totalPrice = float(totalPriceStr)
		except Exception as e:
			self.warning("快速计算价格，总价输入错误 " + totalPriceStr)
			return 0.0
		if not totalPrice or totalPrice == 0:
			self.warning("快速计算价格，请先输入订单总价 " + totalPriceStr)
			return 0.0

		return  totalPrice * discout

	def OnDiscout75( self, event ):
		price = self.CalcutePrice(0.75)
		if price <= 0.1: return
		price = '%.2f' % price

		ret = self.DealMsgEx(price)
		if ret is True:
			self.log("75折发单生成邮件，成功")
		
	def OnDiscout7( self, event ):
		price = self.CalcutePrice(0.7)
		if price <= 0: return

		price = '%.2f' % price
		ret = self.DealMsgEx(price)
		if ret is True:
			self.log("7折发单生成邮件，成功")

