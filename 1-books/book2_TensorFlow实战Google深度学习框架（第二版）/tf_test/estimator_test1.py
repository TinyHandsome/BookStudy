#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: estimator_test1.py
@time: 2019/5/7 16:22
@desc: 基于MNIST数据集，通过Estimator实现全连接神经网络。
"""

import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# 将TensorFlow日志信息输出到屏幕
tf.logging.set_verbosity(tf.logging.INFO)
mnist = input_data.read_data_sets('D:/Python3Space/BookStudy/book2/MNIST_data', one_hot=False)

# 指定神经网络的输入层，所有这里指定的输入都会拼接在一起作为整个神经网络的输入。
feature_columns = [tf.feature_column.numeric_column("image", shape=[784])]

# 通过TensorFlow提供的封装好的Estimator定义神经网络模型。feature_columns参数
# 给出了神经网络输入层需要用到的数据，hidden_units列表中给出了每一层
# 隐藏层的节点数。n_classes给出了总共类目的数量，optimizer给出了使用的优化函数。
# Estimator会将模型训练过程中的loss变化以及一些其他指标保存到model_dir目录下，
# 通过TensorFlow可以可视化这些指标的变化过程。并通过TensorBoard可视化监控指标结果。
estimator = tf.estimator.DNNClassifier(
    feature_columns=feature_columns,
    hidden_units=[500],
    n_classes=10,
    optimizer=tf.train.AdamOptimizer(),
    model_dir="./log"
)

# 定义数据输入。这里x中需要给出所有的输入数据。因为上面feature_columns只定义了一组
# 输入，所以这里只需要制定一个就好。如果feature_columns中指定了多个，那么这里也需要
# 对每一个指定的输入提供数据。y中需要提供每一个x对应的正确答案，这里要求分类的结果
# 是一个正整数。num_epochs指定了数据循环使用的轮数。比如在测试时可以将这个参数指定为1.
# batch_size指定了一个batch的大小。shuffle指定了是否需要对数据进行随机打乱。
train_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"image": mnist.train.images},
    y=mnist.train.labels.astype(np.int32),
    num_epochs=None,
    batch_size=128,
    shuffle=True
)

# 训练模型。注意这里没有指定损失函数，通过DNNClassifier定义的模型会使用交叉熵作为损失函数。
estimator.train(input_fn=train_input_fn, steps=10000)

# 定义测试时的数据输入。指定的形式和训练时的数据输入基本一致。
test_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"image": mnist.test.images},
    y=mnist.test.labels.astype(np.int32),
    num_epochs=1,
    batch_size=128,
    shuffle=False
)

# 通过evaluate评测训练好的模型的效果。
accuracy_score = estimator.evaluate(input_fn=test_input_fn)["accuracy"]
print("\nTest accuracy: %g %%" % (accuracy_score*100))