#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: my_threading.py
@time: 2022/3/7 14:33
@desc: 多线程工具
"""
import sched
import time
from threading import Thread

from config import SCHEDULER_GAP


class MyThread(Thread):
    """我的多线程"""

    def __init__(self, target, daemon, args):
        super(MyThread, self).__init__()
        # 运行状态，控制周期调度任务状态
        self.run_state = True
        # 周期调度时间
        self.scheduler_gap = SCHEDULER_GAP

    def start_scheduler(self, func, fail_func=None):
        """开始周期调度任务"""

        def perform(inc):
            # 检查运行状态是否接着运行
            if not self.run_state:
                return

            # inc时间后调用下一个任务，进入循环
            scheduler.enter(inc, 0, perform, (inc,))

            # 运行函数
            try:
                func()
            except:
                # 运行失败就调用失败后应该进行的函数
                if fail_func is None:
                    ...
                else:
                    fail_func()

        scheduler = sched.scheduler(time.time, time.sleep)
        scheduler.enter(0, 0, perform, (self.scheduler_gap,))
        scheduler.run()
