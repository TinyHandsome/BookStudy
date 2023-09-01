#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: tl_test2.py
@time: 2019/1/20 14:39
@desc: 用新的数据集和已经训练好的模型完成迁移学习
"""

import glob
import os.path
import numpy as np
import tensorflow as tf
from tensorflow.python.platform import gfile
import tensorflow.contrib.slim as slim

# 加载通过TensorFlow-Slim定义好的inception_v3模型
import tensorflow.contrib.slim.python.slim.nets.inception_v3 as inception_v3

# 处理好之后的数据文件
INPUT_DATA = 'C:/Users/Administrator/Desktop/Python3Space/transfer_learning/flower_processed_data.npy'
# 保存训练好的模型的路径。这里可以将使用新数据训练得到的完整模型保存下来，
# 如果计算资源充足，还可以在训练完最后的全连接层之后再训练所有网络层，
# 这样可以使得新模型更加贴近新数据
TRAIN_FILE = 'C:/Users/Administrator/Desktop/Python3Space/transfer_learning/save_model'
# 谷歌提供的训练好的模型文件地址。
CKPT_FILE = 'C:/Users/Administrator/Desktop/Python3Space/transfer_learning/inception_v3.ckpt'

# 定义训练中使用的参数
LEARNING_RATE = 0.0001
STEPS = 300
BATCH = 32
N_CLASSES = 5

# 不需要从谷歌训练好的模型中加载的参数。这里就是最后的全连接层，因为在新的问题中要重新训练这一层
# 中的参数。这里给出的是参数的前缀。
CHECKPOINT_EXCLUDE_SCOPES = 'InceptionV3/Logits, InceptionV3/AuxLogits'
# 需要训练的网络层参数名称，在fine-tuning的过程中就是最后的全连接层。
# 这里给出的是参数的前缀。
TRAINABLE_SCOPES = 'InceptionV3/Logits, InceptionV3/AuxLogits'


# 获取所有需要从谷歌训练好的模型中加载的参数
def get_tuned_variables():
    exclusions = [scope.strip() for scope in CHECKPOINT_EXCLUDE_SCOPES.split(',')]

    variables_to_restore = []
    # 枚举inception-v3模型中所有的参数，然后判断是否需要从加载列表中移除。
    for var in slim.get_model_variables():
        excluded = False
        for exclusion in exclusions:
            if var.op.name.startswith(exclusion):
                excluded = True
                break
        if not excluded:
            variables_to_restore.append(var)

    return variables_to_restore


# 获取所有需要训练的变量列表。
def get_trainable_variables():
    scopes = [scope.strip() for scope in TRAINABLE_SCOPES.split(',')]
    variables_to_train = []
    # 枚举所有需要训练的参数前缀，并通过这些前缀找到所有的参数
    for scope in scopes:
        variables = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope)
        variables_to_train.extend(variables)
    return variables_to_train


def main():
    # 加载预处理好的数据
    processed_data = np.load(INPUT_DATA)
    training_images = processed_data[0]
    n_training_example = len(training_images)
    training_labels = processed_data[1]
    validation_images = processed_data[2]
    validation_labels = processed_data[3]
    testing_images = processed_data[4]
    testing_labels = processed_data[5]
    print("%d training examples, %d validation examples and %d testing examples." %
          (n_training_example, len(validation_labels), len(testing_labels)))

    # 定义inception-v3的输入，images为输入图片，labels为每一张图片对应的标签。
    images = tf.placeholder(tf.float32, [None, 299, 299, 3], name='input_images')
    labels = tf.placeholder(tf.int64, [None], name='labels')

    # 定义inception-v3模型。因为谷歌给出的只有模型参数取值，所以这里需要在这个代码中定义
    # inception-v3的模型结构。虽然理论上需要区分训练和测试中使用的模型，也就是说在测试时
    # 应该使用is_training=False，但是因为预先训练好的inception-v3模型中使用的batch
    # normalization参数与新的数据会有差异，导致结果很差，所以这里直接使用同一个模型来进行测试。
    with slim.arg_scope(inception_v3.inception_v3_arg_scope()):
        logits, _ = inception_v3.inception_v3(images, num_classes=N_CLASSES)
    # 获取需要训练的变量
    trainable_variables = get_trainable_variables()
    # 定义交叉熵损失，注意在模型定义的时候已经将正则化损失加入损失集合了。
    tf.losses.softmax_cross_entropy(tf.one_hot(labels, N_CLASSES), logits, weights=1.0)
    # 定义训练过程。这里minimize的过程中指定了需要优化的变量集合。
    train_step = tf.train.RMSPropOptimizer(LEARNING_RATE).minimize(tf.losses.get_total_loss())

    # 计算正确率
    with tf.name_scope('evaluation'):
        correct_prediction = tf.equal(tf.argmax(logits, 1), labels)
        evaluation_step = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # 定义加载模型的函数。
    load_fn = slim.assign_from_checkpoint_fn(
        CKPT_FILE,
        get_tuned_variables(),
        ignore_missing_vars=True
    )

    # 定义保存新的训练好的模型的函数。
    saver = tf.train.Saver()
    with tf.Session() as sess:
        # 初始化没有加载进来的变量。注意这个过程一定要在模型的加载之前，否则初始化过程会将已经加载好的
        # 变量重新赋值。
        init = tf.global_variables_initializer()
        sess.run(init)

        # 加载谷歌已经训练好的模型。
        print('Loading tuned variables from %s' % CKPT_FILE)
        load_fn(sess)

        start = 0
        end = BATCH
        for i in range(STEPS):
            # 运行训练过程，这里不会更新全部的参数，只会更新指定的部分参数。
            sess.run(train_step, feed_dict={
                images: training_images[start:end],
                labels: training_labels[start:end]
            })

            # 输出日志
            if i % 30 == 0 or i + 1 == STEPS:
                saver.save(sess, TRAIN_FILE, global_step=i)
                validation_accuracy = sess.run(evaluation_step, feed_dict={
                    images: validation_images,
                    labels: validation_labels
                })
                print('Step %d: Validation accuracy = %.1f%%' % (i, validation_accuracy*100.0))

            # 因为在数据预处理的时候已经做过了打乱数据的操作，所以这里只需要顺序使用训练数据就好。
            start = end
            if start == n_training_example:
                start = 0

            end = start + BATCH
            if end > n_training_example:
                end = n_training_example

        # 在最后的测试数据上测试正确率。
        test_accuracy = sess.run(evaluation_step, feed_dict={
            images: testing_images,
            labels: testing_labels
        })
        print('Final test accuracy = %.1f%%' % (test_accuracy*100))


if __name__ == '__main__':
    main()