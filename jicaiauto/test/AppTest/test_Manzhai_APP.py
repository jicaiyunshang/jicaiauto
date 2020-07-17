#! /usr/bin/env python
__author__ = 'Tser'
__email__ = '807447312@qq.com'
__project__ = 'jicaiauto'
__script__ = 'test_UI.py'
__create_time__ = '2020/7/17 2:29'

from jicaiauto.jicaiauto import web_action
from selenium import webdriver
import pytest

browser = None

def setup_module():
    global browser
    if browser is None:
        browser = webdriver.Chrome()

def teardown_module():
    browser.quit()

def test_yewu_a():
    web_action(browser, cmd='打开', loc='', data='https://www.baidu.com')
    web_action(browser, '输入', '//*[@id="kw"]', '小白科技')
    web_action(browser, '点击', '//*[@id="su"]')
    web_action(browser, '停止时间', data=3)
    web_action(browser, '标题', contains_assert='吉彩')

def test_yewu_b():
    web_action(browser, cmd='打开', loc='', data='https://www.baidu.com')
    web_action(browser, '输入', '//*[@id="kw"]', '吉彩云尚')
    web_action(browser, '点击', '//*[@id="su"]')
    web_action(browser, '停止时间', data=3)
    web_action(browser, '标题', contains_assert='吉彩')