#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: test.py
@time: 2020/2/24 17:39
@desc: 
"""

from sklearn import datasets
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_val_score
from improvedAdaboost import AdaImprovement
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score, f1_score, accuracy_score


if __name__ == '__main__':

    # 导入minist手写数据
    minist = datasets.load_digits()
    xx = minist['data']
    yy = minist['target']
    # 只要二分类
    index0 = (yy != 7)
    index1 = (yy == 7)
    X = np.r_[xx[index0], xx[index1]]
    y = np.r_[yy[index0], yy[index1]]

    s = []
    for i in y:
        if i != 7:
            s.append(0)
        else:
            s.append(1)
    y = np.array(s)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=48, stratify=y)

    clf = AdaImprovement(random_state=42, algorithm='SAMME')
    clf.fit(X_train, y_train)
    pre1 = clf.predict(X_test)
    r1 = recall_score(y_test, pre1, average='macro')
    f1 = f1_score(y_test, pre1, average='macro')
    a1 = accuracy_score(y_test, pre1)
    print('改进算法预测结果：', r1, f1, a1)

    clf2 = AdaBoostClassifier(random_state=42, algorithm='SAMME')
    clf2.fit(X_train, y_train)
    pre2 = clf2.predict(X_test)
    r2 = recall_score(y_test, pre2, average='macro')
    f2 = f1_score(y_test, pre2, average='macro')
    a2 = accuracy_score(y_test, pre2)
    print('Adaboost预测结果：', r2, f2, a2)


