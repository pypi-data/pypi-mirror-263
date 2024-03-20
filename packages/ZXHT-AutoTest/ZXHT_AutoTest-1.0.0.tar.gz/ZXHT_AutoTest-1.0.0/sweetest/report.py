# -*- coding: utf-8 -*-
"""
@Time : 2024/1/24 17:41
@Author : TJF

"""
import time
import random

import arrow
from pathlib import Path
from sweetest.globals import g
from sweetest.utility import mkdir

md_file_name = None
md_file_path = None
def reporter(plan_data, testsuites_data, report_data, extra_data):
    # 将计划数据和额外数据添加到额外数据字典中
    extra_data['plan'] = plan_data['plan']
    extra_data['task'] = int(time.time() * 1000)

    # 存储所有测试用例的列表
    testcases = []
    blocase = []
    faicase = []
    # print('this is report_data:', report_data)

    # 遍历报告数据中的每个测试套件
    for key, ts in report_data.items():
        # print('this is key:',key)
        # print('this is ts:',ts[0]['title'])
        # if ts[0]['result'] == 'failure':
        #     faicase.append(ts[0]['title'])
        # print('this is report_data.items():' ,report_data.items())
        # 初始化计数器，记录测试结果的数量
        count = {'result': 'success', 'total': 0, 'success': 0, 'failure': 0, 'blocked': 0}
        no = 1  # 用于记录测试用例编号

        # 遍历测试套件中的每个测试用例
        for tc in ts:
            if tc['result'] == 'failure':
                faicase.append(tc['title'])
            if tc['result'] == 'blocked':
                blocase.append(tc['title'])
            # print('this is faicase', faicase)
            # print('this is blocase', blocase)
            # 将测试套件和编号添加到测试用例中
            tc['testsuite'] = key
            tc['no'] = no
            no += 1

            # 将额外数据和测试用例合并
            tc = {**extra_data, **tc}

            # 获取测试结果，并更新计数器
            res = tc['result'].lower()
            if tc['condition'].lower() in ('base', 'setup', 'snippet'):
                pass  # 忽略基础、设置和代码片段的条件
            elif res in count:
                count[res] += 1
                count['total'] += 1

            # 将测试用例添加到列表中
            testcases.append(tc)

            # 如果有失败或阻塞的测试用例，将结果标记为失败
            if count['failure'] + count['blocked']:
                count['result'] = 'failure'

        # 更新测试套件数据字典
        testsuites_data[key] = {**count, **testsuites_data[key]}

    # 存储所有测试套件的列表
    testsuite = []

    # 初始化总计数器
    count = {'total': 0, 'success': 0, 'failure': 0, 'blocked': 0}
    result = 'success'

    # 遍历测试套件数据字典
    for key, ts in testsuites_data.items():
        # 更新总计数器
        for k in count:
            count[k] += ts[k]

        # 如果测试套件结果不是成功，则将整体结果标记为失败
        if ts['result'] != 'success':
            result = 'failure'

        # 合并额外数据和测试套件数据
        ts = {**extra_data, **ts}
        ts['testsuite'] = key

        # 将测试套件添加到列表中
        testsuite.append(ts)

    # 更新总计数器的结果字段
    count['result'] = result

    # 合并额外数据、总计数器和计划数据
    plan = {**extra_data, **count, **plan_data}

    # 返回合并后的计划、测试套件和测试用例数据
    return plan, testsuite, testcases,faicase,blocase


def local_time(timestamp):
    # Import the time module
    import time

    # Convert timestamp to local time
    t = time.localtime(int(timestamp / 1000))

    # Format local time as a string in the specified format
    return str(time.strftime("%Y/%m/%d %H:%M:%S", t))


def cost_time(start, end):
    # Calculate the time difference between end and start in seconds
    return int((end - start) / 1000)


# 定义一个函数，用于转义特定字符
def escape(data, well='#'):
    return data.replace('|', '\|').replace('<', '\<').replace('>', '\>').replace('\n', '<br>').replace('#', well)


# 定义一个函数，用于格式化时间戳并进行替换
def tm(stamp, dot=' '):
    # 判断dot的值，选择不同的时间格式
    if dot == ' ':
        # 使用arrow库将时间戳转换为本地时间，并按指定格式格式化，同时替换冒号为HTML实体
        return arrow.get(stamp / 1000).to('local').format(f'YYYY-MM-DD{dot}HH:mm:ss').replace(':', '&#58;')
    elif dot == '_':
        # 使用arrow库将时间戳转换为本地时间，并按指定格式格式化，同时去除冒号
        return arrow.get(stamp / 1000).to('local').format(f'YYYYMMDD{dot}HH:mm:ss').replace(':', '')

