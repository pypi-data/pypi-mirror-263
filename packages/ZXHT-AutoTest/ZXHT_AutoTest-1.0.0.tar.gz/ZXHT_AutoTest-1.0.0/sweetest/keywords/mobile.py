# -*- coding: utf-8 -*-
"""
@Time : 2024/1/24 14:50
@Author : TJF

"""
from time import sleep

import re
from sweetest.globals import g
from sweetest.elements import e
from sweetest.windows import w
from sweetest.locator import   locating_element
from sweetest.log import logger
from sweetest.utility import compare
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementClickInterceptedException


class Common():
    @classmethod
    def title(cls, data, output):
        # 记录日志，显示输入数据的文本
        logger.info('DATA:%s' % repr(data['text']))
        # 记录日志，显示实际的页面标题
        logger.info('REAL:%s' % repr(g.driver.title))
        # 如果数据文本以 '*' 开头，断言去除 '*' 后的文本在页面标题中，否则断言数据文本与页面标题相等
        if data['text'].startswith('*'):
            assert data['text'][1:] in g.driver.title
        else:
            assert data['text'] == g.driver.title
        # 将页面标题赋值给输出变量
        for key in output:
            g.var[key] = g.driver.title

    @classmethod
    def current_url(cls, data, output):
        # 记录日志，显示输入数据的文本
        logger.info('DATA:%s' % repr(data['text']))
        # 记录日志，显示实际的当前页面 URL
        logger.info('REAL:%s' % repr(g.driver.current_url))
        # 如果数据文本以 '*' 开头，断言去除 '*' 后的文本在当前页面 URL 中，否则断言数据文本与当前页面 URL 相等
        if data['text'].startswith('*'):
            assert data['text'][1:] in g.driver.current_url
        else:
            assert data['text'] == g.driver.current_url
        # 将当前页面 URL 赋值给输出变量
        for key in output:
            g.var[key] = g.driver.current_url

    def check(step):
        # 获取步骤中的数据，如果没有则获取预期结果
        data = step['data']
        if not data:
            data = step['expected']

        # 获取元素信息和位置
        element = step['element']
        element_location = locating_element(element)
        # 如果元素名中包含 '#'，则获取元素名前面的部分，并在之后添加 '#'
        if '#' in element:
            e_name = element.split('#')[0] + '#'
        else:
            e_name = element
        # 获取元素的定位方式
        by = e.elements[e_name]['by']
        # 获取输出变量
        output = step['output']

        # 如果定位方式为 'title' 或 'current_url'，则调用相应的类方法
        if by in ('title', 'current_url'):
            getattr(Common, by)(data, output)
        else:
            for key in data:
                # 获取预期结果
                expected = data[key]
                # 处理切片操作
                s = re.findall(r'\[.*?\]', key)
                if s:
                    s = s[0]
                    key = key.replace(s, '')

                # 如果键为 'text'，则获取元素的文本值，否则获取元素的属性值
                if key == 'text':
                    real = element_location.text
                else:
                    real = element_location.get_attribute(key)
                # 如果存在切片操作，则执行切片操作
                if s:
                    real = eval('real' + s)

                # 记录日志，显示预期结果和实际结果
                logger.info('DATA:%s' % repr(expected))
                logger.info('REAL:%s' % repr(real))
                # 调用比较函数比较预期结果和实际结果
                compare(expected, real)
        # 获取元素其他属性
        # 遍历output字典中的键值对
        for key in output:
            # 检查output[key]的值是否为'text'
            if output[key] == 'text':
                # 如果是'text', 将元素文本赋值给g.var[key]
                g.var[key] = element_location.text
            # 检查output[key]的值是否为'text…'或'text...'
            elif output[key] in ('text…', 'text...'):
                # 如果元素文本以'...'结尾，将去掉结尾的'...'后的文本赋值给g.var[key]
                if element_location.text.endswith('...'):
                    g.var[key] = element_location.text[:-3]
                # 如果没有'...'结尾，直接将元素文本赋值给g.var[key]
                else:
                    g.var[key] = element_location.text
            # 如果output[key]的值不是'text'，也不是'text…'或'text...'
            else:
                # 获取元素的指定属性值，并赋值给g.var[key]
                g.var[key] = element_location.get_attribute(output[key])


# 定义一个名为notcheck的函数，接受一个名为step的参数
def notcheck(step):
    # 从step字典中获取'data'键对应的值
    data = step['data']
    # 如果data为空，则将step字典中'expected'键对应的值赋给data
    if not data:
        data = step['expected']

    # 从step字典中获取'element'键对应的值
    element = step['element']
    # 判断元素定位方式是否为'title'
    if e.elements[element]['by'] == 'title':
        # 断言数据中的'text'值不等于当前页面的title
        assert data['text'] != g.driver.title


