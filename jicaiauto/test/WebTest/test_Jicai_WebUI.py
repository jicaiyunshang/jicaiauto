#! /usr/bin/env python
__author__ = 'Tser'
__email__ = '807447312@qq.com'
__project__ = 'jicaiauto'
__script__ = 'testJicai.py'
__create_time__ = '2020/7/15 23:34'

from jicaiauto.jicaiauto import web_action
from jicaiauto.utils.jicaiautoEmail import send_email
from jicaiauto.data.GLO_VARS import PUBLIC_VARS
from jicaiauto.config.config import EMAILCONFIG
from os import path
from time import sleep
import pytest

emil = {
    'sender'    : 'jicaiyunshang@163.com',
    'receiver'  : 'jicaiyunshang@qq.com',
    'smtpserver': 'smtp.163.com',
    'smtp_port' : 25,
    'username'  : 'username',
    'password'  : 'password',
    'subject'   : '吉彩云尚自动化测试报告',
    'report'    : 'report.html'
}
PUBLIC_VARS.update(emil)

@pytest.mark.jicai_web
def test_manzhai_Case1(browser):
    web_action(browser, cmd='打开', loc='', data='http://www.baidu.com')
    web_action(browser, '输入', '//*[@id="kw"]', '小白科技')
    web_action(browser, '点击', '//*[@id="su"]')
    web_action(browser, '停止时间', data=3)
    web_action(browser, '标题', contains_assert='小白')

@pytest.mark.jicai_web
def test_manzhai_Case2(browser):
    web_action(browser, cmd='打开', loc='', data='https://www.baidu.com')
    web_action(browser, '输入', '//*[@id="kw"]', '吉彩云尚')
    web_action(browser, '点击', '//*[@id="su"]')
    web_action(browser, '停止时间', data=3)
    web_action(browser, '标题', contains_assert='吉彩-')
    web_action(browser, '关闭')

@pytest.mark.last
def test_last():
    ''' 本次结束测试结束，发送邮件 '''
    print('测试结束了，发个邮件吧')
    sleep(5)
    _emil = EMAILCONFIG()
    _cur_path = path.abspath(path.curdir)
    print(PUBLIC_VARS)
    print(_emil)
    if 'report' in PUBLIC_VARS.keys() and '' != PUBLIC_VARS['report']:
        if path.isfile(_cur_path + '/' + PUBLIC_VARS['report']):
            send_email(_cur_path + '/' + PUBLIC_VARS['report'])
    elif '' != _emil.report:
        if path.isfile(_cur_path + '/' + _emil.report):
            send_email(_cur_path + '/' + _emil.report)

@pytest.mark.run(order=1)
def test_first():
    print('测试开始了')