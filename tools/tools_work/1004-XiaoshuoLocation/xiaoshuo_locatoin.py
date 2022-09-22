#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: xiaoshuo_locatoin.py
@time: 2020/12/19 14:07
@desc: Thief-Book-VSCode查找小说的显示进度
    TODO:
        1. 将路径信息和一行显示字数存储到配置文件，而不是直接在代码中写死
        2. 输入的书本名，就在当前路径中查找改书
"""

# -----------------【可以删除】---------------------
# 这里是获取vscode配置文件json，读取成dict的过程
import sys
sys.path.append("E:/1-Work/3-Code/tools/tools_py")
from constants import get_vscode_json_dict
vscode_json_dict = get_vscode_json_dict()
# --------------------------------------------------


from dataclasses import dataclass
from math import ceil
import os


# 可以直接把文件路径粘到这里就行，不需要像我这样从vscode的配置文件中
book_path = vscode_json_dict.get("thiefBook.filePath")
current_single_page = vscode_json_dict.get("thiefBook.pageSize")
book_name = os.path.split(book_path)[-1]

@dataclass
class XiaoshuoLocation:
    line_length: int
    file_path: str

    def set_line_length(self, line_length: int):
        self.line_length = line_length
        self.init_books()

    def set_file_path(self, file_path: str):
        self.file_path = file_path
        self.init_books()

    def __post_init__(self):
        self.init_books()

    def init_books(self):
        """初始化，获取小说的总页数和内容数组"""
        self.pages, self.view_list, self.after_half_view_list = self.get_location()

    def depart_line(self, line, start_half=False):
        """按行分割，将结果拼接成数组"""
        count = int(len(line) / self.line_length) + 1
        result_line = []
        for i in range(count):

            # 是否开始偏移半个单行显示长度的身位
            if start_half:
                start = i * self.line_length + self.line_length // 2
            else:
                start = i * self.line_length

            end = start + self.line_length
            result_line.append(line[start: end])
        return result_line

    def get_location(self):
        """获取小说的显示页数"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            result = f.read()
            temp = result.replace('\n', " ").replace(
                '\r', " ").replace('　　', " ").replace(' ', " ")

            return ceil(len(temp) / self.line_length), self.depart_line(temp), self.depart_line(temp, True)

    def search_words(self, aim_words):
        """寻找文件所在行"""
        find_count = 0

        # 在原始文件中找
        count = 1
        for line in self.view_list:
            if aim_words in line:
                find_count += 1
                print(count, ": ", line)
            count += 1

        # 如果一直没有查到，将view_list换成往后偏移半个【line_length】的身位，放置查找的信息在边界
        count = 1
        if find_count == 0:
            for line in self.after_half_view_list:
                if aim_words in line:
                    find_count += 1
                    print(count - 1, ": ", line)
                count += 1

    def get_aim_line_info(self, page):
        return self.view_list[page-1]

    def show_current_info(self):
        """输出当前路径和文件信息"""
        current_path, current_book, _ = get_path_name_extension(self.file_path)
        print('当前路径：', current_path)
        print('当前书籍：《' + current_book + '》')
        print('当前一行显示文字数：', self.line_length)
        print()


def get_path_name_extension(file_path):
    """获取文件路径，文件名，扩展名"""
    path, name = os.path.split(file_path)
    filename, extension = os.path.splitext(name)
    return path, filename, extension


if __name__ == '__main__':

    xsloc = XiaoshuoLocation(current_single_page, book_path)
    xsloc.show_current_info()

    info = ''
    while (True):
        info = input('请输入要查找的内容：\n')
        if info == '':
            break

        # new book - full path
        if '-fb' in info:
            # 输入完整路径的操作
            new_file_path = info.replace('-nb', '').strip()
            xsloc.set_file_path(new_file_path)
            xsloc.show_current_info()
            continue

        # new book - current path
        if '-cb' in info:
            # 输入一本书的名字，查看当前目录中是否存在，存在就设置，不存在就报错
            ...

        # new line_length
        if '-nl' in info:
            # 根据新页码进行调整
            new_line_length = info.replace('-nl', '').strip()
            xsloc.set_line_length(int(new_line_length))
            xsloc.show_current_info()

        xsloc.search_words(info)
        print('\n')
