# -*- coding: utf-8 -*-
"""
@Time : 2024/1/24 16:37
@Author : TJF

"""
from time import sleep

import re
from sweetest.log import logger
from sweetest.globals import g, now, timestamp
from sweetest.elements import e
from sweetest.windows import w
from sweetest.snapshot import Snapshot
from sweetest.keywords import mobile, files, common, windows, web, http
from sweetest.config import web_keywords, mobile_keywords, http_keywords, windows_keywords, files_keywords
from sweetest.utility import replace_dict, replace


def elements_format(page, element):
    # 如果未指定页面，则使用当前页面
    if not page:
        page = g.current_page

    # 如果未指定元素，则返回当前页面和空的自定义和元素
    if not element:
        return page, '', element

    # 如果页面为SNIPPET或用例片段，或元素为变量赋值，则返回当前页面和空的自定义和元素
    if page in ('SNIPPET', '用例片段') or element in ('变量赋值',):
        return page, '', element

    # 如果元素包含多个部分，按|分割
    elements = element.split('|')
    if len(elements) == 1:
        # 如果只有一个元素部分，调用e.have获取自定义和元素
        custom, el = e.have(page, element)
        # 更新当前页面
        g.current_page = page
        return page, custom, el
    else:
        # 如果有多个元素部分，逐个获取自定义和元素
        els = []
        for _element in elements:
            custom, el = e.have(page, _element.strip())
            els.append(el)
        # 更新当前页面
        g.current_page = page
        return page, custom, els


def v_data(d, _d):
    data = ''
    # 根据是否包含',,'选择分隔符
    if ',,' in str(_d):
        s = ',,'
    else:
        s = ','

    # 将字典中的键值对以k=v形式拼接，并用分隔符隔开
    for k, v in d.items():
        data += k + '=' + str(v) + s

    # 根据分隔符类型去掉末尾多余的分隔符
    if s == ',,':
        return data[:-2]
    else:
        return data[:-1]


def test_v_data():
    # 测试用例数据
    data = {'a': 1, 'b': 'b'}
    _data = "{'a': 1,, 'b': 'b'}"
    # 调用v_data函数
    return v_data(data, _data)


