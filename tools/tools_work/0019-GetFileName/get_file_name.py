#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: get_file_name.py
@time: 2021/1/27 10:14
@desc: 根据目录获取文件名
"""

from dataclasses import dataclass
import os
import pandas as pd


@dataclass
class GetFileName:
    path: str

    def __post_init__(self):
        ...

    def get_file_names(self, filter=None):
        """获取目标目录中的文件名，包括后缀"""
        files = os.listdir(self.path)
        filter_files = []
        for f in files:
            f_name, f_suffix = os.path.splitext(f)
            if filter is not None:
                if f_suffix == filter or f_suffix == '.' + filter:
                    filter_files.append(f)
            else:
                filter_files.append(f)
        return filter_files

    def save_files_name2excel(self, file_names: list, save_path: str):
        """根据文件名的list存为一个excel"""
        df = pd.DataFrame({'编号': range(1, 1 + len(file_names)), '文件': file_names})
        df.to_excel(save_path, index=False)


if __name__ == '__main__':
    path = r'E:\1-工作\1-工作\20210129-脚本整理\脚本相关'
    gf = GetFileName(path)
    result = gf.get_file_names('jmx')
    gf.save_files_name2excel(result, r'E:\1-工作\1-工作\20210129-脚本整理\test.xlsx')
