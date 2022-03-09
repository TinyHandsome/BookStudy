#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: cmd_decorate.py
@time: 2022/3/8 10:03
@desc: cmd输出颜色美化，
            Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
            Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
            Style: DIM, NORMAL, BRIGHT, RESET_ALL
        参考链接：
            1. https://blog.csdn.net/wy_97/article/details/79663014
            2. https://www.cnblogs.com/xiao-apple36/p/9151883.html
            3. https://www.cnblogs.com/Karl-H/p/14699350.html
            4. https://kernel.blog.csdn.net/article/details/45439671
"""

from colorama import Fore, Back, Style, init

init(wrap=True)


def print_black_null(msg):
    """黑空"""
    print(Fore.BLACK + msg + Fore.RESET)


def print_red_null(msg):
    """红空"""
    print(Fore.RED + msg + Fore.RESET)


def print_green_null(msg):
    """绿空"""
    print(Fore.GREEN + msg + Fore.RESET)


def print_blue_null(msg):
    """蓝空"""
    print(Fore.BLUE + msg + Fore.RESET)


def print_yellow_null(msg):
    """黄空"""
    print(Fore.YELLOW + msg + Fore.RESET)


def print_magenta_null(msg):
    """洋红空"""
    print(Fore.MAGENTA + msg + Fore.RESET)


def print_cyan_null(msg):
    """青空"""
    print(Fore.CYAN + msg + Fore.RESET)


def print_white_null(msg):
    """白空"""
    print(Fore.WHITE + msg + Fore.RESET)


def print_red_white(msg):
    """红白"""
    print(Fore.RED + Back.WHITE + msg + Fore.RESET + Back.RESET)


def print_white_red(msg):
    """白红"""
    print(Fore.WHITE + Back.RED + msg + Fore.RESET + Back.RESET)


def print_white_black(msg):
    """白黑"""
    print(Fore.WHITE + Back.BLACK + msg + Fore.RESET + Back.RESET)


def print_black_white(msg):
    """黑白"""
    print(Fore.BLACK + Back.WHITE + msg + Fore.RESET + Back.RESET)


def print_yello_magenta(msg):
    """黄洋红"""
    print(Fore.YELLOW + Back.MAGENTA + msg + Fore.RESET + Back.RESET)


def print_yello_cyan(msg):
    """黄青"""
    print(Fore.YELLOW + Back.CYAN + msg + Fore.RESET + Back.RESET)


def print_cyan_magenta(msg):
    """青洋红"""
    print(Fore.CYAN + Back.MAGENTA + msg + Fore.RESET + Back.RESET)


if __name__ == '__main__':
    print_black_null('黑空')
    print_blue_null('蓝空')
    print_red_null('红空')
    print_green_null('绿空')
    print_yellow_null('黄空')
    print_magenta_null('洋红空')
    print_cyan_null('青空')
    print_white_null('白空')
    print_red_white('红白')
    print_white_red('白红')
    print_black_white('黑白')
    print_white_black('白黑')
    print_yello_magenta('黄洋红')
    print_yello_cyan('黄青')
    print_cyan_magenta('青洋红')
