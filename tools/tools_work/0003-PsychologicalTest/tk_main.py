#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: main.py
@time: 2020/8/15 8:10
@desc: 主程序
将py文件用pyinstaller打包，打包代码：
pyinstaller -Fw tk_main.py -n Hasaki --add-data "res;res" -i="mind.ico"
"""
import threading
import tkinter as tk
from tkinter import messagebox as ms

from Topic import Table, Result
import sys, os


# 生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def get_file(file):
    return resource_path(os.path.join("res", file))


# 字体设置
font_normal = ("Microsoft YaHei", 14)
font_bigger = ("Microsoft YaHei", 17)
# 输入表格
table = Table(get_file("管理团队角色问卷.md"))
table.file2questionnaire()


def clear_text():
    t1.delete(0.0, tk.END)


def write_topic():
    """写入题和选项"""
    text_info = table.show_topic()
    rewrite_text(text_info)

    continue_text("注意：各个选项的分值总和必须为10\n         点击【下一题】或【回车】提交进入下一题\n\n", "tag_1")


def check_grades():
    """检查分数加起来是否为10，并且分数是否合规"""
    sum = 0
    for var in vars:
        input_var = var.get()

        # 如果为空值，则默认为0
        if input_var == '':
            input_var = 0

        try:
            number = int(input_var)
            if not 0 <= number <= 10:
                continue_text("输入数据越界！请输入0-10的分数！")
                continue_text("\n", "tag_1")
                return False
            else:
                sum += number
        except:
            continue_text("输入数据错误！请输入0-10的分数！")
            continue_text("\n", "tag_1")
            return False

    if sum != 10:
        continue_text("输入总和不为10！请修改！")
        continue_text("\n", "tag_1")
        return False
    return True


def get_grades():
    """获取所有分数"""
    grades = []
    for var in vars:
        x = var.get()
        if x == '':
            x = 0
        grades.append(int(x))
    return grades


def show_end():
    """完成答题后的操作"""
    clear_text()
    clear_input()
    rewrite_text("恭喜你，完成了回答！\n你的结果是：\n\n")

    # 发放结果
    r = Result(get_file('管理团队角色问卷（答案排版）.md'))
    r.count_grade(table.answes)

    continue_text("\t" + "\t".join(r.grades_labels) + "\n", "tag_3")
    continue_text("\t" + "\t".join([str(x) for x in r.results]), "tag_3")


def next_topic():
    """下一题"""
    release_be()
    # 先检查现在的输入是否满足要求，如果题目是0则不记录答案
    if check_grades() or table.start_q == 0:
        # 如果题目是0则不记录答案
        if 1 <= table.start_q <= table.get_topics_length():
            table.set_grades(get_grades())

        # 先检查现在题号是否已经达到上限
        if table.start_q < table.get_topics_length():
            table.start_q += 1
            write_topic()
            clear_input()

        else:
            # 检查是否完成，如果完成输出结果
            if ms.askquestion("答完了哦", "是否提交？") == "yes":
                forbid_be()
                show_end()


def last_topic():
    """上一题"""
    # 先检查现在题号是否已经达到下限
    if table.start_q > 1:
        table.start_q -= 1
        write_topic()
        clear_input()


def rewrite_text(info, font_tag="tag_1"):
    """清空text，写入text"""
    clear_text()
    t1.insert("end", info, font_tag)


def continue_text(info, font_tag="tag_2"):
    """追加信息"""
    t1.insert("end", info, font_tag)
    t1.see("end")


def clear_input():
    """将所有输入设置为0"""
    for var in vars:
        var.set(0)


def bind_next_topic(event):
    """监听回车键"""
    next_topic()


def forbid_be(ignore=None):
    """完成后，禁用所有按钮"""

    for e in entry_list + button_list:
        e.config(state="disabled")

    if ignore == 2:
        button_list[ignore - 1].config(state='normal')


def release_be():
    """开启所有按钮"""
    for e in entry_list + button_list:
        e.config(state="normal")


root = tk.Tk()
root.title("性格测试小工具v0.1" + "【作者：李英俊小朋友】")
root.geometry("700x600+300+100")
# root.resizable(width=False, height=False)
root.resizable(width=True, height=True)

# 变量设置
vars = []
for i in range(10):
    vars.append(tk.StringVar())

f1 = tk.Frame(root)

l1 = tk.Label(f1, text=table.theme, font=("Microsoft YaHei", 20))
l1.pack(side="top", fill="both")

t1 = tk.Text(f1, height=30, width=100)
scroll = tk.Scrollbar(f1)
scroll.pack(side="right", fill="y")
# 将滚动条与文本框关联
# 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
scroll.config(command=t1.yview)
# 将滚动条关联到文本框
t1.config(yscrollcommand=scroll.set)

t1.tag_config("tag_1", font=font_normal)
t1.tag_config("tag_2", backgroun="yellow", foreground="red", font=font_normal)
t1.tag_config("tag_3", font=font_bigger, foreground="red")

# 写入初始信息
rewrite_text(table.show_theme_statement(), "tag_1")
continue_text("\n——>点击【下一题】或【回车】开始答题\n\n", "tag_1")
continue_text("\n\n\n\n\n\n\n\n如有任何问题/bug，请联系作者：李英俊小朋友", "tag_1")

t1.pack(side="top", fill="both", expand=True)

f1.pack(side="top", fill="both", expand=True)

f2 = tk.Frame(root)
f3 = tk.Frame(root)
# 生成10个框
label_list = []
entry_list = []
button_list = []
texts = "ABCDEFGHIJ"
for i in range(10):
    label_temp = tk.Label(f2, text=texts[i], font=font_bigger, width=2)

    entry_temp = tk.Entry(
        f2,
        justify=tk.CENTER,
        width=5,
        font=font_bigger,
        textvariable=vars[i],
        highlightcolor='red',
        highlightthickness=1,
        # validate="focusout",
        # validatecommand=
    )

    # entry_temp.bind("<Button-1>", lambda x : thread_it(func=lambda : entry_temp.delete(0, "end"), args=[]))

    vars[i].set(0)
    if i < 5:
        label_temp.grid(row=0, column=2 * i, sticky='wesn')
        entry_temp.grid(row=0, column=2 * i + 1, sticky='wesn')
    else:
        label_temp.grid(row=1, column=2 * (i - 5), sticky='wesn')
        entry_temp.grid(row=1, column=2 * (i - 5) + 1, sticky='wesn')
    label_list.append(label_temp)
    entry_list.append(entry_temp)

b1 = tk.Button(f2, text='上一题', font=font_bigger, command=last_topic)
b1.grid(row=0, column=10, sticky='wesn')
b2 = tk.Button(f2, text='下一题', font=font_bigger, command=next_topic)
b2.grid(row=1, column=10, sticky='wesn')
b3 = tk.Button(f3, text='  分数  \n  清零  ', font=font_bigger, command=clear_input)
b3.pack(side="left", anchor='sw', fill="both", expand=True)
button_list = [b1, b2, b3]

# 设置初始信息模块不可编辑
forbid_be(2)

# 全局相应事件
b3.bind_all("<Return>", bind_next_topic)

# lambda解决方法：https://www.jianshu.com/p/84f3e0f4d218
for i in range(len(entry_list)):
    entry_list[i].bind("<Button-1>", lambda x, i=i: entry_list[i].delete(0, "end"))

f2.pack(side="left", anchor='sw')
f3.pack(side="right", anchor='se', fill="both", expand=True)

root.mainloop()
