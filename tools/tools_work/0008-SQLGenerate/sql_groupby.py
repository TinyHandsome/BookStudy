#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: sql_groupby.py
@time: 2020/11/4 9:14
@desc: sql贴到流程中去，分组
"""

import pandas as pd
import math
from collections import Counter


path = 'E:/【冲鸭】/【工作】1. 工作安排、文件存储/20201102-新双周+ESMS表注释重命名+质量指标/'
aim_file = path + 'esms各个表是否在123个表中.xlsx'

df = pd.read_excel(aim_file)
df.set_index('序号', inplace=True)

everyone_task_num = math.ceil(df.shape[0] / 6)
groups = {
    0: '李添',
    1: '彭煜',
    2: '于德龙',
    3: '杜世斌',
    4: '窦会涛',
    5: '梁晓峰'
}

result = []
for i in df.index:
    result.append(groups.get(math.floor(i/everyone_task_num)))

print(Counter(result))

df['分组'] = result
df.to_excel(path + 'esms分组修改sql-comment.xlsx')
