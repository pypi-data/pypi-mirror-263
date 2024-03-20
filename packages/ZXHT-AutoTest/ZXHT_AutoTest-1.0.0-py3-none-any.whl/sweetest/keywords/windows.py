# -*- coding: utf-8 -*-
"""
@Time : 2024/1/22 13:12
@Author : TJF

"""
from pywinauto.keyboard import send_keys as sendkeys
import re
from sweetest.log import logger
from sweetest.globals import g
from sweetest.utility import compare
class Windows():
    def __init__(self, app):
        self.app = app
        self.backend = app.backend.name
        self.dialogs = []


def dialog(self, page):
    # 如果输入的 page 是空列表 []
    if page == []:
        # 如果已经存在对话框实例（self.dialogs 不为空），返回最后一个对话框实例
        if self.dialogs:
            return self.dialogs[-1]
        else:
            # 否则，抛出异常，表示在没有父对话框的情况下开始对话
            raise Exception('Dialog: your page starts with "", but there is no parent dialog')

    # 如果 page 的第一个字符是 '<'
    elif page[0] == '<':
        # 如果已有的对话框实例数量大于等于 2
        if len(self.dialogs) >= 2:
            # 弹出最后一个对话框实例（相当于回退到上一级对话框）
            self.dialogs.pop()
            # 递归调用 dialog 函数，处理剩余的 page 字符串
            return self.dialog(page[1:])
        else:
            # 如果已有的对话框实例数量小于 2，抛出异常，表示父对话框数量不足
            raise Exception('Dialog: your page starts with "<", but the parent is less than 1 dialog')

    # 如果 page 的第一个字符是 '>'
    elif page[0] == '>':
        # 如果已经存在对话框实例
        if self.dialogs:
            # 根据后面的字符（page[1]）获取对应的窗口实例
            if self.backend == 'win32':
                current_dialog = self.app.window(best_match=page[1])
            elif self.backend == 'uia':
                current_dialog = self.dialogs[-1].child_window(best_match=page[1])

            # 将获取的窗口实例添加到对话框实例列表中
            self.dialogs.append(current_dialog)

            # 递归调用 dialog 函数，处理剩余的 page 字符串
            return self.dialog(page[2:])
        else:
            # 如果没有已存在的对话框实例，抛出异常
            raise Exception('Dialog: your page starts with ">", but there is no parent dialog')

    # 如果以上条件都不满足，即 page 的第一个字符既不是 '<' 也不是 '>'
    else:
        # 根据第一个字符（page[0]）获取对应的窗口实例
        current_dialog = self.app.window(best_match=page[0])

        # 将获取的窗口实例存储为对话框实例列表
        self.dialogs = [current_dialog]

        # 递归调用 dialog 函数，处理剩余的 page 字符串
        return self.dialog(page[1:])


# 选择菜单项操作
def menu_select(dialog, step):
    element = step['element']
    try:
        # 尝试使用对话框的 menu_select 方法选择菜单项
        dialog.menu_select(element)
    except:
        # 如果失败，通过拆分元素路径，逐级选择菜单项
        for el in element.split('->'):
            dialog.child_window(best_match=el).select()

# 选择操作
def select(dialog, step):
    element = step['element']
    # 根据后端类型选择窗口或子窗口，并执行选择操作
    if dialog.backend.name == 'win32':
        dialog.window(best_match=element).select()
    elif dialog.backend.name == 'uia':
        dialog.child_window(best_match=element).select()

# 点击操作
def click(dialog, step):
    element = step['element']
    # 根据后端类型选择窗口或子窗口，并执行点击输入操作
    if dialog.backend.name == 'win32':
        dialog.window(best_match=element).click_input()
    elif dialog.backend.name == 'uia':
        dialog.child_window(best_match=element).click_input()

# 取消选中操作
def check_off(dialog, step):
    element = step['element']
    # 根据后端类型选择窗口或子窗口，并执行取消选中操作
    if dialog.backend.name == 'win32':
        dialog.window(best_match=element).check()
    elif dialog.backend.name == 'uia':
        dialog.child_window(best_match=element).check()

# 双击操作
def double_click(dialog, step):
    element = step['element']
    # 根据后端类型选择窗口或子窗口，并执行双击输入操作
    if dialog.backend.name == 'win32':
        dialog.window(best_match=element).double_click_input()
    elif dialog.backend.name == 'uia':
        dialog.child_window(best_match=element).double_click_input()

# 输入文本操作
def input(dialog, step):
    element = step['element']
    value = step['data']['text']
    # 根据后端类型选择窗口或子窗口，并输入文本，支持空格和换行符
    if dialog.backend.name == 'win32':
        dialog.window(best_match=element).type_keys(value, with_spaces=True, with_newlines='\r\n')
    elif dialog.backend.name == 'uia':
        dialog.child_window(best_match=element).type_keys(value, with_spaces=True, with_newlines='\r\n')

# 设置文本操作
def set_text(dialog, step):
    element = step['element']
    value = step['data']['text']
    # 根据后端类型选择窗口或子窗口，并设置编辑框的文本
    if dialog.backend.name == 'win32':
        dialog.window(best_match=element).set_edit_text(value)
    elif dialog.backend.name == 'uia':
        dialog.child_window(best_match=element).set_edit_text(value)

# 发送键盘按键操作
def send_keys(dialog, step):
    element = step['element']
    value = step['data'].get('text')
    dialog.set_focus()
    if element:
        # 如果提供了元素信息，根据后端类型选择窗口或子窗口，并设置焦点
        if dialog.backend.name == 'win32':
            dialog.window(best_match=element).set_focus()
        elif dialog.backend.name == 'uia':
            dialog.child_window(best_match=element).set_focus()
        # 发送键盘按键
        sendkeys(value)
    else:
        # 如果没有提供元素信息，直接发送键盘按键
        sendkeys(value)


