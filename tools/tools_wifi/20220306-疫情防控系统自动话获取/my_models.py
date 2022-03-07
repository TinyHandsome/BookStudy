#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: my_models.py
@time: 2022/3/6 7:55
@desc: 建立模型
"""
from dataclasses import dataclass

from config_check_list import CHECK_LIST
from tools import deal_int_time_13


class MyModel:

    def get_address(self):
        """返回地址"""
        return self.address

    def check_address_if_in_check_list(self):
        """检查地址是否在检查列表中"""
        for cl in CHECK_LIST:
            if cl in self.address:
                return True

        return False

    def get_values(self):
        """返回所有成员变量的值"""
        return list(self.__dict__.values())


@dataclass
class UnRevised(MyModel):
    """未修正"""
    # 姓名
    name: str
    # 身份证号/护照
    cardId: str
    # 联系方式
    phone: str
    # 抵烟时间
    arriveTime: int
    # 来源地省市县区
    comeProvinceCityCounty: str
    # 现居住地址
    address: str
    # 来烟方式
    comeMode: str
    # 公安推送来源地区
    comeAreaFull: str
    # 数据来源
    dataFrom: str

    def __post_init__(self):
        self.arriveTime = deal_int_time_13(self.arriveTime)

    @staticmethod
    def get_column_names() -> list:
        return ['姓名', '身份证号/护照', '联系方式', '抵烟时间', '来源地省市县区', '现居住地址', '来烟方式', '公安推送来源地区', '数据来源']


@dataclass
class UnVerified(MyModel):
    """未审核"""
    # 姓名
    name: str
    # 身份证号/护照
    cardId: str
    # 联系方式
    phone: str
    # 来源地区
    comeAreaFull: str
    # 目的地
    address: str
    # 离开风险区域时间
    leaveTheRiskAreaTime: int
    # 抵烟时间
    arriveTime: int

    def __post_init__(self):
        self.leaveTheRiskAreaTime = deal_int_time_13(self.leaveTheRiskAreaTime)
        self.arriveTime = deal_int_time_13(self.arriveTime)

    @staticmethod
    def get_column_names() -> list:
        return ['姓名', '身份证号/护照', '联系方式', '来源地区', '目的地', '离开风险区域时间', '抵烟时间']


if __name__ == '__main__':
    x = UnVerified(1, 1, 1, 1, 1, 1, 1)
    print(x.__dict__)
