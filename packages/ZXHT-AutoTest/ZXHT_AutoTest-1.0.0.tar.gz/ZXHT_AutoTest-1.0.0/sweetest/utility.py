# -*- coding: utf-8 -*-
"""
@Time : 2024/1/10 13:32
@Author : TJF

"""
from pathlib import Path
import xlrd
import xlsxwriter
import csv
import re
import json
import time
from sweetest.config import header
from sweetest.globals import g
import string
import random
from selenium.webdriver.common.keys import Keys


# 创建一个Path对象，表示路径为'lib'
path = Path('lib')
if path.is_dir():
    from sweetest.lib import *
else:
    from sweetest.lib import *


# 定义Excel类
class Excel:
    def __init__(self, file_name, mode='r'):
        # 初始化Excel对象时，根据模式选择使用xlrd或xlsxwriter库来处理Excel文件
        if mode == 'r':
            self.workbook = xlrd.open_workbook(file_name)
        elif mode == 'w':
            self.workbook = xlsxwriter.Workbook(file_name)
        else:
            # 如果模式不是'r'或'w'，抛出异常
            raise Exception('Error: 初始化Excel类时使用了错误的模式：%s' % mode)

    def get_sheet(self, sheet_name):
        # 存储sheet名称的列表
        names = []

        # 检查sheet_name的类型
        if isinstance(sheet_name, str):
            # 如果sheet_name是字符串，并以'*'结尾，则匹配所有以指定字符串开头的sheet名
            if sheet_name.endswith('*'):
                for name in self.workbook.sheet_names():
                    if sheet_name[:-1] in name:
                        names.append(name)
            else:
                # 如果sheet_name是普通字符串，则直接添加到列表中
                names.append(sheet_name)
        elif isinstance(sheet_name, list):
            # 如果sheet_name是列表，则直接使用该列表
            names = sheet_name
        else:
            # 如果sheet_name的类型不是字符串或列表，抛出异常
            raise Exception('Error: 无效的sheet_name类型：%s' % sheet_name)

        # 返回处理后的sheet名称列表
        return names

    def read(self, sheet_name):
        '''
        从指定标签页读取数据

        参数:
        sheet_name: Excel中的标签页名称
        返回值:
        二维列表，包含标签页中所有数据的行
        '''
        # 获取指定标签页对象
        sheet = self.workbook.sheet_by_name(sheet_name)

        # 获取标签页的行数
        nrows = sheet.nrows
        # 初始化一个空列表来存储数据
        data = []
        # 循环遍历每一行，将行数据添加到data列表中
        for i in range(nrows):
            data.append(sheet.row_values(i))
        # 返回包含标签页数据的二维列表
        return data

    def write(self, data, sheet_name):
        # print('this is data',data)
        '''
        将数据写入指定标签页

        参数:
        data: 要写入的数据，二维列表形式
        sheet_name: 要写入的Excel标签页名称
        '''
        # 创建新的标签页对象
        sheet = self.workbook.add_worksheet(sheet_name)

        # 定义不同状态的单元格格式
        red = self.workbook.add_format({'bg_color': 'red', 'color': 'white'})
        gray = self.workbook.add_format({'bg_color': 'gray', 'color': 'white'})
        green = self.workbook.add_format(
            {'bg_color': 'green', 'color': 'white'})
        blue = self.workbook.add_format({'bg_color': 'blue', 'color': 'white'})
        orange = self.workbook.add_format(
            {'bg_color': 'orange', 'color': 'white'})

        # 遍历数据列表，根据不同状态应用不同的单元格格式写入数据
        for i in range(len(data)):
            for j in range(len(data[i])):
                if str(data[i][j]) == 'failure':
                    sheet.write(i, j, str(data[i][j]), red)
                elif str(data[i][j]) == 'NO':
                    sheet.write(i, j, str(data[i][j]), gray)
                elif str(data[i][j]) == 'blocked':
                    sheet.write(i, j, str(data[i][j]), orange)
                elif str(data[i][j]) == 'skipped':
                    sheet.write(i, j, str(data[i][j]), blue)
                elif str(data[i][j]) == 'success':
                    sheet.write(i, j, str(data[i][j]), green)
                else:
                    sheet.write(i, j, data[i][j])

    def close(self):
        '''
        关闭Excel文件
        '''
        # 关闭Excel文件
        self.workbook.close()


