#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: leaphd_deal.py
@time: 2022/1/25 11:02
@desc: 通过脚本操作修改leaphd的流程
"""
import requests

from funcs.func3.my_leaphd_template import QuanLiang
from supports.str_funcs import reduce_space


def generate_headers_by_cookies(cookie):
    """通过cookie生成headers"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Origin': 'http://dmpqas.whchem.com',
        'Host': 'dmpqas.whchem.com',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'X-Requested-With': 'XMLHttpRequest'
    }
    return headers


def generate_component_id(my_headers):
    """【创建新流程】获取组件的id"""
    url = 'http://dmpqas.whchem.com/TaskScheduler/idGen/genId.do?idType=T'
    result = requests.get(url, headers=my_headers).json()
    return result.get('id')


def generate_new_precedure_defjson(cookie, schema_table_name, hivesql1, hivesql2):
    """【创建新流程】主体"""

    my_headers = generate_headers_by_cookies(cookie)
    my_component_id_1 = generate_component_id(my_headers)
    my_hivesql_1 = reduce_space(hivesql1)
    my_component_id_2 = generate_component_id(my_headers)
    my_hivesql_2 = reduce_space(hivesql2)
    my_target = schema_table_name
    my_schedule_name = '_'.join(schema_table_name.split('.')).upper()
    ql = QuanLiang()

    return ql.set_values_return_json([my_component_id_1, my_hivesql_1, my_component_id_2, my_hivesql_2,
                        my_target, my_schedule_name])


def replace_myjson(js, aim_dict):
    for k, v in aim_dict.items():
        js = js.replace(k, v)
    return js


def save_hd_taskschedule(cookie, defjson, aim_dict=None):
    """
    保存leaphd的任务
    :param cookie:
    :param defjson:
    :param aim_dict: 是否替换对应的字段，如果字典为None，则不替换
    :return:
    """
    # 进行替换
    if aim_dict:
        defjson = replace_myjson(defjson, aim_dict)

    headers = generate_headers_by_cookies(cookie)

    data = {
        'jsonDef': defjson,
        'isReplace': '',
        'isPublish': 'N'
    }

    a = requests.post('http://dmpqas.whchem.com/TaskScheduler/process/save.do', headers=headers, data=data)
    return a


if __name__ == '__main__':
    with open('my_cookie', 'r', encoding='utf-8') as f:
        my_cookie = f.read()
    with open('my_json', 'r', encoding='utf-8') as g:
        my_json = g.read()

    aim_dict = {
        'ods_fico.': 'ods_fico_s4.',
        'ods_ps.': 'ods_ps_s4.',
        'ods_mm.': 'ods_mm_s4.',
        'O2H': 'HANA2H',
        'ODS_FICO_ORACLE': 'ODS_FICO_HANA',
    }

    save_hd_taskschedule(my_cookie, my_json, aim_dict)
