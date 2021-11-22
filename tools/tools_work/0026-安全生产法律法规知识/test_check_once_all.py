#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: test_check_once_all.py
@time: 2021/11/22 10:06
@desc: 答题测试
"""

from word_matrix import WordMatrix

import requests
import json
import pandas as pd

pd.set_option('display.max_columns', None)

simulate_id = input('请输入simulate_id后回车：')

url = 'http://yjksapi.sdrhup.com/simulateGetQuestion'
res = requests.post(url, data={"exam_id": 2, "simulate_id": simulate_id})
result = json.loads(res.text)
info = result.get('info')


def get_info(aim_dict, key_name):
    return aim_dict.get(key_name).get('question')


tis = []
tis.extend(get_info(info, 'radio'))
tis.extend(get_info(info, 'check'))
tis.extend(get_info(info, 'judge'))

wm = WordMatrix()
wm.generate_word_matrix()

contents = []
questions = []
for ti in tis:
    contents.append(ti.get('content'))
    questions.append(ti.get('question_num'))
answers = wm.get_answers(contents)

answer_list = []
for question_num, answer, content in zip(questions, answers, contents):
    print('题' + str(question_num) + '：' + content.replace('\n', '').strip())
    print('参考答案：', answer[0], answer[1])
    answer_list.append(answer[0])
    print('*' * 100)

print('所有答案：')
for i in range(len(answer_list) // 5):
    print(i * 5 + 1, '-', i * 5 + 5, ': \t', end='')
    print(', '.join(answer_list[5 * i:5 * (i + 1)]))

if len(answer_list) % 5 != 0:
    curernt_i = len(answer_list) // 5 + 1
    print(curernt_i * 5 + 1, '-', len(answer_list), ': \t', ', '.join(answer_list[curernt_i * 5:]))
