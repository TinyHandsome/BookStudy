#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: xue1_view.py
@time: 2022/2/23 12:25
@desc: 防疫信息获取
"""
from django.shortcuts import render

from supports.topc_title_search import search_title


def xue1(request):
    data = {
        'title': search_title(request),
        'result': '',
        # 显示当前时间，用进度条表示
        'progress_bar': '',
    }

    if request.method == 'GET':
        ...
    elif request.method == 'POST':
        ...
    else:
        data['result'] = '请联系管理员...'

    return render(request, 'xue1_epidemic_prevention/xue1.html', context=data)