#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: statistic_analyze_tool.py
@time: 2020/11/7 10:25
@desc: 数据分析工具，海老师专用，听到没，其他人不许用哦
"""
import statsmodels.api as sm


class StatsModelTools:
    def __init__(self):
        self.model = None

    def stats_analyse(self, X, y, save_file='./result.txt'):
        """利用statsmodels的包进行数据分析"""

        # 需要输出截距的话，就要加上常量行
        ols_X = sm.add_constant(X)

        self.model = sm.OLS(y, ols_X).fit()
        self.summary_save(save_file)

    def summary_save(self, save_file):
        # 如果save_file不为None，则将结果输出为文件
        summary = self.model.summary()

        if save_file is not None:

            # 检查保存文件后缀：
            if save_file.endswith(".csv"):
                results = summary.as_csv()
            elif save_file.endswith(".txt"):
                results = summary.as_text()
            elif save_file.endswith(".html"):
                results = summary.as_html()
            else:
                print("文件后缀有问题！请重新选择。")
                results = None
                exit()

            with open(save_file, 'w') as f:
                f.writelines(results)
