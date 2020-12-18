#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: estimator_test2.py
@time: 2019/5/9 12:31
@desc: 通过自定义的方式使用卷积神经网络解决MNIST问题
"""

import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

tf.logging.set_verbosity(tf.logging.INFO)


# 通过tf.layers来定义模型结构。这里可以使用原生态TensorFlow API或者任何
# TensorFlow的高层封装。X给出了输入层张量，is_training指明了是否为训练。
# 该函数返回前向传播的结果。
def lenet(x, is_training):
    # 将输入转化为卷积层需要的形状
    x = tf.reshape(x, shape=[-1, 28, 28, 1])

    net = tf.layers.conv2d(x, 32, 5, activation=tf.nn.relu)
    net = tf.layers.max_pooling2d(net, 2, 2)
    net = tf.layers.conv2d(net, 64, 3, activation=tf.nn.relu)
    net = tf.layers.max_pooling2d(net, 2, 2)
    net = tf.contrib.layers.flatten(net)
    net = tf.layers.dense(net, 1024)
    net = tf.layers.dropout(net, rate=0.4, training=is_training)
    return tf.layers.dense(net, 10)


# 自定义Estimator中使用的模型，定义的函数有4个输入，features给出了在输入函数中
# 会提供的输入层张量。注意这是一个字典，字典里的内容是通过tf.estimator.inputs.numpy_input_fn
# 中x参数的内容指定的。labels是正确答案，这个字段的内容是通过numpy_input_fn中y参数给出的。
# mode的取值有3中可能，分别对应Estimator类的train、evaluate和predict这3个函数。通过
# 这个参数可以判断当前会否是训练过程。最后params是一个字典，这个字典中可以给出模型相关的任何超参数
# （hyper-parameter）。比如这里将学习率放在params中。
def model_fn(features, labels, mode, params):
    # 定义神经网络的结构并通过输入得到前向传播的结果。
    predict = lenet(features["image"], mode == tf.estimator.ModeKeys.TRAIN)

    # 如果在预测模式，那么只需要将结果返回即可。
    if mode == tf.estimator.ModeKeys.PREDICT:
        # 使用EstimatorSpec传递返回值，并通过predictions参数指定返回的结果。
        return tf.estimator.EstimatorSpec(
            mode=mode,
            predictions={"result": tf.argmax(predict, 1)}
        )

    # 定义损失函数
    loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=predict, labels=labels))
    # 定义优化函数。
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=params["learning_rate"])

    # 定义训练过程。
    train_op = optimizer.minimize(loss=loss, global_step=tf.train.get_global_step())

    # 定义评测标准，在运行evaluate时会计算这里定义的所有评测标准。
    eval_metric_ops = {
        "my_metric": tf.metrics.accuracy(tf.argmax(predict, 1), labels)
    }

    # 返回模型训练过程需要使用的损失函数、训练过程和评测方法。
    return tf.estimator.EstimatorSpec(
        mode=mode,
        loss=loss,
        train_op=train_op,
        eval_metric_ops=eval_metric_ops
    )


mnist = input_data.read_data_sets("D:/Python3Space/BookStudy/book2/MNIST_data", one_hot=False)

# 通过自定义的方式生成Estimator类。这里需要提供模型定义的函数并通过params参数指定模型定义时使用的超参数。
model_params = {"learning_rate": 0.01}
estimator = tf.estimator.Estimator(model_fn=model_fn, params=model_params)

# 和前面的类似，训练和评测模型。
train_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"image": mnist.train.images},
    y=mnist.train.labels.astype(np.int32),
    num_epochs=None,
    batch_size=128,
    shuffle=True
)
estimator.train(input_fn=train_input_fn, steps=30000)
test_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"image": mnist.test.images},
    y=mnist.test.labels.astype(np.int32),
    num_epochs=1,
    batch_size=128,
    shuffle=False
)
test_results = estimator.evaluate(input_fn=test_input_fn)

# 这里使用的my_metric中的内容就是model_fn中eval_metric_ops定义的评测指标。
accuracy_score = test_results["my_metric"]
print("\nTest accuracy: %g %%" % (accuracy_score*100))

# 使用训练好的模型在新数据上预测结果。
predict_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"image": mnist.test.images[:10]},
    num_epochs=1,
    shuffle=False
)
predictions = estimator.predict(input_fn=predict_input_fn)
for i, p in enumerate(predictions):
    # 这里result就是tf.estimator.EstimatorSpec的参数predicitons中指定的内容。
    # 因为这个内容是一个字典，所以Estimator可以很容易支持多输出。
    print("Prediction  %s : %s" % (i + 1, p["result"]))