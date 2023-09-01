#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: dataset_createdata.py
@time: 2019/2/10 13:59
@desc: 创建样例文件
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import time


# 生成整数型的属性。
def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


# 生成字符串型的属性。
def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


a = [11, 21, 31, 41, 51]
b = [22, 33, 44, 55, 66]


# 输出TFRecord文件的地址
filename = './input_file2'
# 创建一个writer来写TFRecord文件
writer = tf.python_io.TFRecordWriter(filename)
for index in range(len(a)):
    aa = a[index]
    bb = b[index]
    # 将一个样例转化为Example Protocol Buffer，并将所有的信息写入这个数据结构。
    example = tf.train.Example(features=tf.train.Features(feature={
        'feat1': _int64_feature(aa),
        'feat2': _int64_feature(bb)
    }))

    # 将一个Example写入TFRecord文件中。
    writer.write(example.SerializeToString())
writer.close()