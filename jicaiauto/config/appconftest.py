#! /usr/bin/env python
__author__ = 'Tser'
__email__ = '807447312@qq.com'
__project__ = 'jicaiauto'
__script__ = 'config.py'
__create_time__ = '2020/7/6 14:11'

from appium import webdriver
from jicaiauto.jicaiauto import PUBLIC_VARS
import pytest

app = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot():
    '''
    截图保存为base64，展示到html中
    :return:
    '''
    app.get_screenshot_as_base64()

@pytest.fixture(scope='session', autouse=True)
def mobile():
    global app
    if app is None:
        app = webdriver.Remote('http://127.0.0.1:4723/wd/hub', PUBLIC_VARS['caps'])
    return app