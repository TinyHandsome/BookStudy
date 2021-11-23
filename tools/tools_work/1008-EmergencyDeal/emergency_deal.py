#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: emergency_deal.py
@time: 2021/11/23 15:24
@desc: 紧急删库跑路按钮，现在只有文件夹考虑
"""
import os
import shutil

path = 'datas/delete_path'


def delete(folder_path):
    shutil.rmtree(folder_path)


def read_need_delete_doc():
    with open(path, 'r', encoding='utf-8') as f:
        folds = f.readlines()
        folds = [f.strip().replace('\n', '').replace('\ufeff', '') for f in folds]

    return folds


def do_delete():
    for p in read_need_delete_doc():
        delete(p)
        print('-> finish delete: ', p)


def main():
    print('输入【u】修改目录')
    info = input("输入y确认删除：")
    info = info.strip().lower()
    if info == 'y':

        print('确定要删除以下文件吗？')
        print('\n'.join(read_need_delete_doc()))
        print('*' * 100)
        x = input('在输入y确认：')
        if x.strip().lower() == 'y':
            do_delete()
            print('删除完毕，快溜~')
        else:
            print('取消命令，告辞~')
    elif info == 'u':
        os.system('notepad.exe ' + path)
    else:
        print('取消命令，告辞~')


if __name__ == '__main__':
    main()
