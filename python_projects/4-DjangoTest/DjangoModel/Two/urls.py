#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: urls.py
@time: 2021/1/20 19:15
@desc: 
"""
from django.conf.urls import url
from Two import views



urlpatterns = [
    url('getuser/', views.get_user),
    url('getusers/', views.get_users),
    url('getorders/', views.get_orders),
    url('getgrades/', views.get_grades),
    url('getcustomer', views.get_customer),
    url('getcompany/', views.get_company),
    url('getanimals/', views.get_animals),
]
