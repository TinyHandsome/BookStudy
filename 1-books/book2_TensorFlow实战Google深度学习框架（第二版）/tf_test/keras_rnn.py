#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: keras_rnn.py
@time: 2019/5/6 12:30
@desc: 用原生态的Keras实现循环神经网络
"""

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
from keras.datasets import imdb

# 最多使用的单词数
max_features = 20000
# 循环神经网络的截断长度。
maxlen = 80
batch_size = 32
# 加载数据并将单词转化为ID，max_features给出了最多使用的单词数。和自然语言模型类似，
# 会将出现频率较低的单词替换为统一的的ID。通过Keras封装的API会生成25000条训练数据和
# 25000条测试数据，每一条数据可以被看成一段话，并且每段话都有一个好评或者差评的标签。
(trainX, trianY), (testX, testY) = imdb.load_data(num_words=max_features)
print(len(trainX), 'train sequences')
print(len(testX), 'test sequences')

# 在自然语言中，每一段话的长度是不一样的，但循环神经网络的循环长度是固定的，所以这里需要先将
# 所有段落统一成固定长度。对于长度不够的段落，要使用默认值0来填充，对于超过长度的段落
# 则直接忽略掉超过的部分。
trainX = sequence.pad_sequences(trainX, maxlen=maxlen)
testX = sequence.pad_sequences(testX, maxlen=maxlen)

print('trainX shape', trainX.shape)
print('testX shape: ', testX.shape)

# 在完成数据预处理之后构建模型
model = Sequential()
# 构建embedding层。128代表了embedding层的向量维度。
model.add(Embedding(max_features, 128))
# 构建LSTM层
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
# 构建最后的全连接层。注意在上面构建LSTM层时只会得到最后一个节点的输出，
# 如果需要输出每个时间点的结果，呢么可以将return_sequence参数设为True。
model.add(Dense(1, activation='sigmoid'))

# 与MNIST样例类似的指定损失函数、优化函数和测评指标。
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 在测试数据上评测模型。
score = model.evaluate(testX, testY, batch_size=batch_size)
print('Test loss: ', score[0])
print('Test accuracy: ', score[1])