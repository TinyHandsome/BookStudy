#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: urls.py
@time: 2021/1/9 16:00
@desc: 
"""
from django.urls import path

from App import views

urlpatterns = [
    path('addpersons/', views.add_persons),
    path('getpersons/', views.get_persons),
    path('addperson/', views.add_person),
]