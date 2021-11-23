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
from threading import Thread

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

current_num = 1
answers_dict = {}


def check_if_output():
    """检查当前数据是否满足输出，不然就等等"""
    global current_num
    print(answers_dict.keys())

    while True:
        temp = answers_dict.get(current_num)
        if temp is None:
            break
        else:
            answer, doc = temp
            print('题' + str(current_num) + '：' + content.replace('\n', '').strip())
            print('参考答案：', answer, doc)
            print('*' * 100)
            current_num += 1


def thread_it(content, question_num):
    answer, info = wm.get_answer(content)
    answers_dict.update({question_num: (answer, info)})
    check_if_output()


# 多线程运行
thread_list = []
for ti in tis:
    content = ti.get('content')
    question_num = ti.get('question_num')
    t = Thread(target=thread_it, args=(content, question_num,))
    thread_list.append(t)

# [Python多线程中阻塞(join)与锁(Lock)使用误区解析](https://blog.csdn.net/cd_xuyue/article/details/52052893)
for t in thread_list:
    t.start()

for t in thread_list:
    t.join()
