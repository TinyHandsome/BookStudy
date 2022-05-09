#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: spider_code.py
@time: 2022/5/8 14:20
@desc: 行政区划代码查询
"""
import requests
from bs4 import BeautifulSoup
import random
import time


def spider_code_country(six_code, if_sleep=True):
    """行政区划代码查询，默认每次查询间隔 1-2 秒的间隔"""

    # 查询代码格式检查
    if isinstance(six_code, int):
        ...
    else:
        try:
            six_code = six_code.strip()
            if len(six_code) != 6:
                return 'error-你输入的code不是6位数'
            six_code = int(six_code)
        except:
            return 'error-你输入的数据不符合要求'

    root_url = 'http://www.kuaichala.com/idcard/'
    aim_url = root_url + str(six_code) + '.html'
    aim_text = requests.get(aim_url).text

    mybs = BeautifulSoup(aim_text, 'lxml')
    loc, code = mybs.h2.text.split('行政区划代码')

    # 行政区和编码
    loc = loc.strip()
    code = code.strip()

    if if_sleep:
        time.sleep(random.random())

    return loc


if __name__ == '__main__':
    print(spider_code_country(371081))
