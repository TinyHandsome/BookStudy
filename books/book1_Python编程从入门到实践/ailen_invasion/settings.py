#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: settings.py
@time: 2018/8/3 9:11
@desc: 创建设置类
"""


class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1
        self.ship_limit = 1     # 三条命
        self.transform_rate = 0.3

        # 子弹设置
        self.bullet_shape = False
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 10
        self.bullet_fps = 30
        self.bullet_fps_reset = self.bullet_fps

        # 子弹旋转速度
        self.bullet_rotate_angle = 90
        self.bullet_rotate_speed = 30

        # 子弹缩放速度
        self.bullet_transform_speed = 10
        self.bullet_transform_limit = 2
        self.bullet_transform_rate = 0.05

        # 开火标志
        self.bullet_fire = False

        # 外星人设置
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 50
        # fleet_direction为1表示向右移动，为-1表示向左移
        self.fleet_direction = 1

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右移动，为-1表示向左移
        self.fleet_direction = 1
        # 计分
        self.alien_points = 5

    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)