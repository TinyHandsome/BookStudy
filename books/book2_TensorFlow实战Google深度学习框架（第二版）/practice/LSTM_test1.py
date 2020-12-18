#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: LSTM_test1.py
@time: 2018/12/23 13:37
@desc: LSTM测试1
"""

import tensorflow as tf

# 定义一个LSTM结构。再Tensorflow中通过一句简单的命令就可以实现一个完整的LSTM结构。
# LSTM中使用的变量也会在该函数中自动被声明
lstm = tf.nn.rnn_cell.BasicLSTMCell(lstm_hidden_size)

# 将LSTM中的状态初始化为全0数组。BasicLSTMCell类提供了zero_state函数来生成全零的初始状态。state是一个包含两个张量的
# LSTMStateTuple类，其中state.c和state.h分别对应了图中的c状态和h状态。
# 和其他神经网络类似，在优化循环神经网络时，每次也会使用一个batch的训练样本。
# 以下代码中，batch_size给出了一个batch的大小。
state = lstm.zero_state(batch_size, tf.float32)

# 定义损失函数。
loss = 0.0
# 虽然在测试时循环神经网络可以处理任意长度的序列，但是在训练中为了将循环网络展开成前馈神经网络，我们需要知道训练数据的序列长度。
# 在以下代码中，用num_steps来表示这个长度。第9章将介绍使用dynamic_rnn动态处理变长序列的方法。
for i in range(num_steps):
    # 在第一个时刻声明LSTM结构中使用的变量，在之后的时刻都需要复用之前定义好的变量。
    if i > 0:
        tf.get_variable_scope().reuse_variables()

    # 每一步处理时间序列中的一个时刻。将当前输入current_input(xt)和前一时刻状态state(ht-1和ct-1)闯入定义的LSTM结构
    # 可以得到当前LSTM的输出lstm_output(ht)和更新后的状态state(ht和ct)。lstm_output用于输出给其他层，state用于输出给
    # 下一时刻，它们在dropout等方面可以有不同的处理方式。
    lstm_output, state = lstm(current_input, state)
    # 将当前时刻LSTM结构的输出传入一个全连接层得到最后的输出。
    final_output = fully_connected(lstm_output)
    # 计算当前时刻输出的损失。
    loss += calc_loss(final_output, expected_output)

# 使用类似第4章中介绍的方法训练模型。
