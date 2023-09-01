#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: dynamic_rnn2.py
@time: 2019/6/17 9:42
@desc: 处理长度可变输入序列
"""

import tensorflow as tf
from tensorflow.contrib.rnn import BasicRNNCell
import numpy as np


n_steps = 2
n_inputs = 3
n_neurons = 5

seq_length = tf.placeholder(tf.int32, [None])
x = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
basic_cell = BasicRNNCell(num_units=n_neurons)
outputs, states = tf.nn.dynamic_rnn(basic_cell, x, dtype=tf.float32, sequence_length=seq_length)

# 假设第二个输出序列仅包含一个输入。为了适应输入张量X，必须使用零向量填充输入。
x_batch = np.array([
    [[0, 1, 2], [9, 8, 7]],
    [[3, 4, 5], [0, 0, 0]],
    [[6, 7, 8], [6, 5, 4]],
    [[9, 0, 1], [3, 2, 1]],
])

seq_length_batch = np.array([2, 1, 2, 2])

init = tf.global_variables_initializer()

with tf.Session() as sess:
    init.run()
    outputs_val, states_val = sess.run([outputs, states], feed_dict={x: x_batch, seq_length: seq_length_batch})
    print(outputs_val)
    print(states_val)