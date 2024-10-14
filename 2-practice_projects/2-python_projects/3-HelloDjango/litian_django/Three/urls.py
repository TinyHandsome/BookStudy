#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: urls.py
@time: 2021/1/6 19:54
@desc: 
"""
from django.urls import path

from Three import views

urlpatterns = [
    path('', views.index),
    path('getgrade/', views.get_grade),
    path('getstudents/', views.get_students)
]