# 定义一个名为input的函数，接受一个名为step的参数
def input(step):
    # 从step字典中获取'data'键对应的值
    data = step['data']
    # 从step字典中获取'element'键对应的值
    element = step['element']
    # 调用locating_element函数定位元素，并将结果赋给element_location
    element_location = locating_element(element)

    # 判断数据中的'text'值是否为元组
    if isinstance(data['text'], tuple):
        # 如果是元组，则将元组解包后传递给send_keys方法
        element_location.send_keys(*data['text'])
    # 判断element_location是否存在
    elif element_location:
        # 判断数据中的'清除文本'或'clear'值是否为'否'或'no'
        if step['data'].get('清除文本', '') == '否' or step['data'].get('clear', '').lower() == 'no':
            # 如果不清除文本，则跳过清除步骤
            pass
        else:
            # 否则，清除元素的文本内容
            element_location.clear()
        # 发送数据中的'text'值给元素
        element_location.send_keys(data['text'])


# 定义一个名为set_value的函数，接受一个名为step的参数
def set_value(step):
    # 从step字典中获取'data'键对应的值
    data = step['data']
    # 从step字典中获取'element'键对应的值
    element = step['element']
    # 调用locating_element函数定位元素，并将结果赋给element_location
    element_location = locating_element(element)

    # 判断数据中的'text'值是否为元组
    if isinstance(data['text'], tuple):
        # 如果是元组，则将元组解包后传递给set_value方法
        element_location.set_value(*data['text'])
    # 判断element_location是否存在
    elif element_location:
        # 判断数据中的'清除文本'或'clear'值是否为'否'或'no'
        if step['data'].get('清除文本', '') == '否' or step['data'].get('clear', '').lower() == 'no':
            # 如果不清除文本，则跳过清除步骤
            pass
        else:
            # 否则，清除元素的文本内容
            element_location.clear()
        # 设置元素的值为数据中的'text'值
        element_location.set_value(data['text'])


def click(step):
    # 获取步骤中的元素信息
    element = step['element']

    # 判断元素类型，如果是字符串则定位元素，如果是列表则循环定位每个元素
    if isinstance(element, str):
        # 定位元素
        element_location = locating_element(element)

        # 尝试点击元素，处理 ElementClickInterceptedException 异常
        try:
            element_location.click()
        except ElementClickInterceptedException:
            # 如果元素不可点击，则等待1秒后重试一次
            sleep(1)
            element_location.click()
    elif isinstance(element, list):
        # 如果元素是列表，循环处理每个元素
        for _e in element:
            # 定位元素
            element_location = locating_element(_e)

            # 尝试点击元素，处理 ElementClickInterceptedException 异常
            try:
                element_location.click()
            except ElementClickInterceptedException:
                # 如果元素不可点击，则等待1秒后重试一次
                sleep(1)
                element_location.click()

            # 等待0.5秒
            sleep(0.5)

    # 等待0.5秒
    sleep(0.5)

    # 获取步骤中指定的元素属性
    output = step['output']
    for key in output:
        if output[key] == 'text':
            # 如果输出属性是'text'，将元素文本赋给全局变量 g.var[key]
            g.var[key] = element_location.text
        elif output[key] == 'tag_name':
            # 如果输出属性是'tag_name'，将元素标签名赋给全局变量 g.var[key]
            g.var[key] = element_location.tag_name
        elif output[key] in ('text…', 'text...'):
            # 处理特殊情况，如果文本以'...'结尾，则去掉'...'并赋给全局变量 g.var[key]
            if element_location.text.endswith('...'):
                g.var[key] = element_location.text[:-3]
            else:
                g.var[key] = element_location.text
        else:
            # 对于其他输出属性，获取元素对应属性值并赋给全局变量 g.var[key]
            g.var[key] = element_location.get_attribute(output[key])

    # 注释部分，可能是处理打开新窗口的逻辑，但是在提供的代码中被注释掉了
    # if w.current_context.startswith('WEBVIEW'):
    #     all_handles = g.driver.window_handles
    #     for handle in all_handles:
    #         if handle not in w.windows.values():
    #             w.register(step, handle)


