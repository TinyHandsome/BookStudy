#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: Topic.py
@time: 2020/8/15 7:57
@desc: 题和答案的类
"""
from collections import OrderedDict


class Table:
    """【问卷】问卷名，说明，题的集合"""

    def __init__(self, file_path):
        self.theme = None
        self.statement = None
        self.statement_context = ""
        self.file_path = file_path
        self.topics = []
        # 记录问题的题号
        self.start_q = 0
        # 记录每题的答案
        self.answes = OrderedDict()

    def get_topics_length(self):
        """获取题目的个数"""
        return len(self.topics)

    def show_topic(self):
        # 获取题和选项
        topic = self.topics[self.start_q - 1]
        text = ""
        text += (str(self.start_q) + ". ")
        text += topic.print_qa()
        # topic.get_user_choices()

        return text

    def show_theme_statement(self):
        text = ""
        text += self.statement + ": \n"
        text += self.statement_context
        return text

    def init_grades(self):
        """初始化分数记录"""
        for i in range(self.get_topics_length()):
            self.answes[i + 1] = [0] * 10

    def set_grades(self, grades):
        """设置分数"""
        self.answes[self.start_q] = grades

    def file2questionnaire(self, file=None):
        """用来解析文档中的数据，解析为一个问卷"""

        # 说明数据和开始记录说明数据的标记
        statement_flag = False
        # 选项数据和开始记录选项数据的标记
        choice_flag = False
        # 开始计数
        num_start = 1

        if file is not None:
            self.file_path = file
        with open(self.file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                line = line.replace("\n", "")

                if line.startswith("# "):
                    # 读取到问卷名
                    self.theme = line.replace("# ", "")

                # 记录选项数据
                if choice_flag and line != "" and not line.startswith("### "):
                    new_topic.answer.append(line)

                if line.startswith("### "):
                    # 问题
                    question = line.replace("### ", "")
                    # 如果选项flag没开，则开启选项flag；如果开了，则建立第一个Topic保存起来，清空前一个内容
                    if not choice_flag:
                        # 说明文件记录完毕，关闭flag和保存说明文件，打开choice_flag
                        statement_flag = False
                        choice_flag = True
                    else:
                        self.topics.append(new_topic)
                        num_start += 1
                    new_topic = Topic(num_start, question, [])

                # 记录说明数据
                if statement_flag and line != "":
                    self.statement_context += line + "\n"
                if line.startswith("## "):
                    # 读取到说明
                    self.statement = line.replace("## ", "")
                    statement_flag = True

                # 收尾处理，如果到最后了，也要保存最后一个topic
                if line == lines[-1].replace("\n", ""):
                    self.topics.append(new_topic)

        # 导入文件后，初始化分数
        self.init_grades()


class Topic:
    """【题】题号，问题，答案"""

    def __init__(self, num, question, answer):
        """
        初始化该类
        :param num: 题的编号
        :param question: 问题，str
        :param answer: 答案，list
        """
        self.num = num
        self.question = question
        self.answer = answer
        self.user_choices = []

    def print_qa(self):
        """
        输出题目和答案，并排版
        """
        text_temp = ""
        answer_index = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        # 输出题
        text_temp += self.question + "\n\n"
        # 输出选项
        for i in range(len(self.answer)):
            index_a = answer_index[i]
            text_temp += index_a + '. '
            text_temp += self.answer[i] + "\n"
        # 空一行
        text_temp += "\n"
        return text_temp


class Result:
    def __init__(self, path):
        self.result_dict = OrderedDict()
        self.grades_labels = None
        self.path = path
        self.results = [0] * 10

        self.deal_file()

    def deal_file(self):
        with open(self.path, 'r') as f:
            lines = [x.strip('\n') for x in f.readlines() if x != '\n']
            self.grades_labels = lines[-1].split(',')
            for i in range(len(lines) - 1):
                self.result_dict[i + 1] = lines[i]

    def count_grade(self, answers):
        """计算各个题对应的分数，key都是题"""
        for k, v in self.result_dict.items():
            grades = answers[k]
            zimus = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

            # 将选项和打分构建为字典
            temp_dict = OrderedDict()
            for i in range(len(grades)):
                temp_dict[zimus[i]] = grades[i]

            # 将v的字母对应分数：
            aim_grades = []
            aim_zimu = v.split(',')

            start = 0
            for zm in aim_zimu:
                aim_g = temp_dict[zm]
                aim_grades.append(aim_g)
                self.results[start] += aim_g
                start += 1

        # temp_ord = OrderedDict()
        # for k, v in zip(self.grades_labels, self.results):
        #     temp_ord[k] = v


if __name__ == "__main__":
    # table = Table("E:/工作数据表/20200814-性格测试表+ppt模板/管理团队角色问卷.md")
    # table.file2questionnaire()
    #
    # table.show_theme_statement()
    # start_q = 1
    # for topic in table.topics:
    #     print(str(start_q) + ". ", end="")
    #     topic.print_qa()
    #     topic.get_user_choices()
    #     start_q += 1

    r = Result('E:/工作数据表/20200814-性格测试表+ppt模板/管理团队角色问卷（答案排版）.md')
    r.count_grade(OrderedDict({1: list(range(10)), 2: list(range(10))}))
