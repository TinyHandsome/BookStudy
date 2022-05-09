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

from funcs.func8_idcard_code_country.spider_code import spider_code_country
from supports.topc_title_search import search_title


def func8_idcard_code_country(request):
    """根据idcard的前6位 查询所在 籍贯"""
    data = {
        'title': search_title(request),
        'idcard6': '',
        'country': '',
        'result': ''
    }

    if request.method == "POST":
        idcard6 = request.POST.get('idcard6')
        data['idcard6'] = idcard6

        try:
            country = spider_code_country(idcard6)
            data['country'] = country
        except Exception as e:
            print(traceback.format_exc())
            data['result'] = '运行报错，查询不到你对应的籍贯'

    elif request.method == "GET":
        ...
    else:
        data['result'] = "出错啦，请联系管理员解决"
    return render(request, 'func8_idcard_code_country/func8.html', context=data)
