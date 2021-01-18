#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: word2pdf.py
@time: 2020/9/11 11:03
@desc: 目标路径word批量转pdf
"""

from win32com.client import Dispatch
from os import walk
import os


class Word2PDFTool:

    def __init__(self):
        self.wdFormatPDF = 17
        self.word = Dispatch('Word.Application')

    def doc2pdf(self, input_file, typed):
        """
        word转pdf，如果type='.doc'
        :return:
        """
        doc = self.word.Documents.Open(input_file)
        doc.SaveAs(input_file.replace(typed, ".pdf"), FileFormat=self.wdFormatPDF)
        doc.Close()

    def close_word(self):
        self.word.Quit()

    @staticmethod
    def delete_file(file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("文件：", file_path, "不存在！")

    @staticmethod
    def batch_transfer(root_path, is_delete=False):
        dt = Word2PDFTool()
        for root, dirs, filenames in walk(root_path):
            for file in filenames:
                if file.endswith(".doc"):
                    typed = ".doc"
                elif file.endswith(".docx"):
                    typed = ".docx"
                else:
                    # print(file)
                    # print("文件类型不是doc或docx！")
                    # typed = None
                    continue

                full_file = root + "\\" + file
                dt.doc2pdf(full_file, typed)
                if is_delete:
                    dt.delete_file(full_file)

        dt.close_word()


if __name__ == "__main__":
    directory = "E:\\【工作】工作安排啊文件啊啥的选我\\20200911-批量word转pdf"
    Word2PDFTool.batch_transfer(root_path=directory, is_delete=True)
