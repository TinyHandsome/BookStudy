#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: batch_repair.py
@time: 2020/12/31 13:26
@desc: 【注意！】使用前一定要备份目标文件夹，否贼内容将被覆盖写入

    【v0.2】 新增增加css和删除css功能、操作记录，修改类名
    【v0.1】 批量修改目标版本
"""

from dataclasses import dataclass
import os
import re
from collections import Counter
from datetime import datetime
from properties import params


@dataclass
class CssDao:
    folder_path: str
    replace_version: str
    increase_version: str
    delete_version: str

    def __post_init__(self):
        # 运行记录，保存在目标文件夹下
        if not os.path.exists(self.folder_path):
            print('【错误！】目标文件夹不存在！')
            exit()

        file_name = 'run_record_' + datetime.strftime(datetime.now(), "%Y-%m-%d-%H-%M-%S")
        self.run_info = open(os.path.join(self.folder_path, file_name), 'w', encoding='utf-8')

    def run(self):
        """启动"""

        info_list = [self.replace_version, self.increase_version, self.delete_version]
        count_result = Counter(info_list)
        if count_result[None] != len(info_list) - 1:
            print('【错误！】配置文件中为None的数量不正确，请调整配置文件！')
            exit()

        index_info = -1
        for info in info_list:
            if info:
                index_info = info_list.index(info)
                break

        if index_info == -1:
            print('【错误！】这谁顶得住啊！联系管理员吧！')
            exit()

        self.walk_folder(index_info)
        self.run_info.close()

    def walk_folder(self, flag):
        """遍历文件夹"""
        for root, firs, files in os.walk(self.folder_path, topdown=False):
            for name in files:
                if name == 'index.html':
                    aim_path_file = os.path.join(root, name)
                    self.run_info.write(aim_path_file + ':\n\t')

                    if flag == 0:
                        self.replace_element_version(aim_path_file)
                    elif flag == 1:
                        self.increase_css(aim_path_file)
                    elif flag == 2:
                        self.delete_css(aim_path_file)

    def increase_css(self, aim_path_file):
        """增加css"""
        with open(aim_path_file, 'r+', encoding='utf-8') as f:
            lines = f.read()
            aim_lines = re.findall(r'(<link.*?(?:archer-)(.*?)(?:\.css\?version.*?)>)', lines)

            # 选取满足要求的第一个当模板
            template = aim_lines[0][0]
            template_replace = aim_lines[0][1]

            # 生成对应的字符串
            generate_css = template.replace(template_replace, self.increase_version)

            # 获取template的位置
            temp_index = lines.index(template)
            # 获取template后面的位置
            aim_index = temp_index + len(template)

            # 将生成的字符串放在template后面
            result = lines[:aim_index] + generate_css + lines[aim_index:]

            self.rewrite_file(f, result)
        self.run_info.write('增加css：' + self.increase_version + '\n')

    def search_css_info(self, aim_lines):
        """查找对应的版本号"""
        for css_line, css_version in aim_lines:
            if css_version == self.delete_version:
                return css_line, css_version
        print('【注意！】你输入的版本：' + self.delete_version + '未找到！请修改后再运行程序！')
        return None, None

    def delete_css(self, aim_path_file):
        """删除css"""
        with open(aim_path_file, 'r+', encoding='utf-8') as f:
            lines = f.read()
            aim_lines = re.findall(r'(<link.*?(?:archer-)(.*?)(?:\.css\?version.*?)>)', lines)
            css_line, css_version = self.search_css_info(aim_lines)
            if css_version is None:
                self.run_info.write('删除css：' + self.delete_version + '失败，未找到对应的version！\n')
                return None

            # 获取 css_line 的位置
            temp_index = lines.index(css_line)
            # 获取template后面的位置
            aim_index = temp_index + len(css_line)

            # 删掉原来中的内容
            result = lines[:temp_index] + lines[aim_index:]

            self.rewrite_file(f, result)
        self.run_info.write('删除css：' + self.delete_version + '\n')

    def replace_element_version(self, aim_path_file):
        """替换版本号"""
        with open(aim_path_file, 'r+', encoding='utf-8') as f:
            lines = f.read()

            # 这里可能有多个版本吧
            aim_words = re.findall(r'(?:archer-)(.*?)(?:\.css\?version)', lines)

            # 全部替换为目标结果
            result = lines
            for am in aim_words:
                result = result.replace(am, self.replace_version)

            self.rewrite_file(f, result)
        self.run_info.write('替换css：' + self.replace_version + '\n')

    def rewrite_file(self, f, result):
        """覆盖写入文件"""
        f.seek(0)
        f.truncate(0)
        f.write(result)


if __name__ == '__main__':
    CssDao(params['path'], params['element_for_replace'], params['element_for_increase'],
           params['element_for_delete']).run()
