#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: inception_test1.py
@time: 2018/12/26 20:42
@desc: Inception-v3模型中结构相对复杂的一个Inception模块的代码实现
"""

import tensorflow as tf

# 加载slim库
slim = tf.contrib.slim

# slim.arg_scope函数可以用于设置默认的参数取值。slim.arg_scope函数的第一个参数是一个函数列表。在这个列表中的函数将使用默认的
# 参数取值。比如通过下面的定义，调用slim.conv2d(new, 320, [1, 1])函数时会自动加上stride=1和padding='SAME'的参数。
# 如果在函数调用时指定了stride，那么这里设置的默认值就不会再使用。通过这种方式可以进一步减少冗余的代码。
with slim.arg_scope([slim.conv2d, slim.max_pool2d, slim.avg_pool2d], stride=1, padding='VALID'):
    # ...
    # 此处省略了Inception-v3模型中其他神经网络结构而直接实现最后面红色方框中的。
    # Inception结构。假设输入图片经过之前的神经网络前向传播的结果保存在变量net中。
    # net = 上一层的输入节点矩阵
    # 为一个Inception模块声明一个统一的变量命名空间。
    with tf.variable_scope('Mixed_7c'):
        # 给Inception模块中每一条路径声明一个命名空间。
        with tf.variable_scope('Branch_0'):
            # 实现一个过滤器变成为1，深度为320的卷积层。
            branch_0 = slim.conv2d(net, 320, [1, 1], scope='Conv2d_0a_1x1')

        # Inception模块中第二条路径。这条计算路径上的结构本身也是一个Inception结构。
        with tf.variable_scope('Branch_1'):
            branch_1 = slim.conv2d(net, 384, [1, 1], scope='Conv2d_0a_1x1')
            # tf.concat函数可以将多个矩阵拼接起来。tf.concat函数的第一个参数指定了拼接的维度，这里给出的“3”代表了矩阵是在深度
            # 这个维度上进行拼接。图中展示了在深度上拼接矩阵的方式。
            branch_1 = tf.concat(3, [
                # 如图所示，此处2层卷积层的输入都是branch1而不是net。
                slim.conv2d(branch_1, 384, [1, 3], scope='Conv2d_0b_1x3'),
                slim.conv2d(branch_1, 384, [3, 1], scope='Conv2d_0c_3x1')
            ])

        # Inception模块中第三条路径。此计算路径也是一个Inception结构。
        with tf.variable_scope('Branch_2'):
            branch_2 = slim.conv2d(net, 448, [1, 1], scope='Conv2d_0a_1x1')
            branch_2 = slim.conv2d(branch_2, 384, [3, 3], scope='Conv2d_0b_3x3')
            branch_2 = tf.concat(3, [
                slim.conv2d(branch_2, 384, [1, 3], scope='Conv2d_0c_1x3'),
                slim.conv2d(branch_2, 384, [3, 1], scope='Conv2d_0d_3x1')
            ])

        # Inception模块中第四条路径。
        with tf.variable_scope('Branch_3'):
            branch_3 = slim.avg_pool2d(net, [3, 3], scope='AvgPool_0a_3x3')
            branch_3 = slim.conv2d(branch_3, 192, [1, 1], scope='Conv2d_0b_1x1')

        # 当前Inception模块的最后输出是由上面4个计算结果拼接得到的。
        net = tf.concat(3, [branch_0, branch_1, branch_2, branch_3])