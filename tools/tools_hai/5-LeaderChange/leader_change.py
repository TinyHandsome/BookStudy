#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: leader_change.py
@time: 2020/10/6 22:48
@desc: 看领导是否改变
"""
import pandas as pd
from collections import OrderedDict


class Leader:
    """领导"""

    def __init__(self, year, leaders, front):
        self.year = year
        self.leaders = leaders
        self.front = front

    def check_two(self, one, two):
        """检查两个领导是否一致"""
        # 先检查长度是否一致，不一致则直接返回true
        if len(one) != len(two):
            return 1
        else:
            # 现在长度一致了，然后检查是否one中每个领导都在two中
            count = 0
            for l in one:
                if l in two:
                    count += 1
            if count == len(one):
                # 说明one和two领导相同
                return 0
            else:
                return 1

    def check_change(self):
        """检查前一年的领导与今年的是否一致"""
        if self.front is None:
            # 如果前一年为空，则当年为第一年，所以没变返回0
            return 0
        else:
            # 否则，检查前一年的领导与今年的是否一致
            front_leaders = self.front.leaders
            return self.check_two(front_leaders, self.leaders)


class Bond:
    """证券"""

    def __init__(self, code):
        # 证券代码
        self.code = code
        # 证券每一年的领导，{年份: [领导们]}
        self.leaders = OrderedDict()
        # 是否改变
        self.leader_change = OrderedDict()

    def get_leaders_keys(self):
        """获取领导字典的年份"""
        return self.leaders.keys()

    def insert_row_data(self, year, name, start_date, end_date):
        """插入行数据，根据行的年，姓名，开始时间，结束时间字段检测是否为当年入职"""
        # 先检查end_date是不是空值，是的话，就暂时设为2050年
        if pd.isna(end_date):
            end_date = '2050'

        if pd.isna(start_date) or start_date == 'N/A,':
            start_date = '1900'

        # 先检查year是否在start和end之间
        if int(start_date) <= int(year) <= int(end_date):
            # 检查这一年是不是在字典中了
            if year not in self.get_leaders_keys():
                self.leaders[year] = [name]
            else:
                self.leaders[year].append(name)

    def print_leads(self):
        """输出证券代号和每一年的领导"""
        print(self.code, '：', end='')
        print(self.leaders)
        print(self.leader_change)

    def cal_leader_change(self):
        """计算该年的领导是否改变"""
        # 生成指向前一年的列表
        front = None
        for year, leaders in self.leaders.items():
            ll = Leader(year, leaders, front)
            front = ll
            # 计算当前年是否有领导改变
            self.leader_change[year] = ll.check_change()


class BondCouple:
    """所有证券"""

    def __init__(self, path):
        self.df = pd.read_excel(path)
        self.nr, self.nc = self.df.shape

        # 保存每个证券，证券代码: Bond
        self.bonds = OrderedDict()

    def get_bonds_keys(self):
        return self.bonds.keys()

    def get_col_value(self, row, col):
        """根据行和列的index返回值"""
        return self.df.iloc[row, col]

    def init(self):
        for i in range(self.nr):
            code = self.get_col_value(i, 0)
            year = self.get_col_value(i, 2)
            name = self.get_col_value(i, 4)
            start_date = self.get_col_value(i, 5)
            end_date = self.get_col_value(i, 6)

            # 如果代码没在bonds中，则需要新建映射，并且该证券也没有bond
            if code not in self.get_bonds_keys():
                # 新建证券，并保存到字典中
                temp_bond = Bond(code)
                temp_bond.insert_row_data(year, name, start_date, end_date)
                self.bonds[code] = temp_bond
            else:
                # 如果已经有该证券了，则直接插入心的数据
                self.bonds[code].insert_row_data(year, name, start_date, end_date)

    def print_bonds(self):
        """输出所有证券的信息"""
        for x in self.bonds.values():
            x.print_leads()

    def cal_bonds_leader_change(self):
        """遍历每一个证券，计算领导是否改变"""
        for x in self.bonds.values():
            x.cal_leader_change()

    def generate_result(self, save_path):
        """生成结果"""
        result = []
        for code, bond in self.bonds.items():
            leaders = bond.leaders
            changes = bond.leader_change
            for year, leader in leaders.items():
                change = changes[year]
                temp = [code, year, "，".join(leader), change]
                result.append(temp)

        data = pd.DataFrame(result, columns=['证券代码', '年份', '姓名', '是否变化'])
        data.set_index('证券代码', inplace=True)
        data.to_excel(save_path + 'result.xlsx')


if __name__ == '__main__':
    path = 'E:\\【冲鸭】\\【我海】1. 选我就完事儿了\\20201006-高管变更\\'
    dt = BondCouple(path + "hanpi.xlsx")
    dt.init()
    dt.cal_bonds_leader_change()
    dt.generate_result(path)
