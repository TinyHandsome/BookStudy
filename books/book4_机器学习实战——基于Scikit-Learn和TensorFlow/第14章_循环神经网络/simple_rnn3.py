#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: simple_rnn3.py
@time: 2019/6/16 10:57
@desc: 同上
"""

import tensorflow as tf
from tensorflow.contrib.rnn import BasicRNNCell
from tensorflow.contrib.rnn import static_rnn
import numpy as np


n_steps = 2
n_inputs = 3
n_neurons = 5

x = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
x_seqs = tf.unstack(tf.transpose(x, perm=[1, 0, 2]))
basic_cell = BasicRNNCell(num_units=n_neurons)
output_seqs, states = static_rnn(basic_cell, x_seqs, dtype=tf.float32)
outputs = tf.transpose(tf.stack(output_seqs), perm=[1, 0, 2])

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