# -*- coding: utf-8 -*-
"""
@Time : 2024/1/24 16:17
@Author : TJF

"""

import requests

from sweetest.injson import check
from sweetest.globals import g
from sweetest.elements import e
from sweetest.log import logger
from sweetest.utility import json2dict
from pathlib import Path
from sweetest.lib import http_handle

path = Path('lib') / 'http_handle.py'


class Http:

    def __init__(self, step):
        # 获取 baseurl
        baseurl = e.get(step['page'] + '-' + 'baseurl', True)[1]

        # 如果未获取到 baseurl，则将 self.baseurl 设置为空字符串
        if not baseurl:
            self.baseurl = ''
        else:
            # 如果 baseurl 不以 '/' 结尾，则添加 '/'
            if not baseurl.endswith('/'):
                baseurl += '/'
            self.baseurl = baseurl

        # 创建一个会话对象，用于发送 HTTP 请求
        self.r = requests.Session()

        # 获取 headers，分别获取 get 和 post 请求的 headers
        self.headers_get = e.get(step['page'] + '-' + 'headers_get', True)[1]
        self.headers_post = e.get(step['page'] + '-' + 'headers_post', True)[1]


def get(step):
    # 调用 request 函数，发起 GET 请求
    request('get', step)


def post(step):
    # 调用 request 函数，发起 POST 请求
    request('post', step)


def put(step):
    # 调用 request 函数，发起 PUT 请求
    request('put', step)


def patch(step):
    # 调用 request 函数，发起 PATCH 请求
    request('patch', step)


def delete(step):
    # 调用 request 函数，发起 DELETE 请求
    request('delete', step)


def options(step):
    # 调用 request 函数，发起 OPTIONS 请求
    request('options', step)


