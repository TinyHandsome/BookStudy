#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: seperate_word_en.py
@time: 2019/4/7 15:37
@desc: 处理好的英文数据进行分词操作
"""

from stanfordcorenlp import StanfordCoreNLP
import time


path = 'D:/Python3Space/Seq2SeqLearning/'
en_path = path + 'train.en'
zh_path = path + 'train.zh'

nlp = StanfordCoreNLP('D:/python包/stanford-corenlp-full-2016-10-31', lang='zh')
# en = open(path + 'test.en', 'w', encoding='utf-8')
zh = open(path + 'test.zh', 'w', encoding='utf-8')
with open(zh_path, 'r', encoding='utf-8') as f:
    data = f.readlines()
    for text in data:
        print(text)
        if text != "\n":
            fenci = nlp.word_tokenize(text)
            sen = ' '.join(fenci)
            zh.write(sen + '\n')
        else:
            zh.write('\n')

zh.close()