# 检查操作
def check(dialog, step):
    element = step['element']
    data = step['data']
    # 如果没有数据，则使用预期结果作为数据
    if not data:
        data = step['expected']
    output = step['output']

    # 遍历数据中的每个键值对
    for key in data:
        # 获取预期结果
        expected = data[key]

        # 处理切片操作，通过正则表达式找到匹配 '[.*?]' 的部分，并替换掉
        s = re.findall(r'\[.*?\]', key)
        if s:
            s = s[0]
            key = key.replace(s, '')

        # 根据键值类型执行相应的操作
        if key == 'text':
            # 获取实际文本值
            if dialog.backend.name == 'win32':
                real = dialog.window(best_match=element).texts()[0].replace('\r\n', '\n')
            elif dialog.backend.name == 'uia':
                real = dialog.child_window(best_match=element).texts()[0].replace('\r\n', '\n')
        elif key == 'value':
            # 获取实际数值
            if dialog.backend.name == 'win32':
                real = dialog.window(best_match=element).text_block().replace('\r\n', '\n')
            elif dialog.backend.name == 'uia':
                real = dialog.child_window(best_match=element).get_value().replace('\r\n', '\n')
        # 如果有切片操作
        if s:
            # 使用 eval 执行切片操作，例如 'real[1:3]' 将获取 real 列表的子列表
            real = eval('real' + s)

        # 根据键值类型执行相应的操作，获取实际值
        if key == 'selected':
            # 获取元素是否被选中
            if dialog.backend.name == 'win32':
                real = dialog.window(best_match=element).is_selected()
            elif dialog.backend.name == 'uia':
                real = dialog.child_window(best_match=element).is_selected()
        elif key == 'checked':
            # 获取元素是否被选中（复选框等情况）
            if dialog.backend.name == 'win32':
                real = dialog.window(best_match=element).is_checked()
            elif dialog.backend.name == 'uia':
                real = dialog.child_window(best_match=element).is_checked()
        elif key == 'enabled':
            # 获取元素是否启用
            if dialog.backend.name == 'win32':
                real = dialog.window(best_match=element).is_enabled()
            elif dialog.backend.name == 'uia':
                real = dialog.child_window(best_match=element).is_enabled()
        elif key == 'visible':
            # 获取元素是否可见
            if dialog.backend.name == 'win32':
                real = dialog.window(best_match=element).is_visible()
            elif dialog.backend.name == 'uia':
                real = dialog.child_window(best_match=element).is_visible()
        elif key == 'focused':
            # 获取元素是否获得焦点
            if dialog.backend.name == 'win32':
                real = dialog.window(best_match=element).is_focused()
            elif dialog.backend.name == 'uia':
                real = dialog.child_window(best_match=element).is_focused()

        # 记录预期值和实际值
        logger.info('DATA:%s' % repr(expected))
        logger.info('REAL:%s' % repr(real))

        # 比较预期值和实际值
        compare(expected, real)
        # 遍历输出字典中的键值对
        for key in output:
            # 获取键对应的值
            k = output[key]

            # 如果元素是编辑框且属性是'text'，则将属性更改为'value'
            if dialog.window(best_match=element).class_name() == 'Edit' and k == 'text':
                k = 'value'

            # 如果属性为'text'
            if k == 'text':
                # 根据后端类型获取元素的文本内容，并将换行符替换为'\n'
                if dialog.backend.name == 'win32':
                    g.var[key] = dialog.window(best_match=element).texts()[0].replace('\r\n', '\n')
                elif dialog.backend.name == 'uia':
                    g.var[key] = dialog.child_window(best_match=element).texts()[0].replace('\r\n', '\n')

            # 如果属性为'value'
            if k == 'value':
                # 根据后端类型获取元素的值，并将换行符替换为'\n'
                if dialog.backend.name == 'win32':
                    g.var[key] = dialog.window(best_match=element).text_block().replace('\r\n', '\n')
                elif dialog.backend.name == 'uia':
                    g.var[key] = dialog.child_window(best_match=element).get_value().replace('\r\n', '\n')


def window(dialog, step):
    # 获取步骤中的元素信息
    element = step['element']

    # 判断元素类型并执行相应的窗口操作
    if element.lower() in ('最小化', 'minimize'):
        dialog.minimize()
    elif element.lower() in ('最大化', 'maximize'):
        dialog.maximize()
    elif element.lower() in ('恢复', 'restore'):
        dialog.restore()
    elif element.lower() in ('关闭', 'close'):
        dialog.close()
    elif element.lower() in ('前台', 'set_focus'):
        dialog.set_focus()
    elif element.lower() in ('重置', 'reset'):
        # 尝试重置窗口，最多重试10次
        for i in range(10):
            # 如果窗口失去焦点
            if not dialog.has_focus():
                try:
                    # 如果弹出保存窗口，尝试点击窗口上的确定按钮
                    save = dialog.get_active()
                    element = '(N)'
                    if dialog.backend.name == 'win32':
                        save.window(best_match=element).click_input()
                    elif dialog.backend.name == 'uia':
                        save.child_window(best_match=element).click_input()
                except:
                    pass
                # 按 Alt+F4 关闭窗口
                sendkeys('%{F4}')
            else:
                # 窗口已经重置成功，跳出循环
                break
        else:
            # 重置窗口失败，抛出异常
            raise Exception(f'Reset the Windows is failure: try Alt+F4 for {i + 1} times')
