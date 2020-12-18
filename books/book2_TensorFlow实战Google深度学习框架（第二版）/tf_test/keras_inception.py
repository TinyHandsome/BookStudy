#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: keras_inception.py
@time: 2019/5/6 14:29
@desc: 用更加灵活的模型定义方法在MNIST数据集上实现全连接层模型。
"""

import keras
from keras.layers import Input, Dense
from keras.models import Model
from keras.datasets import mnist


# 使用前面介绍的类似方法生成trainX、trainY、testX、testY，唯一的不同是这里只用了
# 全连接层，所以不需要将输入整理成三维矩阵。
num_calsses = 10
img_rows, img_cols = 28, 28

# 通过Keras封装好的API加载MNIST数据。其中trainX就是一个60000x28x28的数组，
# trainY是每一张图片对应的数字。
(trainX, trainY), (testX, testY) = mnist.load_data()

trainX = trainX.reshape(len(trainX), -1)
testX = testX.reshape(len(testX), -1)

# 将图像像素转化为0到1之间的实数。
trainX = trainX.astype('float32')
testX = testX.astype('float32')
trainX /= 255.0
testX /= 255.0

# 将标准答案转化为需要的格式（One-hot编码）。
trainY = keras.utils.to_categorical(trainY, num_calsses)
testY = keras.utils.to_categorical(testY, num_calsses)

# 定义输入，这里指定的维度不用考虑batch大小。
inputs = Input(shape=(784, ))
# 定义一层全连接层，该层有500隐藏节点，使用ReLU激活函数。这一层的输入为inputs
x = Dense(500, activation='relu')(inputs)
# 定义输出层。注意因为keras封装的categorical_crossentropy并没有将神经网络的输出
# 再经过一层softmax，所以这里需要指定softmax作为激活函数。
predictions = Dense(10, activation='softmax')(x)

# 通过Model类创建模型，和Sequential类不同的是Model类在初始化的时候需要指定模型的输入和输出
model = Model(inputs=inputs, outputs=predictions)

# 使用与前面类似的方法定义损失函数、优化函数和评测方法。
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.SGD(), metrics=['accuracy'])

# 使用与前面类似的方法训练模型。
model.fit(trainX, trainY, batch_size=128, epochs=10, validation_data=(testX, testY))
