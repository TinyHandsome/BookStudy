#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: index_views.py
@time: 2022/1/26 10:19
@desc: 
"""

from django.shortcuts import render

from app.models import IP, Url, FuncType


def index(request):
    users = IP.objects.all().order_by('-count')

    # 在主页中只展示想要展示的功能类型
    # index中不显示功能：周队专用的数据
    functypes = FuncType.objects.filter(shown_index=True)
    funcs = Url.objects.filter(func_type__shown_index=True)

    # 获取最新更新的功能
    update_func = Url.objects.order_by('-update_time').first()

    funcs_dict = {}

    for functype in functypes:
        onetype_funcs = funcs.filter(func_type=functype)
        output_funcs = []
        for t_func in onetype_funcs:
            if t_func == update_func:
                update_flag = 1
            else:
                update_flag = 0
            t_func.update_flag = update_flag
            output_funcs.append(t_func)

        funcs_dict[functype] = output_funcs

    data = {
        'users': enumerate(users, 1),
        'funcs_dict': funcs_dict
    }

    return render(request, 'index.html', context=data)
