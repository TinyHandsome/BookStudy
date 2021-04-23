#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: file_compare.py
@time: 2021/4/23 10:08
@desc: 文件比较，找到相同了之后抄到新文件夹中
"""
import os
import shutil


def get_name(file_name):
    return file_name.split('--')[0], file_name


def file_compare(file_path_old, file_path_new, aim_file_path):
    new_files = [get_name(f) for f in os.listdir(file_path_new)]
    old_files = [get_name(f) for f in os.listdir(file_path_old)]

    for new_file_name, new_file in new_files:
        for old_file_name, old_file in old_files:
            if old_file_name == new_file_name:
                shutil.copy(os.path.join(file_path_old, old_file), os.path.join(aim_file_path, old_file))
                break


if __name__ == '__main__':
    root_path = r'E:\1-工作\3-代码\tools\tools_work\0022-FileCompare\data'
    file_path_old = os.path.join(root_path, 'bpmn-old')
    file_path_new = os.path.join(root_path, 'bpmn-new')
    aim_file_path = os.path.join(root_path, 'output_path')
    file_compare(file_path_old, file_path_new, aim_file_path)
