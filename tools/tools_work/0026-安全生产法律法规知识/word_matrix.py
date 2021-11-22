#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: word_matrix.py
@time: 2021/11/22 10:52
@desc: 读取所有题干，进行词向量编码
"""

import jieba
from dataclasses import dataclass
from collections import Counter
from operator import itemgetter
import re
import warnings
import pandas as pd
from scipy.spatial import distance_matrix

pd.set_option('display.max_columns', None)


@dataclass
class WordMatrix:
    def __post_init__(self):
        self.ref = pd.read_excel('./datas/安全生产法律法规知识大考试题库.xlsx')
        self.vocab_path = './datas/words.vocab'
        self.vocab_dict = {}

    @staticmethod
    def clear_content(content):
        """去掉括号和空格"""
        return re.sub(r'\s|\(|\)|（|）', '', content)

    @staticmethod
    def get_jieba_words(line):
        return jieba.cut(line, cut_all=False)

    def get_clear_jieba_words(self, content):
        return self.get_jieba_words(self.clear_content(content))

    def get_vocab(self):
        contents = self.ref['题目'].values
        counter = Counter()

        # remove 括号和空格
        for line in contents:
            for word in self.get_clear_jieba_words(line):
                counter[word] += 1

        # 按照词频进行排序，这一步可以去掉毕竟不用我们替换地词频的词
        sorted_word_to_cnt = sorted(counter.items(), key=itemgetter(1), reverse=True)
        # 排序后的单词
        sorted_words = [x[0] for x in sorted_word_to_cnt]

        # 保存vocab
        with open(self.vocab_path, 'w', encoding='utf-8') as f:
            for w in sorted_words:
                f.write(w + '\n')

    def generate_vocab_dict(self):
        with open(self.vocab_path, 'r', encoding='utf-8') as f:
            sorted_words = f.readlines()
            sorted_words = [i.replace('\n', '') for i in sorted_words]

        for nn, ww in enumerate(sorted_words):
            self.vocab_dict.update({ww: nn})

    def apply_map_word_matrix(self, line):
        words = self.get_clear_jieba_words(line)
        words_counter = Counter(words)

        # 词对应的出现次数
        words_dict = {}
        for every_word, count in words_counter.items():
            words_dict.update({self.vocab_dict.get(every_word): count})
        return words_dict

    def generate_word_matrix(self):
        self.generate_vocab_dict()

        # 新建一列，类型为字典dict
        self.ref['词向量'] = self.ref['题目'].apply(self.apply_map_word_matrix)
        self.wv_matrix = pd.DataFrame(self.ref['词向量'].to_list())

    def locate_answer(self, aim_index):
        """获取ref中的答案"""
        answer = self.ref.loc[aim_index, '答案']
        info = self.ref.loc[aim_index, list(answer)]
        return answer, ', '.join(info.to_list())

    def get_answer(self, content):
        """获取指定content的答案"""
        warnings.warn("这个方法即将启用，因为下面有更好的获取所有的答案的方法", DeprecationWarning)
        # 获取content的词向量
        v_aim = self.apply_map_word_matrix(content)
        # 跟词向量合并
        temp_matrix = self.wv_matrix.append(v_aim, ignore_index=True).fillna(0)

        # 获得词向量矩阵
        dm = pd.DataFrame(distance_matrix(temp_matrix.values, temp_matrix.values), index=temp_matrix.index,
                          columns=temp_matrix.index)
        # 取最后一行的值，再去掉最后一样 自己跟自己的距离 即808的值，之后的第一个值的编号
        aim_index = dm.iloc[-1, :-1].sort_values().index[0]
        return self.locate_answer(aim_index)

    def get_answers(self, contents):
        """直接获取所有的答案"""
        answers = []
        temp_matrix = self.wv_matrix
        for content in contents:
            v_aim = self.apply_map_word_matrix(content)
            temp_matrix = temp_matrix.append(v_aim, ignore_index=True).fillna(0)

        # 获得词向量矩阵
        dm = pd.DataFrame(distance_matrix(temp_matrix.values, temp_matrix.values), index=temp_matrix.index,
                          columns=temp_matrix.index)
        # 获取后面多行
        start_index = self.wv_matrix.index[-1] + 1
        results = dm.loc[start_index:, :]

        for t in results.index:
            # 因为是loc，所以是前闭后闭
            line = results.loc[t, :start_index - 1]
            aim_index = line.sort_values().index[0]
            answers.append(self.locate_answer(aim_index))
        return answers


if __name__ == '__main__':
    test1 = "生产经营单位应当向从业人员如实告知作业场所和工作岗位存在的（）。"
    test2 = "《安全生产法》规定：事故调查报告应当依法及时向（）公布。"
    test = [test1, test2]
    wm = WordMatrix()
    wm.generate_word_matrix()
    # wm.get_answers(test)
    print(wm.get_answer(test1))
