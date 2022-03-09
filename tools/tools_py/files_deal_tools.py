#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: functions.py
@time: 2021/2/23 13:43
@desc: 一些文件处理的工具
"""
import os


def get_files_names(files):
    """
    通过文件路径，获取没有后缀的文件名
        1. files:list，返回list
        2. files:str，返回str
    """
    if isinstance(files, str):
        file_name = os.path.basename(files)
        file_name_without_suffix = file_name.split('.')[0]
        return file_name_without_suffix
    elif isinstance(files, (list, tuple)):
        file_name_without_suffixs = []
        for file in files:
            file_name_without_suffixs.append(get_files_names(file))
        return file_name_without_suffixs
    else:
        print(type(files))
        print('咋肥四鸭？')


def check_file_exist(file_path, build=True):
    """检查文件是否存在，否则创建该文件（暂时不创建目录）"""
    if not os.path.exists(file_path):
        if build:
            # 分隔文件夹和文件名
            p, f = os.path.split(file_path)
            # 检查文件夹，没有就创建
            check_filefolder_exist(p)

            # 创建文件，啥也不写
            f = open(file_path, 'w', encoding='utf-8')
            f.close()
        return False
    else:
        return True


def check_filefolder_exist(filefolder, build=True):
    """检查文件夹是否存在，否则创建该目录"""
    if not os.path.exists(filefolder):
        if build:
            os.makedirs(filefolder)
        else:
            ...
        return False
    return True

if __name__ == '__main__':
    x = get_files_names(r'E:\test\gouzei.md')
    print(x)