#统计各状态的用例数量，如失败用例数，阻塞用例数
def case_group(plan_data, testsuites_data, report_data, extra_data):
    plan, testsuites, testcases,faicase,blocase = reporter(
        plan_data, testsuites_data, report_data, extra_data)
    return faicase, blocase

def summary(plan_data, testsuites_data, report_data, extra_data):
    # Call the 'reporter' function to get plan, testsuites, and testcases data
    plan, testsuites, testcases,faicase,blocase = reporter(
        plan_data, testsuites_data, report_data, extra_data)

    # Initialize lists to store summary data and failure details
    data = [['测试套件', '用例总数', '成功', '阻塞', '失败', '测试结果', '开始时间', '结束时间', '耗时(秒)']]
    failures = [['测试套件', '用例编号', '用例标题', '用例结果', '失败步骤', '备注']]

    # Loop through testsuites data and populate the 'data' list
    for suite in testsuites:
        row = [suite['testsuite'], suite['total'], suite['success'], suite['blocked'], suite['failure'],
               suite['result'], local_time(suite['start_timestamp']), local_time(suite['end_timestamp']),
               cost_time(suite['start_timestamp'], suite['end_timestamp'])]
        data.append(row)
        # print('this is data:',data)
        # print('this is suite[total]:',suite['total'])
        # print('this is suite[success]:',suite['success'])
        # print('this is suite[blocked]:',suite['blocked'])
        # print('this is suite[failure]:',suite['failure'])
        # print('this is suite[result]:',suite['result'])

    # Initialize a flag to track whether failure details header is added
    flag = False

    # Loop through testcases data and populate the 'failures' list
    for case in testcases:
        suite_name = '' if flag else case['testsuite']
        row = []

        # Check if the case result is 'blocked'
        if case['result'] == 'blocked':
            row = [suite_name, case['id'], case['title'], case['result']]
        # Check if the case result is 'failure'
        elif case['result'] == 'failure':
            for step in case['steps']:
                # Find the first step with a score of 'NO' and extract details
                if step['score'] == 'NO':
                    desc = '|'.join([step[k] for k in ('no', 'keyword', 'page', 'element')])
                    row = [suite_name, case['id'], case['title'], case['result'], desc, step['remark']]
                    break

        # If row is populated, set the flag to True and add to 'failures' list
        if row:
            flag = True
            failures.append(row)

    # Add separator and total summary to 'data' list
    data.append(['--------'])
    total = ['总计', plan['total'], plan['success'], plan['blocked'], plan['failure'],
             plan['result'], local_time(plan['start_timestamp']), local_time(plan['end_timestamp']),
             cost_time(plan['start_timestamp'], plan['end_timestamp'])]

    data.append(total)

    # If there are failures, add separator and failure details to 'data' list
    if len(failures) > 1:
        data.append(['********'])
        data += failures

    # Return the final summary data
    return data


