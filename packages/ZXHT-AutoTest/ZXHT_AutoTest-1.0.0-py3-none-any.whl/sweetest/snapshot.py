# -*- coding: utf-8 -*-
"""
@Time : 2024/1/23 15:34
@Author : TJF

"""
from pathlib import Path
import random

from PIL import Image
from PIL import ImageChops
import math
import operator
import time
from functools import reduce
from sweetest.globals import g, now
from sweetest.log import logger
from sweetest.utility import mkdir

ran = str(random.randint(1,100))
def crop(element, src, target):
    # 获取元素的位置和大小信息
    location = element.location
    size = element.size

    # 打开原始图片
    im = Image.open(src)

    # 计算裁剪的区域
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    # 裁剪图片
    im = im.crop((left, top, right, bottom))

    # 保存裁剪后的图片
    im.save(target)


def blank(src, boxs):
    # 创建白色背景图片
    white = Image.new('RGB', (5000, 5000), 'white')

    # 打开原始图片
    im = Image.open(src)

    # 遍历每个框，裁剪白色图片并粘贴到原始图片上
    for box in boxs:
        w = white.crop(box)
        im.paste(w, box[:2])

    # 保存修改后的图片
    im.save(src)


def cut(src, target, box):
    # 打开原始图片
    im = Image.open(src)

    # 裁剪指定区域
    im = im.crop(box)

    # 保存裁剪后的图片
    im.save(target)


def get_screenshot(file_path):
    # 如果是无头模式，获取整个页面的大小
    if g.headless:
        width = g.driver.execute_script(
            "return Math.max(document.body.scrollWidth, document.documentElement.clientWidth, "
            "document.documentElement.scrollWidth, document.documentElement.offsetWidth);")
        height = g.driver.execute_script(
            "return Math.max(document.body.scrollHeight, document.documentElement.clientHeight,"
            " document.documentElement.scrollHeight, document.documentElement.offsetHeight);")

        # 设置浏览器窗口大小为整个页面大小
        g.driver.set_window_size(width, height)

        # 等待3秒，确保页面加载完成
        time.sleep(3)

    # 获取屏幕截图并保存到指定路径
    g.driver.get_screenshot_as_file(file_path)

    # 如果是无头模式，重新设置浏览器窗口大小为默认大小
    if g.headless:
        g.driver.set_window_size(1920, 1080)


