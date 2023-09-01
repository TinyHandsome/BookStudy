#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: different_dice.py
@time: 2018/9/6 14:51
@desc: 同时掷两个面数不同的骰子
"""

from die import Die
import pygal

# 创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "results of rolling a D6 and a D10 50000 times"
hist.x_labels = [str(int(i)) for i in range(2, 17)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D10', frequencies)
hist.render_to_file('dice_visual.svg')