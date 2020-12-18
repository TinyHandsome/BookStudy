#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: excelSplit.py
@time: 2020/4/21 11:00
@desc: 将Excel表格中一行分割为多行（分割依据某属性值的多个取值）
"""

import pandas as pd
from collections import OrderedDict, Counter
import os


def excelSplit(file_path, aim_column_index,  split_label='；'):
    """
    分离行业代码和行业分类
    :param file_path:  文件路径
    :param aim_column_index:  行业分类和行业代码所在列
    :param split_label:  分离标记
    :return:
    """
    data = pd.read_excel(file_path)
    values = data.values
    header = data.columns.tolist()

    # 遍历数据
    aim_data = []
    for line in values:
        hangye_fenlei = line[aim_column_index[0]].split(split_label)
        hangye_daima = line[aim_column_index[1]].split(split_label)

        # 遍历行业
        # 如果行业分类数量和行业代码一致，就正常操作
        if len(hangye_fenlei) == len(hangye_daima):
            for fl, dm in zip(hangye_fenlei, hangye_daima):
                new_line = line.copy()
                new_line[aim_column_index[0]] = fl
                new_line[aim_column_index[1]] = dm
                aim_data.append(new_line)

        # 如果不一致，则填写 “待核实”
        else:
            for fl in hangye_fenlei:
                new_line = line.copy()
                new_line[aim_column_index[0]] = fl
                new_line[aim_column_index[1]] = '待核实'
                aim_data.append(new_line)

    df = pd.DataFrame(aim_data, columns=header)
    return df


def analyse(dataFrame, base_columns, aim_column, return_DataFrame):
    """
    根据处理后的数据分析某一列的值，
    1. 无重复值，则取改值
    2. 有重复值，重复值相同则取改值，不同则都写上
    :param dataFrame: 原始数据
    :param base_columns: 需要出现的列
    :param aim_column: 需要统计的目标列
    :param return_DataFrame: 是否返回集成的DataFrame，还是返回目标列的统计list
    :return:
    """
    header = base_columns + [aim_column]
    base_columns_len = len(base_columns)
    data = dataFrame[header]
    data = data.dropna()

    # 生成base_columns对应aim_column的字典
    dd = OrderedDict()
    for line in data.values:
        key = ''
        for i in range(base_columns_len):
            key = key + line[i] + '+'
        key = key[:-1]
        aititude = line[base_columns_len]
        if key not in dd.keys():
            dd[key] = [aititude]
        else:
            dd[key].append(aititude)

    # 处理字典中的aim_column的值
    datas = []
    for k, v in dd.items():
        pp = k.split('+')
        length = len(v)
        if length == 1:
            at = v[0]
        else:
            if len(Counter(v).keys()) == 1:
                at = v[0]
            else:
                at = ','.join(v)
        aim_d = pp + [at]
        datas.append(aim_d)

    result = pd.DataFrame(datas, columns=header)
    aim_list = result[aim_column]

    if return_DataFrame:
        return result
    else:
        return aim_list


def jointDataFrame(main_df, if_save, savepath, *args):
    """拼接一个DataFrame和多个Series"""
    for c in args:
        name = c.name
        value = c.tolist()
        main_df[name] = value

    if if_save:
        main_df.to_excel(savepath, index=False)
    return main_df


def test1():
    """处理省级产业政策"""
    file_path = 'C:/Users/Administrator/Desktop/省级产业政策.xlsx'
    save_path = 'C:/Users/Administrator/Desktop/省级产业政策处理结果.xlsx'
    # 处理原始文件，拆分属性为多行值
    df = excelSplit(file_path, [6, 7])
    # 分析目标属性，获取省政策
    base_columns = ['所属省份', '五年规划', '行业分类2001', '行业代码2001']
    aim_column = '政策态度'
    result = analyse(df, base_columns, aim_column, True)
    aim_column = '是否重点支持产业'
    c1 = analyse(df, base_columns, aim_column, False)
    aim_column = '是否国家重点支持产业'
    c2 = analyse(df, base_columns, aim_column, False)
    # 拼接结果
    result = jointDataFrame(result, True, save_path, c1, c2)


def test2():
    """处理中央产业政策"""
    file_path = 'C:/Users/Administrator/Desktop/中央产业政策.xlsx'
    save_path = 'C:/Users/Administrator/Desktop/中央产业政策处理结果.xlsx'
    # 处理原始文件，拆分属性为多行值
    df = excelSplit(file_path, [5, 6])
    # 分析目标属性，获取省政策
    base_columns = ['五年规划', '行业分类2001', '行业代码2001']
    aim_column = '政策态度'
    result = analyse(df, base_columns, aim_column, True)
    aim_column = '是否重点支持产业'
    c1 = analyse(df, base_columns, aim_column, False)
    # 拼接结果
    result = jointDataFrame(result, True, save_path, c1)


if __name__ == '__main__':
    test1()
    test2()
