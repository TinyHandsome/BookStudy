#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: base_func1.py
@time: 2022/1/28 16:56
@desc: 一些基础函数
"""


def is_None_or_nullstr(s):
    """判断是否为None或空字符串"""
    if s is None or s == '':
        return True
    else:
        return False
