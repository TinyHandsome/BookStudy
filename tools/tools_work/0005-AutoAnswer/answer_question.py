#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: answer_question.py
@time: 2020/9/25 15:22
@desc: 我是一个莫的感情的答题工具
"""


class Subject:
    """题的类"""

    def __init__(self, number: int, first: str, last: str, answer: str, middle_list: [], raw: str):
        self.number = number
        self.first = first
        self.last = last
        self.middle_list = middle_list
        self.answer = answer
        self.raw = raw

    def check_words(self, first_word, last_word):
        """根据第一个和最后一个关键词查询答案"""
        if first_word in self.first and last_word in self.last:
            return True
        else:
            return False

    def get_subject(self):
        return self.raw + '\n' + '-----> ' + self.answer + ' <-----\n'


class AnswerTool:

    def __init__(self, file_path):
        self.file_path = file_path
        # 答案字典，编号：题
        self.subjects = []

        # 初始化
        self.generate_subejects()

    def generate_subejects(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.readlines()
            content.remove('\n')
            for cc in content:
                real_cc = cc.replace('\n', '')

                # 题目编号获取
                number = real_cc.split('.')[0]
                # 答案获取
                answer = real_cc.split('：')[-1]
                rr = real_cc.replace('：' + answer, '')

                # 优化答案为对错的答案
                if answer == '对':
                    answer = '【A】对'
                elif answer == '错':
                    answer = '【B】错'

                # 去掉标题和答案的内容
                rc = real_cc.replace(number + '. ', '').replace('：' + answer, '')
                rc_list = rc.split('，')

                head = rc_list.pop(0)
                end = rc_list.pop(-1)

                # 生成类
                temp_subject = Subject(int(number), head, end, answer, rc_list, rr)
                self.subjects.append(temp_subject)

    def get_subject(self, first_word, last_word):
        """根据第一个和最后一个关键词查询答案，如果结果有多个，通过中间list筛选"""
        results = []
        for s in self.subjects:
            if s.check_words(first_word, last_word):
                results.append(s)

        # if len(results) > 1:

        return results

    def cmd_gui(self):
        x = input("请输入前后关键词，用空格隔开（输入q结束）：\n").strip()
        if x == 'q':
            exit()

        x_list = x.split(" ")

        if len(x_list) != 2:
            print("请输入正确的关键字！\n")
        else:
            first = x_list[0]
            last = x_list[1]
            results = self.get_subject(first, last)

            if len(results) != 0:
                for c in results:
                    print(c.get_subject())
            else:
                print("查无此问题！\n")

    def test_cmd(self):
        while (1):
            self.cmd_gui()


if __name__ == '__main__':
    at = AnswerTool('./题题题.md')
    at.test_cmd()
