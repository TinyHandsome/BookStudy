#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: mytest.py
@time: 2022/3/6 8:35
@desc: 测试
"""
import json

from structure.my_models import UnVerified


def mytest1():
    # path1 = '未修正数据样本.json'
    path1 = '未审核数据样本.json'

    with open(path1, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # temp = UnRevised(**data)
    temp = UnVerified(**data)

    print(temp)

    # print('\n'.join(data.keys()))


if __name__ == '__main__':
    mytest1()
