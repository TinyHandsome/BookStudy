#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: tl_test1.py
@time: 2019/1/15 19:08
@desc: 迁移学习测试1
"""

import glob
import os.path
import numpy as np
import tensorflow as tf
from tensorflow.python.platform import gfile
import joblib


# 原始输入数据的目录，这个目录下有5个子目录，每个子目录底下保存属于该类别的所有图片
INPUT_DATA = 'C:/Users/Administrator/Desktop/Python3Space/transfer_learning/flower_photos'
# 输入文件地址。将整理后的图片数据通过numpy的格式保存。在第7章中将更加详细地介绍数据预处理，这里先通过numpy来保存。
OUTPUT_FILE = 'C:/Users/Administrator/Desktop/Python3Space/transfer_learning/flower_processed_data2.npy'

# 测试数据和验证数据的比例。
VALIDATION_PERCENTAGE = 10
TEST_PERCENTAGE = 10


# 读取数据并将数据分割成训练数据、验证数据和测试数据。
def create_image_lists(sess, testing_percentage, validation_percentage):
    sub_dirs = [x[0] for x in os.walk(INPUT_DATA)]
    is_root_dir = True

    # 初始化各个数据集
    training_images = []
    training_labels = []
    testing_images = []
    testing_labels = []
    validation_images = []
    validation_labels = []
    current_label = 0

    # 读取所有的子目录
    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue

        # 获取一个子目录中所有的图片文件。
        extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']
        file_list = []

        # 从目录字符串中提取文件名
        dir_name = os.path.basename(sub_dir)

        for extension in extensions:
            file_glob = os.path.join(INPUT_DATA, dir_name, '*.' + extension)
            file_list.extend(glob.glob(file_glob))

        if not file_list:
            continue

        # 处理图片数据。
        for file_name in file_list:
            print('正在处理文件：', file_name, '...')
            # 读取并解析图片，将图片转化为299x299以便于inception-v3模型来处理。
            # 更多关于图像预处理的内容将在第7章中介绍。
            image_raw_data = gfile.FastGFile(file_name, 'rb').read()
            image = tf.image.decode_jpeg(image_raw_data)
            if image.dtype != tf.float32:
                image = tf.image.convert_image_dtype(image, dtype=tf.float32)

            image = tf.image.resize_images(image, [299, 299])
            image_value = sess.run(image)

            # 随机划分数据集
            chance = np.random.randint(100)
            if chance < validation_percentage:
                validation_images.append(image_value)
                validation_labels.append(current_label)
            elif chance < (testing_percentage + validation_percentage):
                testing_images.append(image_value)
                testing_labels.append(current_label)
            else:
                training_images.append(image_value)
                training_labels.append(current_label)
        current_label += 1

    # 将训练数据随机打乱以获得更好的训练结果
    # 随机生成器random，每执行一次，random的状态（state）就会变化一次，所以每次产生的随机数都不同，
    # 或随机操作的效果都不同。而当random的状态（state）不变时，多次执行random的同一操作具有相同的效果。
    # 通过设置相同的state,使得random.shuffle以相同的规律打乱两个列表，进而使得两个列表被打乱后，
    # 仍旧能维持两个列表间元素的一一对应关系。这一点在深度学习的标注数据集的打乱的过程中很有用。
    # 一一对应的image_list 与label_list，在分别打乱后，仍能维持一一对应的关系。
    state = np.random.get_state()
    np.random.shuffle(training_images)
    np.random.set_state(state)
    np.random.shuffle(training_labels)

    return np.asarray([training_images, training_labels, validation_images, validation_labels, testing_images, testing_labels])


# 数据整理主函数
def main():
    with tf.Session() as sess:
        processed_data = create_image_lists(sess, TEST_PERCENTAGE, VALIDATION_PERCENTAGE)
        # 通过numpy格式保存处理后的数据。
        # np.save(OUTPUT_FILE, processed_data)
        # 上一句话运行之后报错，MemoryError。百度之后改用下述办法
        with open(OUTPUT_FILE, 'wb') as fo:
            joblib.dump(processed_data, fo)


if __name__ == '__main__':
    main()