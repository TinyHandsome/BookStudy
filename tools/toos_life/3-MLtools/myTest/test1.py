#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: test1.py
@time: 2020/4/29 16:09
@desc: 测试专用
"""

from sklearn.datasets import load_iris

from DimensionReduction import MyPCA
from MLTools import MLTools
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


from Models import MySVM
import numpy as np

from PreAnalysis import PreAnalysis

iris = load_iris()
iris_data = iris['data']
X = iris_data
iris_target = iris['target']
y = iris_target
iris_names = iris['target_names']
feature_names = iris['feature_names']
feature_names = [x.replace(' (cm)', '') for x in feature_names]

# svm = MySVM()
# svm.simple_model(iris_data, iris_target)

# 测试建立指定模型，不会改变类中的初始模型
# print(svm.aim_model(iris_data, iris_target, {'C': [0.1, 0.2, 0.5, 1]}))

# 测试网格调参方法，最后输出网格调参过程和结果
# print(svm.paramsAdjustment_byGridSearch(iris_data, iris_target, {'C': [0.1, 0.2, 0.5, 1], 'kernel': ['linear', 'poly', 'rbf', 'sigmoid']}))

# 测试分布调参方法，
# print(svm.paramsAdjustment_byStep(iris_data, iris_target, {'C': [0.1, 0.2, 0.5, 1], 'kernel': ['linear', 'poly', 'rbf', 'sigmoid']}))

# 测试输出评价结果
# model = svm.paramsAdjustment_byStep(iris_data, iris_target, {'C': [0.1, 0.2, 0.5, 1], 'kernel': ['linear', 'poly', 'rbf', 'sigmoid']})
# print(svm.score_model(model, iris_data, iris_target))

# 测试所有模型一起运行结果
# ml = MLTools().evaluate_origin_model(iris_data, iris_target)

# 测试数据分析的热力图
# PreAnalysis('./myTest/').correlationMatrix(X, names=feature_names)

# 测试矩阵图
# PreAnalysis('./myTest/').correlationPair(X, y, names=feature_names)


# df = pd.DataFrame(X, columns=feature_names)
# df['label'] = y
# df.loc[df["label"] == 0, "label"] = "setosa"  # 把类别这一列数值为0的替换为setosa
# df.loc[df["label"] == 1, "label"] = "versicolor"  # 把类别这一列数值为1的替换为versicolor
# df.loc[df["label"] == 2, "label"] = "virginica"  # 把类别这一列数值为2的替换为virginica
# g = sns.pairplot(df, hue="label", corner=True)
# plt.show()


# 测试PCA
vr = MyPCA().get_vr(X)
datas = MyPCA().get_aim_percent(X)

print(vr)
n = 0
for dd in datas:
    print('-'*50 + str(n+1) + '-'*50)
    print(dd)
    n += 1
