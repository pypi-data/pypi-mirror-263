# -*- coding: utf-8 -*-
"""
@Time : 2024/1/22 13:15
@Author : TJF
判断是什么操作系统的什么浏览器
返回plan_data
"""
from datetime import datetime

'''
判断是什么操作系统的什么浏览器
返回plan_data
'''
import time
from selenium import webdriver


def now():
    '''
    返回以可读字符串表示的当地时间
    @return: 返回当前时间
    '''
    t = time.time()
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d-%H_%M_%S")
    # return time.strftime("@%Y-%m-%d-%H_%M_%S.%f", time.localtime(t))
    return formatted_time


def timestamp():
    # js 格式的时间戳
    return int(time.time() * 1000)

    # 定义一个名为 Global 的类
class Global:
    # 初始化方法，在创建类实例时被调用
    def __init__(self):
        # 记录开始时间，使用 now() 函数获取当前时间
        self.start_time = now()
        # 记录开始时间戳，使用 timestamp() 函数获取当前时间戳
        self.start_timestamp = timestamp()
        # 计划名称
        self.plan_name = ''
        # 工作表名称
        self.sheet_name = ''
        # 存储计划数据的字典
        self.plan_data = {}
        # 存储测试套件数据的字典
        self.testsuite_data = {}
        # 计数器，初始值为 1
        self.no = 1
        # 存储驱动信息的属性
        self.driver = ''
        # 存储代码片段信息的字典
        self.snippet = {}
        # 存储用例集信息的字典
        self.caseset = {}

    # 初始化方法，接受 desired_caps 和 server_url 作为参数
    def init(self, desired_caps, server_url):
        # 存储 desired_caps 参数
        self.desired_caps = desired_caps
        # 存储 server_url 参数
        self.server_url = server_url
        # 从 desired_caps 中获取平台名称，默认为空字符串
        self.platform = desired_caps.get('platformName', '')
        # 从 desired_caps 中获取浏览器名称，默认为空字符串
        self.browserName = desired_caps.get('browserName', '')
        # 从 desired_caps 中获取 headless 属性，默认为 False
        self.headless = desired_caps.pop('headless', False)
        # 从 desired_caps 中获取 snapshot 属性，默认为 False
        self.snapshot = desired_caps.pop('snapshot', False)
        # 从 desired_caps 中获取 executable_path 属性，默认为 False
        self.executable_path = desired_caps.pop('executable_path', False)
        # 从 desired_caps 中获取 mobile 属性，默认为 False
        self.mobile = desired_caps.pop('mobile', False)

    # 设置驱动方法
    def set_driver(self):
        # 初始化测试数据字典，包含一个键值对 {'_last_': False}
        self.test_data = {'_last_': False}
        # 初始化变量字典
        self.var = {}
        # 初始化用例组合执行容器列表
        self.casesets = []  # 用例组合执行容器
        # 初始化当前页面名称为 '通用'
        self.current_page = '通用'
        # 初始化数据库字典
        self.db = {}
        # 初始化 HTTP 请求字典
        self.http = {}
        # 初始化 Windows 操作字典
        self.windows = {}
        # 初始化基础 URL 字典
        self.baseurl = {}
        # 初始化动作字典
        self.action = {}
        # 初始化等待次数为 0
        self.wait_times = 0

        # 如果平台为桌面应用
        if self.platform.lower() == 'desktop':
            # 如果浏览器名称为 IE
            if self.browserName.lower() == 'ie':
                # 如果指定了可执行路径，则使用指定路径创建 IE 驱动实例，否则使用默认路径
                if self.executable_path:
                    self.driver = webdriver.Ie(
                        executable_path=self.executable_path)
                else:
                    self.driver = webdriver.Ie()
            # 如果浏览器名称为 Firefox
            elif self.browserName.lower() == 'firefox':
                # 创建 FirefoxProfile 实例
                profile = webdriver.FirefoxProfile()
                # 允许接受不受信任的证书
                profile.accept_untrusted_certs = True

                # 创建 FirefoxOptions 实例
                options = webdriver.FirefoxOptions()
                # 如果配置了 headless 模式
                if self.headless:
                    options.set_headless()
                    # options.add_argument('-headless')
                    options.add_argument('--disable-gpu')
                    options.add_argument("--no-sandbox")
                    options.add_argument('window-size=1920x1080')

                # 如果指定了可执行路径，则使用指定路径创建 Firefox 驱动实例，否则使用默认路径
                if self.executable_path:
                    self.driver = webdriver.Firefox(
                        firefox_profile=profile, firefox_options=options, executable_path=self.executable_path)
                else:
                    self.driver = webdriver.Firefox(
                        firefox_profile=profile, firefox_options=options)

                # 最大化浏览器窗口
                self.driver.maximize_window()

            elif self.browserName.lower() == 'chrome':
                # 判断浏览器类型是否为Chrome
                options = webdriver.ChromeOptions()  # 创建Chrome浏览器选项对象

                if self.mobile == True:  # 如果是移动端模拟
                    if self.headless:  # 如果是无头浏览器
                        options.add_argument('--headless')  # 启用无头模式
                        options.add_argument('--disable-gpu')  # 禁用GPU加速
                        options.add_argument("--no-sandbox")  # 禁用沙盒模式
                        options.add_argument('window-size=375,812')  # 设置浏览器窗口大小，模拟手机分辨率
                        options.add_argument('--user-agent=iphone x')  # 设置用户代理，模拟iPhone X
                    options.add_argument("--start-maximized")  # 启动时最大化窗口
                    options.add_argument('--ignore-certificate-errors')  # 忽略SSL证书错误

                    # 当"--start-maximized"无效时使用的指定浏览器分辨率
                    options.add_argument('window-size=375,812')  # 模拟手机分辨率
                    options.add_argument('--user-agent=iphone x')  # 模拟手机ua

                    prefs = {}
                    prefs["credentials_enable_service"] = False
                    prefs["profile.password_manager_enabled"] = False
                    options.add_experimental_option("prefs", prefs)  # 添加实验性选项，设置浏览器偏好

                    options.add_argument('disable-infobars')  # 禁用信息栏
                    options.add_experimental_option(
                        "excludeSwitches", ['load-extension', 'enable-automation'])  # 实验性选项，排除指定开关

                if self.mobile == False:  # 如果不是移动端
                    if self.headless:  # 如果是无头浏览器
                        options.add_argument('--headless')  # 启用无头模式
                        options.add_argument('--disable-gpu')  # 禁用GPU加速
                        options.add_argument("--no-sandbox")  # 禁用沙盒模式
                        options.add_argument('window-size=1920x1080')  # 设置浏览器窗口大小

                    options.add_argument("--start-maximized")  # 启动时最大化窗口
                    options.add_argument('--ignore-certificate-errors')  # 忽略SSL证书错误

                    # 指定浏览器分辨率，当"--start-maximized"无效时使用
                    prefs = {}
                    prefs["credentials_enable_service"] = False
                    prefs["profile.password_manager_enabled"] = False
                    options.add_experimental_option("prefs", prefs)  # 添加实验性选项，设置浏览器偏好

                    options.add_argument('disable-infobars')  # 禁用信息栏
                    options.add_experimental_option(
                        "excludeSwitches", ['load-extension', 'enable-automation'])  # 实验性选项，排除指定开关

                if self.executable_path:  # 如果提供了可执行文件路径
                    self.driver = webdriver.Chrome(
                        options=options, executable_path=self.executable_path)  # 使用指定路径启动Chrome浏览器
                else:
                    self.driver = webdriver.Chrome(options=options)  # 启动Chrome浏览器


            else:
                raise Exception(
                    'Error: this browser is not supported or mistake name：%s' % self.browserName)
            # 等待元素超时时间
            # self.driver.implicitly_wait(element_wait_timeout)  # seconds
            # 页面刷新超时时间
            # self.driver.set_page_load_timeout(page_flash_timeout)  # seconds

        elif self.platform.lower() == 'ios':  # 如果平台是iOS
            from appium import webdriver as appdriver
            if not self.driver:  # 如果driver尚未初始化
                self.driver = appdriver.Remote(
                    self.server_url, self.desired_caps)  # 使用Appium的Remote方法初始化iOS驱动

        elif self.platform.lower() == 'android':  # 如果平台是Android
            from appium import webdriver as appdriver
            if not self.driver:  # 如果driver尚未初始化
                self.driver = appdriver.Remote(
                    self.server_url, self.desired_caps)  # 使用Appium的Remote方法初始化Android驱动

        elif self.platform.lower() == 'windows':  # 如果平台是Windows
            from pywinauto.application import Application
            from sweetest.keywords import Windows
            self.desired_caps.pop('platformName')  # 移除平台名称键
            backend = self.desired_caps.pop('backend', 'win32')  # 获取后端，默认为win32
            _path = ''
            if self.desired_caps.get('#path'):  # 如果有指定路径
                _path = self.desired_caps.pop('#path')  # 移除路径键
                _backend = self.desired_caps.pop('#backend')  # 移除后端键

            if self.desired_caps.get('cmd_line'):  # 如果有命令行参数
                app = Application(backend).start(**self.desired_caps)  # 使用pywinauto的Application类启动应用
            elif self.desired_caps.get('path'):  # 如果有路径参数
                app = Application(backend).connect(**self.desired_caps)  # 使用pywinauto的Application类连接到应用
            else:
                raise Exception('Error: Windows GUI start/connect args error')  # 抛出异常，表示Windows GUI启动/连接参数错误
            self.windows['default'] = Windows(app)  # 将启动的应用绑定到自定义的Windows类

            if _path:  # 如果有额外指定路径
                _app = Application(_backend).connect(path=_path)  # 使用pywinauto的Application类连接到指定路径的应用
                self.windows['#'] = Windows(_app)  # 将连接的应用绑定到自定义的Windows类

    def plan_end(self):
        self.plan_data['plan'] = self.plan_name  # 将计划名称存储到计划数据中
        self.plan_data['task'] = self.start_timestamp  # 注释掉的代码，似乎并没有被使用
        self.plan_data['start_timestamp'] = self.start_timestamp  # 存储计划开始时间戳
        # print('this is plan_data:',self.plan_data)
        self.plan_data['end_timestamp'] = int(time.time() * 1000)  # 存储计划结束时间戳（当前时间）

        return self.plan_data  # 返回计划数据


g = Global()
