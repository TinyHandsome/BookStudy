#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: MyModel.py
@time: 2020/4/29 15:19
@desc: 基类，
        参考sklearn官网：https://scikit-learn.org/stable/index.html
        itertools参考连接：https://www.jianshu.com/p/73b17486ef8c
        [scoring的取值](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter)
        注意：交叉验证的抽样方式默认是分层抽样
        每个函数操作的模型是默认模型的深复制

        20200503 完善功能
        TODO：
        1. 分布调参，以及分布调参的绘图
"""
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from collections import OrderedDict
import copy

from MyMatplotlib import MyMatplotlib


class MyModel:

    def __init__(self):
        # 模型名
        self.name = "主类"
        # 默认采用宏平均的计算结果
        self.scoring = 'f1_macro'
        # 输出结果评分为precision、recall、f1-score、accuracy的宏平均
        self.evaluate = ['precision_macro', 'recall_macro', 'f1_macro', 'accuracy']
        # 模型类
        self.model = None
        # 默认调参参数取值
        self.parameters = None
        # 随机种子
        self.random_state = 150
        # 分步调参字典：参数名：[参数取值list，参数得分list，最优参数取值]
        self.step_params_results = OrderedDict()

        # 子类初始化
        try:
            # 固定每个模型的随机种子
            self.model.set_params(**{'random_state': self.random_state})
        except:
            pass

    def simple_model(self, X, y, cv, scoring):
        """
        用默认参数进行建模
        :param X: 数据集
        :param y: 数据标签
        :param cv: 交叉验证折数
        :param scoring: 评分方法
        :return: 用X，y训练的支持向量机
        """
        f_name = "默认参数建模"
        model = copy.deepcopy(self.model)
        return self.modeling(f_name, model, X, y, cv, scoring, True)

    def aim_model(self, X, y, params, cv=3, scoring=None):
        """
        用指定参数进行建模
        :param X: 数据集
        :param y: 数据标签
        :param params: 参数集，字典
        :param cv: 交叉验证折数
        :param scoring: 评分方法
        :return: 用X，y训练的支持向量机
        """
        f_name = "指定参数建模"
        model = copy.deepcopy(self.model)
        model.set_params(**params)
        return self.modeling(f_name, model, X, y, cv, scoring, True)

    def get_params(self):
        """获取对应模型的参数集"""
        params_dict = self.model.get_params()
        params = list(params_dict.keys())
        return params

    def modeling(self, f_name, model, X, y, cv, scoring, is_print=False):
        """
        根据不同的模型建模，基础函数
        :param f_name: 建模方式名称
        :param model: 模型
        :param X: 数据集
        :param y: 数据标签
        :param cv: 交叉验证折数
        :param scoring: 评分方法
        :return: 用X，y训练的模型
        """
        if not scoring:
            scoring = self.scoring

        output_info = "你正在进行【" + f_name + "】（默认参数），结果输出【" + str(cv) + "折】交叉验证结果（" + self.scoring + "）..."
        scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)
        output_info += "\n输出各折的" + self.scoring + "：" + str(scores)
        mean_score = np.mean(scores)
        output_info += "\n输出各折的平均" + self.scoring + "：" + "{:.4f}".format(mean_score)
        model.fit(X, y)

        if (is_print):
            print(output_info)
            return model, output_info
        else:
            return model, mean_score

    def paramsAdjustment_byStep(self, X, y, params=None, cv=3, scoring=None, is_plot=False):
        """
        分步调参
        :param X: 数据集
        :param y: 标签集
        :param params: 参数字典
        :param cv: 折数
        :param scoring: 评分方式
        :return: 最优模型
        """

        if params is None:
            params = self.parameters

        f_name = "分布调参"
        model = copy.deepcopy(self.model)
        best_model = copy.deepcopy(self.model)

        # 参与调参的参数名list
        params_names = params.keys()
        # 每个参数名对应一个list：该list保存了该参数调参的得分值
        params_scores = OrderedDict()
        # 每个参数名对应最佳的参数取值
        better_params = OrderedDict()

        for name in params_names:
            # 每个参数名对应的取值list
            params_values = params[name]
            scores = []
            max_score = 0
            better_value = None
            for value in params_values:
                param = {name: value}
                model.set_params(**param)
                _, score = self.modeling(f_name, model, X, y, cv, scoring)
                scores.append(score)

                if score > max_score:
                    max_score = score
                    better_value = value

            params_scores[name] = scores
            better_params[name] = better_value

            # print(name)
            # print(params_values)
            # print(scores)
            # print(better_value)
            self.step_params_results[name] = [list(params_values), scores, better_value]
        best_model.set_params(**better_params)

        # 绘制调参图
        if is_plot:
            self.plot2list(params, params_scores, better_params)
        return best_model

    def plot2list(self, params, params_scores, better_params):
        pp = MyMatplotlib("myTest/")
        for name in params.keys():
            values = params[name]
            scores = params_scores[name]
            better_param = better_params[name]

            # 这里简单处理了可能存在的嵌套参数的问题
            pp.plot_plot(name.replace('base_estimator__', ''), values, scores, name.replace('base_estimator__', ''),
                         'score', better_param)

    def paramsAdjustment_byGridSearch(self, X, y, save_path_name, params=None, cv=3, scoring=None):
        """
        网格调参
        参考连接：[中文博客](https://blog.csdn.net/weixin_41988628/article/details/83098130)
                 [官网连接](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV)
        :param X: 数据集
        :param y: 标签集
        :param params: 参数字典
        :param cv: 折数
        :param scoring: 评分方式
        :return: 最优模型
        """
        f_name = "网格调参"
        model = copy.deepcopy(self.model)

        if not scoring:
            scoring = self.scoring

        if params is None:
            params = self.parameters

        # 上面已经对params是否为空进行处理了，如果模型自带的也为空，那就算了
        if params is None:
            return self.model

        grid = GridSearchCV(model, params, cv=cv, scoring=scoring, return_train_score=True)
        grid.fit(X, y)
        cv_results = pd.DataFrame(grid.cv_results_)
        cv_results.to_excel(save_path_name, index_label='编号')
        # print(grid.best_params_)
        # print(grid.best_score_)
        return grid.best_estimator_

    def score_model(self, model, X, y, cv=3, scoring=None):
        """
        输出模型的评价打分
        :return: 返回 评价指标：宏平均 的字典
        """
        f_name = "模型评价"
        if not scoring:
            scoring = self.evaluate

        scores = OrderedDict()
        for e in scoring:
            s = np.mean(cross_val_score(model, X, y, cv=cv, scoring=e))
            scores[e] = s
        return scores
