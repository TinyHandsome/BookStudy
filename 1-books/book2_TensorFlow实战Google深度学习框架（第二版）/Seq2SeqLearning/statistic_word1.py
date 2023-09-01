#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: statistic_word1.py
@time: 2019/4/22 9:36
@desc: 首先按照词频顺序为每个词汇分配一个编号，然后将词汇表保存到一个独立的vocab文件中。
"""

import codecs
import collections
from operator import itemgetter


def deal(lang):
    # 训练集数据文件
    ROOT_PATH = "D:/Python3Space/Seq2SeqLearning/"
    if lang == "zh":
        RAW_DATA = ROOT_PATH + "test.zh"
        # 输出的词汇表文件
        VOCAB_OUTPUT = ROOT_PATH + "zh.vocab"
        # 中文词汇表单词个数
        VOCAB_SIZE = 4000
    elif lang == "en":
        RAW_DATA = ROOT_PATH + "test.en"
        VOCAB_OUTPUT = ROOT_PATH + "en.vocab"
        VOCAB_SIZE = 10000
    else:
        print("what?")

    # 统计单词出现的频率
    counter = collections.Counter()
    with codecs.open(RAW_DATA, "r", "utf-8") as f:
        for line in f:
            for word in line.strip().split():
                counter[word] += 1

    # 按照词频顺序对单词进行排序
    sorted_word_to_cnt = sorted(counter.items(), key=itemgetter(1), reverse=True)
    sorted_words = [x[0] for x in sorted_word_to_cnt]

    # 在后面处理机器翻译数据时，出了"<eos>"，还需要将"<unk>"和句子起始符"<sos>"加入
    # 词汇表，并从词汇表中删除低频词汇。在PTB数据中，因为输入数据已经将低频词汇替换成了
    # "<unk>"，因此不需要这一步骤。
    sorted_words = ["<unk>", "<sos>", "<eos>"] + sorted_words
    if len(sorted_words) > VOCAB_SIZE:
        sorted_words = sorted_words[:VOCAB_SIZE]

    with codecs.open(VOCAB_OUTPUT, 'w', 'utf-8') as file_output:
        for word in sorted_words:
            file_output.write(word + "\n")


if __name__ == "__main__":
    # 处理的语言
    lang = ["zh", "en"]
    for i in lang:
        deal(i)
