#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: hana2hive.py
@time: 2022/1/27 9:43
@desc: hana转
"""

from django.db import models


class DMPTbls(models.Model):
    db_name = models.CharField(max_length=32, verbose_name='数据库')
    table_name = models.CharField(max_length=32, verbose_name='表名')
    table_des = models.CharField(max_length=255, verbose_name='表描述', blank=True, null=True)

    class Meta:
        db_table = 'my_table_DMPTbls'

