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
        默认分组为6个人
"""
import os
import pandas as pd
import math
from collections import Counter


class ExcelGroup:
    groups = {
        0: '李添',
        1: '彭煜',
        2: '于德龙',
        3: '杜世斌',
        4: '窦会涛',
        5: '梁晓峰',
        6: '潘彬彬',
        7: '王文辉',
    }

    def __init__(self, excel_path: str, name_dict: dict = groups):
        # 默认分组是六个人
        self.name_dict = name_dict
        self.excel_path = excel_path

        # 默认保存路径
        self.default_save_path = os.path.dirname(self.excel_path)

    def group_task(self):
        """分组"""
        df = pd.read_excel(self.excel_path)
        row_num = df.shape[0]

        # 每个人多少个
        everyone_task_num = math.ceil(row_num / len(self.name_dict))
        group_list = [self.groups.get(int(i/everyone_task_num)) for i in range(row_num)]

        # 分组结果统计
        group_result = Counter(group_list)
        print(group_result)

        # 生成新的表
        df['分组'] = group_list

        # 保存到默认路径
        df.to_excel(os.path.join(self.default_save_path, 'result.xlsx'), index=None)


if __name__ == '__main__':
    eg = ExcelGroup('E:/【冲鸭】/【工作】1. 工作安排、文件存储/20201208-应急预案/万华数据中台(DMP)-PMO-TCK-应急预案补跑表统计-20201207-v1.1.xlsx')
    eg.group_task()
