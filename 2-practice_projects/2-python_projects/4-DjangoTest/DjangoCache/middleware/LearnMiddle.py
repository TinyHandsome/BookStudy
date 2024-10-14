#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: LearnMiddle.py
@time: 2021/4/15 9:31
@desc: 自定义中间件
"""
import random
import time

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class HelloMiddle(MiddlewareMixin):
    def process_request(self, request):
        print(request.META.get("REMOTE_ADDR"))

        ip = request.META.get('REMOTE_ADDR')
        pass

        ''' 白名单、黑名单、访问时限
        if request.path == '/app/getphone/':

            if ip == '127.0.0.1':

                if random.randrange(100) > 20:
                    return HttpResponse('恭喜您免费获得小米8 256G版')

        if request.path == "/app/getticket/":
            if ip == '127.0.0.1':
                return HttpResponse("已抢光")

        if request.path == '/app/search/':
            result = cache.get(ip)
            if result:
                return HttpResponse('您的访问过于频繁，请10秒之后再试！')
            cache.set(ip, ip, timeout=10)
        '''

        '''黑名单
        black_list = cache.get('black', [])

        if ip in black_list:
            return HttpResponse("黑名单用户，告辞！")

        # 后面的 []  代表，如果获取为空的话，返回的为空列表
        requests = cache.get(ip, [])
        # 如果数组中 最新和最旧的时间超过60秒，则除去最旧的记录
        while requests and time.time() - requests[-1] > 60:
            requests.pop()
        requests.insert(0, time.time())
        cache.set(ip, requests, timeout=60)

        if len(requests) > 20:
            black_list.append(ip)
            cache.set('black', black_list, timeout=60*60*24)
            return HttpResponse("小爬虫，小黑屋里呆着叭")

        # 如果60以内的数据大于10个，则频率过高
        if len(requests) > 5:
            return HttpResponse("请求次数过于频繁，请稍后再试")
        '''

    def process_exception(self, request, exception):
        print(exception, request)
        return redirect(reverse('app:index'))


class TwoMiddle(MiddlewareMixin):
    def process_request(self, request):
        print("Two Middleware")
