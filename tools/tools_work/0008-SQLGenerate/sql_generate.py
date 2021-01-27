#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: sql_generate.py
@time: 2020/11/2 9:28
@desc: 根据excel的信息处理生成sql，有的esms的sql语句中没有comment，这里通过更新comment完成
"""

import pandas as pd
import math

root_path = 'E:/【冲鸭】/【工作】1. 工作安排、文件存储/20201102-新双周+ESMS表注释重命名+质量指标/'
file_start = '工程-01-PS-数据字典-数据调研模板_EPS_esms-'
file_name = ['02', '03', '04']
files = [root_path + file_start + fn + '.xlsx' for fn in file_name]

# 统计所有表的数量
count = 0
for file_path in files:
    df = pd.read_excel(file_path, sheet_name=None, header=None)
    for table_name, table in df.items():
        count += 1
# 5个人，每个人的数量
names_dict = {
    1: '邢振东',
    2: '王文辉',
    3: '潘彬彬',
    4: '刘泽宁',
    5: '郑春玲'
}
# 双表增量的表名
double_table_names = ['esms_person_enter_detail', 'esms_inspect_apply_detail', 'esms_inspect_apply',
                      'esms_salary_detail']


def is_double_table(name: str):
    """根据表名检查是否是双表增量"""
    for dn in double_table_names:
        if name.lower() == dn:
            return True
    return False


def write_sql(extra_str, name, table_name_repaired, table):
    """
    写入sql
    :param extra_str: 是否是双表增量的警告
    :param name: 任务分配给谁
    :param table_name_repaired: 表名
    :param table: 数据dataframe
    :return:
    """
    aim_values = table[['列名', '备注']].values
    sql_final = '# ' + extra_str + '【' + name + ': ' + str(cc + 1) + '】' + table_name_repaired + '\n'

    def middle_row():
        sql_temp = ''
        for row in aim_values:

            # 检查字段中是否有正斜杠和反斜杠
            # if not pd.isna(row[0]):
            #     if '\\' in row[0] or '/' in row[0]:
            #         print(row)

            if pd.isna(row[0]):
                break
            if pd.isna(row[1]):
                comment = ''
            else:
                comment = row[1]
            if len(row[0]) <= 10:
                tt = '\t\t\t'
            elif len(row[0]) <= 20:
                tt = '\t\t'
            else:
                tt = '\t'

            sql_temp += '\t' + row[0] + tt + 'string comment ' + "\'" + comment + "\', \n"
        sql_temp = sql_temp.rstrip(", \n")
        sql_temp += ") \n"
        return sql_temp

    sql_final += 'create table if not exists ods_esms.`' + table_name_repaired + '`( \n'
    sql_final += middle_row()
    sql_final += 'comment ' + "\'" + comment_all + "\' \n"
    if extra_str != '':
        # 双表增量
        sql_final += '\n' + 'create table if not exists ods_esms.`' + table_name_repaired + '_inc`( \n'
        sql_final += middle_row()
        sql_final += 'comment ' + "\'" + comment_all + "-增量表\' \n"
    sql_final += "partitioned by (`dt` string comment \'分区字段\');\n\n"

    return sql_final


every_task = math.ceil(count / 5)

table_names = []
drop_result = ''
result = ''
cc = -1
for file_path in files:
    df = pd.read_excel(file_path, sheet_name=None, header=None)
    for table_name, table in df.items():

        cc += 1
        name = names_dict.get(int(cc / every_task) + 1)

        comment_all = table.iloc[0, 1]
        table.columns = table.iloc[1, :]
        table.drop(table.index[0:2], inplace=True)

        # 因为表明sheet有限制，所以需要读取表名的信息
        try:
            table_name_repaired = table['表名'].values[0]
        except:
            table_name_repaired = table_name

        # 开始写dropsql
        table_names.append(table_name_repaired)
        drop_result += 'drop table ods_esms.`' + table_name_repaired + '`;\n'

        # 开始写sql

        if is_double_table(table_name_repaired):
            extra_str = '！！！注意：该表是双表增量！！！'
        else:
            extra_str = ''

        sql = write_sql(extra_str, name, table_name_repaired, table)
        result += sql

with open(root_path + 'esms_sql_generate.txt', 'w', encoding='utf-8') as f:
    f.writelines(result)

with open(root_path + 'esms_drop_sql.txt', 'w', encoding='utf-8') as g:
    g.writelines(drop_result)

with open(root_path + 'esms_tables_rep.txt', 'w', encoding='utf-8') as h:
    h.writelines(','.join(table_names))
