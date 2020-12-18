#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: game_stats.py
@time: 2018/8/12 22:35
@desc: 用于跟踪游戏统计信息
"""


class GameStates():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于活动状态
        self.game_active = False

        # 开始按钮状态
        self.button_clicked = False

        # 在任何情况下都不应重置最高得分
        self.high_score = 0

        # 最高分保存文件的名字
        self.file_name = 'save/high_score.json'

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
