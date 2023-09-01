#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: bullet.py
@time: 2018/8/3 16:37
@desc: 子弹的类
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__()
        self.screen = screen
        self.angle = ai_settings.bullet_rotate_angle
        self.speed = ai_settings.bullet_rotate_speed
        self.reset_rotate = self.speed
        self.transform_speed = ai_settings.bullet_transform_speed
        self.transform_reset = self.transform_speed
        self.transform_rate = ai_settings.bullet_transform_rate
        self.transform_limit = ai_settings.bullet_transform_limit

        # 在(0, 0)处创建一个表示子弹的矩形， 再设置正确的位置
        self.bullet_type = ai_settings.bullet_shape
        if self.bullet_type:
            self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
            self.color = ai_settings.bullet_color
        else:
            # 子弹图片
            self.image = pygame.image.load('images/bullet.png').convert_alpha()
            self.rect = self.image.get_rect()

        # 子弹位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 子弹大小
        self.width = self.rect.width
        self.height = self.rect.height

        # 储存用小数表示子弹的位置
        self.y = float(self.rect.y)

        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y
        # 子弹旋转
        self.speed -= 1
        if self.speed < 0:
            self.image = pygame.transform.rotate(self.image, self.angle)
            self.speed = self.reset_rotate
        # 子弹缩放
        '''
        self.transform_speed -= 1
        if self.transform_speed < 0:
            # if self.width <= self.transform_limit:
            self.width = int(self.width * (1 + self.transform_rate))
            self.height = int(self.height * (1 + self.transform_rate))
            print(self.height)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.transform_speed = self.transform_reset
        '''

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        if self.bullet_type:
            pygame.draw.rect(self.screen, self.color, self.rect)
        else:
            self.screen.blit(self.image, self.rect)
