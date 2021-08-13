#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: sql_seperate.py
@time: 2020/10/12 13:48
@desc: 根据粘贴的文档，获取输出的文档
        print颜色设置[https://www.cnblogs.com/matingfei/articles/8721635.html]
        输出exe文件：pyinstaller -F sql_seperate.py -i pic.ico
"""
import sys
import re
import pyperclip
from colored import printRed, printGreen, printYellow, printBlue

log = '更新日志：\n' + \
      '【v4.5 20201110】\n' + '\t1. 解决了字段前面有缩进会导致结果异常的问题\n' + \
      '【v4.4 20201015】\n' + '\t1. 如果检测有string默认选择y（逻辑：输入的是 "y"或""）\n' + '\t2. 增加字段的缩进\n' + \
      '【v4.3 20201013】\n' + '\t1. 在发现结果中有string之后，增加了删除string后缀的结果处理，并优化了选择逻辑\n' + \
      '【v4.2 20201013】\n' + '\t1. 增加了对输出结果是否有string的监控，防止因粘贴/原sql语句问题导致结果关键字后带有string\n' + '\t2. 显示输出中带有string的关键字，没问题的话直接粘贴就行\n' + \
      '【v4.1 20201013】\n' + '\t1. 修复了括号/括回单独一行无法识别报错的问题。\n' + '\t2. 新增了更新日志输出功能\n'


def print_log():
    """输出log"""
    printBlue(log)
    print('\n\n')


class SQLSeperateTool:
    def __init__(self, aim_list):
        self.aim_list = aim_list
        self.len1 = len(aim_list) - 3
        self.len2 = 0

        self.table_name = None

        # 检查行中是否string
        self.check_error = 0
        self.string_list = []

        # 保存两种结果
        self.result_uncheck = ''
        self.result_checked = ''

        # 是否检测string
        self.check_string = True

    def get_table_name(self, start_line):
        regex = re.compile(r'`(.+)`')
        result = regex.findall(start_line)
        if len(result) > 0:
            self.table_name = result[0]

    def deal_line(self, line: str):
        if line.lower().startswith('create table'):
            # 此时该行为第一行，可以搞到对应的数据库名
            self.get_table_name(line)
            return '', ''
        elif line.lower().startswith('comment ') or line.lower().startswith('partitioned by'):
            return '', ''
        else:
            result = ''
            self.len2 += 1
            line = line.lstrip()
            for word in line:
                if word != ' ' and word != '\t' and word != '\xa0':
                    result += word
                else:

                    # 检查返回的行的处理结果中是否有string
                    if 'string' in result:
                        self.check_error += 1
                        self.string_list.append(result)

                        pattern = re.compile(r'(.+)string')
                        repaired_rr = pattern.findall(result)[0]
                    else:
                        repaired_rr = result

                    result_output = '\t' + result + ',\n'
                    repaired_tt = '\t' + repaired_rr + ',\n'

                    return result_output, repaired_tt

            # 出现了字符串后面不跟空格等，就不要这一行，比如括号或括回
            return '', ''

    def get_results(self):
        """获取结果"""
        self.result_uncheck = 'select \n'
        self.result_checked = 'select \n'
        for line in self.aim_list:
            rr, rep_r = self.deal_line(line)
            self.result_uncheck += rr
            self.result_checked += rep_r
        self.result_uncheck = self.result_uncheck[:-2] + ' \n'
        self.result_checked = self.result_checked[:-2] + ' \n'
        if self.table_name is not None:
            self.result_uncheck += 'from ' + self.table_name
            self.result_checked += 'from ' + self.table_name

        # 检查结果中字段数是否一致
        if self.len2 != self.len1:
            printRed('【注意】输入和输出的关键字不一致！')
            if self.len2 - self.len1 != 3:
                printRed('--> 很明显，结果不正确，请检查输入或联系管理员...\n\n\n')
                self.check_string = False
            else:
                printYellow('--> 这可能是因为你只复制了中间的关键字部分，如果是则忽视该提醒！\n\n\n')
                pyperclip.copy(self.result_uncheck)
                self.check_string = True

        if self.check_string:
            if self.check_error > 0:
                printRed('【注意】结果中的关键字中发现  string  字段！（请检查下述字段，如果没问题，则可直接粘贴结果）')
                printRed('| ' + ' | '.join(self.string_list) + ' |')
                printYellow('【选择】是否需要去掉所有的string后缀？[y/n]（默认为y，直接回车就行）')
                choose = input()
                if choose == 'y' or choose == '':
                    pyperclip.copy(self.result_checked)
                    printGreen('--> 结果已经保存到剪贴板 <--\n\n\n')
                elif choose == 'n':
                    printRed('你选择了否！\n\n\n')
                    pyperclip.copy(self.result_uncheck)
                else:
                    printRed('【警告】你输入了非[y/n]的字符，我就当你选  否  了嗷！\n\n\n')
                    pyperclip.copy(self.result_uncheck)
            else:
                printGreen('--> 结果已经保存到剪贴板 <--\n\n\n')
                pyperclip.copy(self.result_uncheck)


def run():
    aim_list = []
    print('请粘贴sql语句，按回车键结束（输入q退出程序）:')
    while (True):
        x = input()
        if x.lower() == 'q':
            sys.exit(0)
        if x != '':
            aim_list.append(x)
        else:
            break

    if not aim_list:
        printRed('【注意】你什么都没有输入哦！！！\n\n\n')
        return -1

    ss = SQLSeperateTool(aim_list)
    ss.get_results()


if __name__ == '__main__':
    print_log()
    while (True):
        try:
            run()
        except Exception as e:
            printRed('【注意】出大问题，请联系管理员...')
            printRed('报错信息为：' + str(e) + '\n\n\n')

        # run()
