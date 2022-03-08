#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: tools.py
@time: 2022/3/7 15:50
@desc: 工具类

        1. rich参考链接：
            1. https://blog.csdn.net/qq_43954124/article/details/112772262
"""
import os
import time

from rich.console import Console
from rich.table import Table

from pandas import DataFrame
from prettytable import PrettyTable
from rich.progress import track
from tqdm import tqdm

from support.cmd_decorate import print_yello_cyan


def get_annotations_keys(cls):
    """获取类的成员变量名"""
    return list(cls.__dict__.get('__annotations__').keys())


def get_dict_values_from_list(my_dict: dict, my_list: list) -> dict:
    """获取字典中 list 变量的所有值"""
    output_dict = {}

    for l in my_list:
        v = my_dict.get(l)
        output_dict[l] = v

    return output_dict


def get_annotations_keys_dict_from_dict(cls, my_dict: dict):
    """根据类的成员变量，从字典中获取对应字段的值，输出为字典，生成这个类"""
    my_list = get_annotations_keys(cls)
    output_dict = get_dict_values_from_list(my_dict, my_list)

    # 生成类
    return cls(**output_dict)


def deal_int_time_13(my_time):
    """将13位数字转为时间"""
    if my_time is None:
        return my_time
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(my_time / 1000))


def get_current_time():
    """获取当前时间的字符串"""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def decorate_dataframe(df: DataFrame, t='prettytable'):
    """美化dataframe的输出"""
    if t == 'prettytable':
        tb = PrettyTable()
        tb.field_names = df.columns
        for row in df.values:
            tb.add_row(row)

    elif t == 'rich':
        tb = Table(show_header=True, header_style="bold magenta")
        console = Console()
        for c in df.columns:
            tb.add_column(c, justify='center', min_width=50)

        for row in df.values:
            tb.add_row(*row)

        console.print(tb)

    else:
        raise Exception('这是啥table style啊')

    return tb


def check_file_exist(file_path, build=True):
    """检查文件是否存在，否则创建该文件（暂时不创建目录）"""
    if not os.path.exists(file_path):
        if build:
            f = open(file_path, 'w', encoding='utf-8')
            f.close()
        return False
    else:
        return True


def get_mytoken():
    """获取本地的token，如果没有就建一个"""
    file_name = 'config/mytoken'
    if check_file_exist(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            bearer = f.read()
        return bearer
    else:
        return ''


def write_mytoken(t):
    """写入mytoken"""
    with open('../config/mytoken', 'w', encoding='utf-8') as f:
        f.write(t)


class MyTimeBar:

    def __init__(self):
        self.status = True

    def stop(self):
        self.status = False

    def my_time_bar(self, scheduler_gap: int, p='rich'):
        """根据时间gap的进度条"""

        if p == 'tqdm':
            kwargs = {'ascii': True}
            my_bar = tqdm
        elif p == 'rich':
            kwargs = {'description': '下次调度倒计时：'}
            my_bar = track
        else:
            raise Exception('没有你想要的bar')

        for i in my_bar(range(scheduler_gap), **kwargs):
            if self.status:
                time.sleep(1)
            else:
                return


def init_print():
    """初始化的时候告诉大家做啥"""
    with open('config/init_print', 'r', encoding='utf-8') as f:
        s = f.read()
    print_yello_cyan(s)
