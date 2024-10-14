#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: test1.py
@time: 2020/12/26 11:19
@desc: 一些简单的测试
"""

with open('test1.txt', 'a+', encoding='utf-8') as f:
    print('你好吗？', file=f)
    print('狗贼？', file=f)