def markdown(plan, testsuites, testcases, md_path='markdown'):
    ran = str(random.randint(10000, 99999))
    global md_file_name,md_file_path
    # print('this is testcases:', testcases)
    # 定义一些状态对应的HTML格式字符串
    # success = OK = '<font color=#00ff00>通过</font>'
    # failure = NO = '<font color=#FF0000>失败</font>'
    # blocked = '<font color=#FFD306>阻塞</font>'
    # skipped = '<font color=#6C6C6C>-</font>'

    success = OK = "**通过**"
    failure = NO = '**失败**'
    blocked = '**阻塞**'
    skipped = '<**跳过**'

    # 初始化Markdown字符串，包含表头
    md = '| 测试套件名称 | 开始时间 | 结束时间 | 耗时 | 成功个数 | 失败个数 | 阻塞个数 | 总个数 | 结果 |\n'
    md += '| ----------- | ------- | ------- | ---- | ------- | ------- | -------- | ----- | ---- |\n'

    # 初始化一些统计变量
    result = success
    sc, fc, bc, tc = 0, 0, 0, 0

    # 遍历测试套件
    for v in testsuites.values():
        # print('this is v',v)
        # 统计各种状态的数量
        sc += v['success']
        fc += v['failure']
        bc += v['blocked']
        tc += v['total']

        # 根据测试套件的执行结果设置对应的结果字符串
        re = success if v['result'] == 'success' else failure

        # 计算测试套件执行时间
        cost = round((v['end_timestamp'] - v['start_timestamp']) / 1000, 1)

        # 构建Markdown表格行
        md += f'| {v["testsuite"]} | {tm(v["start_timestamp"])} | {tm(v["end_timestamp"])} | {cost} | '
        md += f'{v["success"]} | {v["failure"]} | {v["blocked"]} | {v["total"]} | {re} |\n'

        # 如果有测试套件失败，则整体结果为失败
        if v['result'] == 'failure':
            result = failure

    # 计算整体测试计划的执行时间
    cost = round((plan['end_timestamp'] - plan['start_timestamp']) / 1000, 1)

    # 添加整体测试计划的统计行
    md += f'| **共计** | {tm(plan["start_timestamp"])} | {tm(plan["end_timestamp"])}  | {cost} | '
    md += f'{sc} | {fc} | {bc} | {tc} | {result} |\n'

    # 构建Markdown报告的标题部分
    # title = f'# 「{plan["plan"]}」自动化测试执行报告 {result} #\n\n[历史记录](/{plan["plan"]}/)\n\n'
    # title = f'# 「{plan["plan"]}」自动化测试执行报告 '
    # md = title + f'## 测试计划执行结果\n\n{md}\n\n## 测试套件执行结果\n\n'

    title = f'# {plan["plan"]}        自动化测试执行报告'
    md = title + f'\n\n ## 测试结果:    {result}\n\n{md}\n\n## 测试套件执行结果\n\n'

    # 根据整体结果选择相应的图标
    if result == success:
        icon = '✔️'
    else:
        icon = '❌'

    # 构建测试计划执行完成的消息
    message = f'- {icon} <font color=#9D9D9D size=2>{tm(plan["start_timestamp"])} - {tm(plan["end_timestamp"])}</font> 测试计划'
    message += f'「[{plan["plan"]}]({plan["plan"]}/{plan["plan"]}_{tm(plan["start_timestamp"], "_")})」执行完成，测试结果：{result}，成功：{sc}，失败：{fc}，阻塞：{bc}\n\n'

    # 测试套件 - 测试用例结果
    txt = ''  # 初始化一个空字符串，用于存储 Markdown 格式文本

    # 遍历测试套件字典，k 为测试套件名称，v 为该套件的测试用例列表
    for k, v in testcases.items():
        txt += f'\n- ### {k}\n\n'  # 添加测试套件标题
        txt += '| 用例id  | 用例名称 |   前置条件   |开始时间         | 结束时间       | 耗时   | 结果    |\n'
        txt += '| ------- | ------- | ----------- | -------------- | -------------- | ----- | ------- |\n'  # 添加表头

        # 遍历该测试套件的测试用例列表
        for case in v:
            if case['flag'] == 'N':
                continue  # 如果测试用例的标记为 'N'，跳过该用例
            cost = round((case['end_timestamp'] - case['start_timestamp']) / 1000, 1)  # 计算耗时并四舍五入保留一位小数
            result = eval(case['result'])  # 通过 eval 函数获取测试结果的布尔值
            txt += f'| [{case["id"]}](#{case["id"]}) | {case["title"]} | {case["condition"]} | {tm(case["start_timestamp"])} | {tm(case["end_timestamp"])} | {cost} | {result} |\n'

    # 将生成的测试用例结果文本添加到整体 Markdown 文本中
    md += f'{txt}\n\n## 测试用例执行结果\n'
    txt = ''  # 清空 txt 变量，准备用于下一部分的文本生成
    # 遍历测试套件字典，k 为测试套件名称，v 为该套件的测试用例列表
    for k, v in testcases.items():
        txt += f'\n- ### {k}\n'  # 添加测试套件标题

        # 遍历该测试套件的测试用例列表
        for case in v:
            if case['flag'] == 'N':
                continue  # 如果测试用例的标记为 'N'，跳过该用例

            # 添加测试用例的标题、前置条件、设计者和测试结果信息
            txt += f'\n#### {case["id"]}\n\n**{case["title"]}** | {case["condition"]} | {case["designer"]} | {eval(case["result"])}\n\n'

            # 添加测试步骤表格的表头
            txt += '| 步骤  | 操作  | 页面  | 元素  | 测试数据  | 预期结果 | 输出数据  | 耗时 | 测试结果 | 备注 | 截图   |\n'
            txt += '|------|-------|-------|------|-----------|---------|-----------|-----|---------|------|--------|\n'

            # 遍历该测试用例的测试步骤列表
            for step in case['steps']:
                cost = round((step.get('end_timestamp', 0) - step.get('start_timestamp', 0)) / 1000, 1)  # 计算步骤耗时
                if cost == 0:
                    cost = '-'

                # 判断测试步骤的测试结果，如果未提供结果则标记为 skipped
                if not step['score']:
                    result = skipped

                elif step['score'] == '-':
                    pass
                else:
                    result = eval(step["score"])
                snapshot = ''
                if 'snapshot' in step:
                    # 构建截图的 Markdown 格式链接
                    for k, v in step['snapshot'].items():
                        snapshot += f"[{k}](/report/{v} ':ignore')\n"

                # 添加测试步骤的信息到表格中
                txt += f'| {step["no"]} | {step["keyword"]} | {step["page"]} | {escape(step["element"])} | {escape(step["data"])} | {escape(step["expected"])} | {escape(step["output"])} | {cost} | {result} | {step["remark"]} | {escape(snapshot, "%23")} |\n'

            result = eval(case['result'])  # 获取整个测试用例的测试结果

    # 将生成的测试报告文本添加到整体 Markdown 文本中
    md += txt

    # 设置测试报告的保存路径
    p = Path(md_path) / 'report'
    latest = p / 'latest'
    report = p / g.plan_name


    # 创建测试报告保存目录
    mkdir("markdown")
    mkdir(p)
    mkdir(report)
    mkdir(latest)

    # 打开 README.md 文件进行读取操作
    with open(p / 'README.md', 'w+', encoding='UTF-8') as f:
        # 读取文件内容并存储在变量 txt 中
        txt = f.read()
        # 如果文件内容中包含 '恭喜你安装成功'
        if '恭喜你安装成功' in txt:
            # 将 txt 变量置为空字符串
            txt = ''

    # 打开 README.md 文件进行写入操作
    with open(p / f'README.md', 'w', encoding='UTF-8') as f:
        # 将 message 和之前读取的文件内容写入 README.md 文件
        f.write(message + txt)

    # 打开最新文件夹中以计划名称命名的文件进行写入操作
    with open(latest / f'{g.plan_name}.md', 'w', encoding='UTF-8') as f:
        # 将 md 变量的内容写入以计划名称命名的文件
        f.write(md)

    # 构建 README 文件的路径
    readme = report / 'README.md'

    # 如果 README 文件存在
    if readme.is_file():
        # 打开 README 文件进行读取操作
        with open(report / 'README.md', 'r', encoding='UTF-8') as f:
            # 读取文件内容并存储在变量 txt 中
            txt = f.read()
    else:
        # 如果 README 文件不存在，则将 txt 变量置为空字符串
        txt = ''

    # 打开 README 文件进行写入操作
    with open(report / 'README.md', 'w', encoding='UTF-8') as f:
        # 将 message 和之前读取的文件内容写入 README 文件
        f.write(message + txt)

    # 构建以计划名称和时间戳命名的文件路径
    with (open(report / f'{plan["plan"]}_{tm(plan["start_timestamp"], "_")}_{ran}.md', 'w', encoding='UTF-8') as f):
        # 将 md 变量的内容写入以计划名称和时间戳命名的文件
        f.write(md)
        md_file_name =f'{plan["plan"]}_{tm(plan["start_timestamp"], "_")}_{ran}.md'

        md_file_path = Path(report / md_file_name)

        # print('this is md_file_name',md_file_name)
        # print('this is md_file_path',md_file_path,type(md_file_path))
    # 打开 _sidebar.md 文件进行读取操作
    with open(p / '_sidebar.md', 'w+', encoding='UTF-8') as f:
        # 读取文件内容并存储在变量 txt 中
        txt = f.read()

    # 如果 _sidebar.md 文件中不包含当前计划名称
    if f'[{g.plan_name}]' not in txt:
        # 打开 _sidebar.md 文件进行追加写入操作
        with open(p / '_sidebar.md', 'a', encoding='UTF-8') as f:
            # 在 _sidebar.md 文件中添加当前计划名称的链接
            f.write(f'\n\t* [{g.plan_name}](latest/{g.plan_name})')

    # 初始化文件列表
    files = []

    # 遍历报告文件夹中的文件
    for f in report.iterdir():
        # 排除文件名为 '_sidebar' 和 'README' 的文件
        if f.stem not in ['_sidebar', 'README']:
            # print('this is f.stem', f.stem)
            # 将文件名添加到文件列表中
            files.append(f.stem + '.md')
    # print('this is files', files)

    # 按文件名降序排序文件列表
    files.sort(reverse=True)

    # 打开 _sidebar.md 文件进行写入操作
    with open(report / '_sidebar.md', 'w', encoding='UTF-8') as f:
        # 初始化 _sidebar.md 文件的内容
        txt = f'* 「{g.plan_name}」\n'

        # 遍历文件列表，为每个文件添加链接
        for stem in files:
            txt += f'\n    * [{stem}]({g.plan_name}/{stem})'

        # 将最终的内容写入 _sidebar.md 文件
        print('------')
        # print('this is txt', txt)
        f.write(txt)
    print('this is sc:', sc)
    print('this is fc:', fc)
    print('this is bc:', bc)
    print('this is tc:', tc)
    return sc, fc, bc, tc
