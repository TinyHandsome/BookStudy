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
import pandas as pd
from dataclasses import dataclass

from support.cmd_decorate import print_black_white, print_white_red
from config.config import *
from structure.my_factory import Factory
from structure.my_models import UnRevised, UnVerified
from support.tools import get_annotations_keys_dict_from_dict, decorate_dataframe, get_current_time, \
    get_mytoken, write_mytoken

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)


class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


@dataclass
class EpidemicPrevention:

    def __post_init__(self):

        self.run_state = True
        self.current_str = ''

        authorization = get_mytoken()
        self.update_authorization(authorization)

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

        if result.get('code') == 401:
            raise MyException("401")

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
        """格式化输出最终结果"""
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

        output1 = prefix + ': ' + my_str
        if not empty:
            output2 = decorate_dataframe(df)
        else:
            output2 = ''

        return output1, output2

    def deal_result(self):
        """根据结果处理数据"""
        unrevised_df, unverified_df = self.get_info_from_urls()
        r1, r2 = self.get_num_str(unrevised_df, 1)
        v1, v2 = self.get_num_str(unverified_df, 2)

        print('【' + get_current_time() + '】  ', end='')
        head_msg = r1 + '  ' + v1
        if self.f.unrevised_num + self.f.unverified_num == 0:
            print_black_white(head_msg)
        else:
            print_white_red(head_msg)
        print(r2)
        print(v2)
        print()

    def reset_input_bearer(self):
        """获取输入的数据，bearer"""
        a = input('Bearer验证已失效，请重新粘贴bearer数据：（如果不知道bearer是啥，请联系李英俊小朋友~）\n')
        self.update_authorization(a)
        write_mytoken(a)

    def setup(self):
        """运行主程序"""
        try:
            self.deal_result()
        except MyException:
            self.reset_input_bearer()
            self.deal_result()


if __name__ == '__main__':
    test = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjYxYWY0NGEyLTkyOGYtNDlmNy1hZjQ0LTZmNDkzNDRmOGNlNSJ9.eqwDaBr-d09y7Yj8mCh-owXy-514cNOtq5OQm1vp_YhbHxIi8w9Om2oN6U1GrCWipdT6TSNErMd3Te4ghEGOOw'
    ep = EpidemicPrevention()
    ep.setup()
