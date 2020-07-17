#! /usr/bin/env python
__author__ = 'Tser'
__email__ = '807447312@qq.com'
__project__ = 'jicaiauto'
__script__ = 'jiaciautoEmail.py'
__create_time__ = '2020/7/15 23:13'

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from jicaiauto.config.config import EMAILCONFIG
from datetime import datetime

def send_email(report=''):
    print('发送邮件开始')
    _emil = EMAILCONFIG()
    if report == '':
        report = _emil.report
    f = open(report, 'rb')
    content = f.read()
    f.close()
    message = MIMEText(content, 'html', 'utf-8')
    message['From'] = _emil.sender
    message['To'] = _emil.receiver
    message['Subject'] = Header(_emil.subject, 'utf-8')
    try:
        smtp = smtplib.SMTP()
        smtp.connect(_emil.smtpserver, _emil.smtp_port)
        smtp.login(_emil.username, _emil.password)
        smtp.sendmail(_emil.sender, _emil.receiver, message.as_string())
        print(f"邮件已与{datetime.now()}发送完成")
        smtp.quit()
    except smtplib.SMTPException:
        print(f"邮件已与{datetime.now()}发送失败")