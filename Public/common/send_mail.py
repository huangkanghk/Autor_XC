import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import formatdate
import os
class Email(object):

	def __init__(self):

		# self.gmail_user = "kang2011@gmail.com"
		# self.gmail_pw = "12344321a"
		# self.gmail_pop = "pop.gmail.com"
		# self.gmail_smtp = 'smtp.gmail.com'
		# self.gmail_port = 587

		# self.wy_user = "kang.zheng@okchem.com"
		# self.wy_pw = "1123213!"
		# self.wy_pop = "imaphz.qiye.163.com"
		# self.wy_smtp = "smtphz.qiye.163.com"
		# self.wy_port = 994

		self.qq_user = '1119372261@qq.com'
		self.qq_pw = 'jnhnydiirtjagbhi'
		self.qq_pop = 'pop.qq.com'
		self.qq_smtp = 'smtp.qq.com'
		self.qq_port = 25

		# self.okchem_user = 'kang.zheng@okchem.cn'
		# self.okchem_pw = 'xxxx'
		# self.okchem_pop = 'outlook.office365.com'
		# self.okchem_smtp = 'smtp.office365.com'
		# self.okchem_prot = 587

		# self.sh_user = 'kangl2011@sohu.com'
		# self.sh_pw = '123321a'
		# self.sh_pop = "pop3.sohu.com"
		# self.sh_smtp = 'smtp.sohu.com'

	def get_Email(self,From):

		start_index = From.find('<')
		end_index = From.find('>')
		return From[start_index+1 :end_index]

	def email_Attach(self,pass_count,fail_count,skipped_count,attachad,subject = '邮件标题'):
		# with open(file_new,"rb") as f:
		# 	mail_body=f.read()

		smtpserver = self.qq_smtp
		sender = self.qq_user
		to =['huangkang@digitalchina.com']
		body = """\
		<html>
			<head>Hi,all：</head>
			<body>
				<p>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;信创报价系统测试环境自动化监控脚本已执行完毕，概况如下（附件里面是详细报告，需要在浏览器里打开）：<br>
				<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>本次共执行基本功能用例 {toal_count} 条</b><br>
				<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#00BB00">Pass： {pass_count}条</font><br>
				<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#FF0000">Fail： {fail_count}条</font><br>
				<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="C4C400">Skip： {skipped_count}条</font><br>
				<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;详细报告见附件，如有疑问，请随时联系我 Email:huangkang@digitalchina.com Tel：18140548819，谢谢！
				<br/>
				<br/>Thanks，
				<br/>Kang
				</p>
			</body>
		</html>
		"""\
		.format(pass_count=pass_count,fail_count=fail_count,skipped_count=skipped_count,toal_count=pass_count+fail_count+skipped_count)
		receiver=';'.join(to)
		username = self.qq_user
		password = self.qq_pw

		#如名字所示Multipart就是分多个部分
		msg = MIMEMultipart()
		msg["Subject"] = subject
		msg["From"]    = "系统管理员"
		msg["To"]      =receiver
		#msg['Date'] = email.Utils.formatdate( )

		#---这是文字部分---
		part = MIMEText(body,'html','utf-8')
		msg.attach(part)

		#---这是附件部分---
		ofs=open(attachad,'rb')
		basename = os.path.basename(attachad)
		att = MIMEText(ofs.read(),'base64','gb2312')
		att["Content-Type"] = 'application/octet-stream'
		att.add_header('Content-Disposition', 'attachment', filename=basename)
		msg.attach(att)

		#创建实例登录服务器发送邮件
		# smtp = smtplib.SMTP_SSL(smtpserver,port = self.qq_prot,timeout = 360)
		# smtp.connect()


		smtp = smtplib.SMTP(smtpserver,port = self.qq_port,timeout = 360)
		smtp.ehlo()
		smtp.starttls()
		smtp.login(username,password)
		try:
			smtp.sendmail(sender,to,msg.as_string())
		finally:
			smtp.close()



		# smtp = smtplib.SMTP_SSL(smtpserver,port = self.qq_port,timeout = 360)
		# smtp.ehlo()
		# #smtp.starttls()
		# smtp.login(username,password)
		# try:
		# 	smtp.sendmail(sender,to,msg.as_string())
		# finally:
		# 	smtp.close()

	def email_Text(self,attachad,subject = '邮件标题',log="",error=""):

		smtpserver = self.qq_smtp
		sender = self.qq_user
		to =['huangkang@digitalchina.com']
		# to = ['christina.hu@okchem.cn','gordon.peng@okchem.cn','kevin.guo@okchem.cn','neil.wang@okchem.cn','alex.fan@okchem.cn']
		# to.append('joe.li@okchem.cn')
		# to.append('mark.feng@okchem.cn')
		body = """\
		<html>
			<head>Hi,all：</head>
			<body>
				<p>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OKCHEM线上环境自动化监控脚本检查到异常，具体见截图！测试场景和日志如下：<br>
				<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#FF0000">1、{a}</font><br/>
				<br/>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#FF0000">{b}</font><br/>
				<br/>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如有疑问，请随时联系我Tel：18140548819，谢谢！
				<br/>
				<br/>Thanks，
				<br/>huang Kang
				</p>
			</body>
		</html>
		"""\
		.format(a=log,b=error)
		receiver=';'.join(to)
		username = self.qq_user
		password = self.qq_pw

		#如名字所示Multipart就是分多个部分
		msg = MIMEMultipart()
		msg["Subject"] = subject
		msg["From"]    =sender
		msg["To"]      =receiver
		#msg['Date'] = email.Utils.formatdate( )

		#---这是文字部分---
		part = MIMEText(body,'html','utf-8')
		msg.attach(part)

		#---这是附件部分---
		ofs=open(attachad,'rb')
		basename = os.path.basename(attachad)
		att = MIMEText(ofs.read(),'base64','gb2312')
		att["Content-Type"] = 'application/octet-stream'
		att.add_header('Content-Disposition', 'attachment', filename=basename)
		msg.attach(att)

		#创建实例登录服务器发送邮件
		smtp = smtplib.SMTP(smtpserver, port=self.qq_port, timeout=360)
		smtp.ehlo()
		smtp.starttls()
		smtp.login(username, password)
		try:
			smtp.sendmail(sender, to, msg.as_string())
		finally:
			smtp.close()

	# smtp = smtplib.SMTP_SSL(smtpserver,port = self.qq_port,timeout = 360)
		# smtp.ehlo()
		# smtp.starttls() #smtplib.SMTP QQ发送使用
		# smtp.login(username,password)
		# try:
		# 	smtp.sendmail(sender,to,msg.as_string())
		# finally:
		# 	smtp.close()

	def email_Text_All(self,attachad,subject = '邮件标题',log="",error=""):

		smtpserver = self.wy_smtp
		sender = self.wy_user
		to =['kang.zheng@okchem.com']
		# to = ['christina.hu@okchem.com','gordon.peng@okchem.com','kevin.guo@okchem.com','neil.wang@okchem.com','alex.fan@okchem.com']
		# to.append('joe.li@okchem.com')
		# to.append('mark.feng@okchem.com')
		# to.append('kang.zheng@okchem.com')
		# to.append('elena.li@okchem.com')
		body = """\
		<html>
			<head>Hi,all：</head>
			<body>
				<p>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OKCHEM线上环境自动化监控脚本检查到异常，具体见截图！测试场景和日志如下：<br>
				<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#FF0000">1、{a}</font><br/>
				<br/>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#FF0000">{b}</font><br/>
				<br/>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如有疑问，请随时联系我Tel：18627751735，谢谢！
				<br/>
				<br/>Thanks，
				<br/>Kang
				</p>
			</body>
		</html>
		"""\
		.format(a=log,b=error)
		receiver=';'.join(to)
		username = self.wy_user
		password = self.wy_pw

		#如名字所示Multipart就是分多个部分
		msg = MIMEMultipart()
		msg["Subject"] = subject
		msg["From"]    =sender
		msg["To"]      =receiver
		#msg['Date'] = email.Utils.formatdate( )

		#---这是文字部分---
		part = MIMEText(body,'html','utf-8')
		msg.attach(part)

		#---这是附件部分---
		ofs=open(attachad,'rb')
		basename = os.path.basename(attachad)
		att = MIMEText(ofs.read(),'base64','gb2312')
		att["Content-Type"] = 'application/octet-stream'
		att.add_header('Content-Disposition', 'attachment', filename=basename)
		msg.attach(att)

		#创建实例登录服务器发送邮件
		smtp = smtplib.SMTP_SSL(smtpserver,port = self.wy_port,timeout = 360)
		smtp.ehlo()
		#smtp.starttls() #smtplib.SMTP 通过QQ发送邮件使用
		smtp.login(username,password)
		try:
			smtp.sendmail(sender,to,msg.as_string())
		finally:
			smtp.close()

	def email_Text_QQ(self,attachad,subject = '邮件标题',log="",error=""):

		smtpserver = self.qq_smtp
		sender = self.qq_user
		to =['200735517@qq.com']
		# to = ['christina.hu@okchem.cn','gordon.peng@okchem.cn','kevin.guo@okchem.cn','neil.wang@okchem.cn','alex.fan@okchem.cn']
		# to.append('joe.li@okchem.cn')
		# to.append('mark.feng@okchem.cn')
		body = """\
		<html>
			<head>Hi,all：</head>
			<body>
				<p>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OKCHEM线上环境自动化监控脚本检查到异常，具体见截图！测试场景如下：<br>
				<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#FF0000">1、{a}</font><br/>
				<br/>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color="#FF0000">{b}</font><br/>
				<br/>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如有疑问，请随时联系我Tel：18627751735，谢谢！
				<br/>
				<br/>Thanks，
				<br/>Kang
				</p>
			</body>
		</html>
		"""\
		.format(a=log,b=error)
		receiver=';'.join(to)
		username = self.qq_user
		password = self.qq_pw

		#如名字所示Multipart就是分多个部分
		msg = MIMEMultipart()
		msg["Subject"] = subject
		msg["From"]    =sender
		msg["To"]      =receiver
		#msg['Date'] = email.Utils.formatdate( )

		#---这是文字部分---
		part = MIMEText(body,'html','utf-8')
		msg.attach(part)

		#---这是附件部分---
		ofs=open(attachad,'rb')
		basename = os.path.basename(attachad)
		att = MIMEText(ofs.read(),'base64','gb2312')
		att["Content-Type"] = 'application/octet-stream'
		att.add_header('Content-Disposition', 'attachment', filename=basename)
		msg.attach(att)

		#创建实例登录服务器发送邮件
		smtp = smtplib.SMTP(smtpserver,port = self.qq_port,timeout = 360)
		smtp.ehlo()
		smtp.starttls()
		smtp.login(username,password)
		try:
			smtp.sendmail(sender,to,msg.as_string())
		finally:
			smtp.close()

	def newReport(self,testReport):
		lists = os.listdir(testReport)
		lists2 = sorted(lists)  # 获取排序后的测试报告列表
		file_new = os.path.join(testReport, lists2[-1])  # 获得最新的一条html报告
		return file_new