#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: dataset_test1.py
@time: 2019/2/10 10:52
@desc: 例子：从一个张量创建一个数据集，遍历这个数据集，并对每个输入输出y = x^2 的值。
"""

import tensorflow as tf

# 从一个数组创建数据集。
input_data = [1, 2, 3, 5, 8]
dataset = tf.data.Dataset.from_tensor_slices(input_data)

# 定义一个迭代器用于遍历数据集。因为上面定义的数据集没有用placeholder作为输入参数
# 所以这里可以使用最简单的one_shot_iterator
iterator = dataset.make_one_shot_iterator()
# get_next() 返回代表一个输入数据的张量，类似于队列的dequeue()。
x = iterator.get_next()
y = x * x

with tf.Session() as sess:
    for i in range(len(input_data)):
        print(sess.run(y))