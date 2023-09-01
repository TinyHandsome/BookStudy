#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: bar_descriptions.py
@time: 2018/9/12 15:05
@desc: 添加自定义工具提示
"""

import pygal
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie'},
    {'value': 15028, 'label': 'Description of django'},
    {'value': 14798, 'label': 'Description of flask.'},
]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')