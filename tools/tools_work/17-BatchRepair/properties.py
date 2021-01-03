#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: properties.py
@time: 2020/12/31 14:51
@desc: 配置文件
"""

# 使用时，除了目标文件夹之外，只能有一个key有value，其他的key的value必须为 None
params = {
    # 目标文件夹
    'path': r'E:\12-工作\1-工作\20201231-批量处理+上线\yt',
    # 需要替换的版本号
    'element_for_replace': None,
    # 需要增加的版本号
    'element_for_increase': None,
    # 需要删除的版本号
    'element_for_delete': 'element2.13.9999'
}
