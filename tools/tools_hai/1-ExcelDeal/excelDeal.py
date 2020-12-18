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
        打包代码：pyinstaller -w -F -i pic.ico excelDeal.py
"""

import pandas as pd
import tkinter as tk
import threading
from tkinter.filedialog import askopenfilename, askdirectory


def visualize():
    """生成可视化界面"""
    root = tk.Tk()
    root.title('表格合并工具【作者：李英俊小朋友】')
    root.geometry()
    root.resizable(width=False, height=False)

    # gui配置文件
    label_width = 10
    label_height = 1
    entry_width = 50
    button_width = 5
    button_height = 1
    button_height_large = 5

    # 字体设置
    font_title = ("Microsoft YaHei", 14)
    button_font = ("Microsoft YaHei", 14)

    # 实现路径选择功能
    path1_file = tk.StringVar()
    path2_file = tk.StringVar()
    save_file = tk.StringVar()

    # 清空次数
    global flag
    flag = 0

    # 函数区
    def dealExcel(save_path, path1, path2, left, right, way='left'):
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

        try:
            d1 = pd.read_excel(path1, dtype=str)
            d2 = pd.read_excel(path2, dtype=str)

            # 检查左右关键词是否为空
            left_label = (left == [''] or left == ['', '需要匹配的关键词，用空格隔开'])
            right_label = (right == [''] or right == ['', '需要匹配的关键词，用空格隔开'])

            # 如果left和right其中一个为空，识别关键词相同的词
            if left_label or right_label:
                left_columns = d1.columns.tolist()
                right_columns = d2.columns.tolist()

                # 统计共有列名
                common_names = []
                for name in left_columns:
                    if name in right_columns:
                        common_names.append(name)

                left = common_names
                right = common_names

            d = pd.merge(d1, d2, how=way, left_on=left, right_on=right)
            d.to_excel(save_path + '/处理结果.xlsx', index=False)

            write_info('运行完毕！快去看看保存路径下生成的文件吧【处理结果.xlsx】')
        except:
            write_info("检查一下数据或者哪里没填，报错了哦！")

    def select_file1():
        path1_file.set(askopenfilename())
        e1.configure(fg='black')
        write_info('写入文件1成功！')

    def select_file2():
        path2_file.set(askopenfilename())
        e2.configure(fg='black')
        write_info('写入文件2成功！')

    def select_dir():
        save_file.set(askdirectory())
        e3.configure(fg='black')
        write_info('写入保存路径成功！')

    def clear_entry45(event=None):
        # 删除entry4、5中内容
        global flag
        if flag == 0:
            e4.delete(0, "end")
            e5.delete(0, "end")
            e4.configure(fg='black')
            e5.configure(fg='black')
            flag += 1

    def clear_entry6():
        # 删除entry6中内容
        e6.delete(0, "end")

    def run():
        write_info('正在运行中，请耐心等候...（数据量太大会卡哦，不用担心，在运行呢！）')
        try:
            words_1 = e4.get().split(' ')
            words_2 = e5.get().split(' ')
            # dealExcel(save_file.get(), path1_file.get(), path2_file.get(), words_1, words_2)
            thread_it(dealExcel, (save_file.get(), path1_file.get(), path2_file.get(), words_1, words_2))
        except Exception as e:
            # print(e)
            write_info("检查一下数据或者哪里没填，报错了哦！")

    def write_info(info):
        """写入各种反馈信息"""
        e6.configure(fg='red', state='normal')
        e6.delete(0, "end")
        e6.insert(0, info)
        e6.configure(state='readonly')

    def thread_it(func, args):
        """创建多线程任务"""
        try:
            t = threading.Thread(target=func, args=args)
            t.start()
        except Exception:
            write_info("检查一下数据或者哪里没填，报错了哦！")

    l1 = tk.Label(root, text='表格1路径', width=label_width, height=label_height, font=font_title)
    l1.grid(row=0, column=0, sticky='wesn')
    e1 = tk.Entry(root, width=entry_width, textvariable=path1_file, font=font_title)
    e1.insert(tk.END, ' 点击选择选择文件')
    e1.configure(fg='grey')
    e1.grid(row=0, column=1, sticky='wesn')
    b1 = tk.Button(root, text='选择', font=button_font, width=button_width, height=button_height, command=select_file1)
    b1.grid(row=0, column=2, sticky='wesn')

    l2 = tk.Label(root, text='表格2路径', width=label_width, height=label_height, font=font_title)
    l2.grid(row=1, column=0, sticky='wesn')
    e2 = tk.Entry(root, width=entry_width, textvariable=path2_file, font=font_title)
    e2.insert(tk.END, ' 点击选择选择文件')
    e2.configure(fg='grey')
    e2.grid(row=1, column=1, sticky='wesn')
    b2 = tk.Button(root, text='选择', font=button_font, width=button_width, height=button_height, command=select_file2)
    b2.grid(row=1, column=2, sticky='wesn')

    l3 = tk.Label(root, text='保存路径', width=label_width, height=label_height, font=font_title)
    l3.grid(row=2, column=0, sticky='wesn')
    e3 = tk.Entry(root, width=entry_width, textvariable=save_file, font=font_title)
    e3.insert(tk.END, ' 默认路径：文件所在路径')
    e3.configure(fg='grey')
    e3.grid(row=2, column=1, sticky='wesn')
    b3 = tk.Button(root, text='选择', font=button_font, width=button_width, height=button_height, command=select_dir)
    b3.grid(row=2, column=2, sticky='wesn')

    l4 = tk.Label(root, text='表格1关键词', width=label_width, height=label_height, font=font_title)
    l4.grid(row=3, column=0, sticky='wesn')
    e4 = tk.Entry(root, width=entry_width, font=font_title)
    e4.insert(tk.END, ' 需要匹配的关键词，用空格隔开')
    e4.configure(fg='grey')
    e4.bind('<Button-1>', clear_entry45)
    e4.grid(row=3, column=1, sticky='wesn')

    b4 = tk.Button(root, text='运行', font=button_font, width=button_width, height=button_height_large, command=run)
    b4.grid(row=3, column=2, sticky='wesn', rowspan=3)

    l5 = tk.Label(root, text='表格2关键词', width=label_width, height=label_height, font=font_title)
    l5.grid(row=4, column=0, sticky='wesn')
    e5 = tk.Entry(root, width=entry_width, font=font_title)
    e5.insert(tk.END, ' 需要匹配的关键词，用空格隔开')
    e5.configure(fg='grey')
    e5.bind('<Button-1>', clear_entry45)
    e5.grid(row=4, column=1, sticky='wesn')

    e6 = tk.Entry(root, width=entry_width, font=font_title)
    e6.insert(tk.END, '功能：根据两个表的列名完成表的合并（可匹配多列，但要保证关键词数量相同）')
    e6.configure(fg='grey', state='readonly')
    e6.grid(row=5, column=0, sticky='wesn', columnspan=2)

    root.mainloop()


if __name__ == '__main__':
    visualize()