def data2dict(data):
    '''
    将带有标题行的二维数组转换为以标题为键的字典列表

    参数:
    data: 带有标题行的二维数组

    返回值:
    字典列表，每部字典以标题为键，对应行的数据为值
    '''
    # 初始化一个空列表，用于存储最终的字典数据
    list_dict_data = []

    # 初始化一个空列表，用于存储标题的键
    key = []

    # 初始化全局变量，用于存储用户自定义的标题
    g.header_custom = {}

    # 遍历第一行标题数据
    for d in data[0]:
        # 提取标题并去除可能的注释部分
        k = d.strip().split('#')[0]

        # 如果标题为中文，则尝试替换成对应的英文
        h = header.get(k, k).lower()

        # 将标题添加到键列表中
        key.append(h)

        # 将标题及其对应原始值添加到全局变量中
        g.header_custom[h] = d.strip()

    # 如果全局变量中不存在'expected'键，则初始化为空字符串
    if not g.header_custom.get('expected'):
        g.header_custom['expected'] = ''

    # 遍历除标题外的每一行数据
    for d in data[1:]:
        # 初始化一个空字典，用于存储当前行的数据
        dict_data = {}
        for i in range(len(key)):
            # 将数据转换为字符串并去除首尾空格，然后存入字典中
            if isinstance(d[i], str):
                dict_data[key[i]] = str(d[i]).strip()
            else:
                dict_data[key[i]] = d[i]
        # 将当前行的字典添加到最终的字典列表中
        list_dict_data.append(dict_data)

    # 返回包含字典数据的列表
    return list_dict_data

# 定义一个函数，用于替换字典中的所有值
def replace_dict(data):
    # 遍历字典中的每个键值对
    for key in data:
        # 对每个值进行替换操作，假设已经定义了 replace 函数
        data[key] = replace(data[key])


# 定义一个函数，用于替换列表中的所有元素
def replace_list(data):
    # 遍历列表中的每个元素
    for i in range(len(data)):
        # 对每个元素进行替换操作，假设已经定义了 replace 函数
        data[i] = replace(data[i])

def replace_old(data):
    # 正则匹配出 data 中所有 <> 中的变量，返回列表
    keys = re.findall(r'<(.*?)>', data)
    for k in keys:
        # 正则匹配出 k 中的 + - ** * // / % , ( ) 返回列表
        values = re.split(r'(\+|-|\*\*|\*|//|/|%|,|\(|\)|\'|\")', k)
        for j, v in enumerate(values):
            # 切片操作处理，正则匹配出 [] 中内容
            s = v.split('[', 1)
            index = ''
            if len(s) == 2:
                v = s[0]
                index = '[' + s[1]

            if v in g.var:
                # 如果在 g.var 中是 list
                if isinstance(g.var[v], list):
                    if index:
                        # list 切片取值（值应该是动态赋值的变量，如自定义脚本的返回值）
                        values[j] = eval('g.var[v]' + index)
                    else:
                        if len(g.var[v]) == 1:
                            values[j] = g.var[v][0]
                            g.var['_last_'] = True
                        else:
                            values[j] = g.var[v].pop(0)
                elif isinstance(g.var[v], dict) and index:
                    # 如果是 dict 取键值
                    values[j] = eval('g.var[v]' + index)
                else:
                    # 如果在 g.var 中是值，则直接赋值
                    values[j] = g.var[v]
                    if index:
                        values[j] = eval('g.var[v]' + index)
            # 如果值不在 g.var，且只有一个元素，则尝试 eval，比如<False>,<True>,<1>,<9.999>
            elif len(values) == 1:
                try:
                    values[j] = eval(values[j])
                except:
                    pass

        # 如果 values 长度大于 1，说明有算术运算符，则用 eval 运算
        # 注意，先要把元素中的数字变为字符串
        if len(values) > 1:
            values = eval(''.join([str(x) for x in values]))
        # 如果 values 长度为 1，则直接赋值，注意此值可能是数字
        else:
            values = values[0]
        # 如果 data 就是一个 <>，如 data = '<a+1>',则直接赋值为 values，此值可能是数字
        if data == '<' + keys[0] + '>':
            data = values
            # 如果有键盘操作，则需要 eval 处理
            if isinstance(data, str) and 'Keys.' in data:
                data = eval(data)
        # 否则需要替换，此时变量强制转换为为字符串
        else:
            data = data.replace('<' + k + '>', str(values))
    return data

