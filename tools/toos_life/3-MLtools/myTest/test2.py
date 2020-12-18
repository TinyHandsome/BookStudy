#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: test2.py
@time: 2020/5/4 0:02
@desc: 测试专用2
"""

from sklearn.datasets import load_digits
import numpy as np

from MLTools import MLTools
from PreAnalysis import PreAnalysis

digits = load_digits()
digits_data = digits['images']
digits_target = digits['target']
digits_names = digits['target_names']

shape = digits_data.shape
X = np.array(digits_data).reshape(shape[0], shape[1] * shape[2])
a, b = 4, 9
index1 = digits_target == a
index2 = digits_target == b
X = np.r_[X[index1], X[index2]]
y = np.r_[digits_target[index1], digits_target[index2]]
names = [str(a), str(b)]

# MLTools().evaluate_origin_model(X, y)
# MLTools().evaluate_adjust_model(X, y)

# 测试数据分析的热力图
# PreAnalysis('./myTest/').correlationMatrix(X)

# 测试Adaboost的调参过程是否正常
m = MLTools('C:/Users/Administrator/Desktop/aaa/')
m.set_X(X)
m.set_y(y)
m.aim(0)
