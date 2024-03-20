# -*- coding: utf-8 -*-
"""
@Time : 2024/1/24 16:34
@Author : TJF

"""
from copy import deepcopy  # python内部方法
from sweetest.globals import g
from sweetest.elements import e
from sweetest.junit import TestCase
from sweetest.log import logger
from sweetest.parse import data_format
from sweetest.database import DB
from sweetest.utility import replace_dict, compare
from sweetest.injson import check
from sweetest.utility import json2dict


def execute(step):
    # 先处理循环结束条件
    condition = ''
    for k in ('循环结束条件', 'condition', '#break'):
        if step['data'].get(k):
            # 获取循环结束条件
            condition = step['data'].get(k)
            # 从数据中删除该键值对
            del step['data'][k]

    # 将成功和失败映射为标准条件字符串
    if condition.lower() in ('成功', 'success'):
        condition = 'success'
    elif condition.lower() in ('失败', 'failure'):
        condition = 'failure'

    # 执行赋值操作
    data = step['data']
    for k, v in data.items():
        # 更新全局变量
        g.var[k] = v

    # 导入 TestCase 类
    element = step['element']
    times = 1
    _element = element.split('*')

    # snippet 执行失败是否退出标志
    flag = True
    if element[-1] == '*':
        flag = False

    # 循环次数为 N 标志
    n_flag = False
    if len(_element) >= 2:
        element = _element[0]
        if _element[1].upper() == 'N':
            times = 999
            n_flag = True
        else:
            times = int(_element[1])

    # 初始化测试片段执行结果
    result = 'success'  # 初始化整个测试片段的执行结果为成功
    steps = []  # 初始化步骤列表，用于记录测试片段的各个步骤
    testcase = {}  # 初始化测试用例字典

    # 检查当前步骤是否为用例片段或 SNIPPET
    if step['page'] in ('用例片段', 'SNIPPET'):
        g.var['_last_'] = False  # 设置全局变量 '_last_' 为 False，用于记录是否为变量的最后一个值

        # 循环执行指定次数（times）
        for t in range(times):
            # 如果不是第一次循环，则根据给定的数据格式化数据并替换变量
            if t > 0:
                _data = data_format(str(step['_data']))
                replace_dict(_data)
                for k, v in _data.items():
                    g.var[k] = v

            # 深拷贝当前用例片段，以保持原始用例不受影响
            testcase = deepcopy(g.snippet[element])

            # 创建 TestCase 对象，并运行测试用例
            tc = TestCase(testcase)
            tc.run()

            # 更新步骤的编号，以包含循环信息
            for s in testcase['steps']:
                s['no'] = str(step['no']) + '*' + str(t + 1) + '-' + str(s['no'])

            # 将当前用例片段的步骤添加到总步骤列表中
            steps += testcase['steps']

            # 如果用例片段执行失败
            if testcase['result'] != 'success':
                result = testcase['result']  # 更新整个测试片段的执行结果为当前用例片段的执行结果

                # 如果循环退出条件为失败，则直接返回成功和当前用例片段的步骤列表
                if condition == 'failure':
                    return 'success', testcase['steps']

                # 如果没有结束条件且直接退出标志位为真，则返回整个测试片段的执行结果
                if not condition and flag:
                    return result, steps

            # 如果用例片段执行成功
            else:
                # 如果循环退出条件为成功，则直接返回成功和当前用例片段的步骤列表
                if condition == 'success':
                    return 'success', testcase['steps']

            # 如果循环次数为 N 且变量标志位为真，则判断是否是变量的最后一个值，是则退出循环
            if n_flag and g.var['_last_']:
                g.var['_last_'] = False
                break

        # 执行结束，仍未触发循环退出条件，则返回整个测试片段的执行结果为失败
        if condition:
            return 'failure', testcase['steps']
    # 如果当前步骤的页面是 '用例组合' 或 'CASESET'
    elif step['page'] in ('用例组合', 'CASESET'):
        caseset = element  # 获取用例组合的名称

        # 循环执行指定次数（times）
        for t in range(times):
            # 如果不是第一次循环，则根据给定的数据格式化数据并替换变量
            if t > 0:
                _data = data_format(str(step['_data']))
                replace_dict(_data)
                for k, v in _data.items():
                    g.var[k] = v

            # 遍历当前用例组合中的每个测试用例
            for testcase in g.caseset[caseset]:
                testcase = deepcopy(testcase)  # 深拷贝当前测试用例，以保持原始用例不受影响
                testcase['flag'] = ''  # 重置测试用例的标志位
                g.ts.run_testcase(testcase)  # 运行测试用例
                g.casesets.append(testcase)  # 将当前测试用例添加到总测试用例列表

                # 如果希望在此处判断测试用例执行结果并更新整个测试片段的执行结果，可以取消下面的注释
                # if testcase['result'] != 'success':
                #     result = testcase['result']

    # 返回整个测试片段的最终执行结果和步骤列表
    return result, steps


