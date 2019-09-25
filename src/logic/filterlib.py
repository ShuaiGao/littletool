# -*- coding: utf-8 -*-

import os
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from validators import email as checkEmail
import logic.exception


orders = [
	"ordersName",
	"hotelName",
	"blankLine",
	"orderNumber", # 订单号
	"orderWay",
	"userName",
	"ordertime",
	"roomType",
	"bedType",
	"price",
	"payType",
	"remark",
	"payState",
	"cancelPolicy",
	"cancelPolicy",
	"affirm",
	"bill",
]

mailbody = '''
<div><br></div><div><div style="font-size: 12px;">{dealtime}</div><div style="font-size: 12px;"><div style="color: rgb(144, 144, 144);">\
<div style="font-size: 14.1176px; color: rgb(0, 0, 0);"><div style="color: rgb(144, 144, 144); font-size: 12px;"><div style="font-size: 14.1176px; \
color: rgb(0, 0, 0);"><table border="1" cellpadding="0" cellspacing="0" class="" style="border-collapse: collapse; border: none;">\
<tbody><tr style="height: 20pt;"><td colspan="5" style="   ;; -webkit-font-smoothing: subpixel-antialiased; font-size: 12px; \
width: 411.05pt; border-top: none; border-right: none; border-left: none; border-image: initial; border-bottom: 1pt solid windowtext; \
background: rgb(208, 206, 206); padding: 0cm 5.4pt; height: 20pt;  " valign="top" width="548"><p align="left" class="">\
<b>今嗨订房单<span lang="EN-US"><o:p></o:p></span></b></p></td></tr><tr style="height: 19pt;">\
<td colspan="2" style="   ;; -webkit-font-smoothing: subpixel-antialiased; font-size: 12px; width: 164.35pt; border-top: none; \
border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt; height: 19pt;  " valign="top" width="219">\
<p class="">\
<b>酒店名称</b><font editorwarp__="1" style="display: inline; background-color: rgba(0, 0, 0, 0); font-weight: bold;">：{hotelName}</font>\
</p></td><td colspan="3" style="   ;; -webkit-font-smoothing: subpixel-antialiased; font-size: 12px; width: 246.65pt; border-top: none; border-right:\
 none; border-left: none; border-image: initial; border-bottom: 1pt solid windowtext; padding: 0cm 5.4pt; height: 19pt;  " valign="top" width="329">\
 <p class=""><b>操作时间：<span lang="EN-US">{dealtime}</span></b></p></td></tr><tr style="height: 20pt;"><td colspan="2" style="   ;;\
  -webkit-font-smoothing: subpixel-antialiased; font-size: 12px; width: 164.35pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext;\
   border-right: 1pt solid windowtext; padding: 0cm 5.4pt; height: 20pt;  " valign="top" width="219"><p class="">\
   <b>本单类型：{newOrder}<span lang="EN-US"><o:p></o:p>\
   </span></b></p></td>\
   <td colspan="3" style="   ;; -webkit-font-smoothing: subpixel-antialiased; font-size: 12px;\
    width: 246.65pt; border-top: none; border-right: none; border-left: none; border-image: initial; border-bottom:\
     1pt solid windowtext; padding: 0cm 5.4pt; height: 20pt;  " valign="top" width="329"><p class=""><b>订单号：{orderId}</b>\
     </p>\
     </td>\
     </tr>\
     <tr style="height: 37.1pt;"><td colspan="5" style="-webkit-font-smoothing: subpixel-antialiased; width: 411.05pt; border-top: none; border-right: none;\
      border-left: none; border-image: initial; border-bottom: 1pt solid windowtext; padding: 0cm 5.4pt; height: 37.1pt;" valign="top" width="548">\
      <p class="" style=""><b style="font-size: 12px;">入住人姓名：</b><span style="font-size: 14.1176px;">{userName}</span></p><p class="" style="">\
      <b style="font-size: 12px;">联系方式：</b><span style="font-size: 14.1176px;">{userTelNumber}转</span><span style="font-size: 14.1176px;">{orderNumber}</span></p>\
      <p class="" style=""><b style="text-align: center; font-size: 14px;">套餐名称：{roomType_roomNameDeal}</b></p>\
      </td></tr><tr style="height: 19pt;"><td style="   ;; -webkit-font-smoothing: subpixel-antialiased; font-size: 12px; width: 82.15pt; border-right:\
       1pt solid windowtext; border-bottom: 1pt solid windowtext; border-left: 1pt solid windowtext; border-image: initial; border-top: none; background: rgb(180, 198, 231); padding: 0cm 5.4pt; height: 19pt;  " valign="top" width="110"><p class=""><b>入离日期</b><o:p></o:p></p></td><td style="   ;; -webkit-font-smoothing: subpixel-antialiased; font-size: 12px; width: 82.15pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; background: rgb(180, 198, 231); padding: 0cm 5.4pt; height: 19pt;  " valign="top" width="110"><p class=""><b>房型床型</b>\
       <o:p></o:p></p></td><td style="   ;; -webkit-font-smoothing: subpixel-antialiased; font-size: 12px; width: 82.15pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; background: rgb(180, 198, 231); padding: 0cm 5.4pt; height: 19pt;  " valign="top" width="110"><p class=""><b>间数</b><o:p></o:p>\
       </p></td><td style="   ;; -webkit-font-smoothing: subpixel-antialiased; font-size: 12px; width: 82.15pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; background: rgb(180, 198, 231); padding: 0cm 5.4pt; height: 19pt;  " valign="top" width="110">\
       <p class=""><b>晚数</b><o:p></o:p></p></td><td style="   ;; -webkit-font-smoothing: subpixel-antialiased; font-size: 12px; width: 82.25pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; background: rgb(180, 198, 231); padding: 0cm 5.4pt; height: 19pt;  " valign="top" width="110"><p class=""><b>结算价</b><o:p></o:p></p></td></tr>\
       <tr style="height: 40.05pt;"><td style="   ;; -webkit-font-smoothing: subpixel-antialiased; font-size: 12px; width: 82.15pt; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-left: 1pt solid windowtext; border-image: initial; border-top: none; padding: 0cm 5.4pt; height: 40.05pt;  " valign="top" width="110">\
       <p align="left" class="" style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;"><font size="2"><a name="_Hlk510262824" style="outline: none; text-decoration-line: underline; color: rgb(44, 74, 119);" target="_blank"><b>{ordertime_daystart}日</b></a><b>至<span lang="EN-US">&nbsp;{ordertime_end}日</span></b>\
       </font></p></td><td style="-webkit-font-smoothing: subpixel-antialiased; width: 82.15pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext;\
        border-right: 1pt solid windowtext; padding: 0cm 5.4pt; height: 40.05pt;" valign="top" width="110"><p class="" style="text-align: center;">{roomType_roomNameDeal}</p>\
        </td><td style="   ;; -webkit-font-smoothing: subpixel-antialiased; font-size: 12px; width: 82.15pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt; height: 40.05pt;  " valign="top" width="110">{roomType_number}</td><td style="   ;; -webkit-font-smoothing: subpixel-antialiased; font-size: 12px; width: 82.15pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt; height: 40.05pt;  " valign="top" width="110">\
        <p class=""><b>{ordertime_2}</b>\
        </p></td><td style="   ;; -webkit-font-smoothing: subpixel-antialiased; font-size: 12px; width: 82.25pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt; height: 40.05pt;  " valign="top" width="110">{sendPrice}</td></tr><tr style="height: 53.5pt;">\
        <td colspan="5" style="-webkit-font-smoothing: subpixel-antialiased; width: 411.05pt; border-top: none; border-right: none; border-left: none; border-image: initial; border-bottom: 1pt solid windowtext; padding: 0cm 5.4pt; height: 53.5pt;" valign="top" width="548"><p class="" style="font-size: 12px;"><b>特殊要求：</b></p><p class="" style="">\
        <b style="font-size: 12px;">备注：</b></p></td></tr><tr style="height: 19pt;"><td colspan="2" style="   ;; -webkit-font-smoothing: subpixel-antialiased; font-size: 12px; width: 164.35pt; border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1pt solid windowtext; background: rgb(208, 206, 206); padding: 0cm 5.4pt; height: 19pt;  " valign="top" width="219"><p class=""><b>操作客服：孙婷婷<span lang="EN-US"><o:p></o:p></span></b></p></td>\
        <td colspan="3" style="   ;; -webkit-font-smoothing: subpixel-antialiased; font-size: 12px; width: 246.65pt; border: none; background: rgb(208, 206, 206); padding: 0cm 5.4pt; height: 19pt;  " valign="top" width="329"><p class="">\
        <b>联系电话：<span lang="EN-US">13011070120</span></b></p><div><b><span lang="EN-US"><br></span></b></div></td></tr></tbody>\
        </table></div></div></div></div></div></div><div><div style="color:#909090;font-family:Arial Narrow;font-size:12px"><br><br><br><br></div>\
        <div style="font-size:14px;font-family:Verdana;color:#000;"><div><br></div>
<div id="qb-sougou-search" style="display: none; opacity: 0; left: 420.658px; top: 76.6217px;">\
<p>搜索</p><p class="last-btn">复制</p><iframe src=""></iframe></div></div></div><div>&nbsp;</div><div><tincludetail></tincludetail></div>
'''


