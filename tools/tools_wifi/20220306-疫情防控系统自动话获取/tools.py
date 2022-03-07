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
"""
import time


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
    if my_time is None:
        return my_time
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(my_time / 1000))