class TestCase:
    def __init__(self, testcase):
        # 初始化测试用例对象，接收测试用例数据
        self.testcase = testcase
        self.snippet_steps = {}  # 未提供此部分代码，暂不注释

    def run(self):
        # 替换测试用例标题中的内容
        self.testcase['title'] = replace(self.testcase['title'])
        logger.info('>>> 运行测试用例：%s|%s' %
                    (self.testcase['id'], self.testcase['title']))
        logger.info('-' * 50)
        self.testcase['result'] = 'success'  # 设置测试用例结果为成功
        self.testcase['report'] = ''  # 初始化测试用例报告为空字符串
        if_result = ''  # 初始化条件判断结果为空字符串

        for index, step in enumerate(self.testcase['steps']):
            # 统计步骤开始时间
            step['start_timestamp'] = timestamp()
            step['snapshot'] = {}  # 此部分代码未提供，暂不注释

            # 如果条件为否，则不执行then语句
            if step['control'] == '>' and not if_result:
                step['score'] = '-'  # 设置步骤得分为'-'
                step['end_timestamp'] = timestamp()
                logger.info('跳过 <then> 步骤：%s|%s|%s|%s' % (
                    step['no'], step['page'], step['keyword'], step['element']))
                continue

            # 如果条件为真，则不执行else语句
            if step['control'] == '<' and if_result:
                step['score'] = '-'  # 设置步骤得分为'-'
                step['end_timestamp'] = timestamp()
                logger.info('跳过 <else> 步骤：%s|%s|%s|%s' % (
                    step['no'], step['page'], step['keyword'], step['element']))
                continue

            # 如果不是Windows系统或关键字不在Windows关键字列表中，则进行格式化处理
            if not (g.platform.lower() in ('windows',) and step['keyword'].upper() in windows_keywords):
                step['page'], step['custom'], step['element'] = elements_format(
                    step['page'], step['element'])
            label = g.sheet_name + '#' + \
                    self.testcase['id'] + '#' + str(step['no']).replace('<', '(').replace('>', ')').replace('*', 'x')

            logger.info('运行步骤：%s|%s|%s|%s' %
                        (step['no'], step['page'], step['keyword'], step['element']))

            # 创建一个名为Snapshot的对象实例
            snap = Snapshot()

            # 尝试执行以下代码块
            try:
                # 获取步骤中可能存在的AFTER_FUNCTION字段的值，并将其从step['data']中移除
                after_function = step['data'].pop('AFTER_FUNCTION', '')

                # 处理强制等待时间
                if '#wait_time' in step['data']:
                    # 如果'#wait_time'存在于step['data']中，获取其值并转换为浮点数，然后暂停执行程序
                    t = step['data'].pop('#wait_time', 0)
                    sleep(float(t))
                else:
                    # 如果'#wait_time'不存在，检查'#wait_times'是否存在于step['data']中
                    if '#wait_times' in step['data']:
                        # 如果存在，将'#wait_times'的值赋给全局变量g.wait_times
                        g.wait_times = float(step['data'].pop('#wait_times', 0))
                    # 检查全局变量g.wait_times是否存在且不为0，如果是，则暂停执行程序
                    if g.wait_times:
                        sleep(g.wait_times)

                # 如果步骤中存在page字段，对其进行替换处理
                if step['page']:
                    step['page'] = replace(step['page'])

                # 检查element字段的类型，如果是字符串，则对其进行替换处理，并将结果赋给'_element'字段
                if isinstance(step['element'], str):
                    step['element'] = replace(step['element'])
                    step['_element'] = step['element']
                # 如果是列表类型，则对列表中的每个元素进行替换处理，并将结果以'|'分隔后赋给'_element'字段
                elif isinstance(step['element'], list):
                    for i in range(len(step['element'])):
                        step['element'][i] = replace(step['element'][i])
                    step['_element'] = '|'.join(step['element'])

                # 对data和expected字段中的变量进行替换处理
                replace_dict(step['data'])
                replace_dict(step['expected'])

                # 移除data字段中的BEFORE_FUNCTION字段
                step['data'].pop('BEFORE_FUNCTION', '')

                # 使用v_data函数处理data和'_data'字段，将结果赋给'vdata'字段
                step['vdata'] = v_data(step['data'], step['_data'])

                # 判断平台是否为桌面，且关键字在web_keywords中
                if g.platform.lower() in ('desktop',) and step['keyword'].upper() in web_keywords:
                    # 处理截图数据
                    snap.pre(step, label)

                    # 如果关键字不是'MESSAGE'或'对话框'
                    if step['keyword'].upper() not in ('MESSAGE', '对话框'):
                        # 判断页面是否已经与窗口关联，如果没有，则关联当前窗口，如果已经关联，则判断是否需要切换
                        w.switch_window(step['page'])

                        # 切换 frame 处理，支持变量替换
                        frame = replace(step['custom'])
                        w.switch_frame(frame)

                    # 根据关键字调用web模块中对应的关键字实现
                    element = getattr(web, step['keyword'].lower())(step)
                    # 处理网页截图
                    snap.web_shot(step, element)

                # 如果平台是iOS或Android，且关键字在mobile_keywords中
                elif g.platform.lower() in ('ios', 'android') and step['keyword'].upper() in mobile_keywords:
                    # 切换 context 处理，支持变量替换
                    context = replace(step['custom']).strip()
                    w.switch_context(context)

                    # 如果当前 context 以'WEBVIEW'开头
                    if w.current_context.startswith('WEBVIEW'):
                        # 切换标签页
                        tab = step['data'].get('标签页')
                        if tab:
                            del step['data']['标签页']
                            g.driver.switch_to_window(w.windows[tab])
                        # 记录当前 context 信息
                        logger.info('Current Context: %s' % repr(w.current_context))

                    # 根据关键字调用mobile模块中对应的关键字实现
                    getattr(mobile, step['keyword'].lower())(step)

                # 如果运行平台是Windows，并且关键字在Windows关键字列表中
                elif g.platform.lower() in ('windows',) and step['keyword'].upper() in windows_keywords:
                    # 导入Windows关键字模块
                    _page = ''
                    # 如果步骤的页面以'#'开头，去除'#'
                    if step['page'].startswith('#'):
                        _page = step['page'][1:]
                        page = [x for x in re.split(r'(<|>)', _page) if x != '']
                    else:
                        page = [x for x in re.split(r'(<|>)', step['page']) if x != '']

                    # 如果存在页面信息，使用指定页面的Windows对话框
                    if _page:
                        dialog = g.windows['#'].dialog(page)
                    else:
                        dialog = g.windows['default'].dialog(page)
                    # 获取Windows对话框的屏幕截图
                    snap.pre(step, label)

                    # 根据关键字调用Windows关键字模块中对应的关键字实现
                    getattr(windows, step['keyword'].lower())(dialog, step)
                    # 对Windows对话框进行屏幕截图
                    snap.windows_shot(dialog, step)

                # 如果关键字在HTTP关键字列表中
                elif step['keyword'].upper() in http_keywords:
                    # 根据关键字调用HTTP关键字模块中对应的关键字实现
                    getattr(http, step['keyword'].lower())(step)

                # 如果关键字在文件关键字列表中
                elif step['keyword'].upper() in files_keywords:
                    # 根据关键字调用文件关键字模块中对应的关键字实现
                    getattr(files, step['keyword'].lower())(step)

                # 如果关键字是'execute'
                elif step['keyword'].lower() == 'execute':
                    # 调用通用模块中的'execute'关键字实现
                    result, steps = getattr(common, step['keyword'].lower())(step)
                    # 如果步骤的页面是'SNIPPET'或'用例片段'，将返回的步骤存储在片段步骤中
                    if step['page'] in ('SNIPPET', '用例片段'):
                        self.snippet_steps[index + 1] = steps
                    # 如果执行结果不是'success'，更新测试用例结果并结束测试用例执行
                    if result != 'success':
                        self.testcase['result'] = result
                        step['end_timestamp'] = timestamp()
                        break
                    # elif step['page'] in ('SCRIPT', '脚本'):
                    #     # 判断页面是否已和窗口做了关联，如果没有，就关联当前窗口，如果已关联，则判断是否需要切换
                    #     w.switch_window(step['page'])
                    #     # 切换 frame 处理，支持变量替换
                    #     frame = replace(step['custom'])
                    #     w.switch_frame(frame)
                    #     common.script(step)

                else:
                    # 根据关键字调用关键字实现
                    getattr(common, step['keyword'].lower())(step)

                # 上述代码是一个else语句块的开始，表示在前面的条件不满足时执行的代码块
                # 这里使用了Python的反射机制，根据step字典中的'keyword'键对应的值，调用common模块中相应的函数
                # step字典中的'keyword'值被转换为小写，并作为函数名调用，传递step字典作为参数

                logger.info('>>>>>>>>>>>>>>>>>>>> success <<<<<<<<<<<<<<<<<<<<')
                step['score'] = 'OK'

                # 记录日志，输出信息表示执行成功，并将step字典中的'score'键的值设为'OK'

                # if 语句结果赋值
                if step['control'] == '^':
                    if_result = True

                # 检查step字典中'control'键的值是否为'^'，如果是，则将if_result变量设为True

                if after_function:
                    replace_dict({'after_function': after_function})

                # 如果存在after_function，调用replace_dict函数，传递包含'after_function'键值对的字典作为参数

                # 操作后，等待0.2秒
                sleep(0.2)

            except Exception as exception:
                # 捕获异常，处理可能发生的错误

                if g.platform.lower() in ('desktop',) and step['keyword'].upper() in web_keywords:
                    # 如果平台是desktop，且step字典中'keyword'的大写形式在web_keywords列表中
                    file_name = label + now() + '#Failure' + '.png'
                    step['snapshot']['Failure'] = str(snap.snapshot_folder / file_name)
                    try:
                        if w.frame != 0:
                            g.driver.switch_to.default_content()
                            w.frame = 0
                        g.driver.get_screenshot_as_file(step['snapshot']['Failure'])
                    except:
                        logger.exception('*** 保存截图失败 ***')

                elif g.platform.lower() in ('ios', 'android') and step['keyword'].upper() in mobile_keywords:
                    # 如果平台是ios或android，且step字典中'keyword'的大写形式在mobile_keywords列表中
                    file_name = label + now() + '#Failure' + '.png'
                    step['snapshot']['Failure'] = str(snap.snapshot_folder / file_name)
                    try:
                        g.driver.switch_to.context('NATIVE_APP')
                        w.current_context = 'NATIVE_APP'
                        g.driver.get_screenshot_as_file(u'%s' % step['snapshot']['Failure'])
                    except:
                        logger.exception('*** 保存截图失败 ***')

                logger.exception('Exception:')
                # 记录异常信息，使用logger记录异常的详细信息

                logger.error('>>>>>>>>>>>>>>>>>>>> failure <<<<<<<<<<<<<<<<<<<<')
                # 记录错误信息，使用logger记录错误的标识

                step['score'] = 'NO'
                # 将step字典中的'score'键的值设为'NO'，表示步骤执行失败

                step['remark'] += str(exception)
                # 将异常信息转换为字符串，并追加到step字典中的'remark'键的值中

                step['end_timestamp'] = timestamp()
                # 记录步骤结束的时间戳

                # if 语句结果赋值
                if step['control'] == '^':
                    # 如果step字典中'control'键的值为'^'
                    if_result = False
                    continue
                    # 将if_result变量设为False，并跳过当前循环的剩余部分

                self.testcase['result'] = 'failure'
                # 将测试用例字典中'result'键的值设为'failure'

                self.testcase['report'] = 'step-%s|%s|%s: %s' % (
                    step['no'], step['keyword'], step['element'], exception)
                # 将错误信息格式化为报告字符串，并赋值给测试用例字典中'report'键

                break
                # 跳出循环，结束测试用例的执行

                # 统计结束时间
            step['end_timestamp'] = timestamp()

            steps = []
            i = 0
            for k in self.snippet_steps:
                steps += self.testcase['steps'][i:k] + self.snippet_steps[k]
                i = k
            steps += self.testcase['steps'][i:]
            self.testcase['steps'] = steps
            # 将测试用例字典中的步骤按照snippet_steps的规定进行重新排序，保证执行顺序的正确性
