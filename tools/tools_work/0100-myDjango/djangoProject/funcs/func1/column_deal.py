#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: column_deal.py
@time: 2022/1/27 13:27
@desc: 对每个字段进行的处理
"""


def columns_deal(columns, is_select=False):
    """对所有字段进行处理"""
    if is_select:
        return [select_column_deal(x) for x in columns]
    else:
        return [column_deal(x) for x in columns]


def column_deal(column):
    if column.lower() in ['timestamp', 'application']:
        column = '`' + column + '`'

    if '/' in column or column.startswith('_'):
        column = '`' + column + '`'

    return column


def select_column_deal(column):
    if '/' in column:
        column = '"' + column + '"'

    return column
