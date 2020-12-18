#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: tensorboard_test8.py
@time: 2019/5/13 9:34
@desc: 在生成好辅助数据之后，以下代码展示了如何使用TensorFlow代码生成PROJECTOR所需要的日志文件来可视化MNIST测试数据在最后的输出层向量。
"""

import tensorflow as tf
from BookStudy.book2 import mnist_inference
import os

# 加载用于生成PROJECTOR日志的帮助函数。
from tensorflow.contrib.tensorboard.plugins import projector
from tensorflow.examples.tutorials.mnist import input_data


# 和前面中类似地定义训练模型需要的参数。这里我们同样是复用mnist_inference过程。
BATCH_SIZE = 100
LEARNING_RATE_BASE = 0.8
LEARNING_RATE_DECAY = 0.99
REGULARAZTION_RATE = 0.0001
# 可以通过调整这个参数来控制训练迭代轮数。
TRAINING_STEPS = 10000
MOVING_AVERAGE_DECAY = 0.99

# 和日志文件相关的文件名及目录地址。
LOG_DIR = './log3'
SPRITE_FILE = 'D:/Python3Space/BookStudy/book2/tensorboard_test/log2/mnist_sprite.jpg'
META_FILE = 'D:/Python3Space/BookStudy/book2/tensorboard_test/log2/mnist_meta.tsv'
TENSOR_NAME = 'FINAL_LOGITS'


# 训练过程和前面给出的基本一致，唯一不同的是这里还需要返回最后测试数据经过整个
# 神经网络得到的输出矩阵（因为有很多张测试图片，每张图片对应了一个输出层向量，
# 所以返回的结果是这些向量组成的矩阵。
def train(mnist):
    # 输入数据的命名空间。
    with tf.name_scope('input'):
        x = tf.placeholder(tf.float32, [None, mnist_inference.INPUT_NODE], name='x-input')
        y_ = tf.placeholder(tf.float32, [None, mnist_inference.OUTPUT_NODE], name='y-input')

    regularizer = tf.contrib.layers.l2_regularizer(REGULARAZTION_RATE)
    y = mnist_inference.inference(x, regularizer)
    global_step = tf.Variable(0, trainable=False)

    # 处理滑动平均的命名空间。
    with tf.name_scope("moving_average"):
        variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
        variable_averages_op = variable_averages.apply(tf.trainable_variables())

    # 计算损失函数的命名空间。
    with tf.name_scope("loss_function"):
        cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
        cross_entropy_mean = tf.reduce_mean(cross_entropy)
        loss = cross_entropy_mean + tf.add_n(tf.get_collection('losses'))

    # 定义学习率、优化方法及每一轮执行训练操作的命名空间。
    with tf.name_scope("train_step"):
        learning_rate = tf.train.exponential_decay(
            LEARNING_RATE_BASE,
            global_step,
            mnist.train.num_examples / BATCH_SIZE,
            LEARNING_RATE_DECAY,
            staircase=True
        )

        train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)

        with tf.control_dependencies([train_step, variable_averages_op]):
            train_op = tf.no_op(name='train')

    # 训练模型
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        for i in range(TRAINING_STEPS):
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            _, loss_value, step = sess.run([train_op, loss, global_step], feed_dict={x: xs, y_: ys})

            if i % 1000 == 0:
                print("After %d training step(s), loss on training batch is %g." % (i, loss_value))

        # 计算MNIST测试数据对应的输出层矩阵。
        final_result = sess.run(y, feed_dict={x: mnist.test.images})

    # 返回输出层矩阵的值。
    return final_result


# 生成可视化最终输出层向量所需要的日志文件。
def visualisation(final_result):
    # 使用一个新的变量来保存最终输出层向量的结果。因为embedding是通过TensorFlow中
    # 变量完成的，所以PROJECTOR可视化的都是TensorFlow中的变量。于是这里需要新定义
    # 一个变量来保存输出层向量的取值。
    y = tf.Variable(final_result, name=TENSOR_NAME)
    summary_writer = tf.summary.FileWriter(LOG_DIR)

    # 通过projector.ProjectorConfig类来帮助生成日志文件。
    config = projector.ProjectorConfig()
    # 增加一个需要可视化的embedding结果。
    embedding = config.embeddings.add()
    # 指定这个embedding结果对应的TensorFlow变量名称。
    embedding.tensor_name = y.name

    # 指定embedding结果所对应的原始数据信息。比如这里指定的就是每一张MNIST测试图片
    # 对应的真实类别。在单词向量中可以是单词ID对应的单词。这个文件是可选的，如果没有指定
    # 那么向量就没有标签。
    embedding.metadata_path = META_FILE

    # 指定sprite图像。这个也是可选的，如果没有提供sprite图像，那么可视化的结果
    # 每一个点就是一个小圆点，而不是具体的图片。
    embedding.sprite.image_path = SPRITE_FILE
    # 在提供sprite图像时，通过single_image_dim可以指定单张图片的大小。
    # 这将用于从sprite图像中截取正确的原始图片。
    embedding.sprite.single_image_dim.extend([28, 28])

    # 将PROJECTOR所需要的内容写入日志文件。
    projector.visualize_embeddings(summary_writer, config)

    # 生成会话，初始化新声明的变量并将需要的日志信息写入文件。
    sess = tf.InteractiveSession()
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    saver.save(sess, os.path.join(LOG_DIR, "model"), TRAINING_STEPS)

    summary_writer.close()


# 主函数先调用模型训练的过程，再使用训练好的模型来处理MNIST测试数据，
# 最后将得到的输出层矩阵输出到PROJECTOR需要的日志文件中。
def main(argc=None):
    mnist = input_data.read_data_sets('D:/Python3Space/BookStudy/book2/MNIST_data', one_hot=True)
    final_result = train(mnist)
    visualisation(final_result)


if __name__ == '__main__':
    main()