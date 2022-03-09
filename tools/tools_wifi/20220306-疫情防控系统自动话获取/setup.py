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
            [×] 配置只输出部分列
            [√] 保存最后一次bearer token，自动获取最后一次bearer token
            [√] 增加进度条：两种
            [√] 美化进度条
            [√] 修复多线程中的调度线程退出的问题
        【20220309】
            [√] 新增excel输出
            [√] 新增简单的复制：人名身份证号 电话
            [√] 实现快捷键设置可配
            [√] 重构代码，将白银处理后的结果放到工厂中去，保留产生Dataframe的部分
            [√] 设置邮件告警
            [√] 手动获取时不用发邮件
"""

from config.config import SHORT_CUTS
from support.cmd_decorate import print_cyan_null
from structure.epidemic_prevention_info_get import EpidemicPrevention
from structure.my_threading import ThreadManagement
from system_hotkey import SystemHotkey


class Epidemic:

    def __init__(self):
        self.ep = EpidemicPrevention()
        self.tm = ThreadManagement()
        self.hk = SystemHotkey()
        self.hk.register(SHORT_CUTS.get('查询'), callback=lambda x: self.query())
        self.hk.register(SHORT_CUTS.get('停止'), callback=lambda x: self.stop())
        self.hk.register(SHORT_CUTS.get('导出EXCEL'), callback=lambda x: self.output_excel())
        self.hk.register(SHORT_CUTS.get('简单复制'), callback=lambda x: self.copy_name_id_phone())
        self.hk.register(SHORT_CUTS.get('发送邮件开关'), callback=lambda x: self.change_send_email_status())

    def run(self):
        self.tm.build_thread(self.ep.setup, is_schdule=True, args=(True,))

    def query(self):
        print_cyan_null('\nWARNING: 正在手动获取...')
        self.ep.setup()

    def stop(self):
        print_cyan_null('\nWARNING: 正在结束...')
        self.tm.stop_all_schedule()

    def output_excel(self):
        print_cyan_null('\nWARNING：正在导出EXCEL...')
        self.ep.output_df_excel()

    def copy_name_id_phone(self):
        print_cyan_null('\nWARNING：成功复制[姓名身份证, 电话]...')
        self.ep.easy_copy_name_id_phone()

    def change_send_email_status(self):
        self.ep.change_email_status()
        if self.ep.email_flag:
            print_cyan_null('\nWARNING：发送邮件功能已开启...')
        else:
            print_cyan_null('\nWARNING：发送邮件功能已关闭...')


if __name__ == '__main__':
    e = Epidemic()
    e.run()
