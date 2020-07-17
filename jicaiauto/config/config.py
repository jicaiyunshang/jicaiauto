#! /usr/bin/env python
__author__ = 'Tser'
__email__ = '807447312@qq.com'
__project__ = 'jicaiauto'
__script__ = 'config.py'
__create_time__ = '2020/7/15 23:18'

from os import path
from jicaiauto.data.GLO_VARS import PUBLIC_VARS

class DBCONFIG:
    if 'dbpath' in PUBLIC_VARS.keys():
        dbapth = PUBLIC_VARS['dbpath']
    else:
        dbpath = path.dirname(path.abspath(__file__)) + '/../data/jicaiauto.db'

class EMAILCONFIG:
    if 'sender' in PUBLIC_VARS.keys():
        sender = PUBLIC_VARS['sender']
    else:
        sender = 'jicaiyunshang@163.com'
    if 'receiver' in PUBLIC_VARS.keys():
        receiver = PUBLIC_VARS['receiver']
    else:
        receiver = 'jicaiyunshang@qq.com'
    if 'smtpserver' in PUBLIC_VARS.keys():
        smtpserver = PUBLIC_VARS['smtpserver']
    else:
        smtpserver = 'smtp.163.com'
    if 'smtp_port' in PUBLIC_VARS.keys():
        smtp_port = PUBLIC_VARS['smtp_port']
    else:
        smtp_port = 25
    if 'username' in PUBLIC_VARS.keys():
        username = PUBLIC_VARS['username']
    else:
        username = 'username'
    if 'password' in PUBLIC_VARS.keys():
        password = PUBLIC_VARS['password']
    else:
        password = 'password'
    if 'subject' in PUBLIC_VARS.keys():
        subject = PUBLIC_VARS['subject']
    else:
        subject = 'xxx自动化测试报告'
    if 'report' in PUBLIC_VARS.keys():
        report = PUBLIC_VARS['report']
    else:
        report = 'report.html'