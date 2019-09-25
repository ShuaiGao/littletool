# -*- coding: utf-8 -*-


import smtplib
from email.mime.text import MIMEText
from email.header import Header
from validators import email as checkEmail
from logic.exception import *

def CreateAndSendMail(senderMail, senderName, password, receiverName, receiverMail, content, mailName):
	if not content or len(content) < 10:
		raise ExceptWarring("邮件内容异常，请检查")
	if not password:
		raise ExceptWarring("请先填写发件人密码")
	if not senderMail:
		raise ExceptWarring("请先填写发件人邮箱")
	if checkEmail(senderMail) is not True:
		raise ExceptWarring("发件人邮箱填写错误")
	if not receiverMail or checkEmail(receiverMail) is not True or receiverMail.endswith(".com") is not True:
		raise ExceptWarring("收件人邮箱错误，不支持多邮箱邮件，请检查！")


	receiverMaillist = [receiverMail]
	mail_host = None
	if senderMail.endswith("@qq.com"):
		mail_host = "smtp.qq.com"
	elif senderMail.endswith("@jinhailvyou.com"):
		mail_host = "smtp.exmail.qq.com"
	else:
		raise ExceptWarring("未找到邮箱服务器，当前只支持QQ邮箱发单")

	for tmpMail in receiverMaillist:
		if checkEmail(tmpMail) is not True:
			raise ExceptWarring("收件人邮箱错误 " + tmpMail)

	message = MIMEText(content, "html", 'utf-8')
	message['From'] = Header(senderName, "utf-8")
	message['To'] = Header(receiverName, "utf-8")
	message["subject"] = Header(mailName, "utf-8")

	smtpObj = None
	try:
		if mail_host.endswith("qq.com"):
			smtpObj = smtplib.SMTP()
			smtpObj.connect(mail_host, 25)
		elif mail_host.endswith("jinhailvyou.com"):
			smtpObj = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465) 
		if not smtpObj:
			raise ExceptError("邮箱登录失败，请检查账号密码。")
		smtpObj.login(senderMail, password)
		smtpObj.sendmail(senderMail, receiverMaillist, message.as_string())
		raise Exceptlog("发送邮件成功")
	except smtplib.SMTPException as e:
		raise ExceptError("发送邮件错误 " + str(e)) 
		
	return True