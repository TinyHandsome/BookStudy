#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: TimeTool.py
@time: 2020/5/4 11:44
@desc: 时间相关处理工具
"""

import time
import random


class TimeTool:
    def __init__(self):
        pass

    def getCurrentTime(self):
        # 后面是毫秒
        x = time.time()
        ms = int((x - int(x)) * 1000)
        return time.strftime("%Y-%m-%d-%H-%M-%S-" + str(ms))

    def getct(self):
        return time.strftime("%Y-%m-%d-%H-%M-%S-") + str(random.random())

    def getTimeTag(self):
        return time.strftime("%H:%M:%S  %Y/%m/%d")
