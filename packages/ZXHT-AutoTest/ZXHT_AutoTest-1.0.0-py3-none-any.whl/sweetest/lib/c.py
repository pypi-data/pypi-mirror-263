# -*- coding: utf-8 -*-
"""
@Time : 2024/1/10 14:06
@Author : TJF

"""
import datetime


# write your function this file
def today():
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d')
