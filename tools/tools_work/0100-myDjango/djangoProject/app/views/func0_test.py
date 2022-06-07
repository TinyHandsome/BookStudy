#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: func0_test.py
@time: 2022/6/1 16:22
@desc: 测试view
"""

from django.http import JsonResponse


def test(request):
    return JsonResponse({
        'des': 'test data',
        'data': 'test',
        "msg": '你在干神莫啊朔总'
    })
