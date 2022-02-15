#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: extract_build_hana.py
@time: 2022/1/26 16:00
@desc: 从Oracle中获取建表语句生成hive建表语句和选择语句
"""
import re

from app.mymodels.func2.hana2hive import DMPTbls
from funcs.func1.column_deal import columns_deal
from funcs.my_base_funcs.str_funcs import is_None_or_nullstr
from funcs.test.oracle_test import oracle_data


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


def assemble(column_names, column_names_set):
    """组装列名和备注，如果找不到备注就用空字符串"""
    column_names_dict = {}
    for name, comment in column_names_set:
        column_names_dict[name] = comment

    return_column_names = []
    for c in column_names:
        comment_c = column_names_dict.get(c) or ''
        return_column_names.append((c, comment_c))

    return return_column_names


def analyse_sql(sql: str):
    """
    解析sql
        1. 获取表名
        2. 获取字段
        3. 获取备注
    """
    if is_None_or_nullstr(sql):
        return '', ''

    # 1. sql预处理
    # 1.1 去除sql前后的空格，去掉所有`
    sql = sql.strip().replace('`', '')
    # 1.2 每一行去除前后的空格
    sql = '\n'.join([x.strip() for x in sql.split('\n')])

    # 2. 获取表和schema
    table_schema, table_name = re.search(r'create\s+table\s+\"(\w+)\"\.\"(.+?)\"', sql, re.I | re.M).groups()

    # 3. 获取列
    column_names = re.findall(r'^(?:[\(\s]+)?\"(.*?)\"', sql, re.I | re.M)

    # 4. 获取列和comment
    column_names_set = re.findall(r'\.([^\.]*?)\s+is\s+\'(.*?)\'', sql, re.I | re.M)
    # 组装列和comment
    column_names = assemble(column_names, column_names_set)
    # 处理列名
    columns, comments = zip(*column_names)
    result1_columns = columns_deal(columns)

    # 5. 表的comment，数据库名，表描述
    aim_table = DMPTbls.objects.filter(table_name=table_name.upper())

    # 可能有多条，但是取第一个
    try:
        table_des = aim_table[0].table_des or '【缺少表描述】'
    except:
        table_des = '【缺少表描述】'

    last_row = "COMMENT '" + table_des + "'"

    # 6. 组成结果
    result2_columns = columns_deal(columns, is_select=True)

    new_rows = [x + ' string comment ' + "'" + y + "'" for x, y in zip(result1_columns, comments)]
    result1 = 'create table if not exists ' + 'ods_bpm.' + table_name + ' (\n\t' + ',\n\t'.join(
        new_rows) + '\n) ' + last_row + '\nSTORED AS PARQUET TBLPROPERTIES ("orc.compress"="SNAPPY");'
    result2 = 'select\n\t' + ',\n\t'.join(result2_columns) + '\nfrom ' + table_schema + '.' + table_name

    return result1, result2


def test():
    analyse_sql(oracle_data)


if __name__ == '__main__':
    test()
