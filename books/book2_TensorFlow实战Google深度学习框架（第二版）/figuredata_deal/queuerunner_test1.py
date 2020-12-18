#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: queuerunner_test1.py
@time: 2019/2/3 12:31
@desc: 如何使用tf.QueueRunner和tf.Coordinator来管理多线程队列操作。
"""

import tensorflow as tf

# 声明一个先进先出的队列，队列中最多100个元素，类型为实数
queue = tf.FIFOQueue(100, "float")
# 定义队列的入队操作
enqueue_op = queue.enqueue([tf.random_normal([1])])

# 使用tf.train.QueueRunner来创建多个线程运行队列的入队操作。
# tf.train.QueueRunner的第一个参数给出了被操作的队列，[enqueue_op] * 5
# 表示了需要启动5个线程，每个线程中运行的是enqueue_op操作
qr = tf.train.QueueRunner(queue, [enqueue_op] * 5)

# 将定义过的QueueRunner加入Tensorflow计算图上指定的集合。
# tf.train.add_queue_runner函数没有指定集合
# 则加入默认集合tf.GraphKeys.QUEUE_RUNNERS。下面的函数就是将刚刚定义的
# qr加入默认的tf.GraphKeys.QUEUE_RUNNER集合。
tf.train.add_queue_runner(qr)
# 定义出队操作
out_tensor = queue.dequeue()

with tf.Session() as sess:
    # 使用tf.train.Coordinator来协同启动的线程。
    coord = tf.train.Coordinator()
    # 使用tf.train.QueueRunner时，需要明确调用tf.train.start_queue_runners
    # 来启动所有线程。否则因为没有线程运行入队操作，当调用出队操作的时候，程序会一直
    # 等待入队操作被运行。tf.train.start_queue_runners函数会默认启动
    # tf.GraphKeys.QUEUE_RUNNERS集合中所有的QueueRunner。因为这个函数值支持启动
    # 指定集合中的QueueRunner，所以一般来说tf.train.add_queue_runner函数和
    # tf.trian.start_queue_runners函数会指定同一个集合。
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    # 获取队列中的取值。
    for _ in range(3):
        print(sess.run(out_tensor)[0])

    # 使用tf.train.Coordinator来停止所有的线程
    coord.request_stop()
    coord.join(threads)