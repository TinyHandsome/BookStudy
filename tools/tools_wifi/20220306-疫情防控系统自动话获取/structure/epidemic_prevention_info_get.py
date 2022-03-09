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
import os

import requests
import pandas as pd
import pyperclip

from support.cmd_decorate import print_black_white, print_white_red, print_yello_magenta, print_cyan_null
from config.config import *
from structure.my_factory import Factory
from structure.my_models import UnRevised, UnVerified
from support.my_mail import MyEmail
from support.tools import get_annotations_keys_dict_from_dict, decorate_dataframe, get_current_time, \
    get_mytoken, write_mytoken, generate_str_concat_two_column_excel, save_df2excel, base64_decode_json2dict

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)


class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class EpidemicPrevention:

    def __init__(self):

        self.run_state = True
        self.current_str = ''

        authorization = get_mytoken()
        self.update_authorization(authorization)

        # 工厂类初始化一个实例
        self.f = Factory.new_a_factory()
        # 邮件类的实例
        self.email_flag = DEFAULT_SEND_EMAIL
        # 用户名、密码
        self.my_email = None
        self.email = MyEmail()
        self.init_email()

        # 最终输出结果DataFrame
        self.unrevised_df, self.unverified_df = None, None

    def init_email(self):
        """初始化邮件的配置"""
        with open(MY_EMAIL, 'r', encoding='utf-8') as f:
            s = f.read()
        self.my_email: dict = base64_decode_json2dict(s)
        self.email.login(self.my_email.get('username'), self.my_email.get('imap_smtp'))

        # 设置各种信息
        self.email.set_from('李英俊' + '<' + self.my_email.get('username') + '>')
        self.email.set_to(TO_EMAIL)

    def send_email(self, header_msg, body_msg):
        """发送邮件"""
        if header_msg is None or body_msg is None:
            # 只要没信息，就不发
            return

        self.email.set_subject(header_msg)
        self.email.attach_text_plain(body_msg)
        self.email.send_email(self.my_email.get('username'), TO_EMAIL)

    def change_email_status(self):
        """改变email发送状态"""
        if self.email_flag:
            self.email_flag = False
        else:
            self.email_flag = True

    def update_authorization(self, author):
        """更新请求的headers"""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
            "Authorization": author,
        }

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
        self.f.set_check_list_result()

        # 生成两个DataFrame，注意这个df相关的处理都保留在这个类中
        # 【因为】这个df既需要导出excel，也需要print出结果
        self.unrevised_df = self.f.output_df('r')
        self.unverified_df = self.f.output_df('v')

    def output_df_excel(self):
        """输出结果的excel，根据需求加上额外的列，这个需求在模型中定义"""
        if self.unrevised_df.empty is None or self.unverified_df is None:
            print_yello_magenta('别瞎搞，你还没搞到结果呢...')
            return

        if not self.unrevised_df.empty:
            rdf = generate_str_concat_two_column_excel(self.unrevised_df, UnRevised)
            r_path = os.path.join(OUTPUT_PATH, '【' + get_current_time(remove_colon=True) + '】  未修正.xlsx')
            if save_df2excel(rdf, r_path):
                print_cyan_null('未修正保存成功：' + r_path)

        if not self.unverified_df.empty:
            vdf = generate_str_concat_two_column_excel(self.unverified_df, UnVerified)
            v_path = os.path.join(OUTPUT_PATH, '【' + get_current_time(remove_colon=True) + '】  未审核.xlsx')
            if save_df2excel(vdf, v_path):
                print_cyan_null('未审核保存成功：' + v_path)

    def easy_copy_name_id_phone(self):
        """简单复制[姓名身份证, 电话]"""
        result = self.f.get_aim_name_id_phone()
        pyperclip.copy(result)

    def get_print_from_df_in_dos(self, df, df_type):
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

    def print_and_deal_result(self, if_send_email):
        """获取数据，筛选数据，处理数据，输出dos"""
        # 获取数据，筛选数据，计算最终的输出df
        self.get_info_from_urls()

        r1, r2 = self.get_print_from_df_in_dos(self.unrevised_df, 1)
        v1, v2 = self.get_print_from_df_in_dos(self.unverified_df, 2)

        time_header = '【' + get_current_time() + '】  '
        head_msg = r1 + '  ' + v1
        email_status = '启用' if self.email_flag else '关闭'

        print(time_header, end='')
        print('邮件功能已【' + email_status + '】  ', end='')
        if self.f.unrevised_num + self.f.unverified_num == 0:
            print_black_white(head_msg)
        else:
            print_white_red(head_msg)
        print(r2)
        print(v2)
        print()

        # 发送邮件
        if self.email_flag and if_send_email:
            header_msg = head_msg + time_header
            body_msg = header_msg + '\n' + str(r2) + '\n' + str(v2)
            self.send_email(header_msg, body_msg)

    def reset_input_bearer(self):
        """获取输入的数据，bearer"""
        a = input('Bearer验证已失效，请重新粘贴bearer数据：（如果不知道bearer是啥，请联系李英俊小朋友~）\n')
        self.update_authorization(a)
        write_mytoken(a)

    def setup(self, if_send_email=False):
        """运行主程序"""
        try:
            self.print_and_deal_result(if_send_email)
        except MyException:
            self.reset_input_bearer()
            self.print_and_deal_result(if_send_email)


if __name__ == '__main__':
    test = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjYxYWY0NGEyLTkyOGYtNDlmNy1hZjQ0LTZmNDkzNDRmOGNlNSJ9.eqwDaBr-d09y7Yj8mCh-owXy-514cNOtq5OQm1vp_YhbHxIi8w9Om2oN6U1GrCWipdT6TSNErMd3Te4ghEGOOw'
    ep = EpidemicPrevention()
    ep.setup()
