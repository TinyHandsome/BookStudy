#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: str_funcs.py
@time: 2022/1/28 16:56
@desc: 一些关于字符串的基础函数
"""
import re


def is_None_or_nullstr(s):
    """判断是否为None或空字符串"""
    if s is None or s == '':
        return True
    else:
        return False


def reduce_space(s, keep_enter=True):
    """缩减格"""
    if not keep_enter:
        s = s.replace('\n', '')
    return re.sub(r'[ \t]+', ' ', s)


if __name__ == '__main__':
    # 测试remove_space
    s = """   a  s \n asd"""

