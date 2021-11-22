#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: get_items.py
@time: 2021/11/22 9:26
@desc: 获取安全生产法律法规知识大考试题库
"""

from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

pd.set_option('display.max_columns', None)

url = 'http://yjksapi.sdrhup.com/simulateStudy'
res = requests.post(url, data={"exam_id": 2, "class": 1})
result = json.loads(res.text)
info = result.get('info')
contents = []
t_type = []
A = []
B = []
C = []
D = []
answers = []


def get_info(aim_dict, key_name):
    return aim_dict.get(key_name).replace('\n', '')


for t, v in info.items():
    # 类型，结果
    for every_ti in v:
        contents.append(get_info(every_ti, 'content'))
        t_type.append(t)
        A.append(get_info(every_ti, 'a'))
        B.append(get_info(every_ti, 'b'))
        C.append(get_info(every_ti, 'c'))
        D.append(get_info(every_ti, 'd'))
        answers.append(get_info(every_ti, 'answer'))

target = {'题目': contents, '题型': t_type, '答案': answers, 'A': A, 'B': B, 'C': C, 'D': D}
rr = pd.DataFrame.from_dict(target)
rr.index.name = '编号'

rr.to_excel('./datas/安全生产法律法规知识大考试题库.xlsx')