# dirname = r'./result'

# if not os.path.exists(dirname):
	# os.makedirs(dirname)
platname = r""
# resultname = dirname + os.sep + platname


def SaveTmpFile(msg, filename=r"order.txt"):
	f = open(filename, 'w')
	print(msg, file=f )
	f.close()


def filterMsg(orderid, sendPrice = None, priceDiscout = None):
	if not orderid:
		return
	orderfile = open(platname + r'order.txt', 'r')
	# mailfile = open( r'maildata.html', 'w')

	msgTable = {}
	cancel = ""
	for i, line in enumerate(orderfile.readlines()):
		if len(orders) <= i:
			break
		# print(i, len(orders), orders[i])
		if i == 0:
			msgTable[orders[i]] = line.strip()
		elif i == 1:
			msgTable[orders[i]] = line.strip()
		elif i == 2:
			if len(line.strip()) != 0:
				print("识别格式这里是空行，请检查格式是否有变")
		else:
			if orders[i] in msgTable:
				msgTable[orders[i]].append(line.split(":"))
			else:
				msgTable[orders[i]] = line.split(":")

	
	msgTable["dealtime"] = time.strftime("%Y/%m/%d", time.localtime())
	#处理订单号
	msgTable["orderId"] = orderid
	if msgTable["orderNumber"]:
		tmp = msgTable["orderNumber"][1]
		number = re.findall(r"\d+\.?\d*", tmp)
		if "新订" in tmp:
			msgTable["newOrder"] = "新订单"
		msgTable["orderNumber"] = number[0]
	if msgTable["ordertime"]:
		ordertime = msgTable["ordertime"][1].split(" ")
		
		msgTable["ordertime_2"] = ordertime[3].strip()
		msgTable["ordertime_daystart"] = ordertime[0]
		msgTable["ordertime_end"] = ordertime[2]

	if msgTable["roomType"]:
		# print("="*40)
		# print(msgTable["roomType"])
		roomType = msgTable["roomType"][1].split(" ")
		msgTable["roomType_roomName"] = roomType[0].strip()
		# print(msgTable["roomType_roomName"])
		msgTable["roomType_roomNameSimple"] = re.split('[(（]', msgTable["roomType_roomName"])[0]
		# print(msgTable["roomType_roomNameSimple"])
		if msgTable["roomType_roomNameSimple"].endswith("标准间"):
			msgTable["roomType_roomNameDeal"] = msgTable["roomType_roomNameSimple"] + "+双床房"
		else:
			msgTable["roomType_roomNameDeal"] = msgTable["roomType_roomNameSimple"]
		# print(msgTable["roomType_roomNameDeal"])
		msgTable["roomType_number"] = roomType[-1].strip()
		# print(msgTable["roomType_number"])
		# print("="*40)

	if msgTable["remark"]:
		remark = "".join(msgTable["remark"])
		remark = remark.replace(" ", "")
		remark = remark.replace("\t", "")
		number = re.findall(r"请拨打(\d+),", remark)[0]
		rechecknumber = re.findall(r"验证码(\d+)", remark)[0]
		msgTable["userTelNumber"] = number
		msgTable["rechecknumber"] = rechecknumber

	if msgTable["payType"]:
		payType = msgTable["payType"][2]
		payType = payType.replace(" ", "")
		totalPrice = re.findall(r"RMB(\d+\.\d+)", payType)[0]
		msgTable["totalPrice"] = totalPrice
		if sendPrice:
			msgTable["sendPrice"] = sendPrice
		elif priceDiscout:
			msgTable["sendPrice"] = '%.2f' % (float(totalPrice) * priceDiscout)
		else:
			msgTable["sendPrice"] = totalPrice

	if msgTable["userName"]:
		userName = msgTable["userName"][1]
		userName = userName.split(" ")[0].strip()
		msgTable["userName"] = userName
		msgTable["mailName"] = userName + "预定房间"

	# for key, item in msgTable.items():
		# print(key, item)

	msgTable["mailContent"] = mailbody.format(**msgTable)

	# print(mailbody.format(**msgTable), file=mailfile )

	orderfile.close()
	# mailfile.close()
	return msgTable


