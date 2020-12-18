#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: dynamic_rnn1.py
@time: 2019/6/16 13:37
@desc:  通过时间动态展开 dynamic_rnn
"""

import tensorflow as tf
from tensorflow.contrib.rnn import BasicRNNCell
import numpy as np


n_steps = 2
n_inputs = 3
n_neurons = 5

x = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
basic_cell = BasicRNNCell(num_units=n_neurons)
outputs, states = tf.nn.dynamic_rnn(basic_cell, x, dtype=tf.float32)

x_batch = np.array([
    [[0, 1, 2], [9, 8, 7]],
    [[3, 4, 5], [0, 0, 0]],
    [[6, 7, 8], [6, 5, 4]],
    [[9, 0, 1], [3, 2, 1]],
])

init = tf.global_variables_initializer()

with tf.Session() as sess:
    init.run()
    outputs_val = outputs.eval(feed_dict={x: x_batch})
    print(outputs_val)