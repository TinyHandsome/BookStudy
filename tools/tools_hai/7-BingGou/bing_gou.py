#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: bing_gou.py
@time: 2020/11/7 9:37
@desc: 测试主要X变量与y变量的关系
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statistic_analyze_tool as sat
import random

random.seed(42)


class BingGou:

    def __init__(self, path, aim_x_columns, aim_y_column):
        self.excel_path = path
        self.df = pd.read_excel(aim_path)
        self.aim_x_columns = aim_x_columns
        self.aim_y_column = aim_y_column

        self.X = self.df[self.aim_x_columns]
        self.y = self.df[self.aim_y_column]

        # 用来存放各个阶段的处理后的df
        self.deal_df = None

    def set_xy(self):
        """获取当前阶段的deal_df所对应的xy的值"""
        self.X = self.deal_df[self.aim_x_columns]
        self.y = self.deal_df[self.aim_y_column]

    def set_effective_df(self, subset_columns):
        """根据某几列去空值，将X，y设为去空后的值"""
        self.deal_df = self.df.dropna(subset=subset_columns)
        self.set_xy()

    def remove_negative(self):
        """去除导致斜率为负的样本"""

        buyao_index = self.deal_df.query('eigq==0 and bg==1').index
        # print(buyao_index)
        aim_ind = pd.Index([ind for ind in self.deal_df.index if ind not in buyao_index])
        # print(aim_ind)
        self.deal_df = self.deal_df.loc[aim_ind, :]
        self.set_xy()

    def change_negative(self, change_col, change_percent=0.5):
        """将 0，1 的数据改为 0，0 """
        buyao_index = self.deal_df.query('eigq==0 and bg==1').index

        if change_percent <= 1:
            change_num = int(buyao_index.shape[0] * change_percent)
        else:
            change_num = change_percent

        partial_index = pd.Index(random.sample(list(buyao_index.values), change_num))

        self.deal_df.loc[partial_index, change_col] = 0
        self.set_xy()
        self.deal_df.to_excel(path + 'change_num_df.xlsx', index=None)

    def model_linear_build(self):
        """所有数据建模"""
        model = LinearRegression()
        model.fit(self.X, self.y)
        print(model.coef_)

        tool = sat.StatsModelTools()
        tool.stats_analyse(self.X, self.y, path + 'result.txt')

    def model_linear_main_param(self, main_param):
        """对关心的参数建模"""
        X_param = np.array(self.X[main_param].values).reshape(-1, 1)

        model = LinearRegression()
        model.fit(X_param, self.y)
        print(model.coef_)
        print(model.intercept_)

        y_pre = model.predict(X_param)

        fig = plt.figure(figsize=(4, 3))
        plt.scatter(X_param, self.y)
        plt.scatter(X_param, y_pre)
        plt.show()


if __name__ == '__main__':
    """path是工作路径，aim_path是excel名字"""
    path = 'E:/【冲鸭】/【我海】1. 选我就完事儿了/20201107-并购/'
    aim_path = path + '1107-并购.xlsx'

    """对应的目标x列名和y的列名"""
    x_columns = ['eigq', 'size1', 'tang1', 'ocf1', 'lev1', 'top11', 'indep1', 'tobinq1', 'age22', 'gljy', 'paymode']
    y_column = 'bg'

    bg = BingGou(aim_path, x_columns, y_column)

    """去掉对应列【subset_columns】的空值所在的行"""
    subset_columns = ['lnfsgrant1', 'lngrant1']
    bg.set_effective_df(subset_columns)

    """修改对应的值，(0,1)-> (0,0)"""
    # bg.remove_negative()
    bg.change_negative(change_col='bg', change_percent=0.5)

    """运行模型得出结果，见对应目录下的txt"""
    bg.model_linear_build()

    # bg.model_linear_main_param('eigq')
