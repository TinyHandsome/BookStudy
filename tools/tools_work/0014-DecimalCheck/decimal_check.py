#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: decimal_check.py
@time: 2020/12/7 10:34
@desc: 检查wor有d文档中，包含关键字的comment对应的是否是decimal
        输出exe文件：pyinstaller -F decimal_check.py -i pic.ico
"""
from dataclasses import dataclass
from word_get import WordInfo
import re
import tkinter as tk
from tkinter.filedialog import askopenfilename


@dataclass
class DecimalCheck:
    file_path: str

    def __post_init__(self):
        self.patten = r"(?:\w+)\s+(?P<type>.*?)(?:\s+)comment\s+(?:')(?P<comment>.*?)(?:'),?"

    @staticmethod
    def check_decimal(type_value, name_value):
        """类型，名称"""
        aim_label = ['值', '税率', '含税', '款', '金额', '费']
        flag_check = False
        for label in aim_label:
            if label in name_value:
                flag_check = True

        flag_decimal = 'decimal' in type_value

        if flag_check:
            # 存在目标字段在comment中
            if not flag_decimal:
                # 但是未使用decimal
                return True

        return False

    def get_sql_attribute(self):
        """获取doc的数据，并检查是否是sql指标行（comment在其中），并进行正则匹配"""
        wi = WordInfo(self.file_path)
        value_list = wi.word_get()

        for value in value_list:
            if ('comment' in value) and not (value.startswith('partitioned by') or value.startswith('create table')):
                sea_result = re.search(self.patten, value)
                if sea_result:
                    # print(value)
                    type_value, name_value = sea_result.group(1), sea_result.group(2)
                    if DecimalCheck.check_decimal(type_value, name_value):
                        print(value)
                    else:
                        pass


def show():
    root = tk.Tk()
    root.title('详设Decimal检查工具v1.0')
    path = tk.StringVar()

    font_temp = ("Microsoft YaHei", 14)

    def choosefile():
        _p = askopenfilename()
        path.set(_p)
        print(path.get())

    def run():
        dc = DecimalCheck(path.get())
        dc.get_sql_attribute()

    l1 = tk.Label(root, text='请选择word文档路径', font=font_temp)
    l1.pack(side='left', expand=True, fill='both')

    e1 = tk.Entry(root, textvariable=path, font=font_temp, width=40)
    e1.pack(side='left', expand=True, fill='both')

    b1 = tk.Button(root, text='选择', command=choosefile, font=font_temp)
    b1.pack(side='left', expand=True, fill='both')

    b2 = tk.Button(root, text='运行', command=run, font=font_temp)
    b2.pack(side='left', expand=True, fill='both')

    root.mainloop()


if __name__ == '__main__':
    # path = r'E:\【冲鸭】\【工作】1. 工作安排、文件存储\20201207-新双周+工程详设（安全生产记录）\万华数据中台(DMP)-PMO-TCK-财务-投资完成-指标详细设计-20201207-V2.5.docx'
    # dc = DecimalCheck(path)
    # dc.get_sql_attribute()
    show()
