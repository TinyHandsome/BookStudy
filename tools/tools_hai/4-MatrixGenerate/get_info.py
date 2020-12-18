#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: get_info.py
@time: 2020/9/13 11:59
@desc: 
"""
import os
import pandas as pd
import numpy as np
from collections import OrderedDict
import copy


class GetCompanyInfo:

    def __init__(self, path):
        self.path = path
        self.df = None
        self.aim_columns = ['id', 'year', '所属集团', '行业代码_x', '经度', '纬度']
        self.df_aim = None
        self.years = None
        self.data = OrderedDict()

        self.init()

    def init(self):
        self.df = pd.read_excel(self.path)
        self.df_aim = self.df[self.aim_columns]

        # 获取所有的年份，按每一年遍历
        self.years = self.df_aim.year.drop_duplicates().sort_values().tolist()

        # 计算每年的df，做成字典的形式
        for year in self.years:
            data = self.df_aim[self.df_aim.year == year]
            self.data[year] = data

    def cal_group_industry(self):
        group_list = []
        industry_list = []
        for a, b in zip(self.df['id'], self.df['year']):
            c = Company(a, b, self)
            g = c.cal_group_LD()
            i = c.cal_industry_LD()
            print(g, i)
            group_list.append(g)
            industry_list.append(i)

        self.df['group_value'] = group_list
        self.df['industry_value'] = industry_list

        self.df.to_excel(os.path.dirname(self.path) + '\\result.xlsx', index=False)


class Company:
    def __init__(self, id, year, gci: GetCompanyInfo):
        self.id = id
        self.year = year
        self.primarykey = self.hash()

        # 该公司所在年的所有数据
        self.gci = gci
        self.data = self.gci.data[year]

        self.x = None
        self.y = None
        self.group = None
        self.industry = None

        # 根据配置信息初始化经纬度
        self.init_xy()

    def hash(self):
        return str(self.id) + '-' + str(self.year)

    def get_id_year(self):
        return self.id, self.year

    def get_x_y(self):
        return self.x, self.y

    def init_xy(self):
        """根据id和year，获取对应的经纬度，xy的值"""

        id, year = self.get_id_year()
        self.x = self.data[self.data.id == id].loc[:, '经度'].values[0]
        self.y = self.data[self.data.id == id].loc[:, '纬度'].values[0]
        self.group = self.data[self.data.id == id].loc[:, '所属集团'].values[0]
        self.industry = self.data[self.data.id == id].loc[:, '行业代码_x'].values[0]

    def find_group(self, which_one):
        """找到该公司对应的【集团】或者【行业】的所有公司"""
        if which_one == 'group':
            name = '所属集团'
            key_word = self.group
        elif which_one == 'industry':
            name = '行业代码_x'
            key_word = self.industry
        else:
            name = None
            key_word = None
            print('你输入的什么鬼啊！')

        result = self.data[self.data[name] == key_word][['id', 'year']].values
        coms = []
        for line in result:
            c = Company(line[0], line[1], self.gci)
            coms.append(c)
        return Group(self.year, coms)

    def cal_group_LD(self):
        return self.find_group('group').cal_LD(self)

    def cal_industry_LD(self):
        return self.find_group('industry').cal_LD(self)


class Group:
    def __init__(self, year, coms: [Company]):
        self.year = year
        self.coms = coms

    def cal_LD(self, aim_c):
        temp_coms = copy.deepcopy(self.coms)

        # 删除公司列表中的目标公司，方便计算每一个除了目标公司之外的其他公司与目标公司的ld
        for tc in temp_coms:
            if tc.primarykey == aim_c.primarykey:
                temp_coms.remove(tc)

        sum = 0
        for c_temp in temp_coms:
            dij = self.calculate_d(aim_c, c_temp)
            ld = 1 / (1 + dij)
            sum += ld

        return sum

    @staticmethod
    def calculate_d(c1: Company, c2: Company):
        x1, y1 = c1.get_x_y()
        x2, y2 = c2.get_x_y()
        C = 3437
        if pd.isna(x1) or pd.isna(x2) or pd.isna(y1) or pd.isna(y2):
            d = 0
        else:
            d = C * (np.arccos(np.sin(y1) * np.sin(y2) + np.cos(y1) * np.cos(y2) * np.cos(np.abs(x1 - x2))))
        return d


if __name__ == '__main__':
    # path = 'E:\\【我海】选我就完事儿了\\20200912-计算距离\\经度纬度.xlsx'
    # gci = GetCompanyInfo(path)
    # gci.cal_group_industry()

    GetCompanyInfo('E:\\【我海】选我就完事儿了\\20200912-计算距离\\经度纬度.xlsx').cal_group_industry()
