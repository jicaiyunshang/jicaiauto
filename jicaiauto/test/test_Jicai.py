#! /usr/bin/env python
__author__ = 'Tser'
__email__ = '807447312@qq.com'
__project__ = 'jicaiauto'
__script__ = 'testJicai.py'
__create_time__ = '2020/7/15 23:34'

from jicaiauto.jicaiauto import web_action
import pytest


@pytest.mark.jicai_web
def test_manzhai_Case1(browser):
    web_action(browser, cmd='打开', loc='', data='https://www.baidu.com')
    web_action(browser, '输入', '//*[@id="kw"]', '吉彩云尚')
    web_action(browser, '点击', '//*[@id="su"]')
    web_action(browser, '停止时间', data=3)
    web_action(browser, '标题', contains_assert='吉彩')

@pytest.mark.jicai_web
def test_manzhai_Case2(browser):
    web_action(browser, cmd='打开', loc='', data='https://www.baidu.com')
    web_action(browser, '输入', '//*[@id="kw"]', '吉彩云尚')
    web_action(browser, '点击', '//*[@id="su"]')
    web_action(browser, '停止时间', data=3)
    web_action(browser, '标题', contains_assert='_吉彩')
    web_action(browser, '关闭')