#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: tensorboard_test7.py
@time: 2019/5/12 20:45
@desc: 使用MNIST测试数据生成PROJECTOR所需要的两个文件。（一个sprite图像，一个tsv文件）
"""

import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os
from tensorflow.examples.tutorials.mnist import input_data


# PROJECTOR需要的日志文件名和地址相关参数。
LOG_DIR = './log2'
SPRITE_FILE = 'mnist_sprite.jpg'
META_FILE = "mnist_meta.tsv"


# 使用给出的MNIST图片列表生成sprite图像。
def create_sprite_image(images):
    if isinstance(images, list):
        images = np.array(images)
    img_h = images.shape[1]
    img_w = images.shape[2]
    # sprite图像可以理解成是所有小图片拼成的大正方形矩阵，大正方形矩阵中的每一个
    # 元素就是原来的小图片。于是这个正方形的边长就是sqrt(n)，其中n为小图片的数量。
    # np.ceil向上取整。np.floor向下取整。
    m = int(np.ceil(np.sqrt(images.shape[0])))

    # 使用全1来初始化最终的大图片。
    sprite_image = np.ones((img_h*m, img_w*m))

    for i in range(m):
        for j in range(m):
            # 计算当前图片的编号
            cur = i * m + j
            if cur < images.shape[0]:
                # 将当前小图片的内容复制到最终的sprite图像。
                sprite_image[i*img_h: (i+1)*img_h, j*img_w: (j+1)*img_w] = images[cur]

    return sprite_image


# 加载MNIST数据。这里指定了one_hot=False，于是得到的labels就是一个数字，表示当前图片所表示的数字。
mnist = input_data.read_data_sets('D:/Python3Space/BookStudy/book2/MNIST_data', one_hot=False)

# 生成sprite图像
to_visualise = 1 - np.reshape(mnist.test.images, (-1, 28, 28))
sprite_image = create_sprite_image(to_visualise)

# 将生成的sprite图像放到相应的日志目录下。
path_for_mnist_sprites = os.path.join(LOG_DIR, SPRITE_FILE)
plt.imsave(path_for_mnist_sprites, sprite_image, cmap='gray')
plt.imshow(sprite_image, cmap='gray')

# 生成每张图片对应的标签文件并写到相应的日志目录下。
path_for_mnist_metadata = os.path.join(LOG_DIR, META_FILE)
with open(path_for_mnist_metadata, 'w') as f:
    f.write('Index\tLabel\n')
    for index, label in enumerate(mnist.test.labels):
        f.write("%d\t%d\n" % (index, label))