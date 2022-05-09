#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: password_management.py
@time: 2022/5/9 15:04
@desc: 密码管理
"""
from django.contrib.auth.hashers import make_password


def encode_password(password):
    """加密"""
    return make_password(password)


def check_password():
    ...
