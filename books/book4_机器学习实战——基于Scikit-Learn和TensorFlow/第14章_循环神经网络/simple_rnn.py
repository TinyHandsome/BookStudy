#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: simple_rnn.py
@time: 2019/6/15 16:53
@desc: 实现一个最简单的RNN网络。我们将使用tanh激活函数创建一个由5个
        神经元组成的一层RNN。假设RNN只运行两个时间迭代，每个时间迭代
        输入一个大小为3的向量。
"""
import tensorflow as tf
import numpy as np

n_inputs = 3
n_neurons = 5

x0 = tf.placeholder(tf.float32, [None, n_inputs])
x1 = tf.placeholder(tf.float32, [None, n_inputs])

Wx = tf.Variable(tf.random_normal(shape=[n_inputs, n_neurons], dtype=tf.float32))
Wy = tf.Variable(tf.random_normal(shape=[n_neurons, n_neurons], dtype=tf.float32))
b = tf.Variable(tf.zeros([1, n_neurons], dtype=tf.float32))

y0 = tf.tanh(tf.matmul(x0, Wx) + b)
y1 = tf.tanh(tf.matmul(y0, Wy) + tf.matmul(x1, Wx) + b)

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