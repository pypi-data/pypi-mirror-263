from copy import deepcopy
import random



# 定义一个函数，接受一部字典作为参数，返回其中每个子项的'code'值组成的列表
def rule(data):
    result = []
    for k in data:
        result.append(data[k]['code'])
    return result


# 定义一个函数，接受三个参数，分别是子项（sub）、结果列表（result）、路径（path）
def optimum(sub, result, path):
    # 如果路径不是根目录，则在路径后添加点号
    if path != '/':
        path += '.'

    # 复制结果列表，初始化res
    res = result
    # 遍历子项
    for k in sub:
        # 复制结果列表
        result = deepcopy(res)
        # 复制结果列表，初始化temp
        temp = res
        # 清空结果列表
        res = []
        # 标志，用于判断是否添加了新的结果
        flag = False
        # 遍历结果列表中的每个字典
        for data in result:
            # 如果路径+子项不在当前字典中
            if path + k not in data:
                # 标记为True，表示需要添加新的结果
                flag = True
                # 将当前字典添加到新的结果列表中
                res.append(data)
        # 如果没有标志，表示所有结果都包含了子项，直接返回排序后的第一个结果
        if not flag:
            temp.sort(key=lambda d: rule(d))
            return temp[0]
    # 如果遍历完所有子项后仍有未包含子项的结果，返回排序后的第一个结果
    result.sort(key=lambda d: rule(d))
    return result[0]


# 定义一个函数，接受一个列表作为参数，返回一个以索引字符串为键的字典
def list2dict(data):
    keys = ['[' + str(i) + ']' for i in range(len(data))]
    return dict(zip(keys, data))


