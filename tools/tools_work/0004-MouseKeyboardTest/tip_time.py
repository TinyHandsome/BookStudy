#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: tip_time.py
@time: 2020/8/31 17:33
@desc: 暂停的时间类
"""
import time


class TipTime:
    def __init__(self):
        self.normal_tip = 0.8

    def tip(self, time_tip=None):
        if time_tip is None:
            time_tip = self.normal_tip
        time.sleep(time_tip)

