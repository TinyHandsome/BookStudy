#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: add_double_quatation.py
@time: 2022/1/27 17:03
@desc: 给每一行首位增加双引号，逗号前
"""


def f(l: str, final, add, prefix, case):
    l = l.strip()
    aim_l = l.replace(final, '')
    if case == '1':
        aim_l = aim_l.lower()
    if case == '2':
        aim_l = aim_l.upper()

    return prefix + add + aim_l + add + final


def add_double_quatation(s: str, final=',', add='"', prefix='', case=0):
    s = s.strip()
    s_list = s.split('\n')
    new_slist = [f(a, final, add, prefix, case) for a in s_list]
    return '\n'.join(new_slist)