def SendMailEx(self, mail_host, sender, receiverlist, pwd):
	message = self.CreateMail(receiverlist[0])
	if not message: return
	smtpObj = None
	try:
		if mail_host.endswith("qq.com"):
			smtpObj = smtplib.SMTP()
			smtpObj.connect(mail_host, 25)
		elif mail_host.endswith("jinhailvyou.com"):
			smtpObj = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465) 
		if not smtpObj:
			return self.error("邮箱登录失败，请检查账号密码。")
		smtpObj.login(sender, pwd)
		smtpObj.sendmail(sender, receiverlist, message.as_string())
		self.log("发送邮件成功")
	except smtplib.SMTPException:
		self.log("发送邮件错误")

def CreateMail(msgTable):
	maildata = open( r'maildata.html', 'r')

	message = MIMEText(maildata.read(), "html", 'utf-8')
	message['From'] = Header("MrGao", "utf-8")
	message['To'] = Header("ToTest", "utf-8")

	subject = msgTable.get("mailName","") 
	message["subject"] = Header(subject, "utf-8")
	maildata.close()
	return message

def PreviewSendMail(msgTable):
	message = CreateMail(msgTable)
	return message.as_string()


def SendMail(msgTable, sender, receivers, pwd):
	mail_host = None
	if sender.endswith("qq.com"):
		mail_host = "smtp.qq.com"
	else:
		print("未找到邮箱服务器")
		return

	if checkEmail(sender) is not True:
		print("发件人邮箱错误")
		return
	for tmpMail in receivers:
		if checkEmail(tmpMail) is not True:
			print("收件人邮箱错误")
			return
	if not pwd:
		print("没有密码")
		return

	message = CreateMail(msgTable)
	try:
		smtpObj = smtplib.SMTP()
		smtpObj.connect(mail_host, 25)
		smtpObj.login(mail_user, mail_pass)
		smtpObj.sendmail(sender, receivers, message.as_string())
		print("发送邮件成功")
	except smtplib.SMTPException:
		print("发送邮件错误")

def ProcessSendMail(msgTable):
	message = CreateMail(msgTable)
	mail_user = '597449675@qq.com'
	mail_pass = 'sulppaddgxdtbbdj'
	mail_host = "smtp.qq.com"

	sender = "597449675@qq.com"
	receivers = ["boringmanman@qq.com"]

	try:
		smtpObj = smtplib.SMTP()
		smtpObj.connect(mail_host, 25)
		smtpObj.login(mail_user, mail_pass)
		smtpObj.sendmail(sender, receivers, message.as_string())
		print("发送邮件成功")
	except smtplib.SMTPException:
		print("发送邮件错误")


# if __name__ == '__main__':
# 	msgTable = filterMsg()
	# ProcessSendMail(msgTable)

