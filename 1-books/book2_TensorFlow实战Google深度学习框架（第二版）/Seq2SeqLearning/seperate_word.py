#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: seperate_word.py
@time: 2019/4/1 14:34
@desc: 对处理好的中英文数据进行分词操作(demo)
"""
from stanfordcorenlp import StanfordCoreNLP
import jieba
import nltk
# nltk.download("punkt")

sentence1 = "大家想想，海洋占了地球面积的75％。"
sentence2 = "When you think about it, the oceans are 75 percent of the planet."
# nlp = StanfordCoreNLP('D:/python包/stanford-corenlp-full-2016-10-31', lang='zh')
# nlp2 = StanfordCoreNLP('D:/python包/stanford-corenlp-full-2016-10-31', lang='en')
# print(nlp.word_tokenize(sentence1))
# print(nlp2.word_tokenize(sentence2))

seg_list = jieba.cut(sentence1, cut_all=False)
tokens = nltk.word_tokenize(sentence2)
print(list(seg_list))
print(tokens)