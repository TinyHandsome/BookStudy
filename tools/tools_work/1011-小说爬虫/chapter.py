#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: chapter.py
@time: 2023/8/2 15:31
@desc: 
"""
from dataclasses import dataclass


@dataclass
class Chapter:
    home: str
    title: str
    content: str
    next_chap_url: str

    def get_next_page_url(self):
        return self.home + self.next_chap_url

    def has_next_page(self):
        """如果url不是以 .html 结尾则认为，结束了"""
        return '.html' in self.next_chap_url

    def __str__(self):
        return self.title + self.content

    def get_title(self):
        return self.title