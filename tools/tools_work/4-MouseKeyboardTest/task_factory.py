#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: task_factory.py
@time: 2020/8/31 14:23
@desc: 测试任务能否实现
"""
from mk_factory import MKFactory
from properties import *
import sys
from tip_time import *


class TaskFactory:
    def __init__(self, properties):
        self.mk = MKFactory()
        self.properties = properties
        self.t = TipTime()
        # 是否在terminal输出循环次数
        self.print_flag = True

    def check_close(self):
        """检测鼠标是否在左上角(0 ~ 50, 0 ~ 50)或者右上角（1920+1920-50 ~ 1920+1920, 0 ~ 50）"""
        x, y = self.mk.m.get_mouse_postion()
        flag_1 = (0 <= x <= 50) and (0 <= y <= 50)
        flag_2 = (1920 + 1920 - 50 <= x <= 1920 + 1920) and (0 <= y <= 50)
        if flag_1 or flag_2:
            print("-" * 20 + " 正在退出 " + "-" * 20)
            sys.exit()

    def run(self, loop_times):
        for i in range(loop_times):
            if self.print_flag:
                print("-> 正在循环第", i + 1, "次...")

            for k, coordinate in self.properties.items():

                # 循环每一步前检测是否退出
                self.check_close()

                step, key_type, info = k.split('_')

                # 开始颜色检查
                if key_type == 'colorCheck':
                    self.mk.colorCheck(info, coordinate)

                # 是否颜色检查未通过，跳过部分检测步骤
                if not self.mk.state:
                    if int(step) in self.mk.escape_steps:
                        continue

                if key_type == 'tip':
                    self.t.tip(float(info))
                elif key_type == 'm1':
                    self.mk.m1(coordinate)
                elif key_type == 'm2':
                    self.mk.m2(coordinate)
                elif key_type == 'r1':
                    self.mk.r1(coordinate)


if __name__ == '__main__':
    # 新建多少个任务
    # TaskFactory(properties_taskScheduler).run(10)

    # 停止并删除任务
    # TaskFactory(properties_deleteTaskScheduler).run(20)

    # 删除ecm
    TaskFactory(properties_delete_ecm3).run(500)
