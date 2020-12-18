#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: matrix_generate.py
@time: 2020/9/13 10:20
@desc: 遍历每一年的公司，求取每一年公司之间的d_ij
"""
import pandas as pd
import numpy as np


def matrix_deal(path):
    df = pd.read_excel(path)
    df_aim = df[['id', 'year', '经度', '纬度']]

    # 获取所有的年份，按每一年遍历
    years = df_aim.year.drop_duplicates().sort_values().tolist()

    for year in years:
        data = df_aim[df_aim.year == year].drop(columns='year')

        # 取出所有的id值
        ids = data.id.drop_duplicates().sort_values().tolist()

        # 计算两两id之间的值
        vv = []
        ni = 0
        for i in ids:
            rows = []
            nj = 0
            for j in ids:
                print('正在计算第【', ni, '】行', '第【', nj, '】列的值...')

                x1 = data[data.id == i].values[0][1]
                y1 = data[data.id == i].values[0][2]

                x2 = data[data.id == j].values[0][1]
                y2 = data[data.id == j].values[0][2]

                dij = calculate_d(x1, y1, x2, y2)
                rows.append(dij)
                nj += 1
            vv.append(rows)
            ni += 1

        result = pd.DataFrame(vv, columns=ids, index=ids)
        result.to_excel('E:\\【我海】选我就完事儿了\\20200912-计算距离\\' + str(year) + '.xlsx')
        break


def calculate_d(x1, y1, x2, y2):
    C = 3437
    if pd.isna(x1) or pd.isna(x2) or pd.isna(y1) or pd.isna(y2):
        d = 0
    else:
        d = C * (np.arccos(np.sin(y1) * np.sin(y2) + np.cos(y1) * np.cos(y2) * np.cos(np.abs(x1 - x2))))

    return d


if __name__ == '__main__':
    path = 'E:\\【我海】选我就完事儿了\\20200912-计算距离\\经度纬度.xlsx'
    matrix_deal(path)
