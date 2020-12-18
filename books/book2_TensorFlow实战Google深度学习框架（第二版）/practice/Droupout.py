#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: Droupout.py
@time: 2018/12/24 14:14
@desc: 如何在TensorFlow中实现带dropout的循环神经网络
"""

import tensorflow as tf

# 定义LSTM结构。
lstm_cell = tf.nn.rnn_cell.BasicLSTMCell

# 使用DropoutWrapper类来实现dropout功能。该类通过两个参数来控制dropout的概率，一个参数为input_keep_prob,它可以用来控制
# 输入的dropout概率，（节点被保留的概率），另一个为output_keep_prob，它可以用来控制输出的dropout概率。
# 在使用了DropoutWrapper的基础上定义MultiRNNCell。
stacked_lstm = tf.nn.rnn_cell.MultiRNNCell(
    [tf.nn.rnn_cell.DropoutWrapper(lstm_cell(lstm_size)) for _ in range(number_of_layers)]
)

# 和前面章节中深层循环网络样例程序类似，运行前向传播过程。
