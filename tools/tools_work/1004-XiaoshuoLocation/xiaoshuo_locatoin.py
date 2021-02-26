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
"""

from dataclasses import dataclass
from math import ceil


@dataclass
class XiaoshuoLocation:
    line_length: int
    file_path: str

    def __post_init__(self):
        self.pages, self.view_list = self.get_location()

    def depart_line(self, line):
        count = int(len(line) / 30) + 1
        result_line = []
        for i in range(count):
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

            return ceil(len(temp) / self.line_length), self.depart_line(temp)

    def search_words(self, aim_words):
        count = 1
        for line in self.view_list:
            if aim_words in line:
                print(count, ": ", line)

            count += 1


if __name__ == '__main__':
    info = input('请输入要查找的内容：\n')
    XiaoshuoLocation(30, 'E:\study_books\明朝那些事.txt').search_words(info)
    print('\n\n')
