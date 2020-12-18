#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: excelDeal.py
@time: 2020/3/25 12:52
@desc: 处理两个表，根据关键词进行左连接。关键词可能有两个或者一个，不填写关键词可自动识别两个表相同的列名进行合并
        打包代码：pyinstaller -w -F -i pic.ico excelDeal_v1.0.py

        【20200423更新】 重构代码  v1.2
        1. 重构代码写成类的形式
        2. 如果没有写保存路径，以表1的路径作为保存路径
        3. 根据两个表共有的列名，自动填充到输入栏中
        4. 新增了一部分提示信息，修改了部分提示信息的内容和颜色
        【20200421更新】 增加报错信息，修改信息颜色  v1.1
        【20200325更新】 增加内连接和左外连接的选择  v1.0
        1. 修改页面布局
        2. 增加连接方法的选择

"""

import pandas as pd
import tkinter as tk
import threading
import traceback
import os
from tkinter.filedialog import askopenfilename, askdirectory


class ExcelDeal:

    def __init__(self):
        """生成可视化界面，管理各个属性"""

        # gui配置文件
        label_width = 10
        label_height = 1
        entry_width = 50
        button_width = 5
        button_height = None
        button_height_large = None
        ratio_height = 2

        # 字体设置
        font_title = ("Microsoft YaHei", 14)
        button_font = ("Microsoft YaHei", 14)
        ratio_font = ("Microsoft YaHei", 8)

        # 相关业务数据
        # 表1、表2的DataFrame
        self.d1 = None
        self.d2 = None
        # 表1表2相同的字段
        self.common = None

        # 各个布局的定义
        self.root = tk.Tk()

        # 实现路径选择功能
        self.path1_file = tk.StringVar()
        self.path2_file = tk.StringVar()
        self.save_file = tk.StringVar()

        # 单选框的值
        self.var_ratio = tk.StringVar()
        # 清空次数
        self.flag = 0
        # 注意同一组的需要互斥选中的需要设置variable属性为同一个
        # 单选框样式 flat/sunken/raised/groove/ridge
        style = None
        # 单选框点击背景色
        bc = None

        self.l1 = tk.Label(self.root, text='表格1路径', width=label_width, height=label_height, font=font_title)
        self.e1 = tk.Entry(self.root, width=entry_width, textvariable=self.path1_file, font=font_title)
        self.b1 = tk.Button(self.root, text='选择', font=button_font, width=button_width, height=button_height,
                            command=self.select_file1)

        self.l2 = tk.Label(self.root, text='表格2路径', width=label_width, height=label_height, font=font_title)
        self.e2 = tk.Entry(self.root, width=entry_width, textvariable=self.path2_file, font=font_title)
        self.b2 = tk.Button(self.root, text='选择', font=button_font, width=button_width, height=button_height,
                            command=self.select_file2)

        self.l3 = tk.Label(self.root, text='保存路径', width=label_width, height=label_height, font=font_title)
        self.e3 = tk.Entry(self.root, width=entry_width, textvariable=self.save_file, font=font_title)
        self.b3 = tk.Button(self.root, text='选择', font=button_font, width=button_width, height=button_height,
                            command=self.select_dir)

        self.l4 = tk.Label(self.root, text='表格1关键词', width=label_width, height=label_height, font=font_title)
        self.e4 = tk.Entry(self.root, width=entry_width, font=font_title)
        self.b4 = tk.Button(self.root, text='运行', font=button_font, width=button_width, height=button_height_large,
                            command=self.run_func)

        self.l5 = tk.Label(self.root, text='表格2关键词', width=label_width, height=label_height, font=font_title)
        self.e5 = tk.Entry(self.root, width=entry_width, font=font_title)
        self.e6 = tk.Entry(self.root, width=entry_width, font=font_title)

        self.r1 = tk.Radiobutton(self.root, text='左连接', value='left', height=ratio_height, variable=self.var_ratio,
                                 font=ratio_font,
                                 relief=style, activebackground=bc)
        self.r2 = tk.Radiobutton(self.root, text='内连接', value='inner', height=ratio_height, variable=self.var_ratio,
                                 font=ratio_font,
                                 relief=style, activebackground=bc)

    def init_grids(self):
        """实现布局管理"""

        self.root.title('表格合并工具v1.2【作者：李英俊小朋友】')
        self.root.geometry()
        self.root.resizable(width=False, height=False)

        self.l1.grid(row=0, column=0, sticky='wesn')
        self.e1.insert(tk.END, ' 点击选择目标文件')
        self.e1.configure(fg='grey')
        self.e1.grid(row=0, column=1, sticky='wesn')
        self.b1.grid(row=0, column=2, sticky='wesn')

        self.l2.grid(row=1, column=0, sticky='wesn')
        self.e2.insert(tk.END, ' 点击选择目标文件')
        self.e2.configure(fg='grey')
        self.e2.grid(row=1, column=1, sticky='wesn')
        self.b2.grid(row=1, column=2, sticky='wesn')

        self.l3.grid(row=2, column=0, sticky='wesn')
        self.e3.insert(tk.END, ' 点击选择保存路径（默认为表1的路径）')
        self.e3.configure(fg='grey')
        self.e3.grid(row=2, column=1, sticky='wesn')
        self.b3.grid(row=2, column=2, sticky='wesn')

        self.l4.grid(row=3, column=0, sticky='wesn')
        self.e4.insert(tk.END, ' 需要匹配的关键词，用空格隔开（默认两表的相同字段）')
        self.e4.configure(fg='grey')
        self.e4.bind('<Button-1>', self.clear_entry45)
        self.e4.grid(row=3, column=1, sticky='wesn')
        self.b4.grid(row=5, column=2, sticky='wesn')

        self.l5.grid(row=4, column=0, sticky='wesn')
        self.e5.insert(tk.END, ' 需要匹配的关键词，用空格隔开（默认两表的相同字段）')
        self.e5.configure(fg='grey')
        self.e5.bind('<Button-1>', self.clear_entry45)
        self.e5.grid(row=4, column=1, sticky='wesn')

        self.e6.insert(tk.END, '功能：根据两个表的列名完成表的合并（可匹配多列，但要保证关键词数量相同）')
        self.e6.configure(fg='grey', state='readonly')
        self.e6.grid(row=5, column=0, sticky='wesn', columnspan=2)

        self.r1.grid(row=3, column=2, sticky='wesn')
        self.r2.grid(row=4, column=2, sticky='wesn')

        # 设置单选默认值
        self.var_ratio.set('left')

        self.root.mainloop()

    def select_file1(self):
        self.path1_file.set(askopenfilename())
        self.e1.configure(fg='black')
        self.write_info('写入文件1成功！（默认保存路径获取！）', 'green')
        table1_path = os.path.dirname(self.path1_file.get())
        self.save_file.set(table1_path)

    def select_file2(self):
        self.path2_file.set(askopenfilename())
        self.e2.configure(fg='black')

        # 文件2导入成功后自动进行识别
        self.run_read()

    def e_write(self, e, info, color=False):
        """写入"""
        e.delete(0, "end")
        if color:
            e.configure(fg=color)
        e.insert(0, info)

    def select_dir(self):
        self.save_file.set(askdirectory())
        self.e3.configure(fg='black')
        self.write_info('写入保存路径成功！', 'green')

    def clear_entry45(self, event=None):
        # 第一次单击后，删除entry4、5中内容
        if self.flag == 0:
            self.e4.delete(0, "end")
            self.e5.delete(0, "end")
            self.e4.configure(fg='black')
            self.e5.configure(fg='black')
            self.flag += 1

    def write_info(self, info, fg='red'):
        """写入各种反馈信息"""
        self.e6.configure(fg=fg, state='normal')
        self.e6.delete(0, "end")
        self.e6.insert(0, info)
        self.e6.configure(state='readonly')

    def thread_it(self, func, args):
        """创建多线程任务"""
        try:
            t = threading.Thread(target=func, args=args)
            t.start()
            # t.join()
        except Exception as e:
            self.write_info("【报错啦！】创建线程报错，但你不能解决，联系李英俊吧！")

    def run_read(self):
        self.write_info('正在识别列名中，请耐心等候...', 'green')
        self.thread_it(self.recognieze_keywords, (self.path1_file.get(), self.path2_file.get()))

    def run_func(self):
        self.write_info('正在运行中，请耐心等候...（数据量太大会卡哦，不用担心，在运行呢！）', 'green')
        words_1 = self.e4.get().split(' ')
        words_2 = self.e5.get().split(' ')
        self.thread_it(self.dealExcel,
                       (self.save_file.get(), self.path1_file.get(), self.path2_file.get(), words_1, words_2,
                        self.var_ratio.get()))

    def run(self):
        self.init_grids()

    def recognieze_keywords(self, path1, path2):
        """识别关键词相同的词"""
        try:
            self.d1 = pd.read_excel(path1, dtype=str)
            self.d2 = pd.read_excel(path2, dtype=str)

            left_columns = self.d1.columns.tolist()
            right_columns = self.d2.columns.tolist()

            # 统计共有列名
            common_names = []
            for name in left_columns:
                if name in right_columns:
                    common_names.append(name)

            self.common = common_names

            # 测试特征自动匹配的情况
            # print(left_columns, ',', right_columns)
            # print(self.common)

            # 识别后写入
            if common_names:
                # 识别成功
                self.e_write(self.e4, " ".join(common_names))
                self.e_write(self.e5, " ".join(common_names))
                self.write_info('写入文件2成功！已成功识别共有列名！请点击运行！', 'green')
            else:
                self.write_info('写入文件2成功！但，未能识别共有列名！请手动输入列名', 'red')
                self.e_write(self.e4, "请输入表1的匹配列名（空格隔开）", 'red')
                self.e_write(self.e5, "请输入表2的匹配列名（空格隔开）", 'red')
            return 1

        except Exception as e:
            self.write_info("【报错啦！】读取表出错！你真的输入的是表嘛？")
            # print(e.args[0])
            return -3

    def dealExcel(self, save_path, path1, path2, left, right, way):
        """
        处理两个Excel，返回结果
        :param save_path: 保存路径
        :param path1: 左表路径
        :param path2: 右表路径
        :param left: 左表关键词
        :param right: 右表关键词
        :param way: 连接方式，默认为左外连接
        :return:
        """

        # 检查文件名是否有处理结果
        p1_name = os.path.basename(path1)
        p2_name = os.path.basename(path2)
        if p1_name == '处理结果.xlsx' or p2_name == '处理结果.xlsx':
            self.write_info('【报错啦！】文件名不能叫处理结果哦！')
            return -1

        try:
            # 检查左右关键词是否为空
            left_label = (left == [''] or left == ['', '需要匹配的关键词，用空格隔开'])
            right_label = (right == [''] or right == ['', '需要匹配的关键词，用空格隔开'])

            # 如果left和right其中一个为空，识别关键词相同的词
            if left_label or right_label:
                left, right = self.common, self.common

            d = pd.merge(self.d1, self.d2, how=way, left_on=left, right_on=right)
            d.to_excel(save_path + '/处理结果.xlsx', index=False)

            self.write_info('【运行完毕！】快去看看保存路径下生成的文件吧：处理结果.xlsx', fg='green')
            return 1
        except Exception as e:
            self.write_info("【报错啦！】merge过程出错！这要联系李英俊才可以解决哦！")
            # print(e.args[0])
            return -2


if __name__ == '__main__':
    ExcelDeal().run()
