#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: dataset_test4.py
@time: 2019/2/10 13:44
@desc: 用initializable_iterator来动态初始化数据集的例子
"""

import tensorflow as tf
from figuredata_deal.dataset_test3 import parser


# 解析一个TFRecord的方法。与上面的例子相同不再重复。
# 从TFRecord文件创建数据集，具体文件路径是一个placeholder，稍后再提供具体路径。
input_files = tf.placeholder(tf.string)
dataset = tf.data.TFRecordDataset(input_files)
dataset = dataset.map(parser)

# 定义遍历dataset的initializable_iterator
iterator = dataset.make_initializable_iterator()
feat1, feat2 = iterator.get_next()

with tf.Session() as sess:
    # 首先初始化iterator，并给出input_files的值。
    sess.run(iterator.initializer, feed_dict={input_files: ['./input_file1', './input_file2']})

    # 遍历所有数据一个epoch，当遍历结束时，程序会抛出OutOfRangeError
    while True:
        try:
            sess.run([feat1, feat2])
        except tf.errors.OutOfRangeError:
            break