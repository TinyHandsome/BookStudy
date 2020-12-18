#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: dataset_test2.py
@time: 2019/2/10 11:03
@desc: 数据是文本文件
"""

import tensorflow as tf

# 从文本文件创建数据集。假定每行文字是一个训练例子。注意这里可以提供多个文件。
input_files = ['./input_file11', './input_file22']
dataset = tf.data.TextLineDataset(input_files)

# 定义迭代器用于遍历数据集
iterator = dataset.make_one_shot_iterator()
# 这里get_next()返回一个字符串类型的张量，代表文件中的一行。
x = iterator.get_next()
with tf.Session() as sess:
    for i in range(4):
        print(sess.run(x))