def tap(step):
    # 创建TouchAction对象，用于模拟触摸操作
    action = TouchAction(g.driver)

    # 获取步骤中的元素信息
    element = step['element']

    # 如果元素是字符串类型
    if isinstance(element, str):
        # 如果元素信息中包含逗号，则按照坐标进行点击
        if ',' in element:
            position = element.split(',')
            x = int(position[0])
            y = int(position[1])
            position = (x, y)
            g.driver.tap([position])
        else:
            # 否则，通过定位元素并点击
            element_location = locating_element(element, 'CLICK')
            action.tap(element_location).perform()

    # 如果元素是列表类型
    elif isinstance(element, list):
        # 如果列表中的元素包含逗号，则按照坐标分别点击每个元素
        if ',' in element[0]:
            for el in element:
                position = el.split(',')
                x = int(position[0])
                y = int(position[1])
                position = (x, y)
                g.driver.tap([position])
                sleep(0.5)
        else:
            # 否则，分别定位并点击每个元素
            for _e in element:
                element_location = locating_element(_e, 'CLICK')
                action.tap(element_location).perform()
                sleep(0.5)

    # 休眠0.5秒，等待操作完成
    sleep(0.5)

    # 获取元素的其他属性信息
    output = step['output']
    for key in output:
        if output[key] == 'text':
            g.var[key] = element_location.text
        elif output[key] == 'tag_name':
            g.var[key] = element_location.tag_name
        elif output[key] in ('text…', 'text...'):
            # 处理特殊情况，如果文本以'...'结尾，则去掉'...'
            if element_location.text.endswith('...'):
                g.var[key] = element_location.text[:-3]
            else:
                g.var[key] = element_location.text
        else:
            # 获取元素的其他属性值
            g.var[key] = element_location.get_attribute(output[key])

    # 如果当前上下文是以'WEBVIEW'开头的
    # 注释部分：检查是否打开了新的窗口，并将新窗口添加到所有窗口列表中
    # w.current_context 是一个上下文信息的变量，包含当前所在的上下文信息
    # w.windows 是一个字典，包含已经打开的所有窗口信息
    # w.register 是一个函数，用于注册新打开的窗口
    # 这部分代码根据具体情况可能需要进一步调整和完善，因为相关的变量和函数没有完整提供
    # 暂时注释掉，需要根据具体情况进行适配和补充
    # if w.current_context.startswith('WEBVIEW'):
    #     all_handles = g.driver.window_handles
    #     for handle in all_handles:
    #         if handle not in w.windows.values():
    #             w.register(step, handle)


# 定义一个函数，用于按下指定键码
def press_keycode(step):
    element = step['element']
    # 使用Appium的press_keycode方法按下指定键码
    g.driver.press_keycode(int(element))


# 定义一个函数，用于滑动操作
def swipe(step):
    element = step['element']
    # 获取滑动的持续时间，默认为0.3秒
    duration = step['data'].get('持续时间', 0.3)
    # 检查坐标格式是否正确，格式应为两个点，如：100,200|300,400
    assert isinstance(element, list) and len(
        element) == 2, '坐标格式或数量不对，正确格式如：100,200|300,400'

    # 解析起始点坐标
    start = element[0].replace('，', ',').split(',')
    start_x = int(start[0])
    start_y = int(start[1])

    # 解析结束点坐标
    end = element[1].replace('，', ',').split(',')
    end_x = int(end[0])
    end_y = int(end[1])

    # 如果有指定持续时间，则使用swipe方法进行滑动，否则直接进行滑动
    if duration:
        g.driver.swipe(start_x, start_y, end_x, end_y, sleep(float(duration)))
    else:
        g.driver.swipe(start_x, start_y, end_x, end_y)


# 定义一个函数，用于绘制线条
def line(step):
    element = step['element']
    # 获取绘制线条的持续时间，默认为0.3秒
    duration = float(step['data'].get('持续时间', 0.3))
    # 检查坐标格式是否正确，格式应为多个点，如：258,756|540,1032
    assert isinstance(element, list) and len(
        element) > 1;
    1, '坐标格式或数量不对，正确格式如：258,756|540,1032'
    positions = []

    # 解析所有坐标点
    for _e in element:
        _e = _e.replace('，', ',')
        p = _e.split(',')
        positions.append(p)

    # 使用Appium的TouchAction进行线条绘制
    action = TouchAction(g.driver)
    action = action.press(
        x=positions[0][0], y=positions[0][1]).wait(duration * 1000)
    for i in range(1, len(positions)):
        action.move_to(x=positions[i][0], y=positions[i]
        [1]).wait(duration * 1000)
    action.release().perform()


