#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: urls.py
@time: 2021/1/5 18:07
@desc: Two的各个链接
"""
from django.urls import path

from Two import views

urlpatterns = [
    path('index/', views.index),
    path('addstudent/', views.addstudent),
    path('getstudents/', views.get_students),
    path('updatestudent/', views.update_student),
    path('deletestudent/', views.delete_student),
]
