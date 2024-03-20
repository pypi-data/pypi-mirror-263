# -*- coding: utf-8 -*-
"""
@Time : 2024/1/23 15:26
@Author : TJF

"""
from sweetest.globals import g
from sweetest.log import logger


class Windows:
    def __init__(self):
        # 初始化函数，用于创建一个新的 Windows 实例时调用
        self.init()

    def init(self):
        # 初始化方法，用于设置 Windows 实例的初始状态
        # 当前窗口名字，例如：'新版门户首页窗口', 'HOME'
        self.current_window = ''
        # 所有窗口名字--窗口handle映射表，例如:
        # {'新版门户首页窗口': 'CDwindow-3a12c86f-1986-4c02-ba7b-5a0ed94c5963', 'HOME': 'CDwindow-a3f0c44c-d269-4ff0-af38-c31ad70c69e3'}
        self.windows = {}
        # 当前frame名字
        self.frame = 0
        # 所有页面--窗口名字映射表，例如：{'门户首页': '新版门户首页窗口'}
        self.pages = {}
        # 新开窗口标志
        self.new_window_flag = True
        # App context
        self.current_context = 'NATIVE_APP'

    def switch_window(self, page):
        # 切换窗口的方法，接收页面名字作为参数
        # 获取当前所有窗口的句柄
        all_handles = g.driver.window_handles

        # 遍历已知窗口名字映射表中的键
        for key in list(self.windows.keys()):
            # 如果该窗口名字对应的句柄不在当前所有句柄中，说明窗口已关闭
            if self.windows[key] not in all_handles:
                # 重置当前窗口名字和移除已关闭的窗口映射
                self.current_window = ''
                self.windows.pop(key)

        # 如果是新开窗口，且页面在已知页面映射表中
        if self.new_window_flag:
            if page in list(self.pages):
                # 将页面切换为通用
                page = '通用'
                g.current_page = '通用'
            # 关闭新开窗口标志
            self.new_window_flag = False

        # 如果不是通用页面
        if page != '通用':
            # 如果页面不在已知页面映射表中
            if page not in list(self.pages):
                # 清除和当前窗口绑定的页面映射
                for k in list(self.pages):
                    if self.current_window == self.pages[k]:
                        self.pages.pop(k)
                # 将当前窗口绑定到当前页面
                self.pages[page] = self.current_window

            # 如果页面在已知页面映射表中且与当前窗口不一致
            elif self.pages[page] != self.current_window:
                # 如果当前窗口为 HOME，则关闭之
                if self.current_window == 'HOME':
                    g.driver.close()
                    self.windows.pop('HOME')
                # 切换到需要操作的窗口
                tw = self.windows[self.pages[page]]
                logger.info('--- 切换窗口：%s' % repr(tw))
                g.driver.switch_to_window(tw)
                self.current_window = self.pages[page]
                logger.info('--- 当前窗口：%s' % repr(self.current_window))

    def switch_frame(self, frame):
        # 切换框架的方法
        if frame.strip():
            # 如果框架不为空
            frame = [x.strip() for x in frame.split('|')]
            # 将框架按竖线分割并去除首尾空格
            if frame != self.frame:
                # 如果当前框架与目标框架不一致
                if self.frame != 0:
                    # 如果当前框架不为默认框架
                    g.driver.switch_to.default_content()
                    # 切回默认框架
                for f in frame:
                    # 遍历目标框架列表
                    logger.info('--- Frame Value: %s' % repr(f))
                    # 记录日志，输出目标框架值
                    if f.startswith('#'):
                        # 如果框架值以'#'开头
                        f = int(f[1:])
                        # 将'#'后面的部分转为整数
                    elif '#' in f:
                        # 如果框架值包含'#'

                        # 导入相关模块
                        from testcase import elements_format
                        from locator import locating_element
                        element = elements_format('通用', f)[2]
                        # 根据框架值获取元素格式
                        f = locating_element(element)
                        # 根据元素格式定位元素并获取框架值
                    logger.info('--- Switch Frame: %s' % repr(f))
                    # 记录日志，输出切换的框架值
                    g.driver.switch_to.frame(f)
                    # 切换到目标框架
                self.frame = frame
                # 更新当前框架为目标框架
        else:
            # 如果框架为空
            if self.frame != 0:
                # 如果当前框架不为默认框架
                g.driver.switch_to.default_content()
                # 切回默认框架
                self.frame = 0
                # 更新当前框架为默认框架

    def open(self, step):
        # 打开新窗口的方法
        c = self.windows.get(self.current_window, '')
        # 获取当前窗口名称对应的值，如果不存在则为空字符串
        if c:
            # 如果窗口名称对应的值存在
            for k in list(self.pages):
                # 遍历页面列表
                if self.current_window == self.pages[k]:
                    # 如果当前窗口名称对应的值等于页面列表中的某个值
                    self.pages.pop(k)
                    # 移除该页面
            self.windows.pop(self.current_window)
            # 移除窗口名称和对应的值
        handle = g.driver.current_window_handle
        # 获取当前窗口的句柄
        self.register(step, handle)
        # 注册新窗口的名称和句柄

    def register(self, step, handle):
        # 如果有提供新窗口名字，则使用该名字，否则使用默认名字：HOME
        # new_window = step['data'].get('新窗口', 'HOME')
        # 新窗口 变为 标签页名，兼容原有格式
        new_window = 'HOME'
        for k in ('新窗口', '标签页名', 'tabname', '#tab_name'):
            if step['data'].get(k):
                new_window = step['data'].get(k)
        # 已存在同名的窗口，则
        if new_window in self.windows:
            # 1. 清除和当前窗口同名的旧窗口绑定的页面
            for k in list(self.pages):
                if new_window == self.pages[k]:
                    self.pages.pop(k)

            # 2. 切换到同名旧窗口去关闭它
            g.driver.switch_to_window(self.windows[new_window])
            g.driver.close()
            # 3. 并从窗口资源池 g.windows 里剔除
            self.windows.pop(new_window)
        # 然后切回当前窗口
        g.driver.switch_to.window(handle)
        # 再添加到窗口资源池 g.windows
        self.windows[new_window] = handle
        # 把当前窗口名字改为新窗口名称
        self.current_window = new_window
        # 新窗口标志置为是
        self.new_window_flag = True

    def close(self):
        all_handles = g.driver.window_handles
        for handle in all_handles:
            # 切换到每一个窗口,并关闭它
            g.driver.switch_to_window(handle)
            g.driver.close()
            logger.info('--- Close th Windows: %s' % repr(handle))

    def switch_context(self, context):
        if context.strip() == '':
            context = 'NATIVE_APP'
        # logger.info('--- ALL   Contexts:%s' % g.driver.contexts)
        # logger.info('--- Input  Context:%s' % repr(context))
        if context != self.current_context:
            if context == '':
                context = None
            logger.info('--- Switch Context:%s' % repr(context))
            g.driver.switch_to.context(context)
            self.current_context = context


w = Windows()
