#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: no_populations.py
@time: 2018/9/10 10:03
@desc: 在世界地图上呈现数字数据
"""

import pygal


wm = pygal.maps.world.World()
wm.title = 'Population of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us':309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')