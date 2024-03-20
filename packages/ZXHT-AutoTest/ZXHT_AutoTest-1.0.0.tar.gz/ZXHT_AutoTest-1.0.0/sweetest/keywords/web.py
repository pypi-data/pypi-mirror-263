# -*- coding: utf-8 -*-
"""
@Time : 2024/1/24 13:53
@Author : TJF

"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.select import Select
from time import sleep
import re
from sweetest.globals import g
from sweetest.elements import e
from sweetest.windows import w

from sweetest.locator import locating_element
from sweetest.log import logger
from sweetest.utility import compare, json2dict


class Common():
    @classmethod
    def title(cls, data, output):
        # 记录日志，输出输入的文本数据
        logger.info('DATA:%s' % repr(data['text']))
        # 记录日志，输出当前页面的标题
        logger.info('REAL:%s' % repr(g.driver.title))

        try:
            # 检查标题是否符合预期
            if data['text'].startswith('*'):
                # 如果输入文本以 '*' 开头，则检查剩余部分是否在页面标题中
                assert data['text'][1:] in g.driver.title
            else:
                # 否则，检查输入文本是否与页面标题完全匹配
                assert data['text'] == g.driver.title
        except:
            # 如果检查失败，抛出异常并记录详细信息
            raise Exception(f'Check Failure, DATA:{data["text"]}, REAL:{g.driver.title}')

        # 只能获取到元素标题，将标题信息存储到全局变量中
        for key in output:
            g.var[key] = g.driver.title

        # 返回当前页面的标题
        return g.driver.title

    def current_url(cls, data, output):
        # 记录日志，输出输入的文本数据
        logger.info('DATA:%s' % repr(data['text']))
        # 记录日志，输出当前页面的 URL
        logger.info('REAL:%s' % repr(g.driver.current_url))

        try:
            # 检查 URL 是否符合预期
            if data['text'].startswith('*'):
                # 如果输入文本以 '*' 开头，则检查剩余部分是否在页面 URL 中
                assert data['text'][1:] in g.driver.current_url
            else:
                # 否则，检查输入文本是否与页面 URL 完全匹配
                assert data['text'] == g.driver.current_url
        except:
            # 如果检查失败，抛出异常并记录详细信息
            raise Exception(f'Check Failure, DATA:{data["text"]}, REAL:{g.driver.current_url}')

        # 只能获取到元素的 URL，将 URL 信息存储到全局变量中
        for key in output:
            g.var[key] = g.driver.current_url

        # 返回当前页面的 URL
        return g.driver.current_url


def open(step):
    # 从步骤中获取元素和值
    element = step['element']
    value = e.get(element)[1]

    # 检查是否需要清理缓存，如果是则删除所有cookies
    if step['data'].get('清理缓存', '') or step['data'].get('clear', ''):
        g.driver.delete_all_cookies()

    # 检查打开类型，如果是在新标签页或新窗口中打开，则执行相应的JavaScript代码
    if step['data'].get('#open_type', '') in ('新标签页', 'tab'):
        js = "window.open('%s')" % value
        g.driver.execute_script(js)

        # 获取所有窗口的句柄，检查是否有新窗口打开，并将其添加到窗口列表中
        all_handles = g.driver.window_handles
        for handle in all_handles:
            if handle not in w.windows.values():
                w.register(step, handle)
    else:
        # 如果是在同一浏览器窗口中打开，则检查是否需要打开新浏览器窗口
        if step['data'].get('#open_type', '') in ('新浏览器', 'browser'):
            # 关闭当前窗口，设置新的驱动程序，初始化新的窗口
            w.close()
            g.set_driver()
            w.init()

        # 打开指定的URL
        g.driver.get(value)
        # 执行打开操作，可能会处理新窗口
        w.open(step)

    # 检查是否有需要添加的cookie，如果有则将其转换为字典并添加到浏览器中
    cookie = step['data'].get('cookie', '')
    if cookie:
        g.driver.add_cookie(json2dict(cookie))
        co = g.driver.get_cookie(json2dict(cookie).get('name', ''))
        logger.info(f'cookie is add: {co}')

    # 等待0.5秒，可能是为了确保页面加载完成
    sleep(0.5)


def check(step):
    # 获取步骤中的数据，如果没有则使用期望值
    data = step['data']
    if not data:
        data = step['expected']

    # 获取元素和元素位置
    element = step['element']
    element_location = locating_element(element)

    # 如果元素名称中包含'#'，则提取元素名称（e_name）并获取元素的定位方式（by）
    if '#' in element:
        e_name = element.split('#')[0] + '#'
    else:
        e_name = element
    by = e.elements[e_name]['by']

    # 获取输出值
    output = step['output']
    var = {}

    # 根据定位方式执行不同的操作
    if by in ('title', 'current_url'):
        # 如果是根据标题或当前URL进行检查，则调用Common类中相应的方法
        var[by] = getattr(Common, by)(data, output)

    else:
        # 对每个数据项进行检查
        for key in data:
            # 获取预期结果
            expected = data[key]
            # 切片操作处理
            s = re.findall(r'\[.*?\]', key)
            if s:
                s = s[0]
                key = key.replace(s, '')

            # 获取实际结果
            if key == 'text':
                real = element_location.text
            else:
                real = element_location.get_attribute(key)
            if s:
                real = eval('real' + s)

            # 记录预期和实际结果，然后进行比较
            logger.info('DATA:%s' % repr(expected))
            logger.info('REAL:%s' % repr(real))
            try:
                compare(expected, real)
            except:
                raise Exception(f'Check Failure, DATA:{repr(expected)}, REAL:{repr(real)}')

        # 获取元素的其他属性
        for key in output:
            if output[key] == 'text':
                var[key] = g.var[key] = element_location.text
            elif output[key] in ('text…', 'text...'):
                # 处理特殊情况，如文本以'...'结尾
                if element_location.text.endswith('...'):
                    var[key] = g.var[key] = element_location.text[:-3]
                else:
                    var[key] = g.var[key] = element_location.text
            else:
                var[key] = g.var[key] = element_location.get_attribute(output[key])

    # 如果有变量，则将其添加到步骤的输出中
    if var:
        step['_output'] += '\n||output=' + str(var)

    # 返回元素位置
    return element_location


def notcheck(step):
    # 从步骤中获取数据
    data = step['data']
    # 如果数据不存在，则使用期望的数据
    if not data:
        data = step['expected']

    # 获取元素名称
    element = step['element']

    # 根据元素名称获取元素信息
    # 这里假设有一个叫做 'elements' 的字典，其中包含了元素的定位方式（'by'）等信息
    # 例如：e.elements[element] = {'by': 'title'}
    if e.elements[element]['by'] == 'title':
        # 断言当前页面的标题不等于给定的文本
        assert data['text'] != g.driver.title


def input(step):
    # 从步骤中获取数据
    data = step['data']
    # 获取元素名称
    element = step['element']
    # 根据元素名称获取元素定位方式和位置
    element_location = locating_element(element)

    # 检查是否需要清除文本框内容
    if step['data'].get('清除文本', '') == '否' or step['data'].get('clear', '').lower() == 'no':
        pass
    else:
        # 清除文本框内容
        element_location.clear()

    # 遍历数据中的键值对
    for key in data:
        # 如果键以'text'开头
        if key.startswith('text'):
            # 检查值是否是元组
            if isinstance(data[key], tuple):
                # 如果是元组，将元组解包后输入文本框
                element_location.send_keys(*data[key])
            elif element_location:
                # 如果不是元组，直接输入文本框
                element_location.send_keys(data[key])
        # 如果键为'word'
        if key == 'word':
            # 逐字输入
            for d in data[key]:
                element_location.send_keys(d)

    # 返回输入的元素位置，可能用于后续操作
    return element_location


def click(step):
    # 获取步骤中的元素和数据
    element = step['element']
    data = step['data']

    # 如果元素是字符串
    if isinstance(element, str):
        # 根据元素名称获取元素位置
        element_location = locating_element(element, 'CLICK')

        # 如果找到元素位置
        if element_location:
            try:
                # 尝试点击元素
                element_location.click()
            except ElementClickInterceptedException:
                # 如果元素为不可点击状态，则等待1秒，再重试一次
                sleep(1)
                # 如果存在执行脚本的模式
                if data.get('mode'):
                    # 使用JavaScript执行点击操作
                    g.driver.execute_script("arguments[0].click();", element_location)
                else:
                    # 再次尝试点击元素
                    element_location.click()
    # 如果元素是列表
    elif isinstance(element, list):
        # 遍历元素列表
        for _e in element:
            # 根据每个元素名称获取位置
            element_location = locating_element(_e, 'CLICK')
            try:
                # 尝试点击元素
                element_location.click()
            except ElementClickInterceptedException:
                # 如果元素为不可点击状态，则等待1秒，再重试一次
                sleep(1)
                # 如果存在执行脚本的模式
                if data.get('mode'):
                    # 使用JavaScript执行点击操作
                    g.driver.execute_script("arguments[0].click();", element_location)
                else:
                    # 再次尝试点击元素
                    element_location.click()
            # 等待0.5秒
            sleep(0.5)

    # 在整个操作之后等待0.5秒
    sleep(0.5)

    # 获取步骤中定义的输出属性
    output = step['output']
    for key in output:
        # 根据输出属性类型进行不同的处理
        if output[key] == 'text':
            # 获取元素的文本内容
            g.var[key] = element_location.text
        elif output[key] in ('text…', 'text...'):
            # 如果文本以'...'结尾，去除末尾的'...'
            if element_location.text.endswith('...'):
                g.var[key] = element_location.text[:-3]
            else:
                g.var[key] = element_location.text
        else:
            # 获取元素指定属性的值
            g.var[key] = element_location.get_attribute(output[key])

    # 判断是否打开了新的窗口，并将新窗口添加到所有窗口列表里
    all_handles = g.driver.window_handles
    for handle in all_handles:
        if handle not in w.windows.values():
            # 注册新窗口
            w.register(step, handle)

    # 返回元素位置，可能用于后续操作
    return element_location


# 定义一个名为select的函数，用于选择下拉框中的选项
def select(step):
    # 从步骤中获取数据和元素信息
    data = step['data']
    element = step['element']
    # 使用locating_element函数找到元素的位置
    element_location = locating_element(element)

    # 遍历数据中的键值对
    for key in data:
        # 如果键以'index'开头，使用索引选择选项
        if key.startswith('index'):
            Select(element_location).select_by_index(data[key])
        # 如果键以'value'开头，使用值选择选项
        elif key.startswith('value'):
            Select(element_location).select_by_value(data[key])
        # 如果键以'text'或'visible_text'开头，使用可见文本选择选项
        elif key.startswith('text') or key.startswith('visible_text'):
            Select(element_location).select_by_visible_text(data[key])


# 定义一个名为deselect的函数，用于取消选择下拉框中的选项
def deselect(step):
    # 从步骤中获取数据和元素信息
    data = step['data']
    element = step['element']
    # 使用locating_element函数找到元素的位置
    element_location = locating_element(element)

    # 遍历数据中的键值对
    for key in data:
        # 如果键以'allure-results'开头，取消选择所有选项
        if key.startswith('all'):
            Select(element_location).deselect_all()
        # 如果键以'index'开头，使用索引取消选择选项
        elif key.startswith('index'):
            Select(element_location).deselect_by_index(data[key])
        # 如果键以'value'开头，使用值取消选择选项
        elif key.startswith('value'):
            Select(element_location).deselect_by_value(data[key])
        # 如果键以'text'或'visible_text'开头，使用可见文本取消选择选项
        elif key.startswith('text') or key.startswith('visible_text'):
            Select(element_location).deselect_by_visible_text(data[key])


# 定义一个名为hover的函数，用于将鼠标悬停在元素上
def hover(step):
    # 创建ActionChains对象，用于执行鼠标操作
    actions = ActionChains(g.driver)
    element = step['element']
    # 使用locating_element函数找到元素的位置
    element_location = locating_element(element)
    # 将鼠标移动到元素上
    actions.move_to_element(element_location)
    # 执行鼠标操作
    actions.perform()

    # 返回元素位置
    return element_location


# 定义一个名为context_click的函数，用于执行元素的右键单击操作
def context_click(step):
    # 创建ActionChains对象，用于执行鼠标操作
    actions = ActionChains(g.driver)
    element = step['element']
    # 使用locating_element函数找到元素的位置
    element_location = locating_element(element)
    # 执行右键单击操作
    actions.context_click(element_location)
    # 执行鼠标操作
    actions.perform()

    # 返回元素位置
    return element_location


# 定义一个名为double_click的函数，用于执行元素的双击操作
def double_click(step):
    # 创建ActionChains对象，用于执行鼠标操作
    actions = ActionChains(g.driver)
    element = step['element']
    # 使用locating_element函数找到元素的位置
    element_location = locating_element(element)
    # 执行双击操作
    actions.double_click(element_location)
    # 执行鼠标操作
    actions.perform()

    # 返回元素位置
    return element_location


def drag_and_drop(step):
    # 创建一个ActionChains对象，用于模拟用户的动作
    actions = ActionChains(g.driver)

    # 获取拖拽操作的源元素和目标元素
    element = step['element']
    source = locating_element(element[0])
    target = locating_element(element[1])

    # 执行拖拽操作
    actions.drag_and_drop(source, target)
    actions.perform()
    # 休眠0.5秒，可根据实际情况调整
    # sleep(0.5)


def swipe(step):
    # 创建一个ActionChains对象
    actions = ActionChains(g.driver)

    # 获取滑动操作的元素和滑动数据
    element = step['element']
    data = step['data']

    # 定位滑动操作的元素
    source = locating_element(element)

    # 获取滑动的偏移量
    x = data.get('x', 0)
    y = data.get('y', 0)

    # 执行滑动操作
    actions.drag_and_drop_by_offset(source, x, y)
    actions.perform()
    # 休眠0.5秒，可根据实际情况调整
    # sleep(0.5)


def script(step):
    # 获取执行脚本的元素和脚本内容
    element = step['element']
    value = e.get(element)[1]

    # 使用WebDriver执行JavaScript脚本
    g.driver.execute_script(value)


def message(step):
    # 获取消息框操作的数据
    data = step['data']
    text = data.get('text', '')
    element = step['element']
    value = e.get(element)[1]

    # 根据值的不同执行不同的消息框操作
    if value.lower() in ('确认', 'accept'):
        g.driver.switch_to_alert().accept()
    elif value.lower() in ('取消', '关闭', 'cancel', 'close'):
        g.driver.switch_to_alert().dismiss()
    elif value.lower() in ('输入', 'input'):
        g.driver.switch_to_alert().send_keys(text)
        g.driver.switch_to_alert().accept()
    # 记录日志，切换到Alert窗口
    logger.info('--- 切换到Frame: Alert')
    w.frame = 'Alert'


def upload(step):
    # 导入win32com.client库
    import win32com.client

    # 获取上传操作的数据
    data = step['data']
    element = step['element']
    element_location = locating_element(element)
    file_path = data.get('text', '') or data.get('file', '')

    # 点击上传元素
    element_location.click()
    sleep(3)

    # 使用WScript.Shell对象模拟键盘输入文件路径
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.Sendkeys(file_path)
    sleep(2)

    # 按下Enter键，模拟确认上传
    shell.Sendkeys("{ENTER}")
    sleep(2)


def navigate(step):
    # 获取导航操作的元素
    element = step['element']

    # 根据元素值执行不同的导航操作
    if element.lower() in ('刷新', 'refresh'):
        g.driver.refresh()
    elif element.lower() in ('前进', 'forward'):
        g.driver.forward()
    elif element.lower() in ('后退', 'back'):
        g.driver.back()


def scroll(step):
    # 从步骤中获取数据
    data = step['data']
    # 获取x和y坐标，如果y不存在，则使用text作为y
    x = data.get('x')
    y = data.get('y') or data.get('text')

    # 获取元素
    element = step['element']

    # 如果元素为空字符串
    if element == '':
        # 如果y存在，则滚动到指定的垂直位置
        if y:
            g.driver.execute_script(
                f"document.documentElement.scrollTop={y}")
        # 如果x存在，则滚动到指定的水平位置
        if x:
            g.driver.execute_script(
                f"document.documentElement.scrollLeft={x}")
    else:
        # 获取元素的位置
        element_location = locating_element(element)

        # 如果y存在，则在元素内部滚动到指定的垂直位置
        if y:
            g.driver.execute_script(
                f"arguments[0].scrollTop={y}", element_location)
        # 如果x存在，则在元素内部滚动到指定的水平位置
        if x:
            g.driver.execute_script(
                f"arguments[0].scrollLeft={x}", element_location)