def dedup(text):
    '''
    去掉 text 中括号及其包含的字符
    '''
    _text = ''  # 存储去除括号及其包含字符后的文本
    n = 0  # 记录当前括号的嵌套层数

    # 遍历输入文本的每个字符
    for s in text:
        if s not in ('(', ')'):  # 如果当前字符不是括号
            if n <= 0:
                _text += s  # 若当前不在括号内或者括号已闭合，则添加到结果文本中
        elif s == '(':
            n += 1  # 遇到左括号，增加嵌套层数
        elif s == ')':
            n -= 1  # 遇到右括号，减少嵌套层数

    return _text  # 返回去除括号及其包含字符后的结果文本


def sql(step, var=None):
    response = {}  # 用于存储SQL执行的结果

    element = step['element']  # 从步骤参数中获取要执行的SQL语句的标识
    _sql = e.get(element)[1]  # 从全局配置中获取对应标识的SQL语句

    logger.info('SQL: %s' % repr(_sql))  # 记录SQL语句到日志
    # 获取连接参数
    value = e.get(step['page'] + '-' + 'config')[1]  # 从全局配置中获取连接参数
    arg = data_format(value)  # 格式化连接参数

    if step['page'] not in g.db.keys():
        g.db[step['page']] = DB(arg)  # 如果数据库连接不存在，则创建并存储在全局变量中

    if _sql.lower().startswith('select'):
        row = g.db[step['page']].fetchone(_sql)  # 执行SELECT语句并获取单行结果
        logger.info('SQL response: %s' % repr(row))  # 记录SQL执行结果到日志
        if not row:
            raise Exception('*** Fetch None ***')  # 如果结果为空，抛出异常

    elif _sql.lower().startswith('db.'):
        _sql_ = _sql.split('.', 2)
        collection = _sql_[1]
        sql = _sql_[2]
        response = g.db[step['page']].mongo(collection, sql)  # 执行MongoDB相关操作
        if response:
            logger.info('find result: %s' % repr(response))  # 记录MongoDB查询结果到日志
    else:
        g.db[step['page']].execute(_sql)  # 执行非SELECT语句的SQL操作

    if _sql.lower().startswith('select'):
        text = _sql[6:].split('FROM')[0].split('from')[0].strip()  # 提取SELECT语句中的字段部分
        keys = dedup(text).split(',')  # 去重并拆分字段
        for i, k in enumerate(keys):
            keys[i] = k.split(' ')[-1]  # 提取字段名称
        response = dict(zip(keys, row))  # 将字段和对应的值组成字典
        logger.info('select result: %s' % repr(response))  # 记录SELECT语句执行结果到日志

    expected = step['data']  # 从步骤参数中获取预期结果数据
    if not expected:
        expected = step['expected']  # 如果没有预期数据，则从步骤参数中获取

    if 'json' in expected:
        expected['json'] = json2dict(expected.get('json', '{}'))  # 将预期的JSON数据转换为字典
        result = check(expected.pop('json'), response['json'])  # 检查实际结果和预期JSON数据的一致性
        logger.info('json check result: %s' % result)  # 记录JSON检查结果到日志
        if result['code'] != 0:
            raise Exception(
                f'json | EXPECTED:{repr(expected["json"])}, REAL:{repr(response["json"])}, RESULT: {result}')  # 如果不一致，抛出异常
        elif result['var']:
            var = dict(var, **result['var'])  # 更新全局变量中的变量
            g.var = dict(g.var, **result['var'])  # 更新全局变量
            logger.info('json var: %s' % (repr(result['var'])))  # 记录JSON中提取的变量到日志

    if expected:
        for key in expected:
            sv, pv = expected[key], response[key]
            logger.info('key: %s, expect: %s, real: %s' %
                        (repr(key), repr(sv), repr(pv)))

            compare(sv, pv)  # 比较预期值和实际值

    output = step['output']  # 获取输出参数
    if output:
        _output = {}
        for k, v in output.items():
            if k == 'json':
                sub = json2dict(output.get('json', '{}'))  # 将输出的JSON数据转换为字典
                result = check(sub, response['json'])  # 检查实际结果和输出JSON数据的一致性
                # logger.info('Compare json result: %s' % result)
                var = dict(var, **result['var'])  # 更新全局变量中的变量
                g.var = dict(g.var, **result['var'])  # 更新全局变量
                logger.info('json var: %s' % (repr(result['var'])))  # 记录JSON中提取的变量到日志
            else:
                _output[k] = response[v]
                g.var[k] = response[v]
        logger.info('output: %s' % repr(_output))  # 记录输出结果到日志
