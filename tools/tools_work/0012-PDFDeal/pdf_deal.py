#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: pdf_deal.py
@time: 2020/12/1 10:26
@desc: 处理pdf
        [pdfminer](https://blog.csdn.net/fighting_no1/article/details/51038942)
        [pdfplumber](https://blog.csdn.net/weixin_48629601/article/details/107224376)
"""

# from pdfminer.pdfparser import PDFParser, PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import PDFPageAggregator
# from pdfminer.layout import LTTextBoxHorizontal, LAParams, LTTextBox
# from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

from dataclasses import dataclass
import pdfplumber


@dataclass
class PDFTool:
    def __post_init__(self):
        pass

    def parse_dpfplumber(self, path):
        # 打开pdf文件
        fp = open(path, 'rb')
        with pdfplumber.open(fp) as pdf:
            result = ''
            for page in pdf.pages:
                result += page.extract_text()
        fp.close()
        return result

    def parse_pdf(self):
        """解析目标pdf"""
        # 创建一个pdf文档分析器
        parser = PDFParser(fp)
        # 创建一个PDF文档
        doc = PDFDocument()
        # 链接分析器
        parser.set_document(doc)
        doc.set_parser(parser)

        # 提供初始密码，如果没有密码，就创建一个空字符串
        doc.initialize()

        # 检测文档是否提供txt转换，不提供就忽略
        if not doc.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            # 创建PDF，资源管理器，来共享资源
            rsrcmgr = PDFResourceManager()
            # 创建一个PDF设备对象
            laparams = LAParams()
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)
            # 创建一个PDF解释其对象
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            # 循环遍历列表，每次处理一个page内容
            # doc.get_pages() 获取page列表
            for page in doc.get_pages():
                interpreter.process_page(page)
                # 接受该页面的LTPage对象
                layout = device.get_result()
                # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
                # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
                # 想要获取文本就获得对象的text属性，
                for x in layout:
                    if (isinstance(x, LTTextBoxHorizontal)):
                        results = x.get_text()
                        print(results, end='')


if __name__ == '__main__':
    root_path = 'E:/【冲鸭】/【工作】1. 工作安排、文件存储/20201201-pdf处理/英文/'
    file_path = root_path + 'TDS_WHSI_0009_SA724 Silicone Adhesive_EN V5.0.pdf'
    PDFTool().parse_dpfplumber(file_path)
