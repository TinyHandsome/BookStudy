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

        sched参考链接：
            1. https://www.cnblogs.com/luminousjj/p/9340082.html
"""
import os
import sched
import time
from threading import Thread, Lock

from config.config import SCHEDULER_GAP
from support.tools import init_print, MyTimeBar


class ThreadManagement:
    """线程管理"""

    def __init__(self):
        self.threads = []
        self.lock = Lock()

    def check_threads_empty(self):
        return len(self.threads) == 0

    def build_thread(self, func, fail_func=None, daemon=False, is_schdule=False, args=()):
        """建立线程"""
        t = MyThread(target=func, lock=self.lock, fail_func=fail_func, daemon=daemon, is_schdule=is_schdule, args=args)
        self.threads.append(t)
        t.start()

    def stop_all_schedule(self):
        """关闭循环调度的线程"""
        if not self.check_threads_empty():
            for t in self.threads:
                # 只需要关停循环的线程
                if t.is_schdule:
                    t.stop_schedule()


class MyThread(Thread):
    """我的多线程"""

    def __init__(self, target, lock: Lock, fail_func, daemon, is_schdule, args):
        super().__init__(daemon=daemon)

        self.target = target
        self.lock = lock
        self.fail_func = fail_func
        self.daemon = daemon
        self.is_schdule = is_schdule
        self.args = args

        # 类初始化
        self.scheduler = sched.scheduler(time.time, time.sleep)

        # 运行状态，控制周期调度任务状态
        self.schedule_status = True
        # 构建时间条
        self.mtb = MyTimeBar()
        # 周期调度时间
        self.scheduler_gap = SCHEDULER_GAP
        # 最新预定事件
        self.current_sche = None

    def stop_schedule(self):
        """停止循环调度"""
        self.schedule_status = False
        # 时间条也要停止
        self.mtb.stop()
        # 取消预订事件
        self.scheduler.cancel(self.current_sche)

    def run_target(self):
        """运行函数进行try的封装"""
        self.lock.acquire(timeout=5)
        try:
            self.target(*self.args)
        except:
            # 运行失败就调用失败后应该进行的函数
            if self.fail_func is None:
                ...
            else:
                self.fail_func()
        finally:
            self.lock.release()

    def start_scheduler(self):
        """开始周期调度任务"""

        def perform(inc):
            # 检查运行状态是否接着运行
            if not self.schedule_status:
                return

            # 调度任务的提示信息
            init_print()
            # 运行函数
            self.run_target()
            # inc时间后调用下一个任务，进入循环
            self.current_sche = self.scheduler.enter(inc, 0, perform, (inc,))
            # 进度条
            self.mtb.my_time_bar(self.scheduler_gap)
            # 清空输出
            os.system('cls')

        self.scheduler.enter(0, 0, perform, (self.scheduler_gap,))
        self.scheduler.run()

    def run(self):
        """重写运行函数"""
        if self.is_schdule:
            # 如果是周期调度函数
            self.start_scheduler()
        else:
            # 否则直接运行就行
            self.run_target()
