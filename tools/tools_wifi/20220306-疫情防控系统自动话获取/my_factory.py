#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: my_factory.py
@time: 2022/3/6 8:57
@desc: 我的工厂
"""

from dataclasses import dataclass


@dataclass
class Factory:
    # 未验证
    unrevised_list = []
    # 未审核
    unverified_list = []


