#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: tfrecord_test2.py
@time: 2019/1/20 21:29
@desc: 读取TFRecord文件中的数据
"""

import tensorflow as tf
import tfrecord_test1


# 创建一个reader来读取TFRecord文件中的样例。
reader = tf.TFRecordReader()
# 创建一个队列来维护输入文件列表
# tf.train.string_input_producer函数
filename_queue = tf.train.string_input_producer([tfrecord_test1.filename])

# 从文件中读出一个样例。也可以使用read_up_to函数一次性读取多个样例
_, serialized_example = reader.read(filename_queue)
# 解析读入的一个样例，如果需要解析多个样例，可以用parse_example函数
features = tf.parse_single_example(
    serialized_example,
    features={
        # TensorFlow提供两种不同的属性解析方法。一种方法是tf.FixedLenFeature，
        # 这种方法解析的结果为一个Tensor。另一种方法是tf.VarLenFeature，这种方法
        # 得到的解析结果为SparseFeature，用于处理稀疏数据。这里解析数据的格式需要和
        # 上面的程序写入数据的格式保持一致。
        'image_raw': tf.FixedLenFeature([], tf.string),
        'pixels': tf.FixedLenFeature([], tf.int64),
        'label': tf.FixedLenFeature([], tf.int64),
    }
)

# tf.decode_raw可以将字符串解析成图像对应的像素数组
image = tf.decode_raw(features['image_raw'], tf.uint8)
label = tf.cast(features['label'], tf.int32)
pixels = tf.cast(features['pixels'], tf.int32)

with tf.Session() as sess:
    # 启动多线程处理输入数据，下面将更加详细地介绍TensorFlow多线程的处理。
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    # 每次运行可以读取TFRecord文件中的一个样例。当所有样例都读完之后，在此样例中程序会再重头读取。
    for i in range(10):
        print(sess.run([image, label, pixels]))