#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: main.py
@time: 2020/11/4 9:56
@desc: 主函数
"""


# 根据三个指标excel生成sql，并根据 是否是双表增量 修改特殊的sql
import sql_generate

# 找到上三个excel中不包括的表
import find_difference_table

# 根据表名进行分组
import sql_groupby