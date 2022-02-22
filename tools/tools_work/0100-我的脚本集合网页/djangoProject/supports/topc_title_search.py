#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: topc_title_search.py
@time: 2022/2/21 15:29
@desc: title查询工具
"""
from app.models import UrlManage


def search_title(request):
    path_info = request.path_info
    search_path_info = path_info.replace('/', '') + '/'
    aim_url = UrlManage.objects.filter(func_url=search_path_info)
    return aim_url[0].func_name
