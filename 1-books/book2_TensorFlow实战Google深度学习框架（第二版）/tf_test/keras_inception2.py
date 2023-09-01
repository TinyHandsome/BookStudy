#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: keras_inception2.py
@time: 2019/5/6 15:43
@desc: 用原生态的Keras实现Inception
"""

from keras.layers import Conv2D, MaxPooling2D, Input, Dense, Flatten
import keras
from keras.models import Model
from keras.datasets import mnist
from keras import backend as K


# 使用前面介绍的类似方法生成trainX、trainY、testX、testY，唯一的不同是这里只用了
# 全连接层，所以不需要将输入整理成三维矩阵。
num_calsses = 10
img_rows, img_cols = 28, 28

# 通过Keras封装好的API加载MNIST数据。其中trainX就是一个60000x28x28的数组，
# trainY是每一张图片对应的数字。
(trainX, trainY), (testX, testY) = mnist.load_data()

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

# 定义输入图像尺寸
input_img = Input(shape=(28, 28, 1))

# 定义第一个分支。
tower_1 = Conv2D(64, (1, 1), padding='same', activation='relu')(input_img)
tower_1 = Conv2D(64, (3, 3), padding='same', activation='relu')(tower_1)

# 定义第二个分支。与顺序模型不同，第二个分支的输入使用的是input_img，而不是第一个分支的输出。
tower_2 = Conv2D(64, (1, 1), padding='same', activation='relu')(input_img)
tower_2 = Conv2D(64, (5, 5), padding='same', activation='relu')(tower_2)

# 定义第三个分支。类似地，第三个分支的输入也是input_img。
tower_3 = MaxPooling2D((3, 3), strides=(1, 1), padding='same')(input_img)
tower_3 = Conv2D(64, (1, 1), padding='same', activation='relu')(tower_3)

# 将三个分支通过concatenate的方式拼凑在一起。
output = keras.layers.concatenate([tower_1, tower_2, tower_3], axis=1)

# 将卷积层的输出拉直后作为下面全连接的输入。
tower_4 = Flatten()(output)
# 全连接层，有500个节点。
tower_5 = Dense(500, activation='relu')(tower_4)
# 全连接层，得到最后的输出。
predictions = Dense(num_calsses, activation='softmax')(tower_5)

# 通过Model类创建模型，和Sequential类不同的是Model类在初始化的时候需要指定模型的输入和输出
model = Model(inputs=input_img, outputs=predictions)

# 使用与前面类似的方法定义损失函数、优化函数和评测方法。
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.SGD(), metrics=['accuracy'])

# 使用与前面类似的方法训练模型。
model.fit(trainX, trainY, batch_size=128, epochs=20, validation_data=(testX, testY))

# 在测试数据上评测模型。
score = model.evaluate(testX, testY, batch_size=128)
print('Test loss: ', score[0])
print('Test accuracy: ', score[1])