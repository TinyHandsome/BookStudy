#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: sql_one_line.py
@time: 2021/3/24 10:18
@desc: 将sql优化为一行，并转为帆软可识别的函数格式，用于设置缩放控件的初始边界
"""

from dataclasses import dataclass
import re
import pyperclip

@dataclass
class SQLOneLine:
    sql: str

    def __post_init__(self):
        ...

    def run(self):
        aim_str = self.oneline_str()
        return self.decorate_str(self.pattern_replace(aim_str))

    def oneline_str(self):
        result = ''
        space_index = False
        for word in self.sql:
            if word == ' ' or word == '\t' or word == '\n':
                space_index = True
            else:
                if space_index:
                    result += ' '
                    space_index = False

                result += word
        return result

    def pattern_replace(self, aim_str):
        pattern = re.compile(r"\${(?P<info>\w*)}")
        return (pattern.sub('" + $\g<info> + "', aim_str))

    def decorate_str(self, aim_str):
        return 'sql("EIP_DB","' + aim_str + '",1,1)'


if __name__ == '__main__':
    print("请粘贴sql:")
    all_sql = ''
    while True:
        sql = input()
        if sql == '':
            break

        all_sql += sql + '\n'

    sql_oneline = SQLOneLine(all_sql)
    result = sql_oneline.run()
    pyperclip.copy(result)
    print(result)
    print(r'\\ 已复制到剪贴板 \\')
