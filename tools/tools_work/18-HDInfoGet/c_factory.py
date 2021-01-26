#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: c_factory.py
@time: 2021/1/21 13:24
@desc: 根据生成的ABC三个文件，主要是C文件，提取中的内容，为了excel_compare.py查找
"""

from dataclasses import dataclass
import pandas as pd


@dataclass
class Line:
    """每一行封装成一个类"""
    # 一二三级目录
    a: str
    b: str
    c: str

    # 表名
    table_name: str
    # 表中文名
    table_bussiness: str
    # 是否录入
    is_record: str

    def __post_init__(self):
        # 表名：全部转换为小写
        self.table_name = self.table_name.lower()
        # 去除中文名中的斜杠
        # self.table_bussiness = self.table_bussiness.replace('/', '')
        # 去除中文名中的空格
        # self.table_bussiness = self.table_bussiness.replace(' ', '')

    def cc(self, v1, v2, name):
        if v1 != v2:
            return name + '不同：【表中】' + v1 + '，【系统中】' + v2 + '\n'
        else:
            return ''

    def compare(self, l_list):
        all_result = []
        for l in l_list:
            result = ''

            # 检查是否录入
            result += self.cc(self.a, l.a, '一级目录')
            result += self.cc(self.b, l.b, '二级目录')
            result += self.cc(self.c, l.c, '三级目录')
            result += self.cc(self.table_name, l.table_name, '表名')
            result += self.cc(self.table_bussiness, l.table_bussiness, '表中文名')

            all_result.append(result)

        # 获取result最小的结果
        len_result = [len(x) for x in all_result]
        min_len_result_index = len_result.index(min(len_result))
        return all_result[min_len_result_index]


@dataclass
class C_Factory:
    c_path: str

    def __post_init__(self):
        self.c_df = pd.read_excel(self.c_path)
        self.data = {}

    def create_table_name_dict(self):
        """创建表名映射信息"""
        nrows = self.c_df.shape[0]
        for i in range(nrows):
            # a_item, b_item, c_item, table_name, table_bussiness = self.c_df.loc[i, '一级目录': '表中文名']
            table_name = self.c_df.loc[i, '表名'].lower()
            # 检查data中是否已经有了这个值，有的话，append，这里将每个table_name对应的value设为list了
            if table_name not in self.data.keys():
                self.data[table_name] = [Line(*(self.c_df.loc[i, '一级目录': '表中文名'].tolist() + [-1]))]
            else:
                self.data[table_name].append(Line(*(self.c_df.loc[i, '一级目录': '表中文名'].tolist() + [-1])))

        return self.data


if __name__ == '__main__':
    cf = C_Factory(r'E:\1-工作\1-工作\20210120-数据目录新\三级目录.xlsx')
    cf.create_table_name_dict()
