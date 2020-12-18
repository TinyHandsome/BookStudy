#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: RNN_test3.py
@time: 2018/12/26 16:06
@desc: 循环神经网络练习3
"""

import numpy as np
import tensorflow as tf
from tensorflow.contrib import rnn
# 加载matplotlib工具包画图
import matplotlib as mpl
from tensorflow.contrib.learn.python.learn.estimators.estimator import SKCompat
mpl.use('Agg')

from matplotlib import pyplot as plt

learn = tf.contrib.learn

HIDDEN_SIZE = 30 #LSTM中的隐藏节点个数
NUM_LAYERS = 2 #LSTM的层数

TIMESTEPS = 10 #循环神经网络的截断长度
TRAINING_STEPS = 10000 # 训练次数
BATCH_SIZE = 32 # batch大小

TRAINING_EXAMPLES = 10000 # 训练数据个数
TESTING_EXAMPLES = 1000 # 测试数据个数
SAMPLE_GAP = 0.01 # 采样间隔


#
# 生成数据集
# 通过以步长为1为单位，依次取（TIMESTEPS+1）个连续序列作为训练。
# 其中TIMESTEPS是训练数据的输入状态x，1位输出状态y
def generate_data(seq):
    '''

    :param seq: 总的用于训练的序列点
    :return:
        arrayX: 将序列的一部分作为输入状态
        arrayY： 序列的另一部分作为输出状态
    '''
    x = []
    y = []
    for i in range(len(seq)-TIMESTEPS-1):
        x.append([seq[i:i+TIMESTEPS]])
        y.append([seq[i+TIMESTEPS]])
    return np.array(x,dtype=np.float32),np.array(y,dtype=np.float32)

def LstmCell():
    lstm_cell = rnn.BasicLSTMCell(HIDDEN_SIZE,state_is_tuple=True)
    return lstm_cell

# 定义lstm模型
def lstm_model(X, y):
    cell = rnn.MultiRNNCell([LstmCell() for _ in range(NUM_LAYERS)])
    output, _ = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)
    output = tf.reshape(output, [-1, HIDDEN_SIZE])
    # 通过无激活函数的全连接层计算线性回归，并将数据压缩成一维数组结构
    predictions = tf.contrib.layers.fully_connected(output, 1, None)

    # 实际值和预测值
    labels = tf.reshape(y, [-1]) # 重塑为一维，即默认的一维
    predictions = tf.reshape(predictions, [-1])

    # 输出预测和损失值
    loss = tf.losses.mean_squared_error(predictions, labels)

    # 损失函数优化方法
    train_op = tf.contrib.layers.optimize_loss(loss, tf.contrib.framework.get_global_step(),
                                             optimizer="Adagrad",
                                             learning_rate=0.1)
    return predictions, loss, train_op

#建立深层模型
# Estimator里面还有一个叫SKCompat的类，如果使用x,y而不是input_fn来传参数的形式，需要用这个类包装一下：
# 第二个参数用于本地保存
regressor = SKCompat(learn.Estimator(model_fn = lstm_model, model_dir="Models/model_2"))

test_start = TRAINING_EXAMPLES * SAMPLE_GAP
test_end = (TRAINING_EXAMPLES + TESTING_EXAMPLES) * SAMPLE_GAP
train_X,train_y = generate_data(np.sin(np.linspace(0,test_start,TRAINING_EXAMPLES,dtype=np.float32)))
test_X,test_y = generate_data(np.sin(np.linspace(test_start,test_end,TESTING_EXAMPLES,dtype=np.float32)))
regressor.fit(train_X,train_y,batch_size=BATCH_SIZE,steps=TRAINING_STEPS)
predicted = [[pred] for pred in regressor.predict(test_X)]

# 计算MSE
rmse = np.sqrt(((predicted - test_y) ** 2).mean(axis=0))

fig = plt.figure()
plot_predicted, = plt.plot(predicted, label='predicted')
plot_test, = plt.plot(test_y, label='real_sin')
plt.legend([plot_predicted, plot_test],['predicted', 'real_sin'])
fig.savefig('sin.png')
plt.show()
print("Mean Square Error is:%f" % rmse[0])
