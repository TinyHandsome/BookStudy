#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: test3.py
@time: 2020/5/4 13:08
@desc: 测试专用3：生成数据集
        [make_multilabel_classification详解](https://blog.csdn.net/n889092/article/details/77126754)
"""

from sklearn.datasets import load_breast_cancer
import numpy as np

from MLTools import MLTools
from PreAnalysis import PreAnalysis

data = load_breast_cancer()
X = data['data']
y = data['target']
feature_names = data['feature_names']

# 测试数据分析的热力图
PreAnalysis('/').correlationMatrix(X, names=feature_names)