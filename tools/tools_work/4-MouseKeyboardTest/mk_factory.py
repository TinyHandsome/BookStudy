#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: mk_factory.py
@time: 2020/8/31 17:25
@desc: 鼠标键盘模拟工场
"""
from mouse_action import MouseAction
from keyboard_action import KeyboardAction


class MKFactory:
    def __init__(self):
        self.m = MouseAction()
        self.k = KeyboardAction()
        self.state = True
        self.escape_steps = [1, 2, 3]

    def colorCheck(self, info, coordinate):
        """
        检查颜色是否对应，整个操作流程是否进行的标志
        :param info: r,g,b
        :param coordinate: 坐标
        """
        # 进行循环的时候检测是否满足循环条件，即按键颜色是否符合目标颜色
        rgb_list = [int(a) for a in info.split(',')]
        self.state = self.m.check_mouse_color(rgb_list, coordinate)

        if self.state:
            print('--> 颜色检查通过，开始迭代...')
        else:
            print('--> 颜色检查未通过，进行下一步...')

    def m1(self, xy):
        """单击"""
        self.m.click_position(xy)

    def m2(self, xy):
        """双击"""
        self.m.doubleclick_position(xy)

    def r1(self, xy):
        """右键单击"""
        self.m.rightclick_position(xy)

    def k_str(self, str):
        """输入str"""
        self.k.key_input(str)
