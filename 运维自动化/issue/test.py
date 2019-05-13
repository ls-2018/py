#!/usr/bin/env python
# coding: utf-8 
# @Time   : test.py
# @Author : Derek
# @File   : 2019/1/24 17:27
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_mail(to_list, sub, content):

    mail_host = "smtp.exmail.qq.com"
    mail_user = 'wangshenghui@oldboyedu.com'
    mail_pass = 'Wodehao123'
    msg = MIMEMultipart()
    msg["Subject"] = "这是个带附件的邮件"
    msg['From'] = mail_user  # 发送者

    msg['To'] = ",".join(to_list)  # 接收者

    part = MIMEText("停车坐爱枫林晚,霜叶红于二月花!")
    msg.attach(part)

    att1 = MIMEApplication(open('manage.py', 'rb').read())
    att1.add_header('Content-Disposition','attachment', filename="manage.txt")
    msg.attach(att1)

    # jpg类型附件
    part = MIMEApplication(open('login_bg2.jpg', 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="login.jpg")
    msg.attach(part)

    msg["Subject"] = sub
    msg["From"] = mail_user
    msg["To"] = ",".join(to_list)
    s = smtplib.SMTP(mail_host,25)
    s.login(mail_user, mail_pass)
    s.sendmail(mail_user, to_list, msg.as_string())
    s.close()



# send_mail(['417685417@qq.com','wangshenghui@oldboyedu.com'],'邮件信息','这是一个测试信息')


#
# def r(fuc):
#     def w(*args,**kwargs):
#         print(123)
#         kwargs['c']=123
#         return fuc(*args, **kwargs)
#     return w
#
# @r
# def f1(a='a'):
#     print({'a':123,'b':234})
#
#
# f1()


v=[lambda:x for x in range(10)]
print(v)
print(v[0])