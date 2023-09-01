#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: keras_learn.py
@time: 2019/5/5 17:42
@desc: 使用Keras在MNIST数据集上实现LeNet-5模型。
"""

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras import backend as K


num_calsses = 10
img_rows, img_cols = 28, 28

# 通过Keras封装好的API加载MNIST数据。其中trainX就是一个60000x28x28的数组，
# trainY是每一张图片对应的数字。
(trainX, trainY), (testX, testY) = mnist.load_data()

# 因为不同的底层（TensorFlow或者MXNet）对输入的要求不一样，所以这里需要根据对图像
# 编码的格式要求来设置输入层的格式。
if K.image_data_format() == 'channels_first':
    trainX = trainX.reshape(trainX.shape[0], 1, img_rows, img_cols)
    testX = testX.reshape(trainX.shape[0], 1, img_rows, img_cols)
    # 因为MNIST中的图片是黑白的，所以第一维的取值为1
    input_shape = (1, img_rows, img_cols)
else:
    trainX = trainX.reshape(trainX.shape[0], img_rows, img_cols, 1)
    testX = testX.reshape(testX.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

# 将图像像素转化为0到1之间的实数。
trainX = trainX.astype('float32')
testX = testX.astype('float32')
trainX /= 255.0
testX /= 255.0

# 将标准答案转化为需要的格式（One-hot编码）。
trainY = keras.utils.to_categorical(trainY, num_calsses)
testY = keras.utils.to_categorical(testY, num_calsses)

# 使用Keras API定义模型
model = Sequential()
# 一层深度为32，过滤器大小为5x5的卷积层
model.add(Conv2D(32, kernel_size=(5, 5), activation='relu', input_shape=input_shape))
# 一层过滤器大小为2x2的最大池化层。
model.add(MaxPooling2D(pool_size=(2, 2)))
# 一层深度为64， 过滤器大小为5x5的卷积层。
model.add(Conv2D(64, (5, 5), activation='relu'))
# 一层过滤器大小为2x2的最大池化层。
model.add(MaxPooling2D(pool_size=(2, 2)))
# 将卷积层的输出拉直后作为下面全连接的输入。
model.add(Flatten())
# 全连接层，有500个节点。
model.add(Dense(500, activation='relu'))
# 全连接层，得到最后的输出。
model.add(Dense(num_calsses, activation='softmax'))

# 定义损失函数、优化函数和测评的方法。
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.SGD(), metrics=['accuracy'])

# 类似TFLearn中的训练过程，给出训练数据，batch大小、训练轮数和验证数据，Keras可以自动完成模型的训练过程。
model.fit(trainX, trainY, batch_size=128, epochs=20, validation_data=(testX, testY))

# 在测评数据上计算准确率
score = model.evaluate(testX, testY)
print('Test loss: ', score[0])
print('Test accuracy: ', score[1])