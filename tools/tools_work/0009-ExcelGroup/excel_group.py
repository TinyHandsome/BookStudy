#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: excel_group.py
@time: 2020/11/6 10:15
@desc: 给我一个excel，除了第一行之外，下面每一行都是一个任务，新增一列进行分组
        默认分组为sheet2的第一列（没有表头，只要人名就好）
"""
import os
from random import shuffle

import pandas as pd
import math
from collections import Counter
from dataclasses import dataclass


@dataclass
class ExcelGroup:
    excel_path: str
    shuffled: bool

    def __post_init__(self):
        # 作者名
        self.author = '李添'
        # 默认保存路径
        self.default_save_path = os.path.dirname(self.excel_path)

        df_2 = pd.read_excel(self.excel_path, sheet_name=1, header=None)
        self.default_groups = df_2.to_dict().get(0)

        # 是否打乱顺序
        if self.shuffled:
            self.shuffle_dict()

    def shuffle_dict(self, loc_index=-1):
        """把目标位置放在 loc_index"""
        # 默认为最后的位置
        if loc_index == -1:
            loc_index = len(self.default_groups) - 1

        # 打乱dict顺序
        shuffle(self.default_groups)
        # 找到我的标记
        my_index = list(self.default_groups.values()).index(self.author)
        temp_values = self.default_groups.get(loc_index)
        # 替换数据
        self.default_groups[loc_index] = self.author
        self.default_groups[my_index] = temp_values

    def group_task(self, is_save=False):
        """分组"""
        df = pd.read_excel(self.excel_path)
        row_num = df.shape[0]

        # 每个人多少个
        everyone_task_num = math.ceil(row_num / len(self.default_groups))
        group_list = [self.default_groups.get(int(i / everyone_task_num)) for i in range(row_num)]

        # 分组结果统计
        group_result = Counter(group_list)
        print('结果统计：')
        print(group_result)
        print()

        # 生成新的表
        df['分组'] = group_list

        # 保存到默认路径
        if is_save:
            df.to_excel(os.path.join(self.default_save_path, 'result.xlsx'), index=None)
        else:
            print(df.head())


if __name__ == '__main__':
    path = r'E:\1-工作\1-工作\20210125-新双周\流程导入任务分配.xlsx'
    # 根据是否是整除自己输入，是否打乱顺序
    eg = ExcelGroup(path, True)
    # 是否保存结果
    eg.group_task(True)
