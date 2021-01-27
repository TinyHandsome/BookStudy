#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: print_tool.py
@time: 2021/1/27 10:44
@desc: 输出工具，
        1. 替换print的功能
        2. 将所有的需要输出的内容放到该类中，方便检索和追溯

       参考链接：
        1. [pycharm如何导入其他文件夹模块](https://www.py.cn/tools/pycharm/16853.html)
"""

from dataclasses import dataclass
from queue import LifoQueue, Queue


@dataclass
class Info:
    """信息类"""
    info: str

    def __post_init__(self):
        ...

    def get_info(self):
        """获取info的内容，str"""
        return self.info

    def __str__(self):
        return self.info


@dataclass
class PrintTool:

    def __post_init__(self):
        # 用栈来存储所有的输出信息，专门用来获取，输出
        self.stack = LifoQueue()
        # 用队列来存储所有的输出信息，专门用来保存，序列化
        self.queue = Queue()

    def set_print_info(self, info: str, if_print=True):
        """将需要输出的内容放入该类中"""
        temp_info = Info(info=info)
        self.stack.put(temp_info)
        self.queue.put(temp_info)

        # 是否输出最上面的数据
        if if_print:
            print(self.stack_get())

    def stack_get(self):
        """获取栈的最上层数据类，并输出"""
        return self.stack.get()
