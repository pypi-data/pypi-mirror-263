# -*- coding: utf-8 -*-
"""
@Time : 2024/1/24 17:29
@Author : TJF

"""
from sweetest.utility import Excel, data2dict
from sweetest.config import header
from sweetest.globals import g


def testsuite_format(data):
    '''
    将元素为 dict 的 list，处理为 testcase 的 list
    testcase 的格式：
    {
        'id': 'Login_001',  #用例编号
        'title': 'Login OK',  #用例标题
        'condition': '',  #前置条件
        'designer': 'Leo',  #设计者
        'flag': '',  #自动化标记
        'result': '',  #用例结果
        'remark': '',  #备注
        'steps':
            [
                {
                'no': 1,  #测试步骤
                'keyword': '输入',
                'page': '产品管系统登录页',
                'element': '用户名',
                'data': 'user1',  #测试数据
                'output': '',  #输出数据
                'score': '',  #测试结果
                'remark': ''  #备注
                },
                {……}
                ……
            ]
    }
    '''

    # 初始化一个空的测试套件列表
    testsuite = []

    # 初始化一个测试用例字典
    testcase = {'testsuite': '', 'no': 0}

    # 将输入数据转换成字典格式
    data = data2dict(data)

    for d in data:
        # 如果用例编号不为空，则为新的用例
        if d['id'].strip():
            # 如果 testcase[id] 非空，则添加到 testsuite 里，并重新初始化 testcase
            if testcase.get('id'):
                testsuite.append(testcase)
                testcase = {'testsuite': '', 'no': 0}

            # 将用例的基本信息（id、title、condition等）添加到 testcase 字典中
            for key in ('id', 'title', 'condition', 'designer', 'flag', 'result', 'remark'):
                testcase[key] = d[key]

            # 如果用例编号包含 '#'，则解析 set 和 flag，并设置默认的 priority 为 'M'
            if '#' in d['id']:
                testcase['set'] = d['id'].split('#')[0]
                testcase['flag'] = 'N'
            testcase['priority'] = d['priority'] if d['priority'] else 'M'
            testcase['steps'] = []

        # 如果测试步骤不为空，则为有效步骤，否则用例解析结束
        no = str(d['step']).strip()
        if no:
            step = {}
            step['control'] = ''

            # 判断步骤编号的类型，设置 control 和 no 字段
            if no[0] in ('^', '>', '<', '#'):
                step['control'] = no[0]
                step['no'] = no
            else:
                step['no'] = str(int(d['step']))

            # 将步骤的关键信息（keyword、page、element等）添加到 step 字典中
            for key in ('keyword', 'page', 'element', 'data', 'expected', 'output', 'score', 'remark'):
                step[key] = d.get(key, '')

            # 仅作为测试结果输出时，保持原样
            step['_keyword'] = d['keyword']
            step['_element'] = d['element']
            step['_data'] = d['data']
            step['vdata'] = d.get('data', '')
            step['_expected'] = d.get('expected', '')
            step['_output'] = d.get('output', '')

            # 将当前步骤添加到当前用例的步骤列表中
            testcase['steps'].append(step)

    # 将最后一个用例添加到 testsuite 中
    if testcase:
        testsuite.append(testcase)

    # 返回最终的测试套件列表
    return testsuite


def testsuite_from_excel(file_name, sheet_name):
    # 从Excel文件中读取数据
    d = Excel(file_name)

    # 将读取的数据转换成特定格式的测试套件
    return testsuite_format(data2dict(d.read(sheet_name)))


def testsuite2data(data):
    # 初始化结果列表，包含测试套件的表头
    result = [[g.header_custom[key.lower()] for key in header.values()]]

    # 遍历测试套件中的每个测试用例
    for d in data:
        # 获取测试用例的第一步（通常是标题和第一步合并的）
        s = d['steps'][0]

        # 构建测试用例的行数据
        testcase = [d['id'], d['title'], d['condition'], s['no'], s['_keyword'], s['page'], s['_element'],
                    s['vdata'], s['_output'], d['priority'], d['designer'], d['flag'], s['score'], d['result'],
                    s['remark']]

        # 如果表头中有'expected'字段，则插入预期结果数据
        if g.header_custom['expected']:
            testcase.insert(8, s['_expected'])

        # 将测试用例的行数据添加到结果列表中
        result.append(testcase)

        # 处理测试用例的其余步骤（除了第一步）
        for s in d['steps'][1:]:
            step = ['', '', '', s['no'], s['_keyword'], s['page'], s['_element'],
                    s['vdata'], s['_output'], '', '', '', s['score'], '', s['remark']]

            # 如果表头中有'expected'字段，则插入预期结果数据
            if g.header_custom['expected']:
                step.insert(8, s['_expected'])

            # 将步骤的行数据添加到结果列表中
            result.append(step)

    # 返回最终的结果列表
    return result


def testsuite2report(data):
    # 初始化报告列表
    report = []

    # 遍历测试套件中的每个测试用例
    for case in data:
        # 如果测试用例的条件为'BASE'或'SETUP'，或者标记不为'N'，则处理该用例
        if case['condition'] in ('BASE', 'SETUP') or case['flag'] != 'N':
            # 遍历测试用例的每个步骤
            for step in case['steps']:
                # 重命名步骤中的关键字、元素等字段
                step['keyword'] = step.pop('_keyword')
                step['element'] = step.pop('_element')
                step['data'] = str(step.pop('vdata'))
                step['expected'] = step.pop('_expected')
                step['output'] = step.pop('_output')

            # 将处理后的测试用例添加到报告列表中
            report.append(case)

    # 返回最终的报告列表
    return report
