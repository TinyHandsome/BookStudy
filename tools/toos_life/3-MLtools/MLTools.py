#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: MLTools.py
@time: 2020/5/3 19:29
@desc: 改名为MLtools，重构代码
        各种函数调用工具
        注意：
            1. collections.OrderDict不能用OrderDict({})，否则会依然没有顺序
               [参考链接](https://cloud.tencent.com/developer/ask/53926)
            2. [pd.join、pd.merge](https://www.jianshu.com/p/8344df71b2b3)
            3. [f1报错](https://blog.csdn.net/a6840231/article/details/88416338)
                简单来说就是，实际的y在预测的结果中有的没有预测到，即标签为y_的没有在预测结果中出现，这种情况，该类的f1_score=0.0
            4. [numpy报错：DeprecationWarning: The truth value of an empty array is ambiguous. Returning False, but in future this will result in an error. Use `array.size > 0` to check that an array is not empty.](https://blog.csdn.net/qq_41103544/article/details/81561539?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)
"""
import os
import joblib

import Models as ms
from collections import OrderedDict
import pandas as pd
from sklearn.ensemble import VotingClassifier

from MyModel import MyModel
from PreAnalysis import Tools
from TimeTool import TimeTool


class MLTools(Tools):

    def __init__(self, save_path):
        super().__init__(save_path)
        self.m1 = ms.MyMNB()
        self.m2 = ms.MyGNB()
        self.m3 = ms.MyKNN()
        self.m4 = ms.MyLR()
        self.m5 = ms.MySVM()
        self.m6 = ms.MyDT()
        self.m7 = ms.MyRF()
        self.m8 = ms.MyGBDT()
        self.m9 = ms.MyXGBoost()
        self.m10 = ms.MyAdaboost()

        # 图片保存路径
        self.pic_savePath = None
        # 模型保存路径
        self.model_savePath = None
        # 中间过程，中间结果等路径
        self.middle_savePath = None
        # 报告保存路径
        self.report_savePath = None

        # 集成模型
        self.ensemble_name = ['随机森林', 'Adaboost', 'GBDT', 'XGBoost']
        self.ensemble_set = []

        self.models_dict = OrderedDict([
            (self.m1.name, self.m1),
            (self.m2.name, self.m2),
            (self.m3.name, self.m3),
            (self.m4.name, self.m4),
            (self.m5.name, self.m5),
            (self.m6.name, self.m6),
            (self.m7.name, self.m7),
            (self.m8.name, self.m8),
            (self.m9.name, self.m9),
            (self.m10.name, self.m10)
        ])

        self.model_names = list(self.models_dict.keys())

    def init_models(self):
        for m in self.models_dict.values():
            if m is not None:
                m.init_model()
                print('正在初始化:', m.name)
                m.model.fit(self.X, self.y)

    def init_ensemble_set(self):
        """初始化集成模型架构内容"""
        self.ensemble_set = []

    def init_save_paths(self):
        # 图片保存路径
        self.pic_savePath = os.path.join(self.save_path, 'pics')
        # 模型保存路径
        self.model_savePath = os.path.join(self.save_path, 'models')
        # 中间过程，中间结果等路径
        self.middle_savePath = os.path.join(self.save_path, 'middle')
        # 报告保存路径
        self.report_savePath = os.path.join(self.save_path, 'reports')
        for p in [self.pic_savePath, self.model_savePath, self.middle_savePath, self.report_savePath]:
            if not os.path.exists(p):
                os.makedirs(p)

    def aim(self, t=0):
        self.fig_path = None
        self.return_inf = None
        # 初始化保存路径
        self.init_save_paths()

        if t == 0:
            # 初始化模型
            self.init_models()
            # 运行所有模型，并对进行网格调参
            self.evaluate_oa_model(self.X, self.y)

    def save_model(self, model, save_path):
        """
        保存指定模型
        :param model:
        :param save_path: 保存路径，包括了名字
        :return:
        """
        joblib.dump(model, save_path)

    def evaluate_oa_model(self, X, y):
        """
        调参和未调参都要，调参用的是网格调参
        :param X:
        :param y:
        :return:
        """
        df1 = self.evaluate_origin_model(X, y)
        df2 = self.evaluate_adjust_model(X, y)
        df = df1.join(df2, lsuffix='_未调参', rsuffix='_网格调参')

        excel_name_final = '网格调参优化结果-' + TimeTool().getCurrentTime() + '.xls'
        df.to_excel(os.path.join(self.report_savePath, excel_name_final))

    def evaluate_origin_model(self, X, y, is_ensemble=True):
        """
        使用所有的模型，【不调参】，进行分类，并输出评价指标
        :return:
        """
        result = []
        items = None
        #

        # 获取未调参的模型的结果
        for model_name, model_class in self.models_dict.items():
            model = model_class.model
            print('正在建立未调参的', model_name, '模型...')
            if model is not None:
                # 保存模型
                model_save_name = os.path.join(self.model_savePath, model_name + '-未调参.m')
                self.save_model(model, model_save_name)

                # 根据是否集成
                if is_ensemble:
                    self.fill_ensemble_set(model_name, model_save_name)

                r, eval = self.score_model(model, model_name, X, y)
                result.append(r)
                if items is None:
                    items = ['model_name'] + list(eval.keys())

        # 根据是否集成加上最终集成model
        if is_ensemble:
            r = self.ensemble_model(X, y, '-未调参.m')
            result.append(r)

        data = pd.DataFrame(result, columns=items)
        data.set_index('model_name', inplace=True)

        return data

    def evaluate_adjust_model(self, X, y, is_ensemble=True):
        """
        使用所有的模型，【网格调参】，进行分类，并输出评价指标
        :return:
        """
        result = []
        items = None
        # 获取网格调参的模型的结果
        for model_name, model_class in self.models_dict.items():
            print('正在建立网格调参的', model_name, '模型...')
            model = model_class.model
            if model_class is not None:
                excel_name = '【' + model_name + '】模型-网格调参报告-' + TimeTool().getCurrentTime() + '.xls'
                save_name = os.path.join(self.middle_savePath, excel_name)
                best_model = model_class.paramsAdjustment_byGridSearch(X, y, save_name)
                # 保存最佳模型
                model_save_name = os.path.join(self.model_savePath, model_name + '-网格调参优化.m')
                self.save_model(best_model, model_save_name)

                # 根据是否集成
                if is_ensemble:
                    self.fill_ensemble_set(model_name, model_save_name)

                r, eval = self.score_model(best_model, model_name, X, y)
                result.append(r)
                if items is None:
                    items = ['model_name'] + list(eval.keys())

        # 根据是否集成加上最终集成model
        if is_ensemble:
            r = self.ensemble_model(X, y, '-网格调参优化.m')
            result.append(r)

        data = pd.DataFrame(result, columns=items)
        data.set_index('model_name', inplace=True)

        return data

    def ensemble_model(self, X, y, houzhui, is_weights=False):
        print('正在集成模型...')
        # 根据是否集成加上最终集成model
        model_name = '集成模型'

        if is_weights:
            weights = [1, 1, 3, 5]
        else:
            weights = None
        voting_clf = VotingClassifier(self.ensemble_set, voting='soft', weights=weights)
        voting_clf.fit(X, y)

        model_save_name = os.path.join(self.model_savePath, model_name + houzhui)
        self.save_model(voting_clf, model_save_name)

        # 计算精度等评价指标
        r, _ = self.score_model(voting_clf, model_name, X, y)

        # 集成结束，初始化集成set
        self.init_ensemble_set()

        return r

    def score_model(self, model, model_name, X, y):
        """计算分数"""
        eval = MyModel().score_model(model, X, y)
        r = [model_name] + list(eval.values())
        return r, eval

    def fill_ensemble_set(self, model_name, savepath_name, emsemble_names=None):
        if emsemble_names is None:
            emsemble_names = self.ensemble_name

        if model_name in emsemble_names:
            self.ensemble_set.append((model_name, joblib.load(savepath_name)))

    def evaluate(self, X, y):
        """
        建立未调参和网格调参后的模型，获取交叉验证的评价指标
        :param X:
        :param y:
        :return:
        """

        # 所有模型未调参结果
        un_paramed_result = self.evaluate_origin_model(X, y)
        # 网格调参后结果
        paramed_result = self.evaluate_adjust_model(X, y)

        print(un_paramed_result)
        print(paramed_result)