class Snapshot:
    def __init__(self):
        # 构造函数，初始化快照相关路径
        snapshot_plan = Path('snapshot') / g.plan_name
        self.snapshot_folder = snapshot_plan / g.start_time
        snapshot_expected = Path('snapshot') / 'expected'
        self.expected_folder = snapshot_expected / g.plan_name

        # 创建目录结构
        for p in (snapshot_plan, self.snapshot_folder, snapshot_expected, self.expected_folder):
            mkdir(p)

    def pre(self, step, label):
        # pre方法用于预处理快照，接收步骤和标签作为参数
        self.label = label
        self.screen_flag = False  # 是否需要截取整个屏幕的标志
        self.element_flag = False  # 是否需要截取特定元素的标志

        # 处理输出数据中的截图设置
        self.output = {}
        for k, v in dict(step['output'].items()).items():
            if v in ('#screen_shot', '#ScreenShot'):
                self.output['#screen_shot'] = k
                step['output'].pop(k)
                self.screen_flag = True
            if v == ('#element_shot', '#ElementShot'):
                self.output['#element_shot'] = k
                step['output'].pop(k)
                self.element_flag = True

        # 处理图片比较
        self.expected = {}
        for data in (step['data'], step['expected']):
            if '#screen_shot' in data:
                self.screen_flag = True
                p = Path(data['#screen_shot']).stem
                self.expected['#screen_name'] = '(' + p.split('[')[1].split(']')[0] + ')' if '[' in p else p
                if Path(data['#screen_shot']).is_file():
                    step['snapshot']['expected_screen'] = data.pop('#screen_shot')
                else:
                    step['snapshot']['expected_screen'] = str(self.expected_folder / data.pop('#screen_shot'))
            if '#element_shot' in data:
                # 如果数据中包含'#element_shot'
                self.element_flag = True  # 设置截取特定元素的标志为True
                p = Path(data['#element_shot']).stem
                # 从文件路径中提取元素名称
                self.expected['#element_name'] = '(' + p.split('[')[1].split(']')[0] + ')' if '[' in p else p
                if Path(data['#element_shot']).is_file():
                    # 如果指定的元素截图文件存在，直接使用
                    step['snapshot']['expected_element'] = data.pop('#element_shot')
                else:
                    # 如果文件不存在，使用预期文件夹路径
                    step['snapshot']['expected_element'] = str(self.expected_folder / data.pop('#element_shot'))

            if '#cut' in data:
                # 如果数据中包含'#cut'
                self.expected['#cut'] = data.pop('#cut')  # 将'#cut'对应的值移至预期结果中
            if '#blank' in data:
                # 如果数据中包含'#blank'
                self.expected['#blank'] = data.pop('#blank')  # 将'#blank'对应的值移至预期结果中

    def web_screen(self, step, element):
        # 截图
        screen_v = self.output.get('#screen_shot', '')  # 获取屏幕截图变量名
        element_v = self.output.get('#element_shot', '')  # 获取元素截图变量名

        if g.snapshot or self.screen_flag or self.element_flag:
            # 如果全局截图标志为True，或者屏幕截图标志为True，或者元素截图标志为True
            from selenium.webdriver.support import expected_conditions as EC
            if not EC.alert_is_present()(g.driver):
                # 如果当前页面没有警告框
                if self.expected.get('#screen_name'):
                    # 如果预期结果中包含屏幕名称
                    screen_name = self.expected['#screen_name']
                elif screen_v:
                    # 如果屏幕截图变量存在
                    screen_name = screen_v
                else:
                    screen_name = ''
                if screen_name:
                        # 如果存在屏幕名称，构建截图文件名
                    file_name = self.label + now() + '#screen' + '[' + screen_name + ']' + '.png'
                else:
                    # 否则，构建默认截图文件名
                    file_name = self.label + now() + '#screen' + '.png'
                step['snapshot']['real_screen'] = str(
                    Path(self.snapshot_folder) / file_name)  # 设置实际屏幕截图路径
                get_screenshot(step['snapshot']['real_screen'])  # 执行屏幕截图
                if screen_v:
                    g.var[screen_v] = step['snapshot']['real_screen']  # 将截图文件路径保存到变量中

        if element_v:

            # 如果元素截图变量存在
            file_name = self.label + now() + '#element' + '[' + element_v + ']' + '.png'
            step['snapshot']['real_element'] = str(Path(self.snapshot_folder) / file_name)  # 设置实际元素截图路径
            crop(element, step['snapshot']['real_screen'], step['snapshot']['real_element'])  # 执行元素截图
            g.var[element_v] = step['snapshot']['real_element']  # 将元素截图文件路径保存到变量中

    def web_check(self, step, element):

        def deep(src):
            # 把不需要比较的部分贴白
            if self.expected.get('#blank'):
                blank(src, eval(self.expected.get('#blank')))
            # 裁剪需要比较的部分
            if self.expected.get('#cut'):
                cut(src, src, eval(self.expected.get('#cut')))

        if Path(step['snapshot'].get('expected_screen', '')).is_file():
            # 屏幕截图比较
            image1 = Image.open(step['snapshot']['expected_screen'])
            image2 = Image.open(step['snapshot']['real_screen'])
            deep(step['snapshot']['real_screen'])
            histogram1 = image1.histogram()
            histogram2 = image2.histogram()
            # 计算直方图的差异
            differ = math.sqrt(reduce(operator.add, list(
                map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))
            # 获取图像的差异
            diff = ImageChops.difference(image1.convert('RGB'), image2.convert('RGB'))
            if differ < 0.1:
                # 图片间没有任何不同
                logger.info('SnapShot: screen_shot is the same')
            else:

                file_name = self.label + now() + 'diff_screen' + '.png'
                step['snapshot']['diff_screen'] = str(
                    Path(self.snapshot_folder) / file_name)
                diff.save(step['snapshot']['diff_screen'])
                raise Exception('SnapShot: screen_shot is diff: %s' % differ)
        elif step['snapshot'].get('expected_screen'):
            get_screenshot(step['snapshot']['expected_screen'])
            deep(step['snapshot']['expected_screen'])

        if Path(step['snapshot'].get('expected_element', '')).is_file():
            # 创建实际元素的截图文件名
            file_name = self.label + now() + '#element' + '[' + self.expected['#element_name'] + ']' + '.png'
            step['snapshot']['real_element'] = str(Path(self.snapshot_folder) / file_name)
            # 裁剪元素
            crop(element, step['snapshot']['real_screen'], step['snapshot']['real_element'])
            deep(step['snapshot']['real_element'])

            # 屏幕截图比较

            # 打开第一张截图
            image1 = Image.open(step['snapshot']['expected_element'])
            # 打开第二张截图
            image2 = Image.open(step['snapshot']['real_element'])

            # 计算直方图
            histogram1 = image1.histogram()
            histogram2 = image2.histogram()

            # 计算直方图差异的平方和
            differ = math.sqrt(reduce(operator.add, list(
                map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))

            # 计算图像差异
            diff = ImageChops.difference(image1.convert('RGB'), image2.convert('RGB'))

            # 如果差异小于0.1，输出日志信息表示元素截图相同
            if differ < 0.1:
                logger.info('SnapShot: element_shot is the same')
            # 如果差异大于等于0.1，保存差异图像并抛出异常
            else:
                # 生成差异图像文件名

                file_name = self.label + now() + 'diff_element' + '.png'
                # 设置差异图像路径
                step['snapshot']['diff_element'] = str(
                    Path(self.snapshot_folder) / file_name)
                # 保存差异图像
                diff.save(step['snapshot']['diff_element'])
                # 抛出异常，表示元素截图不同
                raise Exception('SnapShot: element_shot is diff: %s' % differ)

        # 如果存在预期元素截图路径，进行裁剪和深度检查
        elif step['snapshot'].get('expected_element'):
            # 裁剪元素
            crop(element, step['snapshot']['real_screen'], step['snapshot']['expected_element'])
            # 深度检查预期元素
            deep(step['snapshot']['expected_element'])

    # 定义web_shot方法，用于进行网页截图和检查
    def web_shot(self, step, element):
        # 调用web_screen方法进行网页截图
        self.web_screen(step, element)
        # 调用web_check方法进行截图检查

    # 定义windwos_capture方法，用于在Windows环境下进行截图
    def windwos_capture(self, dialog, step):
        # 获取截图变量和元素变量的值
        screen_v = self.output.get('#screen_shot', '')
        element_v = self.output.get('#element_shot', '')

        # 判断是否需要进行截图
        if g.snapshot or self.screen_flag:
            # 获取截图名称
            if self.expected.get('#screen_name'):
                screen_name = self.expected['#screen_name']
            elif screen_v:
                screen_name = screen_v
            else:
                screen_name = ''

            # 构建截图文件名
            if screen_name:
                file_name = self.label + now() + '#screen' + '[' + screen_name + ']' + '.png'
            else:

                file_name = self.label + now() + '#screen' + '.png'

            # 设置实际截图路径并进行截图保存
            step['snapshot']['real_screen'] = str(Path(self.snapshot_folder) / file_name)
            pic = dialog.capture_as_image()
            pic.save(step['snapshot']['real_screen'])

            # 如果有截图变量，将实际截图路径保存到变量中
            if screen_v:
                g.var[screen_v] = step['snapshot']['real_screen']

        # 判断是否需要进行元素截图
        if element_v:
            # 构建元素截图文件名

            file_name = self.label + now() + '#element' + '[' + element_v + ']' + '.png'
            step['snapshot']['real_element'] = str(Path(self.snapshot_folder) / file_name)
            element = step['element']

            # 根据Windows backend类型进行相应的元素截图
            if dialog.backend.name == 'win32':
                pic = dialog.window(best_match=element).capture_as_image()
            elif dialog.backend.name == 'uia':
                pic = dialog.child_window(best_match=element).capture_as_image()

            # 保存元素截图并将路径保存到变量中
            pic.save(step['snapshot']['real_screen'])
            g.var[element_v] = step['snapshot']['real_element']

    def windwos_check(self, dialog, step):
        # windwos_check 方法，用于检查窗口（或对话框）的状态
        # 参数 dialog 是对话框的实例，step 是一个包含检查步骤信息的字典

        element = step['element']
        # 从步骤中获取 'element' 键对应的值，这是要检查的元素

        if Path(step['snapshot'].get('expected_screen', '')).is_file():
            # 如果步骤中存在 'snapshot' 键，且其中 'expected_screen' 键对应的值是文件路径
            # 即，预期屏幕截图存在

            # 打开预期和实际屏幕截图
            image1 = Image.open(step['snapshot']['expected_screen'])
            image2 = Image.open(step['snapshot']['real_screen'])

            # 计算直方图并计算两个直方图之间的差异
            histogram1 = image1.histogram()
            histogram2 = image2.histogram()
            differ = math.sqrt(reduce(operator.add, list(
                map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))

            # 计算两个图片的差异
            diff = ImageChops.difference(image1.convert('RGB'), image2.convert('RGB'))

            if differ < 0.1:
                # 如果差异很小，即图片间没有任何不同
                logger.info('SnapShot: screen_shot is the same')
            else:
                # 如果差异较大，保存差异图片，并抛出异常
                file_name = self.label + now() + 'diff_screen' + '.png'
                step['snapshot']['diff_screen'] = str(
                    Path(self.snapshot_folder) / file_name)
                diff.save(step['snapshot']['diff_screen'])
                raise Exception('SnapShot: screen_shot is diff: %s' % differ)
        elif step['snapshot'].get('expected_screen'):
            # 如果预期屏幕截图存在但实际屏幕截图不存在

            # 捕捉当前对话框的屏幕截图，并保存为预期屏幕截图
            pic = dialog.capture_as_image()
            pic.save(step['snapshot']['expected_screen'])

        if Path(step['snapshot'].get('expected_element', '')).is_file():
            # 如果步骤中存在 'snapshot' 键，且其中 'expected_element' 键对应的值是文件路径
            # 即，预期元素截图存在

            # 生成保存实际元素截图的文件名
            file_name = self.label + now() + '#element' + '.png'
            step['snapshot']['real_element'] = str(Path(self.snapshot_folder) / file_name)

            # 根据对话框的后端类型选择不同的截图方式
            if dialog.backend.name == 'win32':
                pic = dialog.window(best_match=element).capture_as_image()
            elif dialog.backend.name == 'uia':
                pic = dialog.child_window(best_match=element).capture_as_image()

            # 保存实际元素截图
            pic.save(step['snapshot']['real_element'])

            # 屏幕截图比较
            image1 = Image.open(step['snapshot']['expected_element'])
            image2 = Image.open(step['snapshot']['real_element'])
            histogram1 = image1.histogram()
            histogram2 = image2.histogram()

            # 计算直方图差异
            differ = math.sqrt(reduce(operator.add, list(
                map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))

            # 计算两个图片的差异
            diff = ImageChops.difference(image1.convert('RGB'), image2.convert('RGB'))

            if differ < 0.1:
                # 如果差异很小，即图片间没有任何不同
                logger.info('SnapShot: element_shot is the same')
            else:
                # 如果差异较大，保存差异图片，并抛出异常
                file_name = self.label + now() + 'diff_element' + '.png'
                step['snapshot']['diff_element'] = str(
                    Path(self.snapshot_folder) / file_name)
                diff.save(step['snapshot']['diff_element'])
                raise Exception('SnapShot: element_shot is diff: %s' % differ)
        elif step['snapshot'].get('expected_element'):
            # 如果预期元素截图存在但实际元素截图不存在

            # 根据对话框的后端类型选择不同的截图方式
            if dialog.backend.name == 'win32':
                pic = dialog.window(best_match=element).capture_as_image()
            elif dialog.backend.name == 'uia':
                pic = dialog.child_window(best_match=element).capture_as_image()

            # 保存预期元素截图
            pic.save(step['snapshot']['expected_element'])

    def windows_shot(self, dialog, step):
        # 定义名为 windows_shot 的方法，接受 dialog 和 step 两个参数

        # 调用自定义的 windwos_capture 方法，传递 dialog 和 step 参数
        self.windwos_capture(dialog, step)

        # 调用自定义的 windwos_check 方法，传递 dialog 和 step 参数
        self.windwos_check(dialog, step)
