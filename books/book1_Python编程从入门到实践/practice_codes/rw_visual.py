#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: rw_visual.py
@time: 2018/9/6 9:27
@desc: 绘制随机漫步图
"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk的实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.figure(figsize=(10, 6), dpi=128)
    # fig = plt.figure(figsize=(10, 6), dpi=100, facecolor='w', edgecolor='k')
    plt.scatter(rw.x_values, rw.y_values, s=5, c=point_numbers, cmap=plt.cm.rainbow, edgecolors='none')

    # 突出起点和重点
    plt.scatter(0, 0, c='k', edgecolors='none', s=20)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='k', edgecolors='none', s=20)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    # plt.tight_layout()
    plt.show()

    keep_running = input("Make another walk ? (y/n)")
    if keep_running == 'n':
        break
