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

from app.models import User


def index(request):
    users = User.objects.all()

    data = {
        'users': users
    }

    return render(request, 'index.html', context=data)
