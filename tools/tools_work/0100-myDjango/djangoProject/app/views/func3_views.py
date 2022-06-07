#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: func3_views.py
@time: 2022/1/27 14:23
@desc: LeapHD自动保存
        0. 可以添加替换字段
        1. 组件id是获取的：http://dmpqas.whchem.com/TaskScheduler/idGen/genId.do?idType=T
        2. 流程id是自动生成的，流程id和版本号需要置空
"""
from django.shortcuts import render

from funcs.func3.leaphd_deal import save_hd_taskschedule
from supports.topc_title_search import search_title


def func3(request):
    aim_dict = {
        'ods_fico.': 'ods_fico_s4.',
        'ods_ps.': 'ods_ps_s4.',
        'ods_mm.': 'ods_mm_s4.',
        'O2H': 'HANA2H',
        'ODS_FICO_ORACLE': 'ODS_FICO_HANA',
        'ODS_MM_ORACLE': 'ODS_MM_HANA',
        'ODS_PS_ORACLE': 'ODS_PS_HANA',
    }

    data = {
        'title': search_title(request),
        'my_cookie': '',
        'defjson': '',
        'result': '',
        'aim_dict': aim_dict
    }

    if request.method == 'POST':
        my_cookie = request.POST.get('my_cookie')
        defjson = request.POST.get('defjson')
        data['my_cookie'] = my_cookie
        data['defjson'] = defjson

        try:
            resp = save_hd_taskschedule(my_cookie, defjson, aim_dict)
            if resp.status_code == 200:
                data['result'] = '运行成功'
            else:
                data['result'] = '运行失败，返回编号：' + str(resp.status_code) + '，请自查或者联系@李英俊小朋友'
        except Exception as e:
            print('报错：', end='')
            print(repr(e))
            data['result'] = '运行报错，请检查你的cookie和defjson，或者联系@李英俊小朋友'
        finally:
            return render(request, 'func3_leaphddosave/func3.html', context=data)

    elif request.method == 'GET':
        return render(request, 'func3_leaphddosave/func3.html', context=data)
