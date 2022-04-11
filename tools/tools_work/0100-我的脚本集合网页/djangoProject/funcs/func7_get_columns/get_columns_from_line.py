#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: get_columns_from_line.py
@time: 2022/4/11 9:00
@desc: 从一行行代码中获取变量名
        形如：
            1. a = xxxxxx
"""


def split_str_by_enter(lines):
    """按回车分隔为数组"""
    return lines.split("\n")


def assemble_list_by_enter(my_list):
    """通过回车组装列表"""
    return '\n'.join(my_list)


def get_columns_by_equality(lines_list):
    """以等号为分隔"""
    columns = []
    for line in split_str_by_enter(lines_list):
        temp = line.strip().split('=')[0].strip()
        columns.append(temp)

    return assemble_list_by_enter(columns)


if __name__ == '__main__':
    print(get_columns_by_equality(input('aaa:')))
