#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: func3_views.py
@time: 2022/1/27 14:23
@desc: 
"""
from django.shortcuts import render

from funcs.func4.add_double_quatation import add_double_quatation


def func4(request):
    data = {
        'choose': '',
        'end_symbol': '',
        'prefix': '',
        'case': '',
        'my_str': '',
        'result': '',
        'output': ''
    }

    if request.method == 'POST':
        my_str = request.POST.get('my_str')
        choose = request.POST.get('choose')
        end_symbol = request.POST.get('end_symbol')
        prefix = request.POST.get('prefix')
        case = request.POST.get('case')

        if my_str is None or my_str == '':
            return render(request, 'func4/func4.html', context=data)

        if choose is None or choose == '':
            choose = '"'
        if end_symbol is None or end_symbol == '':
            end_symbol = ','
        if prefix is None or prefix == '':
            prefix = ''
        if case is None or case == '':
            case = ''
        try:
            aim_str = add_double_quatation(my_str, final=end_symbol, add=choose, prefix=prefix, case=case)
            data['result'] = '运行成功'
            data['output'] = aim_str
            data['my_str'] = my_str
            data["choose"] = choose
            data["end_symbol"] = end_symbol
            data["prefix"] = prefix
        except Exception as e:
            print('报错：', end='')
            print(repr(e))
            data['result'] = '运行报错，请自查或者联系@李英俊小朋友'
        finally:
            return render(request, 'func4/func4.html', context=data)

    elif request.method == 'GET':
        return render(request, 'func4/func4.html', context=data)
