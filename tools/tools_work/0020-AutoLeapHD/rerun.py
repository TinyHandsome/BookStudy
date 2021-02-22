#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: rerun.py
@time: 2021/2/22 9:25
@desc: 自动重跑
"""

from dataclasses import dataclass


@dataclass
class ReRun:
    """自动重跑的类"""
    rerun_url: str
