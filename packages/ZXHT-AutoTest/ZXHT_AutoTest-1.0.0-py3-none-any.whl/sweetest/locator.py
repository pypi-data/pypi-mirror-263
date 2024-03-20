# -*- coding: utf-8 -*-
"""
@Time : 2024/1/23 15:18
@Author : TJF

"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from sweetest.elements import e
from sweetest.globals import g
from sweetest.log import logger
from sweetest.config import element_wait_timeout


def locating_element(element, action=''):
    # 初始化元素位置为None
    el_location = None
    try:
        # 尝试获取元素及其值
        el, value = e.get(element)
    except:
        # 如果获取失败，记录异常信息，并抛出异常
        logger.exception('定位元素：%s 失败，该元素未定义' % element)
        raise Exception('定位元素：%s 失败，该元素未定义' % element)

    # 检查获取的元素是否为字典类型，如果不是则抛出异常
    if not isinstance(el, dict):
        raise Exception('定位元素：%s 失败，该元素未定义' % element)

    # 初始化等待对象
    wait = WebDriverWait(g.driver, element_wait_timeout)

    # 检查元素的定位方式是否为 'title', 'url', 'current_url'，如果是则返回None
    if el['by'].lower() in ('title', 'url', 'current_url'):
        return None
    else:
        try:
            # 使用等待直到元素可见的方式定位元素
            el_location = wait.until(EC.visibility_of_element_located(
                (getattr(By, el['by'].upper()), value)))
        except:
            # 如果第一次等待失败，等待5秒后重试一次
            sleep(5)
            try:
                el_location = wait.until(EC.visibility_of_element_located(
                    (getattr(By, el['by'].upper()), value)))
            except:
                # 如果重试后仍然失败，抛出超时异常
                raise Exception('定位元素：%s 失败：超时' % element)

    # 尝试滚动到元素位置
    try:
        if g.driver.name in ('chrome', 'safari'):
            g.driver.execute_script(
                "arguments[0].scrollIntoViewIfNeeded(true)", el_location)
        else:
            g.driver.execute_script(
                "arguments[0].scrollIntoView(false)", el_location)
    except:
        pass

    # 根据动作类型进行不同的等待方式
    try:
        if action == 'CLICK':
            # 如果动作是点击，等待元素可点击
            el_location = wait.until(EC.element_to_be_clickable(
                (getattr(By, el['by'].upper()), value)))
        else:
            # 如果没有指定动作，等待元素可见
            el_location = wait.until(EC.visibility_of_element_located(
                (getattr(By, el['by'].upper()), value)))
    except:
        pass

    # 返回定位到的元素位置
    return el_location


def locating_elements(elements):
    # 初始化存储元素位置的字典
    elements_location = {}
    # 遍历元素列表，逐个定位元素并存储到字典中
    for el in elements:
        elements_location[el] = locating_element(el)
    # 返回包含所有元素位置的字典
    return elements_location


def locating_data(keys):
    # 初始化存储数据位置的字典
    data_location = {}

    # 遍历传入的关键字列表
    for key in keys:
        # 对每个关键字调用之前定义的 locating_element 函数进行定位
        data_location[key] = locating_element(key)

    # 返回包含所有数据位置的字典
    return data_location
