#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: sample_data_produce1.py
@time: 2019/2/3 21:46
@desc: 一个简单的程序来生成样例数据
"""

import tensorflow as tf


# 创建TFRecord文件的帮助函数
def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


# 模拟海量数据情况下将数据写入不同的文件。num_shards定义了总共写入多少个文件
# instances_per_shard定义了每个文件中有多少个数据
num_shards = 2
instances_per_shard = 2
for i in range(num_shards):
    # 将数据分为多个文件时，可以将不同文件以类似0000n-of-0000m的后缀区分。其中m表示了
    # 数据总共被存在了多少个文件，n表示当前文件的编号。式样的方式既方便了通过正则表达式
    # 获取文件列表，又在文件名中加入了更多的信息。
    filename = ('./data.tfrecords-%.5d-of-%0.5d' % (i, num_shards))
    writer = tf.python_io.TFRecordWriter(filename)
    # 将数据封装成Example结构并写入TFRecord文件
    for j in range(instances_per_shard):
        # Example结构仅包含当前样例属于第几个文件以及是当前文件的第几个样本
        example = tf.train.Example(features=tf.train.Features(feature={
            'i': _int64_feature(i),
            'j': _int64_feature(j)
        }))
        writer.write(example.SerializeToString())
    writer.close()