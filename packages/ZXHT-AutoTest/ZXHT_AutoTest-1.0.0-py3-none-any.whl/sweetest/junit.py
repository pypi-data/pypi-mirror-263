# -*- coding: utf-8 -*-
"""
@Time : 2024/1/24 17:10
@Author : TJF

"""
from datetime import datetime
from xml.dom.minidom import Document

class TestCase():
    def __init__(self, name, classname):
        # 初始化TestCase对象，设置测试用例的属性和初始状态
        self.state = None  # 测试用例的状态，初始为None
        self.name = name  # 测试用例的名称
        self.classname = classname  # 测试用例所属的类名
        self.priority = 'M'  # 测试用例的优先级，默认为'M'

    def start(self):
        # 开始执行测试用例的方法
        self.time = datetime.now()  # 记录测试用例开始执行的时间
        return self  # 返回测试用例对象自身

    def custom(self, state, type, message):
        # 自定义测试用例状态的方法，包括失败、跳过、错误和阻塞
        if self.state is not None:
            raise Exception("This test case is already finished.")
        self.state = state  # 设置测试用例的状态
        self.message = message  # 设置测试用例的消息
        self.type = type  # 设置测试用例的类型
        td = datetime.now() - self.time
        # 计算测试用例执行的时间并保存
        self.time = float(
            (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10 ** 6)) / 10 ** 6

    def fail(self, type, message):
        # 测试用例执行失败的方法
        self.custom("failure", type, message)

    def skip(self, type, message):
        # 测试用例跳过的方法
        self.custom("skipped", type, message)

    def error(self, type, message):
        # 测试用例执行出错的方法
        self.custom("error", type, message)

    def block(self, type, message):
        # 测试用例被阻塞的方法
        self.custom("blocked", type, message)

    def succeed(self):
        # 测试用例执行成功的方法
        if self.state is not None:
            raise Exception("This test case is already finished.")
        self.state = "success"  # 设置测试用例状态为成功
        td = datetime.now() - self.time
        # 计算测试用例执行的时间并保存
        self.time = float(
            (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10 ** 6)) / 10 ** 6

    def to_xml(self, doc):
        # 将测试用例信息转换为XML格式的方法
        node = doc.createElement("testcase")
        node.setAttribute("name", self.name)
        node.setAttribute("classname", self.classname)
        node.setAttribute("priority", self.priority)
        node.setAttribute("time", "%s" % self.time)
        if self.state != "success":
            # 如果测试用例状态不是成功，则添加相应的子节点
            subnode = doc.createElement(self.state)
            subnode.setAttribute("type", self.type)
            subnode.setAttribute("message", self.message)
            node.appendChild(subnode)
        return node



