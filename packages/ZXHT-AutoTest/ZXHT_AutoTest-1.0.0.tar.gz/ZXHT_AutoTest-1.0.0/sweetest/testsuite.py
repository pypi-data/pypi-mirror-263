# -*- coding: utf-8 -*-
"""
@Time : 2024/1/10 13:45
@Author : TJF

"""
from copy import deepcopy
from sweetest.globals import g, timestamp
from sweetest.testcase import TestCase
from sweetest.log import logger


class TestSuite:
    def __init__(self, testsuite, sheet_name, report, conditions={}):
        self.testsuite = testsuite
        self.sheet_name = sheet_name
        self.report = report
        self.conditions = conditions
        self.result = {}

        # base 在整个测试套件中首先执行一次
        self.base_testcase = {}
        # setup 在每个测试用例执行之前执行一次
        self.setup_testcase = {}
        for testcase in self.testsuite:
            # 如果测试用例的条件为 'base'，将其设置为基础测试用例
            if testcase['condition'].lower() == 'base':
                self.base_testcase = testcase
            # 如果测试用例的条件为 'setup'，将其设置为设置测试用例，并将其标记为 'N'（不执行）
            elif testcase['condition'].lower() == 'setup':
                self.setup_testcase = testcase
                testcase['flag'] = 'N'  # setup 用例只在执行其他普通用例之前执行
            # 如果测试用例的条件为 'snippet'，将其添加到全局变量 g.snippet 中，并标记为 'N'
            elif testcase['condition'].lower() == 'snippet':
                g.snippet[testcase['id']] = testcase
                testcase['flag'] = 'N'
            # 如果测试用例具有 'set' 属性
            elif testcase.get('set'):
                testcase['flag'] = 'N'
                # 如果测试用例集合中不存在该集合，创建该集合并将测试用例添加到集合中
                if testcase['set'] not in g.caseset:
                    g.caseset[testcase['set']] = [testcase]
                # 如果测试用例集合已经存在，将测试用例添加到集合中
                else:
                    g.caseset[testcase['set']].append(testcase)

        # 测试套件开始的方法
    def testsuite_start(self):
        # 将全局变量 g.no 赋值给测试结果字典的 'no' 键
        self.result['no'] = g.no
        # 全局变量 g.no 自增 1，以准备为下一个测试套件分配编号
        g.no += 1
        # 将测试套件的名称赋值给测试结果字典的 'testsuite' 键
        self.result['testsuite'] = self.sheet_name
        # 获取当前时间戳并赋值给测试结果字典的 'start_timestamp' 键
        self.result['start_timestamp'] = timestamp()

        # 测试套件结束的方法
    def testsuite_end(self):
        # 获取当前时间戳并赋值给测试结果字典的 'end_timestamp' 键
        self.result['end_timestamp'] = timestamp()
        # 将测试结果字典添加到全局变量 g.testsuite_data 中，键为当前测试套件的名称
        g.testsuite_data[self.sheet_name] = self.result

        # 设置测试方法，用于执行测试用例的设置操作
    def setup(self, testcase, case):
        # 如果存在设置测试用例
        if self.setup_testcase:
            # 打印设置测试用例开始的日志信息
            logger.info('*** 设置测试用例 ↓ ***')
            logger.info('-' * 50)
        else:
            # 打印没有需要运行的设置测试用例的日志信息
            logger.info('...没有需要运行的设置测试用例...')

        # 定义运行设置操作的内部函数
        def run_setup(testcase):
            # 如果存在测试用例
            if testcase:
                # 创建测试用例对象
                tc = TestCase(testcase)
                # 运行测试用例
                tc.run()
                # 判断测试用例的执行结果，设置标志
                if testcase['result'] == 'success':
                    flag = 'Y'
                else:
                    flag = 'N'
            else:
                # 如果测试用例不存在，标志设置为'O'
                flag = 'O'
            return flag

        # 运行设置测试用例并获取结果标志
        setup_flag = run_setup(deepcopy(self.setup_testcase))

        # 如果设置测试用例执行失败
        if setup_flag == 'N':
            # 运行基础测试用例，并获取结果标志
            base_flag = run_setup(deepcopy(self.base_testcase))

            # 如果基础测试用例执行成功
            if base_flag == 'Y':
                # 再次运行设置测试用例
                setup_flag = run_setup(deepcopy(self.setup_testcase))

                # 如果再次执行设置测试用例失败
                if setup_flag == 'N':
                    # 将当前测试用例标记为阻塞，记录日志
                    testcase['result'] = 'blocked'
                    case.block('Blocked', 'SETUP执行失败')
                    logger.info('-' * 50)
                    logger.info(f'>>> 运行测试用例: {testcase["id"]}|{testcase["title"]}')
                    logger.warn('>>>>>>>>>>>>>>>>>>>> 阻塞 <<<<<<<<<<<<<<<<<<<< SETUP执行失败')
                    return False
            # 如果基础测试用例标志为'O'
            elif base_flag == 'O':
                # 将当前测试用例标记为阻塞，记录日志
                testcase['result'] = 'blocked'
                case.block('Blocked', 'SETUP执行失败')
                logger.info('-' * 50)
                logger.info(f'>>> 运行测试用例: {testcase["id"]}|{testcase["title"]}')
                logger.warn('>>>>>>>>>>>>>>>>>>>> 阻塞 <<<<<<<<<<<<<<<<<<<< SETUP执行失败')
                return False

        # 如果设置测试用例执行成功，返回True
        return True

    def run_testcase(self, testcase):
        # 根据筛选条件，把不需要执行的测试用例跳过
        flag = False
        # 遍历条件字典
        for k, v in self.conditions.items():
            # 如果条件值不是列表，转换为列表形式
            if not isinstance(v, list):
                v = [v]
            # 如果测试用例的条件值不在条件列表中，则将测试用例标记为跳过，并设置标志为True
            if testcase[k] not in v:
                testcase['result'] = 'skipped'
                flag = True
        # 如果有测试用例被跳过，则直接返回
        if flag:
            return

        # 如果测试用例的条件为'base'，记录日志
        if testcase['condition'].lower() == 'base':
            logger.info('*** 基本测试用例 ↓ ***')

        # 如果测试用例的条件为'setup'，直接返回，不执行
        if testcase['condition'].lower() == 'setup':
            return

        # 统计开始时间
        testcase['start_timestamp'] = timestamp()
        # xml 测试报告-测试用例初始化
        if testcase['flag'] != 'N':
            # 如果前置条件失败了，直接设置为阻塞
            if self.blocked_flag:
                testcase['result'] = 'blocked'
                testcase['end_timestamp'] = timestamp()
                return

            # 创建测试报告中的测试用例
            case = self.report.create_case(testcase['title'], testcase['id'])
            case.start()
            case.priority = testcase['priority']
            # 设置测试用例的上下文
            self.previous = self.current
            self.current = testcase
        else:
            # 如果测试用例的标志为'N'，将结果标记为跳过
            testcase['result'] = 'skipped'
            # 记录日志或其他信息
            # case.skip('Skip', 'Autotest Flag is N')
            # logger.info('Run the testcase: %s|%s skipped, because the flag=N or the condition=snippet' % (
            #     testcase['id'], testcase['title']))
            # 统计结束时间
            testcase['end_timestamp'] = timestamp()
            return

        # 检查测试用例的执行条件是否在 ('base', 'setup') 之外
        if testcase['condition'].lower() not in ('base', 'setup'):
            # 如果条件为 'sub'
            if testcase['condition'].lower() == 'sub':
                # 检查前一个用例的执行结果是否为 'success'
                if self.previous['result'] != 'success':
                    # 如果前一个用例执行结果不为 'success'，则将当前用例结果标记为 'blocked'
                    testcase['result'] = 'blocked'
                    case.block(
                        'Blocked', 'Main or pre Sub testcase is not success')
                    logger.info('-' * 50)
                    logger.info(f'>>> Run the testcase: {testcase["id"]}|{testcase["title"]}')
                    logger.warn(
                        '>>>>>>>>>>>>>>>>>>>> blocked <<<<<<<<<<<<<<<<<<<< Main or pre Sub TestCase is not success')
                    # 统计结束时间
                    testcase['end_timestamp'] = timestamp()
                    return
            # 如果条件为 'skip'
            elif testcase['condition'].lower() == 'skip':
                # 如果前置条件为 skip，则此用例不执行前置条件，直接跳过
                pass
            else:
                # 调用 setup 方法执行前置条件，并获取结果
                result = self.setup(testcase, case)
                # 如果前置条件执行结果为 False（not result），则直接返回，不执行当前用例
                if not result:
                    # 统计结束时间
                    testcase['end_timestamp'] = timestamp()
                    return

        try:
            # 创建 TestCase 对象，传入测试用例信息
            tc = TestCase(testcase)
            # 记录测试用例执行开始
            logger.info('-' * 50)
            # 运行测试用例
            tc.run()

            # 统计结束时间
            testcase['end_timestamp'] = timestamp()

            # 根据测试用例执行结果进行相应处理
            if testcase['result'] == 'success':
                # 如果测试用例执行成功，标记为成功
                case.succeed()
            elif testcase['result'] == 'failure':
                # 如果测试用例执行失败，标记为失败，并记录失败信息
                case.fail('Failure', testcase['report'])

                # 根据前置条件进行处理
                if testcase['condition'].lower() == 'base':
                    logger.warn('Run the testcase: %s|%s Failure, BASE is not success. Break the AutoTest' % (
                        testcase['id'], testcase['title']))
                    # 设置 blocked_flag 为 True，中断 AutoTest 的执行
                    self.blocked_flag = True
                    return
                if testcase['condition'].lower() == 'setup':
                    logger.warn('Run the testcase: %s|%s failure, SETUP is not success. Break the AutoTest' % (
                        testcase['id'], testcase['title']))
                    # 设置 blocked_flag 为 True，中断 AutoTest 的执行
                    self.blocked_flag = True
                    return
        except Exception as exception:
            # 如果测试用例执行过程中出现异常，记录错误信息
            case.error('Error', 'Remark:%s |||Exception:%s' % (testcase['remark'], exception))
            logger.exception('Run the testcase: %s|%s failure' % (testcase['id'], testcase['title']))

            # 根据前置条件进行处理
            if testcase['condition'].lower() == 'base':
                logger.warn('Run the testcase: %s|%s error, BASE is not success. Break the AutoTest' % (
                    testcase['id'], testcase['title']))
                # 设置 blocked_flag 为 True，中断 AutoTest 的执行
                self.blocked_flag = True
                return
            if testcase['condition'].lower() == 'setup':
                logger.warn('Run the testcase: %s|%s error, SETUP is not success. Break the AutoTest' % (
                    testcase['id'], testcase['title']))
                # 设置 blocked_flag 为 True，中断 AutoTest 的执行
                self.blocked_flag = True
                return

    def run(self):
        # 执行测试套件开始阶段的初始化操作
        self.testsuite_start()

        # 当前测试用例，初始化为成功
        self.current = {'result': 'success'}
        # 上一个测试用例的信息
        self.previous = {}

        # 前置条件执行失败标志，即未执行用例阻塞标志
        self.blocked_flag = False

        # 遍历测试套件中的每个测试用例进行执行
        for testcase in self.testsuite:
            self.run_testcase(testcase)

        # 完成测试报告的生成
        self.report.finish()

        # 将用例组合执行结果添加到测试套件末尾
        self.testsuite += g.casesets

        # 清理环境阶段
        try:
            # 根据平台类型执行相应的清理操作
            if g.platform.lower() in ('desktop',):
                # 关闭窗口或退出驱动程序
                # w.close()  # 注释掉的代码，可能是关闭窗口的操作
                g.driver.quit()
                logger.info('--- Quit the Driver: %s' % g.browserName)
        except:
            # 记录清理环境操作失败的异常信息
            logger.exception('Clear the environment is failed')

        # 执行测试套件结束阶段的收尾工作
        self.testsuite_end()
