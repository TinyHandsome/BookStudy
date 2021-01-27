#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: ArticleSeperate.py
@time: 2019/11/29 9:36
@desc: 根据章节名把文章分成两部分，根目录下有个end.md：为文章末尾的模板，第1章以前的部分为文章开头模板
       因此具体作用为：把中间部分分为两段，每段都要加上开头和末尾模板，从而生成新的文件
        【20200319】 增加界面
        【20191129】 初始版本
"""
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory


def article_seperate(chaper_name, file_path, save_path):
    """
    根据章节名把文章分成两部分
    :param formate: 文件格式，默认md
    :param chaper_name: 章节名（+#的）
    :param save_path: 分开后文章的保存路径
    :param file_path: 需要处理的文件名
    """

    end = "./end.md"
    with open(end, "rb") as f:
        end_article = f.readlines()

    file_root, tempfilename = os.path.split(file_path)
    file_name, extension = os.path.splitext(tempfilename)
    path1 = save_path + file_name + "_1_2" + extension
    path2 = save_path + file_name + "_2_2" + extension
    w1 = open(path1, "wb")
    w2 = open(path2, "wb")

    flag = True
    x = None
    start_label = "第1章"
    start = b''
    start_flag = True
    with open(file_path, "rb") as f:
        while b'' != x:
            x = f.readline()

            if start_label in bytes.decode(x):
                start_flag = False
            if start_flag:
                start += x

            if chaper_name in bytes.decode(x):
                flag = False
                w1.writelines(end_article)
                w1.close()
                w2.write(start)

            if flag:
                w1.write(x)
            if not flag:
                w2.write(x)

        w2.close()
    w1.close()


def graph():
    root = tk.Tk()
    root.title('文章切分工具【作者：李英俊小朋友】')
    root.geometry()
    root.resizable(width=False, height=False)

    font_title = ("Microsoft YaHei", 14)

    # 实现路径选择功能
    path_file = tk.StringVar()
    save_file = tk.StringVar()

    def select_file():
        path_file.set(askopenfilename())
        global whole_path
        whole_path = path_file.get()
        file_path, file_name = os.path.split(whole_path)
        global default_savepath
        default_savepath = file_path + '/'
        e1.configure(fg='black')

    def select_dir():
        save_file.set(askdirectory())
        global default_savepath
        default_savepath = save_file.get() + '/'
        e2.configure(fg='black')

    def run():
        word = e3.get()
        try:
            article_seperate(word, whole_path, default_savepath)
            e3.delete(0, tk.END)
            e3.insert(0, ' 运行完毕！')
        except Exception:
            print('请输入正确的关键词！')

    def clear(event=None):
        # 删除entry3中内容
        e3.delete(0, "end")
        e3.configure(fg='black')

    l1 = tk.Label(root, text='文件路径', font=font_title)
    l1.grid(row=0, column=0, sticky='wesn')
    e1 = tk.Entry(root, width=50, textvariable=path_file, font=font_title)
    e1.insert(tk.END, ' 点击选择选择文件')
    e1.configure(fg='grey')
    e1.grid(row=0, column=1, sticky='wesn')
    b1 = tk.Button(root, text='选择', font=font_title, width=5, command=select_file)
    b1.grid(row=0, column=2, sticky='wesn')

    l2 = tk.Label(root, text='保存路径', font=font_title)
    l2.grid(row=1, column=0, sticky='wesn')
    e2 = tk.Entry(root, width=50, textvariable=save_file, font=font_title)
    e2.insert(tk.END, ' 默认路径：文件所在路径')
    e2.configure(fg='grey')
    e2.grid(row=1, column=1, sticky='wesn')
    b2 = tk.Button(root, text='选择', font=font_title, width=5, command=select_dir)
    b2.grid(row=1, column=2, sticky='wesn')

    l3 = tk.Label(root, text='切分关键词', width=10, font=font_title)
    l3.grid(row=2, column=0, sticky='wesn')
    e3 = tk.Entry(root, width=50, font=font_title)
    e3.insert(tk.END, ' 需要切分的章节名：如“第四章”')
    e3.configure(fg='grey')
    e3.bind('<Button-1>', clear)
    e3.grid(row=2, column=1, sticky='wesn')
    b3 = tk.Button(root, text='运行', font=font_title, width=5, command=run)
    b3.grid(row=2, column=2, sticky='wesn')

    root.mainloop()


if __name__ == '__main__':
    graph()
