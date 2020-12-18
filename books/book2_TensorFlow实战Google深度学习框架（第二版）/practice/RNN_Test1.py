#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: RNN_Test1.py
@time: 2018/12/22 13:42
@desc: 循环神经网络练习1
"""


import numpy as np

X = [1, 2]
state = [0.0, 0.0]

# 分开定义不同输入部分的权重以方便操作。
w_cell_state = np.asarray([[0.1, 0.2], [0.3, 0.4]])
w_cell_input = np.asarray([0.5, 0.6])
b_cell = np.asarray([0.1, -0.1])

# 定义用于输出的全连接层参数。
w_output = np.asarray([[1.0], [2.0]])
b_output = 0.1

# 按照时间顺序执行循环神经网络的前向传播过程。
for i in range(len(X)):
    # 计算循环体中的全连接层神经网络。
    before_activation = np.dot(state, w_cell_state) + X[i] * w_cell_input + b_cell
    state = np.tanh(before_activation)

    # 根据当前时刻状态计算最终输出。
    final_output = np.dot(state, w_output) + b_output

    # 输出每个时刻的信息
    print("before activation: ", before_activation)
    print("state: ", state)
    print("output: ", final_output)