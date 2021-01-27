#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: mouse_action.py
@time: 2020/8/31 14:10
@desc: 处理鼠标
"""

from pymouse import *
from tip_time import TipTime
import pyautogui


class MouseAction:
    def __init__(self):
        self.m = PyMouse()
        self.t = TipTime()

    def mouse_move_to(self, x, y):
        self.m.move(x, y)

    def mouse_click(self, x, y, choose=1):
        """将鼠标移动到(x,y)，按键1，2代表左右键，n代表点击次数（1，2-单双击）"""
        self.m.click(x, y, choose, 1)

    def mouse_doubleclick(self, x, y, choose=1):
        self.m.click(x, y, choose, 2)

    def click_position(self, xy):
        self.mouse_click(xy[0], xy[1])
        self.t.tip()

    def doubleclick_position(self, xy):
        self.mouse_doubleclick(xy[0], xy[1])
        self.t.tip()

    def rightclick_position(self, xy):
        self.mouse_click(xy[0], xy[1], 2)

    def get_mouse_postion(self, is_print=False):
        p = self.m.position()
        if is_print:
            print(p)
        return p[0], p[1]

    def get_mouse_color(self, is_print=False):
        """获取位置颜色"""
        p = self.m.position()
        try:
            c = pyautogui.screenshot().getpixel(p)
        except:
            c = "坐标越界"
        if is_print:
            print(c)
        return c

    def check_mouse_color(self, rgb, position=None):
        """检查颜色是否符合"""
        if position is None:
            position = self.m.position()
        return pyautogui.pixelMatchesColor(position[0], position[1], rgb)


if __name__ == '__main__':
    mouse = MouseAction()
    mouse.get_mouse_postion(True)
    mouse.get_mouse_color(True)
    print(mouse.check_mouse_color((255, 218, 144)))