# 定义一个函数，用于绘制解锁图案
def line_unlock(step):
    element = step['element']
    # 获取绘制解锁图案的持续时间，默认为0.3秒
    duration = float(step['data'].get('持续时间', 0.3))
    # 检查坐标格式是否正确，格式应为lock_pattern|1|4|7|8|9
    assert isinstance(element, list) and len(
        element) > 2, '坐标格式或数量不对，正确格式如：lock_pattern|1|4|7|8|9'

    # 定位解锁区域的元素
    _e = locating_element(element[0])
    rect = _e.rect
    # 计算每个解锁点的宽度和高度
    w = rect['width'] / 6
    h = rect['height'] / 6

    # 定义每个解锁点的坐标
    key = {}
    key['1'] = (rect['x'] + 1 * w, rect['y'] + 1 * h)
    key['2'] = (rect['x'] + 3 * w, rect['y'] + 1 * h)
    key['3'] = (rect['x'] + 5 * w, rect['y'] + 1 * h)
    key['4'] = (rect['x'] + 1 * w, rect['y'] + 3 * h)
    key['5'] = (rect['x'] + 3 * w, rect['y'] + 3 * h)
    key['6'] = (rect['x'] + 5 * w, rect['y'] + 3 * h)
    key['7'] = (rect['x'] + 1 * w, rect['y'] + 5 * h)
    key['8'] = (rect['x'] + 3 * w, rect['y'] + 5 * h)
    key['9'] = (rect['x'] + 5 * w, rect['y'] + 5 * h)

    # 使用Appium的TouchAction进行解锁图案绘制
    action = TouchAction(g.driver)
    for i in range(1, len(element)):
        k = element[i]
        # 如果是第一个点，则按下
        if i == 1:
            action = action.press(
                x=key[k][0], y=key[k][1]).wait(duration * 1000)
        # 否则，移动到下一个点
        action.move_to(x=key[k][0], y=key[k][1]).wait(duration * 1000)
    # 释放TouchAction，执行解锁动作
    action.release().perform()


# 定义一个摇杆操作的函数
def rocker(step):
    element = step['element']
    # 获取摇杆操作的持续时间，默认为0.3秒
    duration = float(step['data'].get('持续时间', 0.3))
    # 获取摇杆的名称，默认为'rocker'
    rocker_name = step['data'].get('摇杆', 'rocker')
    # 获取是否释放摇杆，默认为False
    release = step['data'].get('释放', False)

    # 如果element是字符串，则转为列表；如果为空字符串，则将element设置为空列表
    if isinstance(element, str):
        if element:
            element = [element]
        else:
            element = []

    # 处理摇杆的位置信息，将中文逗号替换为英文逗号，并拆分成坐标对
    postions = []
    for _e in element:
        _e = _e.replace('，', ',')
        p = _e.split(',')
        postions.append(p)

    # 如果在全局变量g.action中没有此摇杆名，则表示是一个新的摇杆
    if not g.action.get(rocker_name):
        # 在g.action中创建一个新的TouchAction对象，并按下第一个位置的坐标
        g.action[rocker_name] = TouchAction(g.driver)
        g.action[rocker_name].press(
            x=postions[0][0], y=postions[0][1]).wait(duration * 1000)
        # 操作完新摇杆的第一个点后，将其从positions列表中删除
        postions.pop(0)

    # 依次移动到摇杆的每个位置
    for i in range(len(postions)):
        g.action[rocker_name].move_to(
            x=postions[i][0], y=postions[i][1]).wait(duration * 1000)

    # 如果需要释放摇杆
    if release:
        # 释放摇杆，并从g.action中删除该摇杆
        g.action[rocker_name].release().perform()
        del g.action[rocker_name]
    else:
        # 执行摇杆操作
        g.action[rocker_name].perform()


# 定义滚动操作函数
def scroll(step):
    element = step['element']
    # 检查元素参数是否为列表且长度为2，格式应为'origin_el|destination_el'
    assert isinstance(element, list) and len(
        element) == 2, '元素格式或数量不对，正确格式如：origin_el|destination_el'

    # 获取起始和目标元素的定位
    origin = locating_element(element[0])
    destination = locating_element(element[1])

    # 使用driver进行滚动操作
    g.driver.scroll(origin, destination)


# 定义滑动元素操作函数
def flick_element(step):
    element = step['element']
    # 获取滑动速度，默认为10
    speed = step['data'].get('持续时间', 10)

    # 检查元素参数是否为列表且长度为2，格式应为'element|200,300'
    assert isinstance(element, list) and len(
        element) == 2, '坐标格式或数量不对，正确格式如：element|200,300'

    # 使用eval获取元素对象
    _e = eval(element[0])

    # 处理目标坐标信息
    end = element[1].replace('，', ',').split(',')
    end_x = int(end[0])
    end_y = int(end[1])

    # 如果有速度参数，则使用driver进行滑动元素操作
    if speed:
        g.driver.flick_element(_e, end_x, end_y, int(speed))


