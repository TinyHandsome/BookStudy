#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: sample_data_deal1.py
@time: 2019/2/3 22:00
@desc: 展示了tf.train.match_filenames_once函数和tf.train.string_input_producer函数的使用方法
"""

import tensorflow as tf

# 使用tf.train.match_filenames_once函数获取文件列表
files = tf.train.match_filenames_once('./data.tfrecords-*')

# 通过tf.train.string_input_producer函数创建输入队列，输入队列中的文件列表为
# tf.train.match_filenames_once函数获取的文件列表。这里将shuffle参数设为False
# 来避免随机打乱读文件的顺序。但一般在解决真实问题时，会将shuffle参数设置为True
filename_queue = tf.train.string_input_producer(files, shuffle=False)

# 如前面所示读取并解析一个样本
reader = tf.TFRecordReader()
_, serialized_example = reader.read(filename_queue)
features = tf.parse_single_example(
    serialized_example,
    features={
        'i': tf.FixedLenFeature([], tf.int64),
        'j': tf.FixedLenFeature([], tf.int64),
    }
)

with tf.Session() as sess:
    # 虽然在本段程序中没有声明任何变量，但使用tf.train.match_filenames_once函数时
    # 需要初始化一些变量。
    tf.local_variables_initializer().run()
    print(sess.run(files))

    # 声明tf.train.Coordinator类来协同不同线程，并启动线程。
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    # 多次执行获取数据的操作
    for i in range(6):
        print(sess.run([features['i'], features['j']]))

    # 请求处理的线程停止
    coord.request_stop()
    # 等待，直到处理的线程已经停止
    coord.join(threads)