def request(kw, step):
    # 获取请求的元素
    element = step['element']

    # 从配置中获取元素对应的 URL
    url = e.get(element)[1]

    # 如果 URL 以 '/' 开头，则去掉开头的 '/'
    if url.startswith('/'):
        url = url[1:]

    # 获取请求的数据
    data = step['data']

    # 在测试数据解析时，默认添加一个 'text' 键，需要删除
    if 'text' in data and not data['text']:
        data.pop('text')

    # 初始化请求数据的字典
    _data = {}

    # 解析并设置请求头
    _data['headers'] = json2dict(data.pop('headers', '{}'))

    # 如果存在 cookies，将其解析并设置
    if data.get('cookies'):
        data['cookies'] = json2dict(data['cookies'])

    # 根据请求类型设置请求参数
    if kw == 'get':
        _data['params'] = json2dict(
            data.pop('params', '{}')) or json2dict(data.pop('data', '{}'))
    elif kw == 'post':
        # 如果存在 'text' 数据，则将其编码为 utf-8，并设置为请求数据
        if data.get('text'):
            _data['data'] = data.pop('text').encode('utf-8')
        else:
            # 否则，将 'data' 解析并设置为请求数据
            _data['data'] = json2dict(data.pop('data', '{}'))

        # 解析并设置 JSON 数据
        _data['json'] = json2dict(data.pop('json', '{}'))

        # 解析并设置文件数据
        _data['files'] = eval(data.pop('files', 'None'))
    elif kw in ('put', 'patch'):
        # 对于 'put' 和 'patch' 请求，解析并设置请求数据
        _data['data'] = json2dict(data.pop('data', '{}'))
    # 对请求数据进行处理，尝试将包含 '{', '[', 'False', 'True' 的字符串进行 eval 操作
    for k in data:
        for s in ('{', '[', 'False', 'True'):
            if s in data[k]:
                try:
                    data[k] = eval(data[k])
                except:
                    # 捕获 eval 操作失败的异常，并记录警告日志
                    logger.warning('尝试 eval 数据失败：%s' % data[k])
                break

    # 处理预期结果数据
    expected = step['expected']
    expected['status_code'] = expected.get('status_code', None)
    expected['text'] = expected.get('text', None)
    expected['json'] = json2dict(expected.get('json', '{}'))
    expected['cookies'] = json2dict(expected.get('cookies', '{}'))
    expected['headers'] = json2dict(expected.get('headers', '{}'))
    timeout = float(expected.get('timeout', 10))
    expected['time'] = float(expected.get('time', 0))

    # 如果在全局变量 g.http 中不存在当前页面对应的 Http 实例，则创建一个并存储在 g.http 中
    if not g.http.get(step['page']):
        g.http[step['page']] = Http(step)
    http = g.http[step['page']]

    # 根据请求类型更新 Http 实例的请求头
    if kw == 'post':
        if http.headers_post:
            http.r.headers.update(eval(http.headers_post))
    else:
        if http.headers_get:
            http.r.headers.update(eval(http.headers_get))

    # 记录请求的 URL 到日志中
    logger.info('URL: %s' % http.baseurl + url)

    # 处理 before_send 操作，获取 before_send 字段的值，如果存在则调用对应的方法，传入请求类型（kw）、_data 和 data 进行处理
    before_send = data.pop('before_send', '')
    if before_send:
        _data, data = getattr(http_handle, before_send)(kw, _data, data)
    else:
        _data, data = getattr(http_handle, 'before_send')(kw, _data, data)

    # 更新请求头信息，删除为空的请求头，并将非空的请求头更新到 Http 实例中
    if _data['headers']:
        for k in [x for x in _data['headers']]:
            if not _data['headers'][k]:
                del http.r.headers[k]
                del _data['headers'][k]
        http.r.headers.update(_data['headers'])

    # 根据请求类型执行相应的请求操作
    if kw == 'get':
        # 发送 GET 请求，包括 URL、查询参数、超时时间和其他数据
        r = getattr(http.r, kw)(http.baseurl + url,
                                params=_data['params'], timeout=timeout, **data)
        # 如果存在查询参数，则记录到日志中
        if _data['params']:
            logger.info(f'PARAMS: {_data["params"]}')

    elif kw == 'post':
        # 发送 POST 请求，包括 URL、请求体数据、JSON 数据、文件数据、超时时间和其他数据
        r = getattr(http.r, kw)(http.baseurl + url,
                                data=_data['data'], json=_data['json'], files=_data['files'], timeout=timeout, **data)
        # 记录请求体数据到日志中
        logger.info(f'BODY: {r.request.body}')

    elif kw in ('put', 'patch'):
        # 发送 PUT 或 PATCH 请求，包括 URL、请求体数据、超时时间和其他数据
        r = getattr(http.r, kw)(http.baseurl + url,
                                data=_data['data'], timeout=timeout, **data)
        # 记录请求体数据到日志中
        logger.info(f'BODY: {r.request.body}')

    elif kw in ('delete', 'options'):
        # 发送 DELETE 或 OPTIONS 请求，包括 URL、超时时间和其他数据
        r = getattr(http.r, kw)(http.baseurl + url, timeout=timeout, **data)

    # 记录请求的状态码到日志中
    logger.info('status_code: %s' % repr(r.status_code))
    # 尝试解析响应为 JSON 格式，记录到日志中
    try:  # json 响应
        logger.info('response json: %s' % repr(r.json()))
    except:  # 其他响应
        logger.info('response text: %s' % repr(r.text))

    # 构建包含响应相关信息的字典
    response = {
        'status_code': r.status_code,  # 响应状态码
        'headers': r.headers,  # 响应头信息
        '_cookies': r.cookies,  # Cookie 对象
        'content': r.content,  # 响应内容的二进制形式
        'text': r.text  # 响应内容的文本形式
    }

    # 尝试将 Cookie 对象转换为字典形式，如果失败则使用原始 Cookie 对象
    try:
        response['cookies'] = requests.utils.dict_from_cookiejar(r.cookies)
    except:
        response['cookies'] = r.cookies

    # 尝试解析响应为 JSON 格式，将结果存储在字典中，如果失败则字典为空
    try:
        j = r.json()
        response['json'] = j
    except:
        response['json'] = {}

    # 处理 after_receive 操作，获取 after_receive 字段的值，如果存在则调用对应的方法，传入响应信息进行处理
    after_receive = expected.pop('after_receive', '')
    if after_receive:
        response = getattr(http_handle, after_receive)(response)
    else:
        response = getattr(http_handle, 'after_receive')(response)

    # 初始化存储所有输出变量的字典
    var = {}# 存储所有输出变量

    # 检查预期的状态码是否存在
    if expected['status_code']:
        # 如果预期的状态码与实际响应的状态码不匹配，抛出异常
        if str(expected['status_code']) != str(response['status_code']):
            raise Exception(
                f'status_code | 期望值:{repr(expected["status_code"])}, 实际值:{repr(response["status_code"])}')

    # 检查预期的文本是否存在
    if expected['text']:
        # 如果预期的文本以 '*' 开头，检查实际响应的文本是否包含预期文本
        if expected['text'].startswith('*'):
            if expected['text'][1:] not in response['text']:
                raise Exception(f'text | 期望值:{repr(expected["text"])}, 实际值:{repr(response["text"])}')
        # 如果预期的文本不以 '*' 开头，检查实际响应的文本是否与预期文本相同
        else:
            if expected['text'] == response['text']:
                raise Exception(f'text | 期望值:{repr(expected["text"])}, 实际值:{repr(response["text"])}')

    # 检查预期的头部信息是否存在
    if expected['headers']:
        # 使用 check 函数检查头部信息是否符合预期，获取检查结果
        result = check(expected['headers'], response['headers'])
        logger.info('headers check result: %s' % result)
        # 如果检查结果中的 code 不为 0，表示不符合预期，抛出异常
        if result['code'] != 0:
            raise Exception(
                f'headers | 期望值:{repr(expected["headers"])}, 实际值:{repr(response["headers"])}, 检查结果: {result}')
        # 如果检查结果中有变量，更新全局变量和局部变量
        elif result['var']:
            var = dict(var, **result['var'])
            g.var = dict(g.var, **result['var'])
            logger.info('headers var: %s' % (repr(result['var'])))

    # 检查预期的 cookies 是否存在
    if expected['cookies']:
        logger.info('response cookies: %s' % response['cookies'])
        # 使用 check 函数检查 cookies 是否符合预期，获取检查结果
        result = check(expected['cookies'], response['cookies'])
        logger.info('cookies check result: %s' % result)
        # 如果检查结果中的 code 不为 0，表示不符合预期，抛出异常
        if result['code'] != 0:
            raise Exception(
                f'cookies | 期望值:{repr(expected["cookies"])}, 实际值:{repr(response["cookies"])}, 检查结果: {result}')
        # 如果检查结果中有变量，更新全局变量和局部变量
        elif result['var']:
            var = dict(var, **result['var'])
            g.var = dict(g.var, **result['var'])
            logger.info('cookies var: %s' % (repr(result['var'])))
    # 如果预期结果中包含 JSON 数据
    if expected['json']:
        # 进行 JSON 检查
        result = check(expected['json'], response['json'])
        logger.info('json check result: %s' % result)

        # 如果检查结果的 code 不为 0，抛出异常
        if result['code'] != 0:
            raise Exception(
                f'json | EXPECTED:{repr(expected["json"])}, REAL:{repr(response["json"])}, RESULT: {result}')
        # 如果检查结果包含变量，更新全局和局部变量
        elif result['var']:
            var = dict(var, **result['var'])
            g.var = dict(g.var, **result['var'])
            logger.info('json var: %s' % (repr(result['var'])))

    # 如果预期结果中包含时间限制
    if expected['time']:
        # 如果实际响应时间超过预期时间，抛出异常
        if expected['time'] < r.elapsed.total_seconds():
            raise Exception(f'time | EXPECTED:{repr(expected["time"])}, REAL:{repr(r.elapsed.total_seconds())}')

    # 获取步骤的输出定义
    output = step['output']

    # 遍历输出项
    for k, v in output.items():
        # 如果输出项为 'status_code'
        if v == 'status_code':
            # 更新全局变量和记录日志
            g.var[k] = response['status_code']
            logger.info('%s: %s' % (k, repr(g.var[k])))
        # 如果输出项为 'text'
        elif v == 'text':
            # 更新全局变量和记录日志
            g.var[k] = response['text']
            logger.info('%s: %s' % (k, repr(g.var[k])))
        # 如果输出项为 'json'
        elif k == 'json':
            # 将输出的 JSON 字符串转换为字典
            sub = json2dict(output.get('json', '{}'))
            # 进行 JSON 检查
            result = check(sub, response['json'])
            # 更新全局和局部变量
            var = dict(var, **result['var'])
            g.var = dict(g.var, **result['var'])
            logger.info('json var: %s' % (repr(result['var'])))
        # 如果输出项为 'cookies'
        elif k == 'cookies':
            # 将输出的 cookies 字符串转换为字典
            sub = json2dict(output.get('cookies', '{}'))
            # 进行 cookies 检查
            result = check(sub, response['cookies'])
            # 更新全局和局部变量
            var = dict(var, **result['var'])
            g.var = dict(g.var, **result['var'])
            logger.info('cookies var: %s' % (repr(result['var'])))

    # 如果存在变量，将其添加到步骤输出中
    if var:
        step['_output'] += '\n||output=' + str(var)
