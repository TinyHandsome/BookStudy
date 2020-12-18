#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: gru_test1.py
@time: 2019/6/19 17:07
@desc: GRU单元
"""

import tensorflow as tf
import numpy as np
from tensorflow.contrib.layers import fully_connected
from tensorflow.contrib.rnn import GRUCell
from tensorflow.contrib.rnn import MultiRNNCell
from tensorflow.contrib.rnn import OutputProjectionWrapper
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


n_steps = 100
n_inputs = 1
n_neurous = 100
n_outputs = 1

n_layers = 10

learning_rate = 0.00001

n_iterations = 10000
batch_size = 50

X = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
y = tf.placeholder(tf.float32, [None, n_steps, n_outputs])

# 现在在每个时间迭代，有一个大小为100的输出向量，但是实际上我们需要一个单独的输出值。
# 最简单的解决方案是将单元格包装在OutputProjectionWrapper中。
# cell = OutputProjectionWrapper(BasicRNNCell(num_units=n_neurous, activation=tf.nn.relu), output_size=n_outputs)

# 用技巧提高速度
# cell = BasicRNNCell(num_units=n_neurous, activation=tf.nn.relu)
# multi_layer_cell = MultiRNNCell([cell] * n_layers)
layers = [GRUCell(num_units=n_neurous, activation=tf.nn.relu) for _ in range(n_layers)]
multi_layer_cell = MultiRNNCell(layers)
rnn_outputs, states = tf.nn.dynamic_rnn(multi_layer_cell, X, dtype=tf.float32)
stacked_rnn_outputs = tf.reshape(rnn_outputs, [-1, n_neurous])
stacked_outputs = fully_connected(stacked_rnn_outputs, n_outputs, activation_fn=None)
outputs = tf.reshape(stacked_outputs, [-1, n_steps, n_outputs])

loss = tf.reduce_mean(tf.square(outputs - y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
training_op = optimizer.minimize(loss)

init = tf.global_variables_initializer()

X_data = np.linspace(0, 15, 101)
with tf.Session() as sess:
    init.run()
    for iteration in range(n_iterations):
        X_batch = X_data[:-1][np.newaxis, :, np.newaxis]
        y_batch = X_batch * np.sin(X_batch) / 3 + 2 * np.sin(5 * X_batch)
        sess.run(training_op, feed_dict={X: X_batch, y: y_batch})
        if iteration % 100 == 0:
            mse = loss.eval(feed_dict={X: X_batch, y: y_batch})
            print(iteration, "\tMSE", mse)

    X_new = X_data[1:][np.newaxis, :, np.newaxis]
    y_true = X_new * np.sin(X_new) / 3 + 2 * np.sin(5 * X_new)
    y_pred = sess.run(outputs, feed_dict={X: X_new})

print(X_new.flatten())
print('真实结果：', y_true.flatten())
print('预测结果：', y_pred.flatten())

plt.rcParams['font.sans-serif']=['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
fig = plt.figure(dpi=150)
plt.plot(X_new.flatten(), y_true.flatten(), 'r', label='y_true')
plt.plot(X_new.flatten(), y_pred.flatten(), 'b', label='y_pred')
plt.title('GRU预测')
plt.legend()
plt.show()