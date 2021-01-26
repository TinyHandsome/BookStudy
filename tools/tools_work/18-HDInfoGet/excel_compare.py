#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: excel_compare.py
@time: 2021/1/21 10:22
@desc: 根据excel的数据目录对比系统，查看是否一致
        1. 先直接excel对比C.xlsx，
        2. 有时间的，再实现逐条对比，调用的情况
"""
from dataclasses import dataclass
import pandas as pd
from c_factory import C_Factory, Line


@dataclass
class ExcelCompare:
    excel_path: str

    def __post_init__(self):
        self.df_list = pd.read_excel(self.excel_path, sheet_name=None)
        self.all_line = []

    def set_using_df(self, index_start, index_end):
        """设置想要的数据列的index，前闭后开"""
        self.aim_dfs = list(self.df_list.values())[index_start: index_end]

    def walk_aim_dfs(self):
        """遍历每个df，将所有信息放到[Line]中"""
        for df in self.aim_dfs:
            line_list = self.get_df_info(df)
            self.all_line = self.all_line + line_list

    def get_df_info(self, df):
        """根据df，获取每个df 的一级目录，二级目录，三级目录，表名，表中文名"""
        line_list = []
        df = df.drop(columns='负责人')
        temp_df = df.loc[:, '一级目录': '备注']
        for line in temp_df.values:
            l = Line(*line)
            line_list.append(l)
        return line_list

    def walk_lines(self):
        """遍历all_line，对比数据"""
        cf = C_Factory(r'E:\1-工作\1-工作\20210120-数据目录新\三级目录.xlsx')
        data = cf.create_table_name_dict()

        # 遍历每一行，查找在data中的分布
        count = 0
        for line in self.all_line:
            # line是excel数据，data是系统数据的字典
            # 检查是否录入，不录入就不检查
            if not isinstance(line.is_record, str):
                table_name = line.table_name

                l_list = data.get(table_name)
                if l_list is None:
                    # 检查是否在HD中录入了该名字
                    print('表：', table_name, '：', end='')
                    print('该表未录入系统中...')
                    count += 1
                else:
                    # 找到了，再检查其他对不对
                    result = line.compare(l_list)
                    # 如果检查没问题，则不输出
                    if result != '':
                        # 检查是否在HD中录入了该名字
                        print('正在检查：', table_name, '：', end='')
                        print('\n' + result)
                        count += 1
        print('一共有：', count, '个问题需要解决...')


if __name__ == '__main__':
    ec = ExcelCompare(r'E:\1-工作\1-工作\20210125-新双周\new_data.xls')
    ec.set_using_df(1, -1)
    ec.walk_aim_dfs()
    ec.walk_lines()
