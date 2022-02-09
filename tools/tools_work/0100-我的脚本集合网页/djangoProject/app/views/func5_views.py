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
import base64
import traceback

from django.http import HttpResponse
from django.shortcuts import render

from funcs.func5.get_url_pic import GetUrlPic
from funcs.my_base_funcs.str_funcs import is_None_or_nullstr


def func5(request):
    data = {
        'root_url': '',
        'chapter': '',
        'page': '',
        'pic_format': '',
        'page_zero_fill': '',
        'result': ''
    }
    # TODO

    if request.method == 'POST':
        root_url = request.POST.get('root_url')
        chapter = request.POST.get('chapter')
        page = request.POST.get('page')
        pic_format = request.POST.get('pic_format')
        page_zero_fill = request.POST.get('page_zero_fill')

        data['root_url'] = root_url
        data['chapter'] = chapter
        data['page'] = page
        data['pic_format'] = pic_format
        data['page_zero_fill'] = page_zero_fill

        gup = GetUrlPic(root_url)

        if is_None_or_nullstr(page_zero_fill):
            page_zero_fill = 0
        if is_None_or_nullstr(chapter):
            chapter = None

        if is_None_or_nullstr(page):
            start_page = 1
            end_page = None

        else:
            try:
                if '-' not in page:
                    end_page = None
                    start_page = int(page)
                else:
                    start_page, end_page = page.split('-')
                    start_page = int(start_page)
                    end_page = int(end_page)
            except:
                data['result'] = '你的页码输入有误'
                return render(request, 'func5_pic_spider/func5.html', context=data)
        try:
            img = gup.get_chapter(chapter, start_page, end_page, int(page_zero_fill), pic_format)
            return HttpResponse(base64.b64encode(img))
        except Exception as e:
            data['result'] = '运行报错，请自查或者联系@李英俊小朋友'
            print(traceback.format_exc())
            return render(request, 'func5_pic_spider/func5.html', context=data)

    elif request.method == 'GET':
        return render(request, 'func5_pic_spider/func5.html', context=data)
