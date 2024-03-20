# -*- coding: utf-8 -*-
"""
@Time : 2024/1/23 14:09
@Author : TJF

"""
from sweetest.log import logger
from sweetest.utility import Excel, data2dict, replace


def elements_format(data):
    # 创建一个空字典用于存储格式化后的元素信息
    elements = {}
    # 初始化页面和自定义信息为空字符串
    page = ''
    custom = ''

    # 遍历输入的数据列表
    for d in data:
        # 如果页面信息不为空，则更新当前页面和自定义信息
        if d['page'].strip():
            page = d['page']
            custom = ''
        else:
            # 如果页面信息为空，则使用上一次非空页面信息
            d['page'] = page

        # 如果自定义信息不为空，则更新当前自定义信息
        if d.get('custom', '').strip():
            custom = d['custom']
        else:
            # 如果自定义信息为空，则使用上一次非空自定义信息
            d['custom'] = custom

        # 将页面和元素名组合作为字典的键，并存储格式化后的元素信息
        elements[d['page'] + '-' + d['element']] = d

    # 返回格式化后的元素信息字典
    return elements


class Elements:
    def __init__(self):
        pass

    def env(self):
        pass

    def get_elements(self, elements_file):
        # 从 Excel 文件中读取元素信息并格式化
        d = Excel(elements_file)
        self.elements = elements_format(data2dict(d.read('elements')))

    def have(self, page, element):
        # 将元素按#号分割
        ele = element.split('#')

        if len(ele) >= 2:
            _el = ele[0] + '#'
        else:
            _el = element
        # 如果有<>,则不进行判断，直接返回通用格式
        if '<' in _el:
            return '', '通用' + '-' + element
        # 在元素定位表中查询
        elem = page + '-' + _el
        if self.elements.get(elem, ''):
            return self.elements[elem]['custom'], page + '-' + element
        else:
            # 如果在当前页面找不到元素，则在通用元素中查找
            elem = '通用' + '-' + _el
            if self.elements.get(elem, ''):
                return self.elements[elem]['custom'], '通用' + '-' + element
            else:
                # 如果仍然找不到，记录日志并返回空值
                logger.info('Page:%s element:%s' % (page, element))
                return '', element

    def get(self, element, flag=False):
        # 将元素按#号分割
        ele = element.split('#')
        # #号后面的值，即用户输入的变量
        _v = []
        # 支持多个变量替代，但是顺序要对应
        if len(ele) >= 2:
            _el = ele[0] + '#'
            _v = ele[1:]
        else:
            _el = element
        # 在元素信息字典中查找元素
        el = self.elements.get(_el, '')
        if not el:
            # 如果找不到元素，根据标志返回原始格式或者空值
            if flag:
                return _el, ''
            return _el, element.split('#', 1)[-1]
        # 获取元素的值
        value = el['value']
        # 替换元素值中的#符号
        for v in _v:
            v = '#' if v == '^' else v  # 当 value 中的 # 无需替换时，用例中的元素使用 ^ 表示
            value = value.replace('#', v, 1)
        return el, replace(value)
e = Elements()
