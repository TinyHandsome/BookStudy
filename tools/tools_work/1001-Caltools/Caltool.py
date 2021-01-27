#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: Caltools.py
@time: 2020/1/15 9:32
@desc: 小朋友计算小程序
        【version 1.0】 20200115 实现基本功能
        1. 输入数字a，计算a以内的加减法
"""
import random


class Caltool:
    def __init__(self):
        # 随机影子
        self.random_state = None
        random.seed(self.random_state)
        # 多少以内的加减法
        self.number_limit = 20
        # 生成多少个算术
        self.count = 5
        # 运算符包含
        self.operator = ['+', '-']
        # 统计正确率
        self.sum = 0
        # 序号统计
        self.xuhao = 0
        # 最后结果
        self.strings = ''
        # 计算式统计，防止重复
        self.lists = []

    def reset(self):
        self.xuhao = 0
        self.strings = ''
        self.sum = 0
        self.lists = []

    def check(self):
        if self.count == self.xuhao:
            return True
        else:
            return False

    def cal(self):
        # 开始
        while self.xuhao < self.count:
            x = random.randint(1, self.number_limit)
            y = random.randint(1, self.number_limit)

            ope = random.choice(self.operator)

            # 判断
            if ope == '+':
                result = x + y
                string = str(self.xuhao + 1) + '. ' + str(x) + ope + str(y)

            elif ope == '-':
                if x < y:
                    temp = x
                    x = y
                    y = temp
                result = x - y
                string = str(self.xuhao + 1) + '. ' + str(x) + ope + str(y)

            else:
                print('报错了，看看啥问题！')

            info = string + '=?'
            print(info)

            # 获取输入
            rr = input()
            try:
                int_rr = int(rr)
            except:
                print('只许输入数字哦，小朋友！')
                continue

            if int_rr == result:
                print('(√)恭喜你答对啦！')
                self.sum += 1
                flag = True
            else:
                print('(×)答错了哦！')
                flag = False

            self.strings += info + '\t\t你的答案：' + rr + '\t\t正确答案：' + str(result) + '\t\t' + ('√' if flag else '×') + '\n'

            # 序号+1
            self.xuhao += 1

        print('*' * 30)
        print('小朋友你的得分是：', int((self.sum / self.count) * 100), '分')
        print('*' * 30)
        print(self.strings)

    def next_ti(self):
        x = random.randint(1, self.number_limit)
        y = random.randint(1, self.number_limit)

        ope = random.choice(self.operator)

        # 初始化
        ti = None
        result = None
        string = None

        # 判断
        if ope == '+':
            result = x + y
            ti = str(x) + ope + str(y) + '=?'
            string = str(self.xuhao + 1) + '. ' + str(x) + ope + str(y) + '=?'

        elif ope == '-':
            if x < y:
                temp = x
                x = y
                y = temp
            result = x - y
            ti = str(x) + ope + str(y) + '=?'
            string = str(self.xuhao + 1) + '. ' + str(x) + ope + str(y) + '=?'

        else:
            pass

        # 检查是否超纲
        if result > self.number_limit:
            return self.next_ti()
        else:
            # 检查是否重复
            if ti not in self.lists:
                self.lists.append(ti)
                return ti, result, string
            else:
                return self.next_ti()


if __name__ == '__main__':
    tt = Caltool()
    tt.cal()
