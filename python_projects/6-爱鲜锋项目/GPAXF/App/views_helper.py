#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: views_helper.py
@time: 2021/10/20 17:05
@desc: 
"""
import hashlib

from django.core.mail import send_mail
from django.template import loader


def hash_str(source):
    return hashlib.new('sha512', source.encode('utf-8')).hexdigest()


def send_email_activate(request):

    subject = 'AXF Activate2'
    message = '<h1>Hello</h1>'
    from_email = 'litian_django_test@163.com'
    recipient_list = ['2528897250@qq.com', '694317828@qq.com']

    data = {
        "username": 'gouzei',
        'activate_url': 'http://www.1000phone.com'
    }

    html_message = loader.get_template('user/activate.html').render(data)

    send_mail(subject=subject, message="", html_message=html_message, from_email=from_email, recipient_list=recipient_list)