#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: patent_cal.py
@time: 2020/9/27 20:43
@desc: 计算专利
"""

import pandas as pd
from collections import OrderedDict


class Patent:
    def __init__(self, code, date, patent_grant, creation_grant):
        self.code = code
        self.date = date
        self.patent_grant = patent_grant
        self.creation_grant = creation_grant

    def get_year(self):
        return int(self.date.split('-')[0])

    def get_patent_grant(self):
        return self.patent_grant

    def get_creation_grant(self):
        return self.creation_grant


class PatentAssemble:
    def __init__(self, file_path):
        self.file_path = file_path

        # 所有专利的实例
        self.patents = []

        # 以证券代码为key的专利实例
        self.patents_dict = OrderedDict()
        self.init_patents()

        self.df = None

    def init_patents(self):
        self.df = pd.read_excel(self.file_path)
        nrows, ncols = self.df.shape

        for i in range(nrows):
            code = self.df.iloc[i, 0]
            date = self.df.iloc[i, 1]
            patent_grant = self.df.iloc[i, 2]
            creation_grant = self.df.iloc[i, 3]
            p_temp = Patent(code, date, patent_grant, creation_grant)

            self.patents.append(p_temp)
            if code not in self.patents_dict.keys():
                self.patents_dict[code] = [p_temp]
            else:
                self.patents_dict[code].append(p_temp)

    def cal_code_year(self, code, year):
        """
        根据证券代码和年份计算前三年的均值
            1. 若存在找不到的情况，用0补充，并计算算数平均
            2. 若存在找不到的情况，忽略该记录，并计算算数平均；若三年都没有，则返回空值
        :param code:
        :param year:
        :return:
        """

        def check_year(py):
            """检查patent的年是否为要找的年"""
            aim_years = [int(year) - 1, int(year) - 2, int(year) - 3]
            if py in aim_years:
                return True
            else:
                return False

        patents_list = self.patents_dict[code]

        # 记录满足年份的patent
        satisfied_patents = []
        for pat in patents_list:
            pat_year = pat.get_year()
            if check_year(pat_year):
                satisfied_patents.append(pat)

        def count_aim(type):
            """计算满足年份的patent的均值"""

            def get_val_by_type():
                """根据type类型返回对应的值"""
                if type == 'patent':
                    return sp.get_patent_grant()
                else:
                    return sp.get_creation_grant()

            # 情况1：
            sum1 = 0
            if len(satisfied_patents) != 0:
                for sp in satisfied_patents:
                    sum1 += get_val_by_type()
            average1 = sum1 / 3
            # 情况2：
            sum2 = 0
            if len(satisfied_patents) == 0:
                average2 = None
            else:
                for sp in satisfied_patents:
                    sum2 += get_val_by_type()
                average2 = sum2 / len(satisfied_patents)

            return average1, average2

        patent_ave1, patent_ave2 = count_aim('patent')
        creation_ave1, creation_ave2 = count_aim('creation')
        return patent_ave1, patent_ave2, creation_ave1, creation_ave2


if __name__ == '__main__':
    pa = PatentAssemble('E:\\hanpi\\专利.xlsx')

    aim_table = pd.read_excel("E:\\hanpi\\被并方专利.xlsx")
    nr, nc = aim_table.shape
    aim_list1 = []
    aim_list2 = []
    aim_list3 = []
    aim_list4 = []
    for i in range(nr):
        code = aim_table.iloc[i, 3]
        year = aim_table.iloc[i, 1]
        try:
            patent_ave1, patent_ave2, creation_ave1, creation_ave2 = pa.cal_code_year(code, year)
        except:
            patent_ave1, patent_ave2, creation_ave1, creation_ave2 = [None] * 4

        print(code, year)
        print(patent_ave1, patent_ave2, creation_ave1, creation_ave2)
        print('\n')

        aim_list1.append(patent_ave1)
        aim_list2.append(patent_ave2)
        aim_list3.append(creation_ave1)
        aim_list4.append(creation_ave2)

    aim_table['patent_ave1'] = aim_list1
    aim_table['patent_ave2'] = aim_list2
    aim_table['creation_ave1'] = aim_list3
    aim_table['creation_ave2'] = aim_list4

    aim_table.to_excel("E:\\hanpi\\result.xlsx", index=False)
