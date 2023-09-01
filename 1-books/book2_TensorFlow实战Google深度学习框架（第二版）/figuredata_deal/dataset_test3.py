#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: dataset_test3.py
@time: 2019/2/10 13:16
@desc: 数据是TFRecord文件
"""

import tensorflow as tf


# 解析一个TFRecord的方法。record是从文件中读取的一个样例。前面介绍了如何解析TFRecord样例。
def parser(record):
    # 解析读入的一个样例
    features = tf.parse_single_example(
        record,
        features={
            'feat1': tf.FixedLenFeature([], tf.int64),
            'feat2': tf.FixedLenFeature([], tf.int64),
        }
    )
    return features['feat1'], features['feat2']


# 从TFRecord文件创建数据集。
input_files = ['./input_file1', './input_file2']
dataset = tf.data.TFRecordDataset(input_files)

# map()函数表示对数据集中的每一条数据进行调用相应方法。使用TFRecordDataset读出的是二进制的数据。
# 这里需要通过map()函数来调用parser()对二进制数据进行解析。类似的，map()函数也可以用来完成其他的数据预处理工作。
dataset = dataset.map(parser)

# 定义遍历数据集的迭代器
iterator = dataset.make_one_shot_iterator()

# feat1, feat2是parser()返回的一维int64型张量，可以作为输入用于进一步的计算。
feat1, feat2 = iterator.get_next()

with tf.Session() as sess:
    for i in range(10):
        f1, f2 = sess.run([feat1, feat2])
        print(f1, f2)