#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: file_deal.py
@time: 2019/3/19 11:05
@desc: 对两个文件进行处理，将两个文件中的表头信息清除
"""

import re


def txt_clean(x):
    pattern = re.compile(r'<\w*>|</\w*>')
    result = pattern.search(x)
    return result


def main():
    path = 'D:/Python3Space/Seq2SeqLearning/en-zh/'
    # file = 'train.tags.en-zh.en'
    # save_path = 'D:/Python3Space/Seq2SeqLearning/train.en'

    file = 'train.tags.en-zh.zh'
    save_path = 'D:/Python3Space/Seq2SeqLearning/train.zh'
    path1 = path + file

    output = open(save_path, 'w', encoding='utf-8')
    with open(path1, 'r', encoding='utf-8') as f:
        x = f.readlines()
        for y in x:
            result = txt_clean(y)
            # print(result)
            if result is None:
                # print(y)
                output.write(y)
    output.close()


if __name__ == '__main__':
    main()