#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: time_funcs.py
@time: 2022/2/7 10:34
@desc: 时间处理小脚本
"""
import datetime
import random
import time

BASE_PAUSE_TIME = 1


def sleep_random_and_base_pause_time(change_base_pause_time=None):
    """暂停一个随机时间+基础时间"""
    if not change_base_pause_time:
        change_base_pause_time = BASE_PAUSE_TIME

    time.sleep(random.random() + change_base_pause_time)


def get_now_year_month_day():
    """获取当前的年月日"""
    now = datetime.datetime.now()
    return now.strftime('%Y/%m/%d/')


def get_now_hour_minute_second():
    """获取当前的时分秒"""
    now = datetime.datetime.now()
    return now.strftime('%H%M%S')