#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: views_helper.py
@time: 2021/10/20 17:05
@desc: 
"""
import hashlib


def hash_str(source):
    return hashlib.new('sha512', source.encode('utf-8')).hexdigest()
