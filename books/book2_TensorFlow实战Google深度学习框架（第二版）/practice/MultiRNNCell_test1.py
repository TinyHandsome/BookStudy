#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: MultiRNNCell_test1.py
@time: 2018/12/24 10:57
@desc: 深层循环神经网络练习1
"""

import tensorflow as tf

# 定义一个基本的LSTM结构作为循环体的基础结构。深层循环神经网络也支持使用其他的循环体结构。
lstm_cell = tf.nn.rnn_cell.BasicLSTMCell

# 通过MultiRNNCell类实现深层循环神经网络中每一个时刻的前向传播过程。其中number_of_layers表示有多少层，也就是图中
# 从xt到ht需要经过多少个LSTM结构。注意从TensorFLow 1.1版本起，不能使用[lstm_cell(lstm_size)] * N的形式来初始化
# MultiRNNCell，否则TensorFlow会在每一层之间共享参数。
stacked_lstm = tf.nn.rnn_cell.MultiRNNCell([lstm_cell(lstm_size) for _ in range(number_of_layers)])

# 和经典神经网络一样，可以通过zero_state函数来获取初始状态。
state = stacked_lstm.zero_state(batch_size, tf.float32)

# 和前面中给出的代码一样，计算每一时刻的前向传播结果。
for i in range(len(num_steps)):
    if i > 0:
        tf.get_variable_scope().reuse_variables()
    stacked_lstm_output, state = stacked_lstm(current_input, state)
    final_output = fully_connected(stacked_lstm_output)
    loss += calc_loss(final_output, expected_output)
