#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: test2.py
@time: 2020/2/26 16:51
@desc: 获取mnist数据学习算法效果
"""
from sklearn.ensemble import AdaBoostClassifier
from AdaImprovement import AdaImprovement
from mnist_test import MnistExtraction


if __name__ == '__main__':
    mnist = MnistExtraction()

    clf1 = AdaImprovement(random_state=42)
    clf2 = AdaBoostClassifier(random_state=42, algorithm='SAMME')
    mnist.model_train(name='改进算法', model=clf1, binary=True)
    mnist.model_train(name='Adaboost', model=clf2, binary=True)
