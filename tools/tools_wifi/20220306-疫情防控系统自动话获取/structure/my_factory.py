#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: my_factory.py
@time: 2022/3/6 8:57
@desc: 我的工厂
"""

from dataclasses import dataclass
import pandas as pd
from structure.my_models import UnRevised, UnVerified


@dataclass
class Factory:
    """所有未修正和未审核的信息，不仅仅是白银河的"""
    # 未验证
    unrevised_list: list or None
    unrevised_num: int or None
    # 未审核
    unverified_list: list or None
    unverified_num: int or None

    def __post_init__(self):
        # 白银河专属未审核和未验证
        self.unrevised, self.unverified = None, None

    def get_unrevised_num_str(self):
        return str(self.unrevised_num)

    def get_unverified_num_str(self):
        return str(self.unverified_num)

    @classmethod
    def new_a_factory(cls):
        return cls(None, None, None, None)

    def set_unrevised(self, unrevised_list, unrevised_num):
        self.unrevised_list = unrevised_list
        self.unrevised_num = unrevised_num

    def set_unverified(self, unverified_list, unverified_num):
        self.unverified_list = unverified_list
        self.unverified_num = unverified_num

    def set_info(self, my_model_class, l, n):
        """初始化类的数据"""
        if my_model_class == UnRevised:
            self.set_unrevised(l, n)
        elif my_model_class == UnVerified:
            self.set_unverified(l, n)
        else:
            raise Exception('出大问题')

    def set_check_list_result(self):
        """检查未验证和未审核中是否有字段列表，获得需要的类列表"""
        self.unrevised = [x for x in self.unrevised_list if x.check_address_if_in_check_list()]
        self.unverified = [x for x in self.unverified_list if x.check_address_if_in_check_list()]

    def output_df(self, my_cls):
        """根据类输出对应的DataFrame"""
        if my_cls == 'r':
            return pd.DataFrame([x.get_values() for x in self.unrevised], columns=UnRevised.get_column_names())
        elif my_cls == 'v':
            return pd.DataFrame([x.get_values() for x in self.unverified], columns=UnVerified.get_column_names())

    def get_aim_name_id_phone(self):
        """获取简单复制需要的信息"""
        result = ''
        for i in self.unrevised:
            result += i.get_name_id_phone() + '\n'

        for j in self.unverified:
            result += j.get_name_id_phone() + '\n'

        return result
