#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: test_water.py
@time: 2020/5/15 11:34
@desc:  测试油水井数据的各种操作
"""
from MLTools import MLTools
from PreAnalysis import *
from MyMatplotlib import *
from Models import *
import pandas as pd
import pickle


def plot_heatmap(p_hot):
    """测试热力图"""
    df = pd.read_excel(p_hot)
    mat = MyMatplotlib(save_path)
    mat.plot_heatmap(df, change_ticks_fontsize=True, vmax=None, vmin=None, center=None)


def pca_columns(aim_columns, predict_X=None):
    """对部分列进行降维"""
    pca = MyPCA(save_path)
    for column in aim_columns:
        xx = X[column]
        print(pca.get_vr(xx))
    pca.pca_patial(X, aim_columns, y, predict_X=predict_X)


def maxmin_pca(X, y=None):
    """输入样本数据进行标准化"""
    mm = DataTransfer(save_path)
    new_X = mm.myMaxMinScaler(X, y)
    return new_X


def ml_all(X, y):
    """进行所有的分类并评估"""
    ml = MLTools(save_path + '分类-42/')
    ml.set_X(X)
    ml.set_y(y)
    ml.init_save_paths()
    ml.init_models()

    ml.evaluate_oa_model(X, y)


def test_model_step(X, y):
    model_names = ['随机森林', 'Adaboost', 'GBDT', 'XGBoost']
    models = [MyRF(), MyAdaboost(), MyGBDT(), MyXGBoost()]
    data = OrderedDict()
    for name, model in zip(model_names, models):
        model.init_model()
        model.paramsAdjustment_byStep(X, y)
        # 参数名：[参数取值list，参数得分list，最优参数取值]
        aim_dict = model.step_params_results
        data[name] = aim_dict
    # time_now = TimeTool().getCurrentTime()
    with open('F:/BookStudy/tools/MLtools/myTest/分步调参数据' + '.plk', 'wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    well_types = [
        'oil', 'water'
    ]

    for well_type in well_types:
        path2 = 'C:/Users/Administrator/Desktop/小论文第一次返修/小论文第一次修改备份/'
        if well_type == 'oil':
            # path = 'C:/Users/Administrator/Desktop/油井/油井标准化数据.xls'
            path = path2 + '油井/油井训练集-标准化降维后数据.xls'
            save_path = path2 + '油井/'
            p_hot = 'C:/Users/Administrator/Desktop/油井/相关系数/油井相关系数.xls'
            aim_columns = [['日产液量', '月产液量', '年产液量'], ['油压', '套压']]
        else:
            # path = 'C:/Users/Administrator/Desktop/水井/水井标准化数据.xls'
            path = path2 + '水井/水井训练集-标准化降维后数据.xls'
            save_path = path2 + '水井/'
            p_hot = 'C:/Users/Administrator/Desktop/水井/相关系数/水井相关系数.xls'
            aim_columns = [['日注水量', '月注水量', '年注水量'], ['油压', '套压']]

        data = pd.read_excel(path)
        column_names = data.columns
        y = data[column_names[-1]].tolist()
        X = data.drop(columns=column_names[-1])

        # 绘制热力图
        # plot_heatmap(p_hot)
        # 降维pca
        # pca_columns(aim_columns)
        # 运行所有的机器学习
        # ml_all(X, y)
        # 将要预测的数据标准化和降维
        # maxmin_pca(X, pred)
        # 测试分布调参
        test_model_step(X, y)
