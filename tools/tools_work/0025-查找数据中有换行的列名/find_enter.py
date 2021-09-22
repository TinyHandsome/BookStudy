#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: find_enter.py
@time: 2021/9/22 19:09
@desc: 查找数据中有换行的列名
"""

import pandas as pd

file_path = r'E:\1-工作\1-工作\20210922-正式环境上线流程\派车单_20210922(1).csv'

df = pd.read_csv(file_path)
columns = df.columns
current_column_number = 0
count = 0
count_columns = []

for x in df.values:
    current_column_number += 1
    for c, v in zip(columns, x):
        v = str(v)
        if '\n' in v or '\r' in v:
            count += 1
            if c not in count_columns:
                count_columns.append(c)
            print(current_column_number, '行有换行符', '值为：', v, '列名为：', c, '来源：', x[-2])

print('一共有：', count, '个')
print(count_columns)