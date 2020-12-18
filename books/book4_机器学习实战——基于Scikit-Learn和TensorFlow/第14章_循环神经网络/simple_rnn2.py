#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: simple_rnn2.py
@time: 2019/6/15 17:06
@desc: 与前一个程序相同
"""

import tensorflow as tf
from tensorflow.contrib.rnn import BasicRNNCell
from tensorflow.contrib.rnn import static_rnn
import numpy as np

n_inputs = 3
n_neurons = 5

x0 = tf.placeholder(tf.float32, [None, n_inputs])
x1 = tf.placeholder(tf.float32, [None, n_inputs])

basic_cell = BasicRNNCell(num_units=n_neurons)
output_seqs, states = static_rnn(basic_cell, [x0, x1], dtype=tf.float32)

y0, y1 = output_seqs

init = tf.global_variables_initializer()

# Mini-batch：包含4个实例的小批次
x0_batch = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 0, 1]])   # t=0
x1_batch = np.array([[9, 8, 7], [0, 0, 0], [6, 5, 4], [3, 2, 1]])   # t=1

with tf.Session() as sess:
    init.run()
    y0_val, y1_val = sess.run([y0, y1], feed_dict={x0: x0_batch, x1: x1_batch})
    print(y0_val)
    print('-'*50)
    print(y1_val)