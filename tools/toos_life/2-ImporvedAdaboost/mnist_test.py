#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: mnist_test.py
@time: 2020/2/26 14:52
@desc: 提取minist数据集，处理成二分类模式
"""
from sklearn.datasets import fetch_mldata
from sklearn.metrics import recall_score, f1_score, accuracy_score, precision_score
from sklearn.model_selection import train_test_split


class MnistExtraction:
    def __init__(self):
        self.mnist = fetch_mldata('F:/Python3Space/MNIST_data/MNIST original')

    def printMnist(self):
        """获取mnist原始文件信息"""
        print(self.mnist)

    def getXY(self):
        """获取完整的X，y数据样本"""
        X = self.mnist['data']
        y = self.mnist['target']
        return X, y

    def getBinaryClassificationSample(self):
        """获取二分类样本，4作为目标样本"""
        y_temp = []
        X, y = self.getXY()
        label_1 = y == 4
        for label in label_1:
            if label:
                y_temp.append(1)
            else:
                y_temp.append(0)
        return X, y_temp

    def getTrainTestSplit(self, random_state=42, stratify=True, binary=False):
        """
        获取划分训练集测试集之后的数据（分层抽样）
        :param random_state: 是否设置随机种子，否的话None
        :param stratify: 是否分层抽样，否的话None
        :param binary: 是否抽取二分类数据
        """
        if binary:
            X, y = self.getBinaryClassificationSample()
        else:
            X, y = self.getXY()

        if stratify:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state,
                                                                stratify=y)
        else:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)
        return X_train, X_test, y_train, y_test

    def model_train(self, name, model, binary=True):
        """模型训练并输出评价指标"""
        X_train, X_test, y_train, y_test = self.getTrainTestSplit(binary=binary)
        model.fit(X_train, y_train)
        pre = model.predict(X_test)
        p1 = precision_score(y_test, pre, average='macro')
        r1 = recall_score(y_test, pre, average='macro')
        f1 = f1_score(y_test, pre, average='macro')
        a1 = accuracy_score(y_test, pre)
        print(name, '预测结果：', 'precision: ', p1, 'recall:', r1, 'f1_score:', f1, 'accuracy:', a1)
