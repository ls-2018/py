#!/usr/bin/python
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import sys

smtp_addr = "smtp.163.com"
myemail = "15733101139@163.com"
password = "No15733101139"
print(sys.argv)
recvmail = sys.argv[1]
subject = sys.argv[2]
content = sys.argv[3]

msg = MIMEText(f"{content}", "plain", "utf-8")
msg["Subject"] = Header(subject, "utf-8").encode()
msg["From"] = myemail
msg["To"] = recvmail

try:
    smtp = SMTP_SSL(smtp_addr)
    smtp.login(myemail, password)
    smtp.sendmail(myemail, recvmail.split(","), msg.as_string())
    smtp.quit()
    print("success")
except Exception as e:
    print("fail: " + str(e))
if __name__ == "__main__":
    # python zabbix_sendmail.py 1214972346@qq.com "zabbix disk" "content: disk > 90%"
    pass
