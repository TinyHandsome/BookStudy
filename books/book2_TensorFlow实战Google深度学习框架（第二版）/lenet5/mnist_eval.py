#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: mnist_eval.py
@time: 2018/12/7 18:19
@desc: BP神经网络3/3：定义了神经网络的测试过程。
"""

import time
import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 加载mnist_inference.py和mnist_train.py中定义的常量和函数。
import LeNet_5.mnist_inference as mnist_inference
import LeNet_5.mnist_train as mnist_train

# 每10秒加载一次最新的模型，并在测试数据上测试最新模型的正确率。
EVAL_INTERVAL_SECS = 3


def evaluate(mnist):
    with tf.Graph().as_default() as g:
        '''
        # 定义输入输出的格式
        x = tf.placeholder(tf.float32, [None, mnist_inference.INPUT_NODE], name='x-input')
        '''

        # 调整输入数据placeholder的格式，输入一个四维矩阵。
        x = tf.placeholder(tf.float32, [
            mnist_train.BATCH_SIZE,  # 第一维表示一个batch中样例的个数。
            mnist_inference.IMAGE_SIZE,  # 第二维和第三维表示图片的尺寸。
            mnist_inference.IMAGE_SIZE,
            mnist_inference.NUM_CHANNELS  # 第四维表示图片的深度，对于RGB格式的图片，深度为3。
        ], name='x-input')

        y_ = tf.placeholder(tf.float32, [None, mnist_inference.OUTPUT_NODE], name='y-input')
        xs, ys = mnist.validation.next_batch(mnist_train.BATCH_SIZE)
        xt = np.reshape(xs, (
            mnist_train.BATCH_SIZE,
            mnist_inference.IMAGE_SIZE,
            mnist_inference.IMAGE_SIZE,
            mnist_inference.NUM_CHANNELS
        ))
        validate_feed = {x: xt, y_: ys}

        # 直接通过调用封装好的函数来计算前向传播的结果。因为测试时不关注正则化损失的值，所以这里用于计算正则化损失的函数
        # 被设置为None。
        y = mnist_inference.inference(x, False, None)

        # 使用前向传播的结果计算正确率。如果需要对未知的样例进行分类，那么使用tf.argmax(y, 1)就可以得到输入样例的预测类别了、
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        # 通过变量重命名的方式来加载模型，这样在前向传播的过程中就不需要调用求滑动平均的函数来获取平均值了。这样就可以完全共用
        # mnist_inference.py中定义的前向传播过程。
        variable_averages = tf.train.ExponentialMovingAverage(mnist_train.MOVING_AVERAGE_DECAY)
        variables_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variables_to_restore)

        # 每隔EVAL_INTERVAL_SECS秒调用一次计算正确率的过程以检测训练过程中正确率的变化。
        while True:
            with tf.Session() as sess:
                # tf.train.get_checkpoint_state函数会通过checkpoint文件自动找到目录中最新模型的文件名。
                ckpt = tf.train.get_checkpoint_state(mnist_train.MODEL_SAVE_PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    # 加载模型。
                    saver.restore(sess, ckpt.model_checkpoint_path)
                    # 通过文件名得到模型保存时迭代的轮数。
                    gloabl_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                    accuracy_score = sess.run(accuracy, feed_dict=validate_feed)
                    print("After %s training step(s), validation accuracy = %g" % (gloabl_step, accuracy_score))
                else:
                    print('No checkpoint file found')
                    return
            time.sleep(EVAL_INTERVAL_SECS)


def main(argv=None):
    mnist = input_data.read_data_sets("./MNIST_data", one_hot=True)
    evaluate(mnist)


if __name__ == '__main__':
    tf.app.run()