#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: properties.py
@time: 2020/8/31 17:14
@desc: 配置文件
"""
from collections import OrderedDict

# 离线批处理配置文件
properties_taskScheduler = OrderedDict({
    '1_m1_复制流程': (3700, 635),
    '2_m1_确认复制流程': (2942, 428),
    '3_m1_启用流程': (3674, 632),
    '4_m1_确认启用流程': (2933, 431),
    '5_m1_操作成功': (2883, 314)
})

# 中止并删除离线批处理配置文件
properties_deleteTaskScheduler = OrderedDict({
    '0_colorCheck_242,70,70': (3675, 635),
    '1_m1_停用流程': (3675, 635),
    '2_m1_确认停用流程': (2942, 428),
    '3_m1_操作成功': (2883, 314),
    '4_m1_删除流程': (3702, 636),
    '5_m1_确认删除流程': (2942, 428),
    '6_m1_操作成功': (2883, 314)
})

# 删除ecm文件夹中的数据
properties_delete_ecm1 = OrderedDict({
    # '1_fileColor_255,218,144': (205, 189),

    '2_r1_右键调出菜单': (204, 192),
    '3_m1_更多操作': (281, 380),
    '4_m1_删除': (376, 436),
    '5_m1_接受': (1233, 637),
    '-1_tip_0.5': None,
})
properties_delete_ecm2 = OrderedDict({
    '2_r1_右键调出菜单': (204, 192+20),
    '3_m1_更多操作': (281, 380+20),
    '4_m1_删除': (376, 436+20),
    '5_m1_接受': (1233, 637),
    '-1_tip_0.5': None,
})
properties_delete_ecm3 = OrderedDict({
    '2_r1_右键调出菜单': (204, 192+48),
    '3_m1_更多操作': (281, 380+48),
    '4_m1_删除': (376, 436+48),
    '5_m1_接受': (1233, 596),
    '-1_tip_1.2': None,
})