def replace(data):
    '''
    替换数据中的变量表达式，并返回替换后的结果

    参数:
    data: 待替换的数据字符串

    返回值:
    替换后的数据字符串
    '''

    # 全局变量，用于存储解析过程中的变量值
    global values

    # 如果数据以三个单引号开头且以三个单引号结尾，直接返回去除三个单引号的内容
    if data.startswith("'''") and data.endswith("'''"):
        return data[3:-3]

    # 定义特殊字符，用于在替换过程中暂时替代尖括号
    left_angle = 'dsfw4rwfdfstg43'
    right_angle = '3dsdtgsgt43trfdf'
    left_delimiter = '<'
    right_delimiter = '>'

    # 替换转义的尖括号，以免干扰后续处理
    data = data.replace(r'\<', left_angle).replace(r'\>', right_angle)

    # 检查是否存在双尖括号，以确定替换的尖括号形式
    if '<<' in data and '>>' in data:
        left_delimiter = '<<'
        right_delimiter = '>>'

    # 使用正则表达式匹配尖括号中的变量名，并存储在列表 keys 中
    keys = re.findall(r'%s' % (left_delimiter + '(.*?)' + right_delimiter), data)

    # 初始化一部字典，用于存储变量名和对应的值
    _vars = {}

    # 遍历每个变量名
    for k in keys:
        # 还原被特殊字符替代的尖括号
        k = k.replace(left_angle, '<').replace(right_angle, '>')

        # 使用正则表达式切分变量名中的运算符和括号，存储在列表 values 中
        values = re.split(r'(\+|-|\*\*|\*|//|/|%|,|\(|\))', k)

        # 遍历 values 列表中的每个元素
        for v in values:
            # 切片操作处理，正则匹配出 [] 中内容
            s = v.split('[', 1)
            index = ''
            if len(s) == 2:
                v = s[0]
                index = '[' + s[1]

            # 如果变量不在 _vars 中
            if v not in _vars:
                # 如果在 g.var 中，则直接赋值
                if v in g.var:
                    _vars[v] = g.var[v]
                # 如果在 g.test_data 中
                elif v in g.test_data:
                    # 如果 g.test_data[v] 为空列表，则报错
                    if len(g.test_data[v]) == 0:
                        raise Exception('The key:%s is no value in data csv' % v)
                    # 如果 g.test_data[v] 只有一个元素，则赋值，并标记循环到最后一个变量
                    elif len(g.test_data[v]) == 1:
                        _vars[v] = g.test_data[v][0]
                        g.var['_last_'] = True
                    # 如果 g.test_data[v] 多于一个元素，则弹出第一个元素赋值
                    else:
                        _vars[v] = g.test_data[v].pop(0)

        # 尝试使用 eval 函数计算变量表达式的值
        try:
            value = eval(k, globals(), _vars)
        except NameError:
            # 如果出现 NameError，说明变量未定义，将其保留在尖括号中
            value = left_delimiter + k + right_delimiter

        # 如果数据中只包含一个变量表达式，则直接用计算结果替换整个数据
        if data == left_delimiter + keys[0] + right_delimiter:
            data = value
        # 否则需要替换，此时将变量值强制转换为字符串
        else:
            data = data.replace(left_delimiter + k + right_delimiter, str(value))

    # 假设之前的代码中已经定义了变量 left_angle 和 right_angle，分别表示左尖括号和右尖括号

    # 检查变量 data 是否是字符串类型
    if isinstance(data, str):
        # 如果是字符串类型，使用 replace 方法将 left_angle 替换为 '<'，再将 right_angle 替换为 '>'
        data = data.replace(left_angle, '<').replace(right_angle, '>')

    # 返回经过替换处理后的 data
    return data


# 定义一个测试函数
def test_replace():
    # 假设 g.var 是一个全局变量，其值为字典 {'a': 1, 'b': 'B'}
    g.var = {'a': 1, 'b': 'B'}

    # 遍历给定的字符串列表，假设 replace 函数已经定义
    for d in ('<a+1>', '<b>', 'abc<a>', 'abc<a+1>', '<a*(8+4)/2//3>', '<u.td(-3)>'):
        # 对每个字符串进行替换操作，假设已经定义了 replace 函数
        data = replace(d)


