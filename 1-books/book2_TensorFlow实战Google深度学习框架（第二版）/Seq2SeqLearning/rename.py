#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: rename.py
@time: 2019/4/29 14:23
@desc: 修改TensorFlow训练保存的参数名
"""

import tensorflow as tf
import argparse
import os

parser = argparse.ArgumentParser(description='')

# 原参数路径
parser.add_argument("--checkpoint_path", default='./seq2seq_ckpt-9800', help="restore ckpt")
# 新参数保存路径
parser.add_argument("--new_checkpoint_path", default='./', help="path_for_new ckpt")
# 新参数名称中加入的前缀名
parser.add_argument("--add_prefix", default='nmt_model/', help="prefix for addition")

args = parser.parse_args()

l = ["encoder", "decoder"]


def main():
    # 如果改之后的模型路径不存在就建立这个路径
    if not os.path.exists(args.new_checkpoint_path):
        os.makedirs(args.new_checkpoint_path)
    with tf.Session() as sess:
        # 新建一个空列表存储更新后的Variable变量
        new_var_list = []
        # 得到checkpoint文件中所有的参数（名字，形状）元组
        for var_name, _ in tf.contrib.framework.list_variables(args.checkpoint_path):

            # 得到上述参数的值
            var = tf.contrib.framework.load_variable(args.checkpoint_path, var_name)

            # 如果参数名是我们要修改的l中的两个中的一个，我们就在前面加上nmt_model/
            if l[0] in var_name or l[1] in var_name:
                new_name = var_name
                # 在这里加入了名称前缀，大家可以自由地作修改
                new_name = args.add_prefix + new_name
            else:
                new_name = var_name

            # 除了修改参数名称，还可以修改参数值（var）
            print('Renaming %s to %s.' % (var_name, new_name))
            # 使用加入前缀的新名称重新构造了参数
            renamed_var = tf.Variable(var, name=new_name)
            # 把赋予新名称的参数加入空列表
            new_var_list.append(renamed_var)

        print('starting to write new checkpoint !')
        # 构造一个保存器
        saver = tf.train.Saver(var_list=new_var_list)
        # 初始化一下参数（这一步必做）
        sess.run(tf.global_variables_initializer())
        # 构造一个保存的模型名称
        model_name = 'new_seq2seq_ckpt'
        # 构造一下保存路径
        checkpoint_path = os.path.join(args.new_checkpoint_path, model_name)
        # 直接进行保存
        saver.save(sess, checkpoint_path)
        print("done !")


if __name__ == '__main__':
    main()