def check(sub, parent, sp='/', pp='/'):
    '''
    sp: 子路径
    pp: 父路径
    '''
    # 初始化一个字典re，包含'code'、'result'、'var'、'none'四个键值对
    re = {'code': 0, 'result': {}, 'var': {}, 'none': []}

    # 如果子路径不是根目录，则在子路径后添加点号
    if sp != '/':
        sp += '.'

    # 如果父路径不是根目录，则在父路径后添加点号
    if pp != '/':
        pp += '.'

    # 定义一个内部函数_in，接受两个参数，键k和数据字典data
    def _in(k, data):
        try:
            # 尝试通过eval函数获取data中键为k的值
            return eval('data[k]')
        except:
            # 如果发生异常，返回空字符串
            return ''

    for k, sv in sub.items():
        # 判断键值是否是 <value> 格式，如果是，则表明是变量赋值
        var_flag = isinstance(sv, str) and sv.startswith('<') and sv.endswith('>')
        index = ''
        _k = k

        # 如果键中包含点号（.），则进行处理
        if '.' in k:
            s = k.split('.')
            # 遍历点号后的每个部分
            for _s in s[1:]:
                # 如果部分中包含左方括号（[），则进行处理
                if '[' in _s:
                    d = _s.split('[', 1)
                    index += '[\'' + d[0] + '\']' + '[\'' + d[1]
                else:
                    index += '[\'' + _s + '\']'

            # 如果键的起始部分包含左方括号（[），则进行处理
            if '[' in s[0]:
                k = s[0].split('[', 1)[0]
                index = '[' + s[0].split('[', 1)[1] + index
            else:
                k = s[0]

        # 如果键中包含左方括号（[），则进行处理
        elif '[' in k:
            s = k.split('[', 1)
            index = '[' + s[1]
            k = s[0]

        # 预期键不存在
        if sv == '-':
            # 如果预期键不存在，但实际键存在
            if k in parent:
                # 记录结果为代码4，表示预期键不存在但实际键存在
                re['result'][sp + _k] = {'code': 4, 'sv': sv, 'pp': pp + _k, 'pv': parent[k]}

        # 预期键存在
        elif sv == '+':
            # 如果预期键存在，但实际键不存在
            if k not in parent:
                # 记录结果为代码3，表示预期键存在但实际键不存在
                re['result'][sp + _k] = {'code': 3, 'sv': sv, 'pp': None, 'pv': None}

        # 如果键存在于父字典中
        elif k in parent:
            if index:
                try:
                    # 使用 eval 根据索引获取实际值
                    pv = eval('parent[k]' + index)
                except:
                    # 处理可能的异常情况
                    if var_flag:
                        # 如果是变量赋值，记录变量为 None
                        re['var'][sv[1:-1]] = None
                        re['none'].append(sv[1:-1])
                    else:
                        # 否则记录结果为代码3，表示预期键存在但实际键不存在
                        re['result'][sp + _k] = {'code': 3, 'sv': sv, 'pp': None, 'pv': None}
                    continue
            else:
                # 如果没有索引，直接获取实际值
                pv = parent[k]

            # 初始化代码为0
            code = 0

            # 如果是变量赋值，记录变量的实际值，并继续下一次循环
            if var_flag:
                re['var'][sv[1:-1]] = pv
                continue

            # 如果预期值是字符串
            elif isinstance(sv, str):
                # 根据不同的预期值格式进行比较
                if sv.startswith('#'):
                    # 预期值以'#'开头，直接比较字符串形式
                    if sv[1:] == str(pv):
                        code = 1
                elif sv.startswith('<>'):
                    # 预期值以'<>开头，如果实际值为数字，比较数值相等
                    if (isinstance(pv, int) or isinstance(pv, float)) and pv == float(sv[2:]):
                        code = 1
                elif sv.startswith('>='):
                    # 预期值以'>='开头，如果实际值为数字，比较是否大于等于预期值
                    if (isinstance(pv, int) or isinstance(pv, float)) and pv < float(sv[2:]):
                        code = 1
                elif sv.startswith('>'):
                    # 预期值以'>'开头，如果实际值为数字，比较是否大于预期值
                    if (isinstance(pv, int) or isinstance(pv, float)) and pv <= float(sv[1:]):
                        code = 1
                elif sv.startswith('<='):
                    # 预期值以'<='开头，如果实际值为数字，比较是否小于等于预期值
                    if (isinstance(pv, int) or isinstance(pv, float)) and pv > float(sv[2:]):
                        code = 1
                elif sv.startswith('<'):
                    # 预期值以'<'开头，如果实际值为数字，比较是否小于预期值
                    if (isinstance(pv, int) or isinstance(pv, float)) and pv >= float(sv[1:]):
                        code = 1
                elif not isinstance(pv, str):
                    # 预期值不是以'#'开头的字符串，但实际值类型不一致，记录代码为2
                    code = 2  # 键值的数据类型不一致
                elif sv.startswith('*'):
                    # 预期值以'*'开头，检查是否是实际值的子字符串
                    if sv[1:] not in pv:
                        code = 1
                elif sv.startswith('^'):
                    # 预期值以'^'开头，检查是否以预期值开头
                    if not pv.startswith(sv[1:]):
                        code = 1
                elif sv.startswith('$'):
                    # 预期值以'$'开头，检查是否以预期值结尾
                    if not pv.endswith(sv[1:]):
                        code = 1
                elif sv.startswith('\\'):
                    # 预期值以'\'开头，去掉'\'字符
                    sv = sv[1:]
                elif sv != pv:
                    # 预期值不满足以上条件，直接比较字符串形式
                    code = 1  # 键值不等

            elif isinstance(sv, int):
                # 如果sv是整数类型
                if not isinstance(pv, int):
                    code = 2  # 键值的数据类型不一致
                elif sv != pv:
                    code = 1  # 键值不等

            elif isinstance(sv, float):
                # 如果sv是浮点数类型
                if not isinstance(pv, float):
                    code = 2  # 键值的数据类型不一致
                elif sv != pv:
                    code = 1  # 键值不等

            elif isinstance(sv, list):
                # 如果sv是列表类型
                if not isinstance(pv, list):
                    code = 2  # 键值的数据类型不一致
                else:
                    for i in range(len(sv)):  # 把二级列表转换为 dict
                        if isinstance(sv[i], list):
                            sv[i] = list2dict(sv[i])
                    for i in range(len(pv)):  # 把二级列表转换为 dict
                        if isinstance(pv[i], list):
                            pv[i] = list2dict(pv[i])

                    if isinstance(sv[0], dict):  # 如果列表的第一个元素是字典类型
                        for i, sv_i in enumerate(sv):  # 遍历列表中的每个元素
                            result = []  # 用于存储中间结果
                            flag = False  # 标记，表示是否找到匹配项
                            for j, pv_i in enumerate(pv):  # 遍历目标列表中的每个元素
                                r = check(sv_i, pv_i, sp + _k + '[%s]' % i, pp + _k + '[%s]' % j)  # 递归调用check函数比较两个字典
                                if r['code'] == 0:  # 如果匹配成功
                                    flag = True  # 设置标记为True
                                    re['var'] = dict(re['var'], **r['var'])  # 更新变量结果
                                    break  # 跳出内层循环，因为已找到匹配项
                                else:
                                    result.append(r['result'])  # 将中间结果添加到列表中
                            if result:  # 如果中间结果列表非空
                                o = optimum(sv_i, result, sp + k + '[%s]' % i)  # 调用optimum函数获取最优结果
                            else:
                                o = {}  # 如果中间结果列表为空，则设置o为空字典
                            re['var'] = dict(re['var'], **re['var'])  # 更新变量结果（此处可能存在拼写错误，应该更新re['var']而不是re['var']）

                            if not flag:  # 如果没有找到匹配项
                                re['result'] = dict(re['result'], **o)  # 更新结果

                    else:  # list 子项为 int/str/float/None/False/True
                        for v in sv:
                            if v not in pv:
                                code = 5  # 预期的 list 值在实际值的 list 不存在
                                re['result'][sp + _k] = {'code': 5, 'sv': sv, 'pp': pp + _k, 'pv': pv}

            elif isinstance(sv, dict):  # 如果sv是字典类型
                if not isinstance(pv, dict):  # 如果pv不是字典类型
                    code = 2  # 键值的数据类型不一致，将错误码设置为2
                else:
                    r = check(sv, pv, sp + k, pp + k)  # 调用check函数比较两个字典
                    if r['code'] == 0:  # 如果匹配成功
                        re['var'] = dict(re['var'], **r['var'])  # 更新变量结果
                        continue  # 继续下一轮循环
                    else:
                        re['result'] = dict(re['result'], **r['result'])  # 更新结果
                        for k in r['var']:  # 遍历变量结果中的键
                            r['var'][k] = None  # 将变量结果中的值设置为None
                            if k not in re['none']:  # 如果键不在none列表中
                                re['none'].append(k)  # 将键添加到none列表中
                        re['var'] = dict(re['var'], **r['var'])  # 更新变量结果
            if code != 0:
                re['result'][sp + _k] = {'code': code, 'sv': sv, 'pp': pp + _k, 'pv': pv}
        else:  # 键不存在
            if var_flag:
                re['var'][sv[1:-1]] = None
                re['none'].append(sv[1:-1])
            else:
                re['result'][sp + _k] = {'code': 3, 'sv': sv, 'pp': None, 'pv': None}

    re['code'] = len(re['result'])
    return re
