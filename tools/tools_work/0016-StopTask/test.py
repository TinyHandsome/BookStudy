#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: test.py
@time: 2020/12/30 17:56
@desc: 测试，获取结果
"""


from task_schedule_info import MysqlInfo


mi = MysqlInfo()
sql = "select * from metadata.dict_dataset where urn = 'hive://hive_xfliang/wh_test';"
df = mi.select_sql(sql)
for v in df.values[0]:
    print(v)
    print('-'*100)
