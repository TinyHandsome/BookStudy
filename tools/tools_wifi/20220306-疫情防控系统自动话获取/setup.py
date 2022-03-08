#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: setup.py.py
@time: 2022/3/8 8:42
@desc: 运行主程序
        notepad配置：cmd /k cd "(CURRENT_DIRECTORY)" &  python "(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT
        【20220308】
            [√] 实现多线程和快捷键控制输出，现在按 Q 可以直接查询不用等待
            [√] 增加核心数据的颜色
            [ ] 配置只输出部分列
            [√] 保存最后一次bearer token，自动获取最后一次bearer token
            [ ] 设置邮件告警
            [√] 增加进度条：两种
            [√] 美化进度条
            [√] 修复多线程中的调度线程退出的问题
"""
import sys

from support.cmd_decorate import print_cyan_null, print_red_null
from structure.epidemic_prevention_info_get import EpidemicPrevention
from structure.my_threading import ThreadManagement
from system_hotkey import SystemHotkey


class Epidemic:

    def __init__(self):
        self.ep = EpidemicPrevention()
        self.tm = ThreadManagement()
        self.hk = SystemHotkey()
        self.hk.register(('control', 'q'), callback=lambda x: self.q())
        self.hk.register(('control', 'w'), callback=lambda x: self.s())

    def run(self):
        self.tm.build_thread(self.ep.setup, is_schdule=True)

    def q(self):
        print_cyan_null('\n\nWARNING: 正在手动获取...\n\n')
        self.ep.setup()

    def s(self):
        print_cyan_null('\n\nWARNING: 正在结束...\n\n')
        self.tm.stop_all_schedule()


if __name__ == '__main__':
    e = Epidemic()
    e.run()
