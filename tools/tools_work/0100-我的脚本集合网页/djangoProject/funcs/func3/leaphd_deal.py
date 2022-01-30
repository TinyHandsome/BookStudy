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


def replace_myjson(js, aim_dict):
    for k, v in aim_dict.items():
        js = js.replace(k, v)
    return js


def save_hd_taskschedule(cookie, defjson, aim_dict):
    # 进行替换
    defjson = replace_myjson(defjson, aim_dict)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Origin': 'http://dmpqas.whchem.com',
        'Host': 'dmpqas.whchem.com',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'X-Requested-With': 'XMLHttpRequest'
    }

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
