#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: urls.py
@time: 2022/2/28 17:15
@desc: 
"""
from django.urls import path

from xue.views import xue1_view

urlpatterns = [
    path('epidemic_prevention/', xue1_view.xue1, name='xue1'),
]