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

from app.models import User, UrlManage, FuncType


def index(request):
    users = User.objects.all().order_by('-count')
    functypes = FuncType.objects.filter(shown_index=True)
    funcs = UrlManage.objects.filter(func_type__shown_index=True)

    # index中不显示功能：周队专用的数据

    funcs_dict = {}

    for functype in functypes:
        funcs_dict[functype] = funcs.filter(func_type=functype)

    data = {
        'users': enumerate(users, 1),
        'funcs_dict': funcs_dict
    }

    return render(request, 'index.html', context=data)
