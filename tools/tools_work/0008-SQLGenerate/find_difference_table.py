#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: find_difference_table.py
@time: 2020/11/2 15:48
@desc: 根据123个表名和146个表名，找出其中没有的表
"""

import pandas as pd

root_path = 'E:/【冲鸭】/【工作】1. 工作安排、文件存储/20201102-新双周+ESMS表注释重命名+质量指标/'
esms_tables_path = root_path + 'esms表.xlsx'
esms_alters_path = root_path + 'esms_tables_rep.txt'

with open(esms_alters_path, 'r') as f:
    esms_alters = f.readline()
esms_alters = esms_alters.split(',')

df = pd.read_excel(esms_tables_path)
esms_tables = df['系统表'].values


def check_in_alter(table_name: str):
    """检查表名是否再alter表中"""
    for ea in esms_alters:
        if ea.lower() == table_name.lower():
            return True
    return False


# 不缺是1，缺是0
is_refer = []
file_not_in = []
for name in esms_tables:
    if not check_in_alter(name):
        is_refer.append(0)
        file_not_in.append(name)
    else:
        is_refer.append(1)

# 保存信息
df['是否在123个表中'] = is_refer
df.set_index('序号', inplace=True)
df.to_excel(root_path + 'esms各个表是否在123个表中.xlsx')

print(file_not_in)
print('没有统计的表数量：', len(file_not_in))
print(len(esms_tables), len(esms_alters))
print('应该的值：', len(esms_tables) - len(esms_alters))
