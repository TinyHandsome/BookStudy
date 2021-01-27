#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: AdaImprovement.py
@time: 2020/2/24 14:27
@desc: 基于sklearn改进Adabosot代码
"""

import numpy as np
from numpy.core.umath_tests import inner1d
from sklearn.ensemble import AdaBoostClassifier


class AdaImprovement(AdaBoostClassifier):
    def _boost_real(self, iboost, X, y, sample_weight, random_state):
        estimator = self._make_estimator(random_state=random_state)
        estimator.fit(X, y, sample_weight=sample_weight)

        y_predict_proba = estimator.predict_proba(X)

        if iboost == 0:
            self.classes_ = getattr(estimator, 'classes_', None)
            self.n_classes_ = len(self.classes_)

        y_predict = self.classes_.take(np.argmax(y_predict_proba, axis=1), axis=0)
        incorrect = y_predict != y
        print('迭代次数：', iboost)
        print('真实值：', y[:10])
        print('预测值：', y_predict[:10])
        print('预测为1的概率：', y_predict_proba[:, 1][:10])
        print('原始预测错误率：', incorrect.astype('int')[:10])

        # 错误率修正算法
        incorrect = np.abs(y_predict_proba[:, 1] - y)
        print('修正后的预测错误率：', incorrect[:10])

        # 计算分类器错误率，引入惩罚因子gamma，incorrect为错误矩阵
        estimator_error = np.mean(np.average(self._gamma(incorrect, y), weights=sample_weight, axis=0))
        estimator_error_old = np.mean(np.average(incorrect, weights=sample_weight, axis=0))
        print('新错误率计算结果：', estimator_error)
        print('旧错误率计算结果：', estimator_error_old)
        print('-' * 50)

        if estimator_error <= 0:
            return sample_weight, 1., 0.

        n_classes = self.n_classes_
        classes = self.classes_
        y_codes = np.array([-1. / (n_classes - 1), 1.])
        y_coding = y_codes.take(classes == y[:, np.newaxis])

        proba = y_predict_proba
        proba[proba < np.finfo(proba.dtype).eps] = np.finfo(proba.dtype).eps

        estimator_weight = (-1. * self.learning_rate
                            * (((n_classes - 1.) / n_classes) *
                               inner1d(y_coding, np.log(y_predict_proba))))

        if not iboost == self.n_estimators - 1:
            # Only boost positive weights
            sample_weight *= np.exp(estimator_weight *
                                    ((sample_weight > 0) |
                                     (estimator_weight < 0)))

        return sample_weight, 1., estimator_error

    def _gamma(self, incorrect, y):
        """计算分类器错误率，引入惩罚因子gamma"""
        # 若incorrect<0.5，则分类正确，gamma=1，incorrect*gamma=0
        # 若incorrect>=0.5，则分类错误，gamma_套损样本=w，incorrect*gamma=w，gamma_非套损样本=1-w，incorrect*gamma=1-w
        # 其中w=正样本权值，其计算方法如公式(4.28)和公式(4.29)所示
        w = self.sample_weight_cal(y)
        incorrect = np.array(incorrect)
        new_incorrect = []
        for value, y_true in zip(incorrect, y):
            if value < 0.5:
                new_incorrect.append(value * 1)
            else:
                if y_true == 1:
                    new_incorrect.append(value * w * 10)
                else:
                    new_incorrect.append(value)

        return np.array(new_incorrect)

    def sample_weight_cal(self, y):
        """优化样本初始权值分布"""
        r0 = 1 / (np.sum(y == 0) / len(y))
        r1 = 1 / (np.sum(y == 1) / len(y))
        w = r1 / (r0 + r1)
        return w

    def get_samples_weights(self, y):
        weights = []
        w = self.sample_weight_cal(y)
        for v in y:
            if v == 1:
                weights.append(w)
            else:
                weights.append(1 - w)

        return weights
