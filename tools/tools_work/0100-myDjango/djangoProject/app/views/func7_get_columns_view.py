#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: func7_get_columns_view.py
@time: 2022/4/11 9:11
@desc: 获取列表
"""
import traceback

from django.shortcuts import render

from app.views import utils_views
from funcs.func7_get_columns.get_columns_from_line import get_columns_by_equality
from supports.topc_title_search import search_title


def func7_get_columns(request):
    """处理sql"""
    data = {
        'title': search_title(request),
        'result': '',
        'my_str': '',
        'output': ''
    }

    if request.method == "POST":
        my_str = request.POST.get('my_str')
        data['my_str'] = my_str

        try:
            output = get_columns_by_equality(my_str)
            data['output'] = output
        except Exception as e:
            print(traceback.format_exc())
            data['result'] = '运行报错，请自查或者联系@李英俊小朋友'

    elif request.method == "GET":
        ...
    else:
        data['result'] = "请联系管理员"
    return render(request, 'func7_get_columns/func7.html', context=data)
