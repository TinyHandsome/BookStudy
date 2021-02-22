#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: get_url.py
@time: 2021/2/22 9:52
@desc: 根据url和传入的参数获取数据
"""
import requests
import json


def post_url(url, headers, data):
    return requests.post(url, headers=headers, data=data).json()


def transform_form_data_json(form_data):
    """将form_data的&转为json"""

    def split_equal(temp):
        """将等号两边的制作成字典"""
        temp_list = temp.split('=')
        if len(temp_list) == 2:
            return temp_list[0], temp_list[1]
        elif len(temp_list) == 1:
            return temp_list[0], ''
        else:
            print('【注意】结果有问题：', temp_list)

    forms = form_data.split('&')
    result = {}

    for f in forms:
        key, value = split_equal(f)
        result[key] = value

    return result


if __name__ == '__main__':
    root_path = 'http://dmp.whchem.com/TaskScheduler/process/'
    aim_path = root_path + 'searchProcess.do'

    headers = {
        'Referer': 'http://dmp.whchem.com/TaskScheduler/views/process_run_list.jsp;jsessionid=4r1iydzd540qydkrhhr78c9i?click=prl_prl1',
    }

    cookies = {}

