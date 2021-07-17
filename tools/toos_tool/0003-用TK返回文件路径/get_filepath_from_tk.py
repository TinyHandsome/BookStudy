#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: get_filepath_from_tk.py
@time: 2021/7/17 9:57
@desc: 通过隐藏的tk，可以通过可视化界面获得，文件的路径
"""

from tkinter import Tk

from tkinter.filedialog import askopenfilename
from dataclasses import dataclass


@dataclass
class GetPathByTK:

    def __post_init__(self):
        self.root = Tk()
        self.root.withdraw()

    def get_path(self, formats: list = None):
        if formats is None:
            return askopenfilename()
        else:
            path = askopenfilename()
            for f in formats:
                if path.endswith(f):
                    return path, 1
            return path, -1


if __name__ == '__main__':
    GetPathByTK().get_path()
