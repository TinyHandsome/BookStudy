#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: word_get.py
@time: 2020/12/7 10:39
@desc: 获取一个word中的所有数据
"""
from dataclasses import dataclass
import docx


@dataclass
class WordInfo:
    file_path: str

    def __post_init__(self):
        pass

    def word_get(self, ignore_enter=True):
        """
        获取word中的所有数据
        :param ignore_enter: 是否忽略空行，或者全是空格的行
        :return: 每一行合起来的list
        """
        file = docx.Document(self.file_path)
        result = []
        for para in file.paragraphs:
            value = para.text.strip()
            if ignore_enter:
                if value != '':
                    result.append(value)
            else:
                result.append(value)

        return result
