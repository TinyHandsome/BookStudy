#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: compare_hana_oracle.py
@time: 2022/1/24 13:53
@desc: 比较hana和oracle的元数据是否一致
"""
import os
import time

import pandas as pd
from pandas import DataFrame

pd.set_option('display.max_columns', None)

base_path = 'E:/1-Work/1-工作/20220124-软考'
path_hana = os.path.join(base_path, 'hanaMeta_20220124.csv')
path_oracle = os.path.join(base_path, 'oraMeta_20220124.csv')
# 关联库名和表描述
dmp_tbls = pd.read_excel(os.path.join(base_path, 'dmp_tbls.xlsx'))[['数据库', '表名', '表描述']]
dmp_tbls['表名'] = dmp_tbls['表名'].apply(lambda x: x.upper())
dmp_tbls.set_index('表名', inplace=True)


def get_columns_data(path: str, columns: list):
    """获取目标数据"""
    temp = pd.read_csv(path)
    return temp[columns]


def get_table_counts(df: DataFrame):
    """对比每个表的长度"""
    return df.groupby('TABLE_NAME').count()


my_columns = ['TABLE_NAME', 'COLUMN_NAME']
my_hana = get_columns_data(path_hana, my_columns)
my_oracle = get_columns_data(path_oracle, my_columns)

# 统计每个表的个数，通过shape已经验证过两个库的表数量一致，都是55个
hana_count = get_table_counts(my_hana)
oracle_count = get_table_counts(my_oracle)

count_result = pd.merge(hana_count, oracle_count, how='outer', on='TABLE_NAME', suffixes=("_hana", "_oracle"))
count_result['if_uniformity'] = count_result['COLUMN_NAME_hana'] == count_result['COLUMN_NAME_oracle']


# print(count_result)


# 对比oracle中的列名是否在hana中都有
def concat_columns(x, column_name='COLUMN_NAME'):
    """合并列名"""
    return list(x[column_name])


c1 = 'hana_columns'
c2 = 'oracle_columns'


def get_intersection(x):
    """获取值的交集"""
    try:
        return set(x[c1]).intersection(set(x[c2]))
    except:
        return ''


def get_difference_c1(x):
    """获取c1与c2的差集，c1有，c2没有"""
    try:
        return set(x[c1]).difference(set(x[c2]))
    except:
        return ''


def get_difference_c2(x):
    """获取c2与c1的差集，c2有，c1没有"""
    try:
        return set(x[c2]).difference(set(x[c1]))
    except:
        return ''


hana_columns = my_hana.groupby('TABLE_NAME').apply(concat_columns)
hana_columns = pd.DataFrame({'TABLE_NAME': hana_columns.index, 'hana_columns': hana_columns.values})
oracle_columns = my_oracle.groupby('TABLE_NAME').apply(concat_columns)
oracle_columns = pd.DataFrame({'TABLE_NAME': oracle_columns.index, 'oracle_columns': oracle_columns.values})

columns_result = pd.merge(hana_columns, oracle_columns, how='outer', on='TABLE_NAME')
columns_result.set_index('TABLE_NAME', inplace=True)
columns_result['intersection'] = columns_result.apply(get_intersection, axis=1)
columns_result['c1have_c2nohave'] = columns_result.apply(get_difference_c1, axis=1)
columns_result['c2have_c1nohave'] = columns_result.apply(get_difference_c2, axis=1)
columns_result['is_same'] = columns_result.apply(
    lambda x: x['c2have_c1nohave'] == set() and x['c1have_c2nohave'] == set(), axis=1)

# 输出所有结果
result = pd.merge(count_result, columns_result, how='left', on='TABLE_NAME')
# 关联表描述
result = pd.merge(result, dmp_tbls, how='left', left_index=True, right_index=True)

result.to_excel(os.path.join(base_path, 'result_' + time.strftime("%Y%m%d") + '.xlsx'))