# 定义滑动操作函数
def flick(step):
    element = step['element']
    # 检查元素参数是否为列表且长度为2，格式应为'100,200|300,400'
    assert isinstance(element, list) and len(
        element) == 2, '坐标格式或数量不对，正确格式如：100,200|300,400'

    # 处理起始坐标信息
    start = element[0].replace('，', ',').split(',')
    start_x = int(start[0])
    start_y = int(start[1])

    # 处理目标坐标信息
    end = element[1].replace('，', ',').split(',')
    end_x = int(end[0])
    end_y = int(end[1])

    # 使用driver进行滑动操作
    g.driver.flick(start_x, start_y, end_x, end_y)


# 定义拖放操作函数
def drag_and_drop(step):
    element = step['element']
    # 检查元素参数是否为列表且长度为2，格式应为'origin_el|destination_el'
    assert isinstance(element, list) and len(
        element) == 2, '元素格式或数量不对，正确格式如：origin_el|destination_el'

    # 获取起始和目标元素的定位
    origin = locating_element(element[0])
    destination = locating_element(element[1])

    # 使用driver进行拖放操作
    g.driver.drag_and_drop(origin, destination)


def long_press(step):
    # 创建TouchAction对象，用于模拟触摸屏交互
    action = TouchAction(g.driver)

    # 获取步骤中的元素和持续时间信息
    element = step['element']
    duration = step['data'].get('持续时间', 1000)

    # 如果元素包含逗号或中文逗号，解析出x和y坐标
    if ',' in element or '，' in element:
        position = element.replace('，', ',').split(',')
        x = int(position[0])
        y = int(position[1])
        # 在指定位置长按一段时间
        action.long_press(x=x, y=y, duration=duration).perform()
    else:
        # 否则，通过定位元素找到元素的位置，然后在该位置长按一段时间
        element_location = locating_element(element)
        action.long_press(element_location, duration=duration).perform()
    # 等待0.5秒
    sleep(0.5)


def pinch(step):
    # 获取步骤中的元素、百分比和步长信息
    element = step['element']
    element_location = locating_element(element[0])
    percent = step['data'].get('百分比', 200)
    steps = step['data'].get('步长', 50)
    # 执行缩小操作
    g.driver.pinch(element_location, percent, steps)


def zoom(step):
    # 获取步骤中的元素、百分比和步长信息
    element = step['element']
    element_location = locating_element(element[0])
    percent = step['data'].get('百分比', 200)
    steps = step['data'].get('步长', 50)
    # 执行放大操作
    g.driver.zoom(element_location, percent, steps)


def hide_keyboard(step):
    # 隐藏键盘
    g.driver.hide_keyboard()


def shake(step):
    # 摇晃设备
    g.driver.shake()


def launch_app(step):
    # 启动应用程序
    g.driver.launch_app()


def is_locked(step):
    # 检查设备是否被锁定
    status = g.driver.is_locked()
    # 如果未锁定，则抛出断言错误
    assert status, "it's not locked"


def lock(step):
    # 锁定设备
    g.driver.lock()


def unlock(step):
    # 解锁设备
    g.driver.unlock()


def tab_name(step):
    # 获取步骤中的元素和窗口名称信息
    element = step['element']
    name = step['data']['text']

    # 从所有窗口中获取窗口句柄列表
    all_handles = g.driver.window_handles
    logger.info('All Handles: %s' % all_handles)

    # 标志变量，用于表示是否成功找到指定元素
    flag = False

    # 遍历所有窗口句柄
    for handle in all_handles:
        # 如果当前窗口句柄不在窗口资源池中
        if handle not in w.windows.values():
            # 切换至当前窗口
            g.driver.switch_to_window(handle)
            try:
                # 尝试在当前窗口中定位关键元素（'CLICK'表示点击操作）
                locating_element(element, 'CLICK')

                # 将当前窗口句柄添加到窗口资源池 g.windows 中，以窗口名称为键
                w.windows[name] = handle

                # 将当前窗口名字改为新窗口名称
                w.current_window = name

                # 设置标志为True，表示成功找到元素
                flag = True

                # 记录当前窗口和句柄信息
                logger.info('Current Window: %s' % repr(name))
                logger.info('Current Handle: %s' % repr(handle))
            except:
                pass

    # 如果标志仍为False，说明在所有窗口中未找到指定元素，抛出异常
    if not flag:
        raise Exception(
            'Tab Name failure: the element:%s in all tab is not found' % element)
