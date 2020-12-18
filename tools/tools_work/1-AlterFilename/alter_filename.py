#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: alter_filename.py
@time: 2019/10/5 15:25
@desc: 【小工具】批量修改文件夹下所有文件的文件名后缀
        注意：记得保留源文件，该工具是直接对源文件重命名。
"""

import os
import tkinter as tk
from tkinter.filedialog import askdirectory


def alter_suffix(old_suffix, new_suffix, filefold_path, is_deep=False):
    """
    修改文件后缀名
    :param old_suffix:旧后缀名
    :param new_suffix:新后缀名
    :param filefold_path:文件路径
    :param is_deep:是否遍历子文件夹
    """

    # 操作文件计数
    count = 0

    # 如果文件夹中还有文件夹，遍历所有文件夹
    if is_deep:
        names = []
        for root, dirs, files in os.walk(filefold_path):
            for file in files:
                names.append(os.path.join(root, file))
    else:
        names = os.listdir(filefold_path)
        names = [os.path.join(filefold_path, name) for name in names if
                 os.path.isfile(os.path.join(filefold_path, name))]

    for file_name in names:
        x = os.path.splitext(file_name)
        name = x[0]
        suffix = x[1]
        if suffix == old_suffix:
            os.rename(file_name, name + new_suffix)
            count += 1

    print('总共对', count, '个文件进行了重命名...')


def show(old_suffix, new_suffix):
    root = tk.Tk()
    root.title('批量修改文件夹下所有文件的文件名后缀')
    # 防止用户调整尺寸
    root.resizable(0, 0)

    # 参数区
    checkVar1 = tk.IntVar()
    path = tk.StringVar()

    def selectPath():
        path_ = askdirectory()
        path.set(path_)

    def run():
        try:
            alter_suffix(old_suffix, new_suffix, path.get(), checkVar1.get())
        except FileNotFoundError:
            print("你倒是输入正确的路径啊！")
        except Exception:
            print("哇哦！报错了！联系李英俊解决一下吧！")

    button0 = tk.Button(root, text="文件路径", command=selectPath).grid(row=0, column=0, sticky=tk.W + tk.E)
    entry1 = tk.Entry(root, width=30, textvariable=path).grid(row=0, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
    checkbutton1 = tk.Checkbutton(
        root,
        text="是否深层遍历",
        variable=checkVar1,     # 选定或不选定存放在variable这个变量里面。
        onvalue=True,           # 如果选定了，那么checkVar的值就是True
        offvalue=False,         # 如果没有选定，那checkVar的值就是False
    ).grid(row=0, column=2, sticky=tk.W + tk.E)
    button1 = tk.Button(root, text="运行", command=run).grid(row=0, column=3, sticky=tk.W + tk.E)

    root.mainloop()


if __name__ == '__main__':
    show('.txt', '.html')
    # file_path = 'C:/Users/Administrator/Desktop/test/'
    # alter_suffix('.txt', '.html', file_path, is_deep=True)
