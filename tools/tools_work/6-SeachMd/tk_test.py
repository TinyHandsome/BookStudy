#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: tk_test.py
@time: 2020/8/28 10:30
@desc: 可视化界面
"""

import os
import tkinter as tk
from abc import abstractmethod
from tkinter.filedialog import askdirectory

from searchMD import SearchMD, Result


class MyTag:
    def __init__(self, tags_count, start, end, content):
        self.tags_count = tags_count
        self.start = start
        self.end = end
        self.content = content
        self.temp_tag_name = None

    def get_add(self):
        return self.temp_tag_name, self.start, self.end

    def get_name(self):
        return self.temp_tag_name

    @abstractmethod
    def get_configure(self): pass


class HangTag(MyTag):
    def __init__(self, tags_count, start, end, content):
        super().__init__(tags_count, start, end, content)
        self.temp_tag_name = "temp_hang_" + str(self.tags_count)

    def get_configure(self):
        return dict(tagName=self.get_name(), foreground="red", underline=False)


class LinkTag(MyTag):
    def __init__(self, tags_count, start, end, link, content):
        super().__init__(tags_count, start, end, content)
        self.temp_tag_name = "temp_link_" + str(self.tags_count)
        self.link = link

    def get_configure(self):
        return dict(tagName=self.get_name(), foreground="blue", underline=True)


class Visualize:
    def __init__(self):
        # 粗体：bold
        # 斜体：italic
        # 下划线：underline
        # 删除线：overstrike
        self.font_normal = ("Microsoft YaHei", 20)
        self.font_text = ("Microsoft YaHei", 14)

        self.tags = []
        self.tags_count = 0

        # 全局组件
        self.root = tk.Tk()
        self.t = None
        self.e1 = None

        # 全局组件内容
        self.path = tk.StringVar()
        self.key_words = tk.StringVar()

        self.current_link = None

    def get_path(self):
        p = askdirectory()
        self.path.set(p)
        self.e1.config(fg='black')

    def clear_text(self):
        self.t.delete('1.0', 'end')
        # 删除tags
        self.tags = []

    def run(self):
        self.clear_text()

        md = SearchMD(self.path.get(), self.key_words.get())
        md.findMdFile(is_print=False)
        aim_results = md.aim_results

        if aim_results:
            for result in aim_results:
                self.show_text(result)

            # 给链接上色
            self.colored_text()
            # 增加链接和鼠标样式
            self.link_text()

        else:
            self.show_text("没有查到哦！")

    def colored_text(self):
        """给超链接上色"""
        for temp_tag in self.tags:
            self.t.tag_add(*temp_tag.get_add())
            self.t.tag_config(**temp_tag.get_configure())

    def link_text(self):
        """给超链接添加链接和鼠标样式"""
        for tag in self.tags:
            try:
                self.current_link = tag.link
                # 鼠标指向
                self.t.tag_bind(tag.temp_tag_name, '<Enter>', lambda event: self.t.config(cursor='hand2'))
                # 鼠标离开
                self.t.tag_bind(tag.temp_tag_name, '<Leave>', lambda event: self.t.config(cursor='xterm'))
                # 左键点击
                self.t.tag_bind(tag.temp_tag_name, '<Button-1>', lambda event, link=tag.link: os.startfile(link))
            except:
                pass

    def show_text(self, info):
        """根据x和y的值插入数据"""
        if type(info) == Result:
            # 获取光标位置
            t_index = self.t.index('insert')
            # 获取关键字
            key_words = self.key_words.get()

            # 获取【链接】开始位置
            start, end, link = info.get_link_location(t_index)

            # 获取【行】开始位置
            t_index = str(float(t_index) + 1)
            hang_locs = info.get_key_words_locations(key_words, t_index)

            # 将上色和超链接的结果保存起来，最后再渲染
            temp_tag = LinkTag(self.tags_count, start, end, link, info.line_info)
            self.tags_count += 1
            self.tags.append(temp_tag)

            # 保存内容tag
            for hangl in hang_locs:
                temp_tag = HangTag(self.tags_count, hangl[0], hangl[1], info.line_info)
                self.tags_count += 1
                self.tags.append(temp_tag)

            # 插入链接
            self.t.insert('end', info.number_file_path + '\n')
            # 插入查询结果，去除了查找内容的前后空格，并增加了新的回车
            self.t.insert('end', info.line_play + '\n', "tag_bold")
            self.t.insert('end', info.more_play + '\n')

        else:
            self.t.insert('end', info + '\n')

    # 全局相应事件
    def bind_return(self, event):
        """监听回车键"""
        self.run()

    def tk_show(self):

        self.root.title("MarkDown文件内容查询工具")
        self.root.geometry("800x600+300+100")
        self.root.resizable(width=False, height=False)

        # 要将窗口变成ToolWindow Style
        # self.root.attributes("-toolwindow", 1)

        # 要将窗口设为置顶窗口
        # self.root.attributes("-topmost", 1)

        # 要在启动时最大化，可以调用TK.state("zoomed")。要最小化可以调用TK.iconify方法。要还原最小化可以调用TK.deiconify方法。

        default_path = 'E:\\【冲鸭】\\【工作】2. 工作记录、笔记和总结'
        self.path.set(default_path)

        f1 = tk.Frame(self.root)
        l1 = tk.Label(f1, text='路径', font=self.font_normal,
                      width=6, takefocus=False)
        l1.pack(fill='both', side='left')
        self.e1 = tk.Entry(f1, textvariable=self.path,
                           font=self.font_normal, width=38, takefocus=False)
        self.e1.config(fg='grey')
        self.e1.pack(fill='both', side='left')
        b1 = tk.Button(f1, text='选择', font=self.font_normal,
                       width=4, command=self.get_path, takefocus=False)
        b1.pack(fill='both', side='left', expand='yes')
        f1.pack(fill='x', expand='no', side='top')

        f2 = tk.Frame(self.root)
        l2 = tk.Label(f2, text='关键词', font=self.font_normal,
                      width=6, takefocus=False)
        l2.pack(fill='both', side='left')
        e2 = tk.Entry(f2, font=self.font_normal,
                      textvariable=self.key_words, width=38)
        e2.pack(fill='both', side='left')
        b2 = tk.Button(f2, text='查找', font=self.font_normal,
                       width=4, command=self.run, takefocus=False)
        b2.pack(fill='both', side='left', expand='yes')
        b2.bind_all("<Return>", self.bind_return)

        f2.pack(fill='x', expand='no', side='top')

        f3 = tk.Frame(self.root)

        scroll1 = tk.Scrollbar(f3)
        scroll1.pack(side="right", fill="y")
        scroll2 = tk.Scrollbar(f3, orient='horizontal')
        scroll2.pack(side="bottom", fill="x")

        # wrap: "none"（不自动换行），"char"(默认)（按字符自动换行）和 "word"（按单词自动换行）
        self.t = tk.Text(f3, font=self.font_text, wrap='none', yscrollcommand=scroll1.set, xscrollcommand=scroll2.set,
                         takefocus=False)

        scroll1.config(command=self.t.yview)
        scroll2.config(command=self.t.xview)

        self.t.pack(fill='both', side='left', expand='yes')

        self.t.tag_config("tag_bold", font=("Microsoft YaHei", 14, 'bold'))

        f3.pack(fill='both', expand='yes', side='top')

        self.root.mainloop()


if __name__ == '__main__':
    Visualize().tk_show()
