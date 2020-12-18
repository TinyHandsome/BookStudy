#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: statsmodels_study.py
@time: 2020/9/7 10:21
@desc: 我海的数据处理项目
        1. 文件预处理，列选择，去空
        2. 根据目标文件进行statsmodels分析
        3. 获取分析结果，导出为文件
        4. 实现针对结果的目标文件的数据清洗：删除一定百分比的远离线性回归的点的记录
        5. 输出新的删除部分数据后的文档
       参考链接：
        1. 中文用户手册：https://github.com/Squidxwh/statsmodels
        2. statsmodels官方文档：https://www.statsmodels.org/stable/index.html
        3. summary参数详解：https://blog.csdn.net/zm147451753/article/details/83107535
"""
import pandas as pd
import numpy as np
import copy
import statsmodels.api as sm


class MyHaiStatsmodel:

    def __init__(self, file_path):
        self.file_path = file_path
        # 原始数据
        self.data = None
        self.columns = None
        # 抽列
        self.aim_data = None
        # 去空
        self.deal_data = None

        self.X = None
        self.y = None

        # 这里的模型是会实时更新的模型，下面的预测和错误也是
        self.model = None
        self.predicts = None
        self.errors = None

    def read_excel(self, file_path=None):
        """读取目标excel"""
        if file_path is None:
            file_path = self.file_path

        try:
            self.data = pd.read_excel(file_path)
            self.columns = self.data.columns
            return 1
        except:
            print("文件路径不是正常的excel！")
            return -1

    def get_columns(self):
        """获得数据的列"""
        return self.columns

    def set_aimColumns(self, aim_columns):
        """设置目标列，包括输入列和输出列"""
        self.aim_data = self.data[aim_columns]

    def data_preprocess(self):
        """数据预处理，去空"""
        self.deal_data = self.aim_data.dropna()

    def generate_xy(self, y_name, is_log=True):
        """
        根据y的列名，生成x，y输入输出数据
        :param y_name: y的列名
        :param is_log: 是否对y+1取自然对数，+1是为了将0值保留为0
        :return:
        """
        temp_aimData = copy.deepcopy(self.deal_data)
        y_raw = temp_aimData.pop(y_name)
        if is_log:
            self.y = np.log(y_raw + 1)
        else:
            self.y = y_raw

        self.X = temp_aimData

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

    def stats_analyse(self, save_file=None, X=None, y=None):
        """利用statsmodels的包进行数据分析"""
        if X is None:
            X = self.X
        if y is None:
            y = self.y

        # 需要输出截距的话，就要加上常量行
        ols_X = sm.add_constant(X)

        self.model = sm.OLS(y, ols_X).fit()
        # 生成模型时则计算预测
        self.predicts = self.model.predict(ols_X)
        # 同时也能计算平方差
        self.errors = (self.predicts - y) ** 2

        self.summary_save(save_file)

    def errors_analysis(self, save_file=None, rate=0.8, save_oringin_path=None):
        """错误分析，获取举例超平面最远的%多少的点是哪些"""
        err_sort = self.errors.sort_values()
        ration = int(len(err_sort) * rate)
        select_err = err_sort[:ration].sort_index()
        select_index = select_err.index

        # 计算更改后的结果
        if save_file is not None:
            # 计算新的X和y
            new_X = self.X.loc[select_index, :]
            new_y = self.y[select_index]
            # 重跑模型
            self.stats_analyse(save_file, new_X, new_y)

        # 是否保存删了点之后的数据
        if save_oringin_path is not None:
            temp_oringin = self.data.loc[select_index, :]
            temp_oringin.to_excel(save_oringin_path)

        # 返回保留数据的的index
        return select_index


if __name__ == '__main__':
    # 主要路径，也就是我的工作路径，这里换成你的就行
    main_path = 'E:\\【我海】选我就完事儿了\\'
    # 设置文件路径
    file_path = main_path + 'hmd(1).xlsx'

    # 建立处理数据的模型
    model = MyHaiStatsmodel(file_path)

    # 读取文件内容
    model.read_excel()

    # 获取输入输出的列
    aim_columns = ['合计发明专利申请量', 'group', 'ROA', 'size(企业规模）', '资本密集度', 'OCF（经营活动现金流比率）', 'lev（资产负债率）',
                   'TOP1(第一大股东持股占比)', '独董占比', 'TobinQ(市值A)', 'HHI', 'age1公司成立日期年龄']
    model.set_aimColumns(aim_columns)

    # 生成xy，并进行数据预处理，去空值
    model.data_preprocess()
    y_colname = '合计发明专利申请量'
    model.generate_xy(y_colname)

    # 数据分析
    save_path1 = main_path
    # 导出结果可根据需求，选择csv/txt/html的后缀来获取对应的结果文件
    model.stats_analyse(save_file=save_path1 + 'result_all.csv')

    # 进行 保留 80% 数据的清洗操作，并重新计算得到结果
    save_path2 = main_path
    model.errors_analysis(save_file=save_path2 + 'result_80.csv', rate=0.8, save_oringin_path=save_path2 + 'origin_80.xls')
