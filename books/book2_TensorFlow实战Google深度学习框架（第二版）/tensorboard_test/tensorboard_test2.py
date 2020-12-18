#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: tensorboard_test2.py
@time: 2019/5/10 10:26
@desc: tf.variable_scope与tf.name_scope函数的区别
"""

import tensorflow as tf


with tf.variable_scope("foo"):
    # 在命名空间foo下获取变量"bar"，于是得到的变量名称为“foo/bar”。
    a = tf.get_variable("bar", [1])
    # 输出：foo/bar: 0
    print(a.name)

with tf.variable_scope("bar"):
    # 在命名空间bar下获取变量“bar”，于是得到的变量名称为“bar/bar”。此时变量
    # “bar/bar”和变量“foo/bar”并不冲突，于是可以正常运行。
    b = tf.get_variable("bar", [1])
    # 输出：bar/bar：0

with tf.name_scope("a"):
    # 使用tf.Variable函数生成变量会受到tf.name_scope影响，于是这个变量的名称为“a/Variable”。
    a = tf.Variable([1])
    # 输出：a/Variable：0
    print(a.name)

    # tf.get_variable函数不受tf.name_scope函数的影响。
    # 于是变量并不在a这个命名空间中。
    a = tf.get_variable("b", [1])
    # 输出：b：0
    print(a.name)

with tf.name_scope("b"):
    # 因为tf.get_variable不受tf.name_scope影响，所以这里试图获取名称为
    # “a”的变量。然而这个变量已经被声明了，于是这里会报重复声明的错误
    tf.get_variable("b", [1])