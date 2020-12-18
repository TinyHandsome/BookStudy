#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: keywords_search.py
@time: 2018/8/1 20:37
@desc: 查找文件中的关键字 是否存在关键字
"""

import os


def keyswords_search(keyword, file_path):
    """
    根据文件路径寻找该文件路径下的.py文件中会不会有关键字
    :param keyword: 关键字
    :param file_path: 文件路径
    :return: 含有关键字的文件名
    """

    file_name = []
    time_show = 1
    for root, dirs, files in os.walk(file_path):
        # print('******************************************************************************************')
        # print('当前目录路径：' + str(root))  # 当前目录路径
        # print('当前路径下所有子目录：' + str(dirs))  # 当前路径下所有子目录
        # print('当前路径下所有非目录子文件：' + str(files))  # 当前路径下所有非目录子文件

        for i in files:
            houzhui = os.path.splitext(i)[1]
            if houzhui == '.py':
                with open(root + '/' + i, 'r', encoding='UTF-8') as f:
                    contents = f.readlines()
                    # print(contents)
                    for cont in contents:
                        if keyword in cont:
                            print('***********************************************************'
                                  '***********************************************************'
                                  '***********************************************************')
                            print('\n关键字第' + str(time_show) + '次出现在文件：' + root + '/' + i)
                            time_show += 1
                            print('出现的语句为：' + cont.strip() + '\n')
                            file_name.append(root + '/' + i)
    print('-----------------------------------结果显示---------------------------------------')
    print('包含关键字【' + keyword + '】的文件有：')
    for j in file_name:
        print('        ' + j)


def main():
    keyword = 'text'
    file_path = 'C:/Users/Administrator/Desktop/Python WorkSpace'
    keyswords_search(keyword, file_path)


if __name__ == '__main__':
    main()
