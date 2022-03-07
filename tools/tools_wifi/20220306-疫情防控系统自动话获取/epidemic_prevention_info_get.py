#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: epidemic_prevention_info_get.py
@time: 2022/3/7 14:31
@desc:  获取疫情信息
"""

import requests
import time
import sched
import pandas as pd
from dataclasses import dataclass

from config_check_list import *
from my_factory import Factory
from my_models import UnRevised, UnVerified
from tools import get_annotations_keys_dict_from_dict

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)


@dataclass
class EpidemicPrevention:
    authorization: str
    scheduler_gap: int = 600

    def __post_init__(self):
        self.run_state = True
        self.current_str = ''
        self.update_authorization(self.authorization)

        # 工厂类初始化一个实例
        self.f = Factory.new_a_factory()

    def update_authorization(self, author):
        """更新请求的headers"""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
            "Authorization": author,
        }

    def clear_after_run(self):
        """运行后需要清空一些变量"""
        self.output = []

    def get_url_json(self, url, cls):
        """
        获得连接中所有的信息
            1. 转化为类的对象
        """
        resp = requests.get(url, headers=self.headers)
        result = resp.json()

        # 获取数据list和num
        rows = result.get('rows')
        try:
            total = int(result.get('total'))
        except:
            total = 0

        my_models = [get_annotations_keys_dict_from_dict(cls, x) for x in rows]
        self.f.set_info(cls, my_models, total)

    def get_info_from_urls(self):
        """根据表头获取两个地址的json数据，返回两个df"""
        # 获取未修正的数据
        self.get_url_json(UNREVISED_URL, UnRevised)
        # 获取未审核的数据
        self.get_url_json(UNVERIFIED_URL, UnVerified)
        # 查找白银河小区的未验证和未审核
        unrevised, unverified = self.f.get_check_list_result()
        # 生成两个DataFrame
        unrevised_df = pd.DataFrame([x.get_values() for x in unrevised], columns=UnRevised.get_column_names())
        unverified_df = pd.DataFrame([x.get_values() for x in unverified], columns=UnVerified.get_column_names())
        return unrevised_df, unverified_df

    def get_num_str(self, df, df_type):
        """根据dataframe获取数量"""
        if df.empty:
            my_str = '0'
            empty = True
        else:
            my_str = str(df.shape[0])
            empty = False

        if df_type == 1:
            my_str += '/' + self.f.get_unrevised_num_str()
            prefix = '未修正'
        else:
            my_str += '/' + self.f.get_unverified_num_str()
            prefix = '未审核'

        print(prefix + ': ' + my_str)
        if not empty:
            print(df)

    def deal_result(self):
        """根据结果处理数据"""
        unrevised_df, unverified_df = self.get_info_from_urls()
        self.get_num_str(unrevised_df, 1)
        self.get_num_str(unverified_df, 2)


if __name__ == '__main__':
    test = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImY0MjVmODQ5LTdhZTctNDQ1Mi04MDFjLTI4ZmRkNzhjOGYwOSJ9.bLS1Y7obdI_K25FvliX-iUJEr78HmxPSVftnOV8mDJZ5bGY5Su7L9vc_aksgf817pgHMnsXOyuLcFBN1QUxGnA'
    ep = EpidemicPrevention(test)
    ep.deal_result()
