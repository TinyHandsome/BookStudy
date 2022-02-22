#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: file_folder_funcs.py
@time: 2022/2/7 10:25
@desc: 一些关于文件和文件夹的基础函数
"""
import os


def if_path_not_exists_create_path(path):
    """如果文件路径不存在就创建"""
    if not os.path.exists(path):
        os.makedirs(path)