class TestSuite():
    def __init__(self, name, hostname):
        # 初始化TestSuite对象，设置测试套件的属性和初始状态
        self.properties = []  # 存储测试套件的属性
        self.name = name  # 测试套件的名称
        self.hostname = hostname  # 测试套件运行的主机名
        self.open = False  # 测试套件的状态，是否处于打开状态
        self.cases = []  # 存储测试套件中的测试用例
        self.systemout = None  # 用于存储测试套件的标准输出
        self.systemerr = None  # 用于存储测试套件的标准错误

    def start(self):
        # 开始测试套件的方法
        self.open = True  # 将测试套件状态设置为打开
        self.time = datetime.now()  # 记录测试套件开始的时间
        self.timestamp = datetime.isoformat(self.time)  # 将时间格式化为ISO格式
        return self  # 返回测试套件对象自身

    def create_case(self, name, classname=""):
        # 创建测试用例的方法
        if self.open:
            # 如果测试套件处于打开状态
            case = TestCase(name, classname)  # 使用TestCase类创建一个测试用例对象
            self.cases.append(case)  # 将创建的测试用例添加到测试套件中
            return case  # 返回新创建的测试用例对象
        else:
            # 如果测试套件不处于打开状态，抛出异常
            raise Exception(
                "This test suite cannot be modified in its current state")

    def append_property(self, name, value):
        # 向测试套件添加属性的方法
        self.properties.append([name, value])  # 将属性名称和值作为列表添加到属性列表中

    def finish(self, output=None, error=None):
        # 如果测试处于打开状态
        if self.open == True:
            # 关闭测试状态
            self.open = False

            # 计算测试所花费的时间
            td = datetime.now() - self.time
            self.time = float((td.microseconds + (td.seconds + td.days * 24 * 3600) * 10 ** 6)) / 10 ** 6

            # 重置各项统计数据
            self.errors = 0
            self.high_errors = 0
            self.medium_errors = 0
            self.low_errors = 0
            self.failures = 0
            self.high_failures = 0
            self.medium_failures = 0
            self.low_failures = 0
            self.skipped = 0
            self.disabled = 0
            # 遍历测试用例列表
            for case in self.cases:
                # 检查测试用例状态是否为None
                if case.state == None:
                    # 如果是，记录错误并强制结束测试
                    case.error("XmlUnit Finished", "测试由于测试套件已完成而被强制结束。")

                # 获取测试用例状态并转换为小写
                status = case.state.lower()

                # 根据状态进行统计
                if status == "failure":
                    self.failures += 1
                    # 根据优先级增加相应计数
                    if case.priority == 'H':
                        self.high_failures += 1
                    elif case.priority == 'M':
                        self.medium_failures += 1
                    elif case.priority == 'L':
                        self.low_failures += 1
                elif status == "error":
                    self.errors += 1
                    # 根据优先级增加相应计数
                    if case.priority == 'H':
                        self.high_errors += 1
                    elif case.priority == 'M':
                        self.medium_errors += 1
                    elif case.priority == 'L':
                        self.low_errors += 1
                elif status == "skipped":
                    self.skipped += 1
                elif status == "blocked":
                    self.disabled += 1
                else:
                    pass  # 其他状态不进行处理

            # 统计测试用例总数
            self.tests = len(self.cases)

            # 设置输出和错误信息
            self.output = output
            self.error = error

            # 返回None表示函数执行完毕
            return None
        else:
            # 如果测试套件已完成，抛出异常
            raise Exception("This test suite is already finished.")

    def to_xml(self, doc):
        # 创建一个名为 "testsuite" 的XML节点
        node = doc.createElement("testsuite")

        # 设置 "testsuite" 节点的属性
        node.setAttribute("name", self.name)
        node.setAttribute("hostname", self.hostname)
        node.setAttribute("timestamp", self.timestamp)
        node.setAttribute("tests", "%s" % self.tests)

        # 设置失败相关属性，包括总数和详细信息
        node.setAttribute("failures", "%s" % self.failures)
        node.setAttribute("failures_detail", "H:%s M:%s L:%s" % (
            self.high_failures, self.medium_failures, self.low_failures))

        # 设置错误相关属性，包括总数和详细信息
        node.setAttribute("errors", "%s" % (self.errors + self.skipped + self.disabled))
        node.setAttribute("errors_detail", "H:%s M:%s L:%s" % (
            self.high_errors, self.medium_errors, self.low_errors))

        # 设置执行时间属性
        node.setAttribute("time", "%s" % self.time)

        # 设置跳过和禁用的测试用例数属性
        node.setAttribute("skipped", "%s" % self.skipped)
        node.setAttribute("disabled", "%s" % self.disabled)

        # 遍历测试用例列表，将每个测试用例的XML节点添加到 "testsuite" 节点下
        for case in self.cases:
            node.appendChild(case.to_xml(doc))

        # 返回构建好的 "testsuite" 节点
        return node


class JUnit():
    def __init__(self):
        # 初始化JUnit对象，创建一个空的测试套件列表
        self.testsuites = []

    def create_suite(self, name, hostname="localhost"):
        # 创建测试套件的方法，接受套件名称和主机名参数，默认为"localhost"
        suite = TestSuite(name, hostname)
        # 使用TestSuite类创建一个测试套件对象
        self.testsuites.append(suite)
        # 将创建的测试套件添加到JUnit对象的测试套件列表中
        return suite
        # 返回新创建的测试套件对象

    def finish(self):
        # 完成测试套件的方法
        for suite in self.testsuites:
            # 遍历JUnit对象的测试套件列表
            if suite.open == True:
                # 如果测试套件的open属性为True（表示测试套件还未结束）
                suite.finish()
                # 调用测试套件的finish方法，完成测试套件的结束操作

    def write(self, file):
        # 写入测试结果到文件的方法
        self.finish()
        # 确保所有测试套件都已经结束
        doc = Document()
        # 创建一个XML文档对象
        root = doc.createElement("testsuites")
        # 创建根节点为"testsuites"
        doc.appendChild(root)
        # 将根节点添加到XML文档中
        for suite in self.testsuites:
            # 遍历JUnit对象的测试套件列表
            root.appendChild(suite.to_xml(doc))
            # 将测试套件的XML表示添加到根节点下
        file.write(doc.toprettyxml())
        # 将XML文档内容写入文件，使用漂亮的格式

