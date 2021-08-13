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
        输出exe文件：pyinstaller -F extract_built_sql.py -i pic.ico
"""
import sys
import re
import pyperclip
from dataclasses import dataclass


@dataclass
class SqlExtract:
    sql: str

    def __post_init__(self):
        self.analyse_sql()

    def analyse_sql(self):
        """
        解析sql
            1. 获取表名
            2. 获取字段
            3. 获取备注
        """

        # 1. sql预处理
        # 去除sql前后的空格，去掉所有`
        self.sql = self.sql.strip().replace('`', '')

        # 2. 将sql分为三部分
        sql_list = self.sql.split('\n')
        first_row = sql_list.pop(0)
        last_row = sql_list.pop(-1).split()[-1].replace('=', ' ')
        middle_rows = [x.strip() for x in sql_list]

        # 3. 获取表名
        pattern = re.compile(r'\s+(\w+)\s+\(')
        table_name = pattern.search(first_row, re.I).group(1)

        # 4. 获取列名和备注
        def get_column_comment(row):
            # 去掉最右边的逗号
            column_name = row.split()[0]
            comment = re.search(r"comment\s+(.*)", row, re.I).group(1).rstrip(',')
            return column_name, comment

        columns, comments = zip(*[get_column_comment(x) for x in middle_rows])

        # 5. 组成结果
        new_rows = [x + ' string comment ' + y for x, y in zip(columns, comments)]
        result1 = 'create table if not exists ods_cis.' + table_name + ' (\n\t' + ',\n\t'.join(
            new_rows) + '\n) ' + last_row + '\nSTORED AS PARQUET TBLPROPERTIES ("orc.compress"="SNAPPY");'
        result2 = 'select\n\t' + ',\n\t'.join(columns) + '\nfrom ' + table_name
        print(result1)
        r1 = input('是否需要复制创表语句？[回车表示复制，任意键跳过]')
        if r1 == '':
            pyperclip.copy(result1)
            print('--> 已复制')
        else:
            ...
        print('-' * 50)
        print(result2)
        r2 = input('是否需要复制选择字段语句？[回车表示复制，任意键跳过]')
        if r2 == '':
            pyperclip.copy(result2)
            print('--> 已复制')
        else:
            ...

    def __repr__(self):
        return repr(self.sql)


def run():
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
    print('-' * 50 + '\n' + '处理完毕，等待新的输入【输入q，退出程序】\n' + '-' * 50 + '\n')


if __name__ == '__main__':
    while True:
        run()
