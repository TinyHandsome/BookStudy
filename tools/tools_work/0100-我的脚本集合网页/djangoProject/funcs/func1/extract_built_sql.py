#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: extract_built_sql.py
@time: 2021/8/13 10:54
@desc: 抽取建表语句中的字段名字，改为select ... from table
        起名：mysql create table到hive建表+select字段工具
        输出exe文件：pyinstaller -F extract_built_sql.py -i pic.ico

        - 【20210823】 v0.1
            1. 新增中台创表语句的字段提取功能
            2. 新增时间pause功能
"""
import sys
import re
import time
from dataclasses import dataclass

from funcs.func1.column_deal import columns_deal

update_info = """
**************************************************************************************************************
【mysql create table到hive建表 + select字段工具】 v0.1 20210823
本工具为sql解析工具，包括以下功能：
    1. cis到ods_cis开发
        通过复制CIS原表的 show create table 中的内容，获得 (1)中台ods_cis创表语句 以及 (2)select各个字段的语句
    2. 数据中台select字段语句的生成
        通过dmp的某创表语句，生成select字段的语句（比如从dw到dm层时，辅助生成insert语句中的select语句）

                                                                                                 @李英俊小朋友
**************************************************************************************************************
"""


@dataclass
class SqlExtract:
    sql: str

    def __post_init__(self):
        # 是否是中台的创表语句（是否有.），是的话，就不需要新建创表语句
        self.dmp_flag = False

    def analyse_sql(self):
        """
        解析sql
            1. 获取表名
            2. 获取字段
            3. 获取备注
        """
        if self.sql is None or self.sql == '':
            return '', ''

        # 1. sql预处理
        # 去除sql前后的空格，去掉所有`
        self.sql = self.sql.strip().replace('`', '')

        # 2. 将sql分为三部分
        sql_list = self.sql.split('\n')
        first_row = sql_list.pop(0)
        last_row = sql_list.pop(-1).replace('=', ' ').replace(';', '').replace(')', '').strip()
        middle_rows = [x.strip() for x in sql_list]

        # 3. 获取表名
        pattern = re.compile(r'\s+([\w\.]+)\s+\(')
        table_name = pattern.search(first_row, re.I).group(1)
        if '.' in table_name:
            self.dmp_flag = True

        # 4. 获取列名和备注
        def get_column_comment(row):
            # 去掉最右边的逗号
            column_name = row.split()[0]
            comment = re.search(r"comment\s+(.*)", row, re.I).group(1).rstrip(',')
            return column_name, comment

        columns, comments = zip(*[get_column_comment(x) for x in middle_rows])
        result1_columns = columns_deal(columns)

        # 5. 组成结果
        new_rows = [x + ' string comment ' + "'" + y + "'" for x, y in zip(result1_columns, comments)]
        result1 = 'create table if not exists ' + 'ods_cis.' + table_name + ' (\n\t' + ',\n\t'.join(
            new_rows) + '\n) ' + last_row + '\nSTORED AS PARQUET TBLPROPERTIES ("orc.compress"="SNAPPY");'

        result2_columns = columns_deal(columns, True)
        result2 = 'select\n\t' + ',\n\t'.join(result2_columns) + '\nfrom ' + table_name
        return result1, result2

    def __repr__(self):
        return repr(self.sql)


def run():
    print('粘贴你的sql内容：')
    aim_sqls = []
    while (True):
        x = input()
        if x.lower() == 'q':
            sys.exit(0)
        if x != '':
            aim_sqls.append(x)
        else:
            break

    se = SqlExtract('\n'.join(aim_sqls))
    se.analyse_sql()
    print('-' * 50 + '\n' + '处理完毕，等待新的输入【输入q，退出程序】\n' + '-' * 50 + '\n')


def main():
    print(update_info)
    while True:
        try:
            run()
        except:
            print('【警告】你粘贴的东西不行，请检查sql，或者联系【管理员】李英俊小朋友解决！！！')
            time.sleep(1)


def extract_built_sql(sql):
    se = SqlExtract(sql)
    try:
        return se.analyse_sql()
    except:
        return -1, -1


if __name__ == '__main__':
    main()