# 定义一个读取 CSV 文件的函数
def read_csv(csv_file, encoding=None):
    # 初始化一个空列表，用于存储读取的 CSV 数据
    data = []

    # 打开 CSV 文件进行读取，假设已经导入了 csv 模块
    with open(csv_file, encoding=encoding) as f:
        # 使用 csv 模块的 reader 函数创建一个 CSV 读取器
        reader = csv.reader(f)

        # 遍历读取器中的每一行数据
        for line in reader:
            # 将每一行数据添加到数据列表中
            data.append(line)

    # 返回读取的 CSV 数据
    return data


# 定义一个写入 CSV 文件的函数
def write_csv(csv_file, data, encoding=None):
    # 使用 with 语句打开文件，确保文件操作完成后自动关闭
    with open(csv_file, 'w', encoding=encoding, newline='') as f:
        # 创建 CSV 写入器对象
        writer = csv.writer(f)

        # 使用 writerows 方法将数据写入 CSV 文件
        writer.writerows(data)


# 定义一个函数，用于从 CSV 文件中获取记录
def get_record(data_file):
    # 初始化变量 encoding 为 None
    encoding = None

    # 尝试使用 utf-8 编码读取 CSV 文件
    try:
        data = read_csv(data_file, encoding='utf-8')
        encoding = 'utf-8'
    # 如果出现异常（可能是编码问题），则使用默认编码方式继续读取
    except:
        data = read_csv(data_file)

    # 定义一个内部函数 read_data 用于读取数据并更新记录
    def read_data():
        # 根据标志 flag 决定要读取的列数
        num = len(data[0]) - 1 if flag else len(data[0])

        # 遍历每一列数据
        for i in range(num):
            # 判断当前单元格是否非空
            if d[i]:
                k = data[0][i]  # 获取列名
                # 判断记录中是否已存在该列名
                if record.get(k, None):
                    # 如果已存在，则将当前值追加到该列对应的值列表中
                    record[k].append(d[i])
                else:
                    # 如果不存在，则创建一个新地列表，并将当前值赋值给该列表
                    record[k] = [d[i]]

                # 对特殊字符进行处理，将"&quot;"转换为空字符串
                if record[k][-1] == '&quot;':
                    record[k][-1] = ''

    # 初始化记录字典
    record = {}

    # 根据数据的最后一列是否为 'flag' 判断是否需要处理标志位
    flag = False
    if data[0][-1].lower() == 'flag':
        flag = True

    # 遍历数据的每一行（除了第一行，因为第一行是列名）
    for d in data[1:]:
        # 如果不需要处理标志位，或者标志位为 'N'，或者标志位非 'Y'，则调用 read_data 处理数据
        if not flag or d[-1] == 'N' or d[-1] != 'Y':
            read_data()
        # 如果需要处理标志位，并且标志位为 'Y'，则调用 read_data 处理数据，并将标志位设置为 'Y'
        elif d[-1] == 'Y':
            read_data()
            d[-1] = 'Y'
            # 调用写入 CSV 的函数（假设已经定义了 write_csv 函数），并指定编码方式
            write_csv(data_file, data, encoding=encoding)
            # 结束循环
            break

    # 返回获取到的记录字典
    return record


# 定义一个将字符串转换为整数的函数
def str2int(s):
    # 将输入的字符串转换为字符串类型，去除其中的逗号，并根据小数点进行拆分
    s = str(s).replace(',', '').split('.', 1)

    # 如果拆分后的列表长度为2，说明有小数部分
    if len(s) == 2:
        dot = s[-1]  # 获取小数部分
        assert int(dot) == 0  # 断言小数部分为0
    return int(s[0])  # 返回整数部分


# 定义一个递归函数，用于去除浮点数末尾多余的零
def zero(s):
    # 如果字符串不为空且末尾为零
    if s and s[-1] == '0':
        s = s[:-1]  # 去除末尾的零
        s = zero(s)  # 递归调用自身
    return s  # 返回处理后的字符串


