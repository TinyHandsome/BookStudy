#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: views_constant.py
@time: 2021/10/19 10:11
@desc: 
"""

ALL_TYPE = "0"

#ORDER
ORDER_TOTAL = "0"
ORDER_PRICE_UP = "1"
ORDER_PRICE_DOWN = "2"
ORDER_SALE_UP = "3"
ORDER_SALE_DOWN = "4"

# 已下单，未付款
ORDER_STATUS_NOT_PAY = 1
# 已下单，已付款，未发货
ORDER_STATUS_NOT_SEND = 2
# 已下单，已付款，已发货，未收货
ORDER_STATUS_NOT_RECEIVE = 3
# 已下单，已付款，已发货，已收货，未确认
# 已下单，已付款，已发货，已收货，已确认，未评价
# 已下单，已付款，已发货，已收货，已确认，已评价，未追评
# 已下单，已付款，已发货，已收货，已确认，已评价
    # 申请售后
        # 退货
        # 返修
        # 换货

# HTTP CODE
HTTP_USER_EXISTS = 901
HTTP_OK = 200