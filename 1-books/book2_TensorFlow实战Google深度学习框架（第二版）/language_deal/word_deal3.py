#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: word_deal3.py
@time: 2019/2/23 16:36
@desc: 从文本文件中读取数据，并按照下面介绍的方案将数据整理成batch。
        方法是：先将整个文档切分成若干连续段落，再让batch中的每一个位置负责其中一段。
"""

import numpy as np
import tensorflow as tf


# 使用单词编号表示的训练数据
TRAIN_DATA = './ptb.train'
TRAIN_BATCH_SIZE = 20
TRAIN_NUM_STEP = 35


# 从文件中读取数据，并返回包含单词编号的数组
def read_data(file_path):
    with open(file_path, "r") as fin:
        # 将整个文档读进一个长字符串
        id_string = ' '.join([line.strip() for line in fin.readlines()])
    # 将读取的单词编号转为整数
    id_list = [int(w) for w in id_string.split()]
    return id_list


def make_batches(id_list, batch_size, num_step):
    # batch_size: 一个batch中样本的数量
    # num_batches：batch的个数
    # num_step: 一个样本的序列长度
    # 计算总的batch数量。每个batch包含的单词数量是batch_size * num_step
    num_batches = (len(id_list) - 1) // (batch_size * num_step)

    # 将数据整理成一个维度为[batch_size, num_batches*num_step]的二维数组
    data = np.array(id_list[: num_batches * batch_size * num_step])
    data = np.reshape(data, [batch_size, num_batches * num_step])

    # 沿着第二个维度将数据切分成num_batches个batch，存入一个数组。
    data_batches = np.split(data, num_batches, axis=1)

    # 重复上述操作，但是每个位置向右移动一位，这里得到的是RNN每一步输出所需要预测的下一个单词
    label = np.array(id_list[1: num_batches * batch_size * num_step + 1])
    label = np.reshape(label, [batch_size, num_batches * num_step])
    label_batches = np.split(label, num_batches, axis=1)
    # 返回一个长度为num_batches的数组，其中每一项包括一个data矩阵和一个label矩阵
    print(len(id_list))
    print(num_batches * batch_size * num_step)
    return list(zip(data_batches, label_batches))


def main():
    train_batches = make_batches(read_data(TRAIN_DATA), TRAIN_BATCH_SIZE, TRAIN_NUM_STEP)
    # 在这里插入模型训练的代码。训练代码将在后面提到。
    for i in train_batches:
        print(i)


if __name__ == '__main__':
    main()
