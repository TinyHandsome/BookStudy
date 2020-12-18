#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: keras_test4.py
@time: 2019/5/7 15:45
@desc: 实现Keras与TensorFlow联合起来解决MNIST问题。
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


mnist_data = input_data.read_data_sets('D:/Python3Space/BookStudy/book2/MNIST_data', one_hot=True)

# 通过TensorFlow中的placeholder定义输入。类似的，Keras封装的网络层结构也可以支持使用
# 前面章节中介绍的输入队列。这样可以有效避免一次性加载所有数据的问题。
x = tf.placeholder(tf.float32, shape=(None, 784))
y_ = tf.placeholder(tf.float32, shape=(None, 10))

# 直接使用TensorFlow中提供的Keras API定义网络结构。
net = tf.keras.layers.Dense(500, activation='relu')(x)
y = tf.keras.layers.Dense(10, activation='softmax')(net)

# 定义损失函数和优化方法。注意这里可以混用Keras的API和原生态TensorFlow的API
loss = tf.reduce_mean(tf.keras.losses.categorical_crossentropy(y_, y))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

# 定义预测的正确率作为指标。
acc_value = tf.reduce_mean(tf.keras.metrics.categorical_accuracy(y_, y))

# 使用原生态TensorFlow的方式训练模型。这样可以有效地实现分布式。
with tf.Session() as sess:
    tf.global_variables_initializer().run()

    for i in range(10000):
        xs, ys = mnist_data.train.next_batch(100)
        _, loss_value = sess.run([train_step, loss], feed_dict={x: xs, y_: ys})

        if i % 1000 == 0:
            print("After %d training step(s), loss on training batch is %g." % (i, loss_value))

    print(acc_value.eval(feed_dict={x: mnist_data.test.images,
                                    y_: mnist_data.test.labels}))