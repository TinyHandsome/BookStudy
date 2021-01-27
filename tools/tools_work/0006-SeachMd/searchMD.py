#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: searchMD.py
@time: 2020/8/28 10:36
@desc: 根据文件路径查询md后缀文件中，目标行和所属文件
"""
import os


class Result:
    """查询的结果类"""

    def __init__(self, number, times, file_path, line_info, more_info=None):
        self.number = number
        self.times = times
        self.file_path = file_path

        # 文件路径加编号
        self.number_file_path = str(self.number) + ". " + self.file_path
        # 对应的行
        self.line_info = line_info
        # 对应行的显示
        self.line_play = '    ' + self.line_info.strip()
        # 行以下的信息
        self.more_info = more_info
        # 更多信息的显示
        self.more_play = ''
        for line in self.more_info.split('\n'):
            self.more_play += '    ' + line + '\n'

    def print_result(self, is_print=True):
        """书否打印结果"""
        if is_print:
            print(self.number_file_path)
            print(self.line_info)

    def print_time(self, time, is_print=True):
        """检测该结果是否是最优结果"""
        if self.times == time:
            self.print_result(is_print)
            return True
        else:
            return False

    def cal_start_end(self, t_index, s, e):
        start = t_index[:-1] + str(s)
        end = t_index[:-1] + str(e)
        return start, end

    def get_link_location(self, t_index):
        """获取连接的颜色定位"""
        link_index_start = self.number_file_path.index('.') + 2
        link_index_end = len(self.number_file_path)
        link = self.number_file_path[link_index_start:]
        start, end = self.cal_start_end(t_index, link_index_start, link_index_end)

        return start, end, link

    def get_key_words_locations(self, key_words, t_index):
        """根据关键字定位每个关键字在句子中的位置（这里两边去空了）"""
        words = key_words.split(' ')

        se_list = []
        # 要把关键字和句子都转换为小写，这样才能知道位置鸭
        lower_sentence = self.line_play.lower()
        for word in words:
            word = word.lower()
            if word in lower_sentence:
                link_index_start = lower_sentence.index(word)
                link_index_end = link_index_start + len(word)
                start, end = self.cal_start_end(t_index, link_index_start, link_index_end)
                se_list.append((start, end))

        return se_list


class SearchMD:
    """查询md的类"""

    def __init__(self, path, aim_name):
        # 需要遍历的文件夹
        self.file_path = path
        # 要查找的字段，字符串，查询的关键词用空格隔开
        self.aim_name = aim_name
        # 统计找到的个数
        self.count = 0
        # 找到的结果
        self.results = []
        # 找到的最大关键字结果
        self.aim_results = []

    def get_max_time(self):
        """根据搜索结果，获取最大的出现次数"""
        max = 0
        for r in self.results:
            if max < r.times:
                max = r.times

        return max

    def findMdFile(self, path=None, is_print=True):
        """遍历目标路径"""
        if path is None:
            path = self.file_path

        # 文件名和文件路径记录
        files_count = []

        # topdown --可选，为 True，则优先遍历 top 目录，否则优先遍历 top 的子目录(默认为开启)。
        # 如果 topdown 参数为 True，walk 会遍历top文件夹，与top 文件夹中每一个子目录。
        for root, dirs, files in os.walk(path, topdown=False):
            # root：根目录
            # dirs：根目录的文件夹list
            # files：根目录的文件list
            for name in files:
                absolute_path = os.path.join(root, name).replace('\\', '/')
                if name.endswith(".md"):
                    files_count.append([name, absolute_path])

                    # 处理md文件
                    self.dealMD(absolute_path)

        self.get_max_results(is_print)

    def get_max_results(self, is_print=True):

        if self.count == 0:
            if is_print:
                print('未找到鸭。。。')
        else:
            # 输出关键字最多的结果
            max_time = self.get_max_time()
            for rr in self.results:
                if rr.print_time(max_time, is_print):
                    self.aim_results.append(rr)
                    # print(rr.more_info)

    def get_moreinfo(self, lines, current_hang, ex_hang=20):
        """获取更多的信息，不包括自己"""
        nr = len(lines)
        result = ''
        for i in range(ex_hang):
            aim_hang = current_hang + i + 1
            if aim_hang < nr:
                if lines[aim_hang].strip() != '':
                    result += lines[aim_hang].strip() + '\n'
        return result

    def dealMD(self, mdFile, name=None):
        """寻找该md中是否有对应的字段"""

        if name is None:
            name = self.aim_name

        with open(mdFile, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                line = lines[i]
                cc = self.checkIFIN(name, line)
                if cc > 0:
                    self.count += 1
                    more_info = self.get_moreinfo(lines, i)
                    rr = Result(self.count, cc, mdFile, line, more_info)
                    self.results.append(rr)

    def checkIFIN(self, aim_name, line):
        """检查是否在句子中"""
        cc = 0

        names = aim_name.strip().split(' ')
        for an in names:
            for name in an.split(" "):
                if name.lower() in line.lower():
                    cc += 1

        # 返回关键字出现的次数，2，就是两个关键字在该行都出现了
        return cc


if __name__ == '__main__':
    md = SearchMD('E:\\【冲鸭】\\【工作】2. 工作记录、笔记和总结', 'HWMS ： 管理 34')
    md.findMdFile()
