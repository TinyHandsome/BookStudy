#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: middlewares.py
@time: 2022/1/26 15:28
@desc: 中间件
"""
from django.utils.deprecation import MiddlewareMixin

from app.models import User
from djangoProject.settings import MY_HOST


class RememberIP(MiddlewareMixin):
    def process_request(self, request):
        """在视图运行之前记住ip"""
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        if not User.objects.filter(ip=ip).exists():
            print('新用户访问，IP：', ip)
            user = User()
            user.ip = ip
            user.count = 1
            user.save()
        else:
            user = User.objects.get(ip=ip)
            user.count = user.count + 1
            user.save()
            if ip != MY_HOST:
                print('老用户【' + user.name + '】访问，IP：', ip)
