# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep 10 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.html

###########################################################################
## Class home
###########################################################################

class home ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"发单小助手  v1.0.0", pos = wx.DefaultPosition, size = wx.Size( 1200,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.file = wx.Menu()
		self.m_setting = wx.MenuItem( self.file, wx.ID_ANY, u"设置"+ u"\t" + u"Ctrl-B", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.Append( self.m_setting )

		self.m_quit = wx.MenuItem( self.file, wx.ID_ANY, u"退出"+ u"\t" + u"Ctrl-Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.Append( self.m_quit )

		self.m_menubar1.Append( self.file, u"文件" )

		self.help = wx.Menu()
		self.m_about = wx.MenuItem( self.help, wx.ID_ANY, u"关于..."+ u"\t" + u"F1", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.Append( self.m_about )

		self.m_menubar1.Append( self.help, u"帮助" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		left = wx.BoxSizer( wx.VERTICAL )

		fgSizer3 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"发单设置" ), wx.VERTICAL )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"发单价格", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer13.Add( self.m_staticText9, 0, wx.ALIGN_LEFT|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_price = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_price, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"元", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer13.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer2.Add( bSizer13, 1, wx.EXPAND, 0 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"订单号   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer12.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_orderid = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		bSizer12.Add( self.m_orderid, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer2.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_dealmsg = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"处理信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_dealmsg, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer2.Add( bSizer15, 1, wx.EXPAND, 5 )


		fgSizer3.Add( sbSizer2, 1, wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"快速计算价格" ), wx.VERTICAL )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText14 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"价格快速计算，输入总价：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer18.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer4.Add( bSizer18, 1, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_totalprice = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_totalprice, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl11 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"元", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl11.Wrap( -1 )

		bSizer16.Add( self.m_textCtrl11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer4.Add( bSizer16, 1, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_discout75 = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"7.5折", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_discout75, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_discout7 = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"7折", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_discout7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer4.Add( bSizer17, 1, wx.EXPAND, 5 )


		fgSizer3.Add( sbSizer4, 1, wx.EXPAND, 5 )


		left.Add( fgSizer3, 0, wx.EXPAND, 5 )

		self.m_sourcemessage = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_WORDWRAP )
		left.Add( self.m_sourcemessage, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer9.Add( left, 2, wx.EXPAND|wx.ALL, 10 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer9.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		right = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer14.SetMinSize( wx.Size( -1,50 ) )
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"邮件信息" ), wx.HORIZONTAL )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )

		self.sender_label = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"发件人   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sender_label.Wrap( -1 )

		fgSizer2.Add( self.sender_label, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_sender = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), wx.TE_READONLY )
		fgSizer2.Add( self.m_sender, 0, wx.ALL|wx.EXPAND, 5 )

		self.receiver_label = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"收件人   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.receiver_label.Wrap( -1 )

		fgSizer2.Add( self.receiver_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_receiver = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_receiver, 0, wx.ALL|wx.EXPAND, 5 )

		self.title_label = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"邮件标题", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title_label.Wrap( -1 )

		fgSizer2.Add( self.title_label, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_mailtitle = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer2.Add( self.m_mailtitle, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer3.Add( fgSizer2, 2, wx.EXPAND, 5 )

		self.sendmail = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"发送邮件", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.sendmail, 1, wx.ALIGN_RIGHT|wx.ALL|wx.ALIGN_BOTTOM, 5 )


		bSizer14.Add( sbSizer3, 1, wx.EXPAND, 5 )


		right.Add( bSizer14, 0, wx.EXPAND, 5 )

		self.m_contenthtml = wx.html.HtmlWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
		self.m_contenthtml.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		right.Add( self.m_contenthtml, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )


		bSizer9.Add( right, 50, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.ALL, 10 )


		bSizer3.Add( bSizer9, 3, 0, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"日志" ), wx.HORIZONTAL )

		sbSizer21.SetMinSize( wx.Size( -1,50 ) )
		self.m_textlog = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2|wx.TE_WORDWRAP )
		self.m_textlog.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

		sbSizer21.Add( self.m_textlog, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( sbSizer21, 1, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.Bind( wx.EVT_MENU, self.OnSetting, id = self.m_setting.GetId() )
		self.Bind( wx.EVT_MENU, self.OnExit, id = self.m_quit.GetId() )
		self.Bind( wx.EVT_MENU, self.OnAbout, id = self.m_about.GetId() )
		self.m_dealmsg.Bind( wx.EVT_BUTTON, self.OnDealMsg )
		self.m_discout75.Bind( wx.EVT_BUTTON, self.OnDiscout75 )
		self.m_discout7.Bind( wx.EVT_BUTTON, self.OnDiscout7 )
		self.sendmail.Bind( wx.EVT_BUTTON, self.OnSendMail )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnSetting( self, event ):
		event.Skip()

	def OnExit( self, event ):
		event.Skip()

	def OnAbout( self, event ):
		event.Skip()

	def OnDealMsg( self, event ):
		event.Skip()

	def OnDiscout75( self, event ):
		event.Skip()

	def OnDiscout7( self, event ):
		event.Skip()

	def OnSendMail( self, event ):
		event.Skip()


###########################################################################
## Class about
###########################################################################

class about ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"About...", pos = wx.DefaultPosition, size = wx.Size( 339,103 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.RESIZE_BORDER|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"小工具由冬瓜提供，如有疑问请致信", wx.DefaultPosition, wx.DefaultSize, wx.ST_ELLIPSIZE_MIDDLE )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer12.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"boringmanman@qq.com", wx.DefaultPosition, wx.DefaultSize, wx.ST_ELLIPSIZE_MIDDLE )
		self.m_staticText5.Wrap( -1 )

		bSizer12.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class setting
###########################################################################

class setting ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"设置", pos = wx.DefaultPosition, size = wx.Size( 300,400 ), style = wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 300,400 ), wx.Size( 300,400 ) )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"登入邮箱设置" ), wx.VERTICAL )

		bSizer101 = wx.BoxSizer( wx.VERTICAL )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer3.Add( ( 0, 0), 13, wx.ALL|wx.EXPAND, 5 )

		self.m_helpBtn = wx.BitmapButton( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 40,40 ), wx.BU_AUTODRAW|0 )

		self.m_helpBtn.SetBitmap( wx.NullBitmap )
		gSizer3.Add( self.m_helpBtn, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 0 )


		bSizer101.Add( gSizer3, 1, wx.EXPAND, 0 )

		self.m_staticText6 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"发件人QQ邮箱", wx.Point( -1,-1 ), wx.Size( 80,-1 ), 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer101.Add( self.m_staticText6, 0, wx.ALL|wx.BOTTOM, 5 )

		self.m_sendermail = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
		bSizer101.Add( self.m_sendermail, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.senderpwd = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"QQ邮箱授权码", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.senderpwd.Wrap( -1 )

		self.senderpwd.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer101.Add( self.senderpwd, 0, wx.ALIGN_LEFT|wx.ALL, 5 )

		self.m_senderpwd = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), wx.TE_PASSWORD )
		bSizer101.Add( self.m_senderpwd, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 5 )

		self.receivermail = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"收件人邮箱", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.receivermail.Wrap( -1 )

		self.receivermail.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer101.Add( self.receivermail, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_receiver = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
		bSizer101.Add( self.m_receiver, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 5 )


		bSizer101.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 0, 5, 0, 0 )


		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_ok = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"确定", wx.DefaultPosition, wx.Size( -1,40 ), 0|wx.TAB_TRAVERSAL )
		gSizer2.Add( self.m_ok, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_cancel = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"取消", wx.Point( -1,-1 ), wx.Size( -1,40 ), 0|wx.TAB_TRAVERSAL )
		gSizer2.Add( self.m_cancel, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer101.Add( gSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 0 )


		sbSizer5.Add( bSizer101, 1, wx.ALIGN_CENTER_HORIZONTAL, 0 )


		self.m_panel1.SetSizer( sbSizer5 )
		self.m_panel1.Layout()
		sbSizer5.Fit( self.m_panel1 )
		bSizer8.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND, 10 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ICONIZE, self.OnIconize )
		self.Bind( wx.EVT_MAXIMIZE, self.OnMaximize )
		self.m_helpBtn.Bind( wx.EVT_BUTTON, self.OnHelpButton )
		self.m_ok.Bind( wx.EVT_BUTTON, self.OnOk )
		self.m_cancel.Bind( wx.EVT_BUTTON, self.OnCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnIconize( self, event ):
		event.Skip()

	def OnMaximize( self, event ):
		event.Skip()

	def OnHelpButton( self, event ):
		event.Skip()

	def OnOk( self, event ):
		event.Skip()

	def OnCancel( self, event ):
		event.Skip()


