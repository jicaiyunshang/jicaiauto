# 简介
    jicaiauto是对自动化框架的第三次更新，功能覆盖UI自动化与API自动化
    意在帮助对自动化有更多需求且过多时间写代码的人群，让大家的时间
    花在业务的实现上
## 架构
    -----------------------jicaiauto---------------------
                                  |
    -----------------------------------------------------
    |              |                 |         |         |
    定时任务(后期)  邮件发送（后期）   数据管理   日志内容   测试报告
## 开始使用
#### 了解测试用例目录
    project
    |
    |--__init__.py
    |--conftest.py (复制模板即可)
    |--test_jicaiyunshang_search.py
    |--test_jicaiyunshang_api.py
    |--...

#### 了解关键词
| 序号 | CMD | key |
| :--- | :--- | :--- |
| 1 | 打开网页 | URL |
|2 | 点击 | CLICK |
|3 | 输入 | SENDKEY |
|4 | 刷新页面 | REFRESH |
|5 | 后退 | BACK |
|6 | 关闭 | CLOSE |
|7 | 退出 | QUIT |
|8 | 标签 | CHECKTAG |
|9 | 属性[使用属性值定位] | CHECKATTR |
|10 | URL | CHECKURL |
|11 | 标题 | CHECKTITLE |
|12 | 跳转标签页[序号(1开始)] | SWITCHTOWINDOW |
|13 | Alert弹出框-[确定] | ALERT0 |
|14 | Alert弹出框-[取消] | ALERT1 |
|15 | Alert弹出框-[输入框] | ALERT2 |
|16 | Alert弹出框-[文本] | ALERT3 |
|17 | 停止时间 | WAIT |
|18 | 运行JS脚本 | SCRIPT |
|19 | 添加cookie | COOKIE |
|20 | 滑屏 | SWIPE |
|21 | 截屏 | SCREENSHOT |

#### 准备conftest.py(直接复制即可, 本库自带webconftest与appconftest，可自取)
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from appium import webdriver as app_webdriver
    from jicaiauto.jicaiauto import PUBLIC_VARS
    import pytest
    
    b = None
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
        try:
            return b.get_screenshot_as_base64()
        except Exception as e:
            return app.get_screenshot_as_base64()
        except:
            pass
    
    # web测试(app与web不要同时出现)
    @pytest.fixture(scope='session', autouse=True)
    def browser():
        global b
        if b is None:
            chrome_options = Options()
            b = webdriver.Chrome(chrome_options=chrome_options)
        return b
    
    # app测试(app与web不要同时出现)
    @pytest.fixture(scope='session', autouse=True)
    def mobile():
        global app
        if app is None:
            app = app_webdriver.Remote('http://127.0.0.1:4723/wd/hub', PUBLIC_VARS['caps'])
        return app

#### 编写test_manzhai_search.py(依据自己的业务实现步骤,保证conftest.py同目录)
    from jicaiauto.jicaiauto import web_action, app_action, api_action, PUBLIC_VARS
    import pytest
    
    @pytest.mark.manzhai_web
    def test_manzhai(browser):
        web_action(browser, cmd='打开', loc='', data='https://www.baidu.com')
        web_action(browser, '输入', '//*[@id="kw"]', '郑州慢宅')
        web_action(browser, '点击', '//*[@id="su"]')
        web_action(browser, '标题', '', '', contains_assert='郑州慢宅')
    
    @pytest.mark.manzhai_app
    def test_manzhai(mobile):
        caps={}
        '''
            caps配置信息
            caps['automationName'] = 'uiautomator2'                 #引入uiautomator2，用于定位toast
            caps['platformName'] = 'Android'                        # 设备系统
            caps['platformVersion'] = '5.1'                         # 设备系统版本
            caps['deviceName'] = 'emulator-5555'                    # 设备名称
            caps['app'] = 'D:\\jicai.apk'                       # 测试app(若已安装可不写)
            caps['appPackage'] = 'com.jicai.games'                  # 获取包名
            caps['appActivity'] = 'com.jicai.games.LaunchActivity'  # 获取activity启动
            caps['unicodeKeyboard'] = 'True'                        #支持unicode输入法(支持中文输入)
            caps['resetKeyboard'] = 'True'                          #重置键盘(支持中文输入)
            caps['noReset'] = 'true'                                # 模拟用户非首次启动
        '''
        PUBLIC_VARS['caps']=caps  # 加载app配置信息
        app_action(mobile, '输入', '//*[@id="kw"]', '郑州慢宅')
        app_action(mobile, '点击', '//*[@id="su"]')
        app_action(mobile, '标题', '', '', contains_assert='郑州慢宅')
    
    @pytest.mark.manzhai_api
    def test_manzhai_api_case01():
        api_action(url='https://www.baidu.com/',
                method='get', _re='<title>(.+?)</title>', _re_var='title')
        print(PUBLIC_VARS) # PUBLIC_VARS <Dict> 里面保存着当前接口的提取结果，正则提取，变量名为_re_var的值

##### 备注
- 若APP测试需要获取toast信息可以写一个方法添加到自己的项目中,代码样例如下：
   ```
  def find_toast(self, message, timeout, poll_frequency):
        new_message = f"//*[@text=\'{message}\']"
        element = WebDriverWait(self.driver, timeout, poll_frequency).until(
            EC.presence_of_element_located((By.XPATH, new_message)))
        return element.text
  ```
  
#### 运行脚本
    pytest --html=report.html --self-contained-html
    or
    pytest --html=report.html --self-contained-html -m xiaobai_web
    or
    pytest --html=report.html --self-contained-html -o log_cli=true -o log_cli_level=INFO

## 更新日志
| 版本 | 功能 |
| :---- | :---- |
| 0.0.1 | 实现UI部分功能，待扩展 |
| 0.0.1.2 | 实现api部分功能，待扩展，新增web环境检测cmd下运行jicaicheck |
| 0.0.1.3 | 更新web环境检测 |
| 0.0.1.4 | 更新主方法名web_action,app_action,api_action新增app环境检测 |
| 0.0.1.5 | 更新上一版本的小BUG |
| 0.0.1.6 | 代码调整 |
| 0.0.1.7 | 小更新 |
| 0.0.2.0 | 添加邮件发送，用例排序，chrome提示框禁止等等 |