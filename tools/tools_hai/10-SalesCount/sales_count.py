#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: sales_count.py
@time: 2020/9/28 21:44
@desc: 
"""

import pandas as pd
import numpy as np


class Sale:
    def __init__(self, id, year, sales):
        self.id = id
        self.year = year
        self.sales = sales


def check_empty(sales_list):
    """检查五个数，只要有一个为空则不计算"""
    for sale in sales_list:
        if pd.isna(sale.sales):
            return False
    return True


def check_id(sales_list):
    """检查五个数，必须id相同"""
    temp_id = sales_list[0].id
    for sale in sales_list:
        if sale.id != temp_id:
            return False
    return True


def count_mean(sales_list):
    """计算均值"""
    if check_empty(sales_list) and check_id(sales_list):
        sum = 0
        for sale in sales_list:
            sum += sale.sales
        return sum / 5
    else:
        return None


def count_std(sales_list):
    """计算标准差"""
    if check_empty(sales_list) and check_id(sales_list):
        sales = []
        for sale in sales_list:
            sales.append(sale.sales)
        return np.std(sales)
    else:
        return None


def count_aim_value(col, df, method, name):
    nr, nc = df.shape

    # 遍历每一行，注意这里要考虑最后的边界问题
    aim_values = []
    for i in range(4, nr):
        numbers = [0, 1, 2, 3, 4]
        sales_list = []
        for num in numbers:
            id1 = df.iloc[i - num, 0]
            year1 = df.iloc[i - num, 2]
            sales1 = df.iloc[i - num, col]
            temp_sale = Sale(id1, year1, sales1)
            sales_list.append(temp_sale)

        if method == 'mean':
            result = count_mean(sales_list)
        else:
            result = count_std(sales_list)
        aim_values.append(result)
    aim_values = [None] * 4 + aim_values

    df[name] = aim_values
    # df.to_excel('result_mean_count.xlsx', index=False)


if __name__ == '__main__':
    root_path = 'E:\\hanpi\\'
    df = pd.read_excel(root_path + '销售收入1.xlsx')
    count_aim_value(3, df, 'mean', 'sales_mean')
    count_aim_value(10, df, 'std', 'nsales_sd')
    df.to_excel(root_path + 'hanpi.xlsx', index=False)
