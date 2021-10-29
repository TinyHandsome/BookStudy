#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: middleware.py
@time: 2021/10/27 8:51
@desc: 
"""
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from App.models import AXFUser

REQUIRE_LOGIN_JSON = [
    '/axf/addtocart/',
    '/axf/changecartstatus/',
    '/axf/makeorder/',
]
REQUIRE_LOGIN = [
    '/axf/cart/',
    '/axf/orderdetail/',
    '/axf/orderlistnotpay/',
]


class LoginMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path in REQUIRE_LOGIN_JSON:

            user_id = request.session.get('user_id')
            if user_id:
                try:
                    user = AXFUser.objects.get(pk=user_id)
                    request.user = user
                except:
                    # return redirect(reverse('axf:login'))
                    data = {
                        'status': 302,
                        'msg': 'user not available'
                    }
                    return JsonResponse(data=data)
            else:
                # return redirect(reverse('axf:login'))
                data = {
                    'status': 302,
                    'msg': 'user not login'
                }
                return JsonResponse(data=data)

        if request.path in REQUIRE_LOGIN:
            user_id = request.session.get('user_id')
            if user_id:
                try:
                    user = AXFUser.objects.get(pk=user_id)
                    request.user = user
                except:
                    return redirect(reverse('axf:login'))
            else:
                return redirect(reverse('axf:login'))
