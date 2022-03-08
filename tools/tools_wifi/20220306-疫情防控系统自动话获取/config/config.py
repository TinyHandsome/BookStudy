#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: config.py
@time: 2022/3/7 14:32
@desc: 需要检测里面有没有哪些字段的检查列表
"""

# 检查字段列表
CHECK_LIST = ['富力湾', '锦园', '辉盛岚海']
# 周期调度时间，单位：秒
SCHEDULER_GAP = 600
# 【设想，待完善】是否展示所有列名：int：展示[0: int]；list：展示list中的列名；'default'：展示姓名、联系方式、来源、地址
SHOW_SET = 'default'

# 未修正
UNREVISED_URL = 'http://lsqzdrqgkxt.ytlaishan.gov.cn:18081/key/area/personnel/re/xz/list?pageNum=1&pageSize=1000&auditStatus=0'
# 未审核
UNVERIFIED_URL = 'http://lsqzdrqgkxt.ytlaishan.gov.cn:18081/system/declare/list?pageNum=1&pageSize=1000&declarationStatus=0'
