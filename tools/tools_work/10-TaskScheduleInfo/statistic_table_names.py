#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: statistic_table_names.py
@time: 2020/11/13 9:26
@desc: 统计重复的表名
"""

from task_schedule_info import MysqlInfo
from collections import Counter
import pandas as pd


db = MysqlInfo()
sql = "select * from P_PROCESS_DEF where process_name like 'ODS_%' "
data = db.select_sql(sql)

# 处理数据，将所有的后缀统计一遍
data_dict: dict = {}
for name in data['process_name']:
    task = '_'.join(name.split('_')[2:])

    if task not in data_dict.keys():
        data_dict[task] = [name]
    else:
        data_dict[task].append(name)

# result
result = []
for key, value in data_dict.items():
    if len(value) >= 2 and key != '':
        result.append([key] + value)

rr = pd.DataFrame(result, columns=['重复的表名', '流程1', '流程2'])
print(rr)
rr.to_excel('E:/【冲鸭】/【工作】1. 工作安排、文件存储/20201109-ODS修改/重复入湖的表名统计.xlsx', index=False)