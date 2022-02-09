#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: extract_build_hana.py
@time: 2022/1/26 16:00
@desc: 从hana中获取建表语句生成hive建表语句和选择语句
"""
import re

from app.mymodels.func2.hana2hive import DMPTbls
from funcs.func1.column_deal import columns_deal
from funcs.my_base_funcs.str_funcs import is_None_or_nullstr
from funcs.test.hana_test import hana_data


def find_comment(column, column_names):
    """找到列名的comment，找不到就用空字符串"""
    column = column.replace('"', '').replace("'", '').strip().lower()
    for col, comment in column_names:
        if col.lower() == column:
            return column, comment

    return column, ''


def deal_view_to_newrows(result2_columns, column_names):
    """处理view获取每个实际列名，主要是获取comment"""
    result1_columns = []
    comments = []
    for c in result2_columns:
        column, comm = find_comment(c, column_names)
        result1_columns.append(column)
        comments.append(comm)

    return result1_columns, comments


def analyse_sql(sql: str, view: str, hive_db=None, view_name=None, view_desc=None):
    """
    解析sql
        1. 获取表名
        2. 获取字段
        3. 获取备注
    """
    if sql is None or sql == '':
        return '', ''

    # 1. sql预处理
    # 去除sql前后的空格，去掉所有`
    sql = sql.strip().replace('`', '')

    # 2. 获取表
    table_name = re.search(r'create\s+column\s+table\s+\"\w+\"\.\"(.+?)\"', sql, re.I | re.M).group(1)

    # 3. 获取列
    column_names = re.findall(r'\"([^(\"\']*?)\"\s+[^\"]*?COMMENT\s+\'(.*?)\'', sql, re.I | re.M)

    # 4. 获取列和comment
    columns, comments = zip(*column_names)
    result1_columns = columns_deal(columns)

    # 5. 表的comment，数据库名，表描述
    aim_table = DMPTbls.objects.filter(table_name=table_name.lower())

    # 可能有多条，但是取第一个
    try:
        db_name = aim_table[0].db_name
        table_des = aim_table[0].table_des
    except:
        db_name = '【缺少库名】'
        table_des = '【缺少表描述】'

    # 有可能需要自定义库名、表名和表描述，比如hana的视图

    if not is_None_or_nullstr(hive_db):
        db_name = hive_db
    if not is_None_or_nullstr(view_name):
        table_name = view_name
    if not is_None_or_nullstr(view_desc):
        table_des = view_desc

    last_row = "COMMENT '" + table_des + "'"

    # 6. 组成结果
    if view is None or view == '':
        result2_columns = columns_deal(columns, is_select=True)
    else:
        # 处理视图，那么应该以视图的列为主
        result2_columns = view.split(',')
        result1_columns, comments = deal_view_to_newrows(result2_columns, column_names)

    result1_columns = columns_deal(result1_columns, is_select=False)

    new_rows = [x + ' string comment ' + "'" + y + "'" for x, y in zip(result1_columns, comments)]
    result1 = 'create table if not exists ' + db_name + '_s4.' + table_name + ' (\n\t' + ',\n\t'.join(
        new_rows) + '\n) ' + last_row + '\nSTORED AS PARQUET TBLPROPERTIES ("orc.compress"="SNAPPY");'
    result2 = 'select\n\t' + ',\n\t'.join(result2_columns) + '\nfrom ' + '"' + table_name + '"'

    return result1, result2


if __name__ == '__main__':
    a, b = analyse_sql(hana_data, '')
    print(a, b)