# 定义一个将字符串转换为浮点数的函数，可以指定小数部分的精度
def str2float(s, n=None):
    s = str(s).replace(',', '')  # 将输入的字符串转换为字符串类型，去除其中的逗号
    number = s.split('.', 1)  # 根据小数点进行拆分

    # 如果指定了小数部分的精度
    if n:
        f = float(s)  # 将字符串转换为浮点数
        return round(f, n), n  # 返回四舍五入到指定精度的浮点数以及精度值

    dot = '0'  # 初始化小数部分
    # 如果拆分后的列表长度为2，说明有小数部分
    if len(number) == 2:
        dot = number[-1]  # 获取小数部分
        dot = zero(dot)  # 去除小数部分末尾多余的零
    f = float(number[0] + '.' + dot)  # 将整数部分和处理过的小数部分组合成浮点数

    return round(f, len(dot)), len(dot)  # 返回四舍五入到小数部分长度的浮点数以及小数部分的长度


# 定义一个函数用于判断两个浮点数值是否相同，可以接受字符串或浮点数类型的输入
def f(v, e, n=2):
    '''
    判断2个 float 数值是否相同，类型可以是 str 或 float
    v: 实际值，如：12.345, '1234.56', '1,234.5600'
    e: 预期结果, 示例值同 v
    n: 小数点精确位数
    '''
    # 将输入的字符串中的逗号去除，确保字符串可以转换为浮点数
    v = str(v).replace(',', '')
    e = str(e).replace(',', '')

    # 将字符串转换为浮点数并四舍五入到指定精度
    _v = round(float(v), n)
    _e = round(float(e), n)

    # 使用断言判断实际值和预期结果是否相同
    assert round(_v, n) == round(_e, n)


# 定义一个函数用于创建目录，接受一个路径参数
def mkdir(p):
    # 使用 Path 类创建路径对象
    path = Path(p)
    # 如果路径不是一个目录，就创建该目录
    if not path.is_dir():
        path.mkdir()


# 定义一个函数用于将字符串转换为字典
def json2dict(s):
    # 如果输入已经是字典类型，直接返回
    if isinstance(s, dict):
        return s

    # 将输入转换为字符串
    s = str(s)

    # 初始化一个空字典
    d = {}

    try:
        # 尝试使用json.loads将字符串解析为字典
        d = json.loads(s)
    except:
        try:
            # 如果解析失败，尝试使用eval解析
            d = eval(s)
        except:
            # 如果仍然失败，替换一些特殊字符串，并再次使用eval解析
            s = s.replace('true', 'True').replace('false', 'False').replace(
                'null', 'None').replace('none', 'None')
            d = eval(s)

    # 返回解析得到的字典
    return d

def compare(data, real):
    # 检查输入是否为字符串类型
    if isinstance(data, str):

        # 如果字符串以 '#' 开头，断言去掉 '#' 后的部分不等于真实值
        if data.startswith('#'):
            assert data[1:] != str(real)
            return
        # 如果字符串以 ':' 开头，使用 exec 函数执行指定的表达式
        elif data.startswith(':'):
            exec('v=real;' + data[1:])
            return

        # 断言真实值也为字符串类型
        assert isinstance(real, str)

        # 如果字符串以 '*' 开头，断言去掉 '*' 后的部分在真实值中
        if data.startswith('*'):
            assert data[1:] in real
            return
        # 如果字符串以 '^' 开头，断言真实值以去掉 '^' 后的部分开头
        elif data.startswith('^'):
            assert real.startswith(data[1:])
            return
        # 如果字符串以 '$' 开头，断言真实值以去掉 '$' 后的部分结尾
        elif data.startswith('$'):
            assert real.endswith(data[1:])
            return

        # 如果字符串以 '\' 开头，去掉 '\' 后的部分
        elif data.startswith('\\'):
            data = data[1:]

        # 断言去掉 '\' 后的部分等于真实值
        assert data == real

    # 如果输入为整数类型，断言真实值也为整数类型且相等
    elif isinstance(data, int):
        assert isinstance(real, int)
        assert data == real
    # 如果输入为浮点数类型，断言真实值也为浮点数类型且相等
    elif isinstance(data, float):
        assert isinstance(real, float)
        # 调用 str2float 函数将字符串转换为浮点数，并获取小数点位置
        data, p1 = str2float(data)
        real, p2 = str2float(real)
        # 取小数点位置的最小值，用于在断言中保留相同的小数位数
        p = min(p1, p2)
        # 断言四舍五入后的值相等
        assert round(data, p) == round(real, p)
    else:
        # 对于其他类型的输入，直接断言它们相等
        assert data == real

def timestamp():
    # js 格式的时间戳
    return int(time.time() * 1000)