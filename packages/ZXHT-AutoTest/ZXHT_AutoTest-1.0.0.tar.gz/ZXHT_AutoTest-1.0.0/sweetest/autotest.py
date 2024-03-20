# -*- coding: utf-8 -*-
"""
@Time : 2024/1/24 17:51
@Author : TJF

"""
import os
import random
import shutil
import time
from pathlib import Path
import sys
import json
import requests
from sweetest.data import testsuite_format, testsuite2data, testsuite2report
from sweetest.parse import parse
from sweetest.elements import e
from sweetest.globals import g
from sweetest.windows import w
from sweetest.testsuite import TestSuite
from sweetest.utility import Excel, get_record, mkdir
from sweetest.log import logger, set_log
from sweetest.junit import JUnit
from sweetest.report import summary, markdown, reporter,case_group
from sweetest.config import _testcase, _elements, _report
from requests_toolbelt import MultipartEncoder


class Autotest:

    def __init__(self, file_name, sheet_name, desired_caps={}, server_url=''):
        # 初始化函数，接受文件名、表格名、设备参数（默认为空字典）和服务器地址（默认为空字符串）作为参数
        if desired_caps:
            self.desired_caps = desired_caps
        else:
            # 如果没有提供设备参数，则使用默认的桌面浏览器配置
            self.desired_caps = {
                'platformName': 'Desktop', 'browserName': 'Chrome'}
        self.server_url = server_url
        self.conditions = {}  # 初始化测试条件字典
        g.plan_name = file_name.split('-')[0]  # 从文件名中提取计划名称
        g.init(self.desired_caps, self.server_url)  # 使用全局变量 g 进行初始化

        # 构建文件和目录路径
        plan_path = Path('snapshot') / g.plan_name
        task_path = plan_path / g.start_time

        for p in ('JUnit', 'report', 'snapshot', plan_path, task_path, 'report/' + g.plan_name):

            mkdir(p)  # 在指定路径下创建目录

        g.plan_data['log'] = set_log(logger, task_path)  # 设置日志记录器

        # 构建测试用例文件、元素文件和测试报告文件的路径
        self.testcase_file = str(
            Path('testcase') / (file_name + '-' + _testcase + '.xlsx'))
        self.elements_file = str(
            Path('element') / (g.plan_name + '-' + _elements + '.xlsx'))
        self.testcase_workbook = Excel(self.testcase_file, 'r')  # 读取测试用例文件
        self.sheet_names = self.testcase_workbook.get_sheet(sheet_name)  # 获取指定表格


        ran  = str(random.randint(10000,99999))
        if str(Path('JUnit') / (file_name + '-' + _report + g.start_time + '.xml')):
            self.report_xml = str(
                Path('JUnit') / (file_name + '-' + _report + g.start_time + '_' + ran + '.xml'))
        else:
            self.report_xml = str(Path('JUnit') / (file_name + '-' + _report + g.start_time + '.xml'))

        if str(Path('report') / g.plan_name / (file_name + '-' + _report + g.start_time + '.xlsx')):
            self.report_excel = str(Path(
                'report') / g.plan_name / (file_name + '-' + _report + g.start_time + '_' + ran + '.xlsx'))
        else:
            self.report_excel = str(Path(
                'report') / g.plan_name / (file_name + '-' + _report + g.start_time + '.xlsx'))

        self.report_workbook = Excel(self.report_excel, 'w')  # 写入测试报告文件
        self.report_filename = str(
            file_name + '-' + _report + g.start_time + '.xlsx')
        self.report_data = {}  # 存储测试报告详细数据的字典



    def fliter(self, **kwargs):
        print('执行了fliter')

        # 筛选要执行的测试用例
        self.conditions = kwargs  # 将传入的筛选条件保存在实例变量中

    # 统计各状态的用例数量，如失败用例数，阻塞用例数
    def case_group_cou(self):
        faicase,blocase = case_group(
            self.plan_data, self.testsuite_data, self.report_data, {})
        return faicase, blocase
    def plan(self):
        self.code = 0  # 返回码

        # 1.解析配置文件
        try:
            e.get_elements(self.elements_file)  # 调用 get_elements 方法解析配置文件
        except:
            logger.exception('*** 解析配置文件失败 ***')
            self.code = -1  # 解析失败时设置返回码为 -1
            sys.exit(self.code)  # 退出程序

        self.junit = JUnit()
        self.junit_suite = {}  # 初始化 JUnit 测试套件字典

        # 2.逐个执行测试套件
        for sheet_name in self.sheet_names:
            g.sheet_name = sheet_name
            # xml 测试报告初始化
            self.junit_suite[sheet_name] = self.junit.create_suite(
                g.plan_name, sheet_name)  # 创建 JUnit 测试套件
            self.junit_suite[sheet_name].start()  # 启动测试套件

            self.run(sheet_name)  # 执行测试

        self.plan_data = g.plan_end()  # 获取测试计划结束数据
        self.testsuite_data = g.testsuite_data  # 获取测试套件数据

        summary_data = summary(
            self.plan_data, self.testsuite_data, self.report_data, {})  # 生成测试总结数据
        self.report_workbook.write(summary_data, '_Summary_')  # 将总结数据写入测试报告
        self.report_workbook.close()  # 关闭测试报告文件

        with open(self.report_xml, 'w', encoding='utf-8') as f:
            self.junit.write(f)  # 将 JUnit 测试报告写入 XML 文件

    def run(self, sheet_name):
        # 1.从 Excel 获取测试用例集
        try:
            data = self.testcase_workbook.read(sheet_name)  # 从测试用例工作簿中读取数据
            testsuite = testsuite_format(data)  # 格式化测试套件数据
            # logger.info('从Excel导入的测试套件:\n' +
            #             json.dumps(testsuite, ensure_ascii=False, indent=4))
            logger.info('从Excel导入测试套件成功')
        except:
            logger.exception('*** 从Excel导入测试套件失败 ***')
            self.code = -1  # 设置返回码为 -1
            sys.exit(self.code)  # 退出程序

        # 2.初始化全局对象
        try:
            g.set_driver()  # 设置全局对象中的驱动
            # 如果测试数据文件存在，则从该文件里读取数据，赋值到全局变量列表里
            data_file = Path('data') / (g.plan_name +
                                        '-' + sheet_name + '.csv')
            if data_file.is_file():
                g.test_data = get_record(str(data_file))  # 从文件中读取测试数据
            w.init()  # 初始化全局对象 w
        except:
            logger.exception('*** 初始化全局对象失败 ***')
            self.code = -1  # 设置返回码为 -1
            sys.exit(self.code)  # 退出程序

        # 3.解析测试用例集
        try:
            parse(testsuite)  # 解析测试套件
            logger.debug('测试套件已解析:\n' + str(testsuite))
        except:
            logger.exception('*** 解析测试套件失败 ***')
            self.code = -1  # 设置返回码为 -1
            sys.exit(self.code)  # 退出程序

        # 4.执行测试套件
        g.ts = TestSuite(testsuite, sheet_name,
                         self.junit_suite[sheet_name], self.conditions)  # 创建 TestSuite 实例
        g.ts.run()  # 执行测试套件

        # 5.判断测试结果
        if self.junit_suite[sheet_name].high_errors + self.junit_suite[sheet_name].medium_errors + \
                self.junit_suite[sheet_name].high_failures + self.junit_suite[sheet_name].medium_failures:
            self.code = -1  # 如果存在高、中错误或失败，设置返回码为 -1

        # 6.保存测试结果
        try:
            data = testsuite2data(testsuite)  # 将测试套件数据转换为报告数据
            self.report_workbook.write(data, sheet_name)  # 将报告数据写入测试报告
            self.report_data[sheet_name] = testsuite2report(testsuite)  # 将测试套件数据转换为测试报告数据
        except:
            logger.exception('*** 保存测试报告失败 ***')



    def report(self, md_path):
        return  markdown(self.plan_data, self.testsuite_data,self.report_data, md_path)

    def report_case(self,):
        return reporter(self.plan_data, self.testsuites_data, self.report_data, self.extra_data)


    # 定义一个函数，用于发送文本消息到飞书机器人
    def sendMessage(status, name):
        print('执行了sendmessage')  # 打印调试信息

        headers = {'content-type': "application/json"}  # 设置请求头，指定内容类型为 JSON
        url = "https://open.feishu.cn/open-apis/bot/v2/hook/6b10abf6-cbd9-4e4e-94c6-aedbabac71d2"  # 飞书机器人的 Webhook URL

        if status == 1:
            result = "测试通过"
        else:
            result = "测试失败"

        # 准备发送的文本消息内容
        content = {
            "msgtype": "text",
            "text": {
                "content": "自动化测试用例：\n" + "用例名：" + name + "\n测试结果：" + result,
                "mentioned_mobile_list": ["18939881330"]  # @提及的手机号列表
            }
        }

        # 发送 POST 请求到飞书机器人 Webhook URL
        requests.post(url=url, data=json.dumps(content), headers=headers)

    # 定义一个函数，用于发送文件消息到飞书机器人
    def sendFile(key, file_id):
        print('执行了sendflie')  # 打印调试信息

        url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"  # 微信企业号的 Webhook URL
        headers = {'content-type': "application/json"}  # 设置请求头，指定内容类型为 JSON

        # 准备发送的文件消息内容
        content = {
            "msgtype": "file",
            "file": {
                "media_id": file_id
            }
        }

        # 发送 POST 请求到微信企业号 Webhook URL
        s = requests.post(url=url, data=json.dumps(content), headers=headers)
        print(s.text)

    # 定义一个函数，用于上传文件并获取文件的 media_id
    def uploadFile(filepath, filename, access_token):
        print('执行了uploadfile')  # 打印调试信息

        post_file_url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={access_token}&type=file"  # 微信企业号的上传文件 URL

        # 使用 MultipartEncoder 封装文件上传的请求体
        m = MultipartEncoder(fields={
            filename: (filename, open(filepath, 'rb'))  # 设置上传文件的字段名和文件内容
        })

        print(m)

        # 发送 POST 请求上传文件
        r = requests.post(url=post_file_url, data=m, headers={'Content-Type': "multipart/form-data"})
        print(r.text)

        # 返回上传文件成功后得到的 media_id
        return r.json()['media_id']

def rm_path():
    path_allure = os.getcwd() + '\\allure-report'
    path_JUnit = os.getcwd() + '\\JUnit'
    path_log = os.getcwd() + '\\log'
    path_report = os.getcwd() + '\\report'
    path_snapshot = os.getcwd() + '\\snapshot'
    for path in (path_allure,path_JUnit, path_report, path_snapshot, path_log):
        if os.path.exists(path):
            shutil.rmtree(path)