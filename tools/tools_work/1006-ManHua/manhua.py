#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: manhua.py
@time: 2021/10/25 13:30
@desc: 《杀戮都市》漫画获取所写脚本 end chapter 2766138
"""
import os
import time
from io import BytesIO
from system_hotkey import SystemHotkey

import requests
from PIL import Image
from dataclasses import dataclass

root_url = 'https://res99.shut123.com/image/view/'
save_path = 'E:/img_temp/'


@dataclass
class ManHua:
    start_chapter = 2766135
    end_chapter = 2766138
    page = 0

    def __post_init__(self):
        self.hk = SystemHotkey()
        self.current_save_path = save_path + str(self.start_chapter) + '/'
        self.hk.register(('control', 'e'), callback=lambda e: self.next_page())

    def update_save_path(self):
        self.current_save_path = save_path + str(self.start_chapter) + '/'

    def get_img(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
        }
        url = root_url + str(self.start_chapter) + '/' + str(self.page) + '.webp'
        a = requests.get(url, headers=headers)
        if a.status_code == 404:
            raise Exception('访问被拒绝，返回代码为：', a.status_code)
        f = BytesIO(a.content)
        img = Image.open(f)
        if img.mode == 'P' or img.mode == 'RGBA':
            img = img.convert('RGB')
        return img

    def show_img(self, img):
        img.show()

    def next_page(self):
        self.page += 1

    def next_chapter(self):
        self.page = 0
        self.start_chapter += 1
        self.update_save_path()
        return self.start_chapter > self.end_chapter

    def save_img(self, img):
        if not os.path.exists(self.current_save_path):
            os.makedirs(self.current_save_path)

        img.save(self.current_save_path + str(self.page) + '.jpg')


if __name__ == '__main__':
    mh = ManHua()
    while True:
        try:
            print('current location:', mh.start_chapter, mh.page)
            img = mh.get_img()
            mh.save_img(img)
            mh.next_page()
        except Exception as e:
            print("an exception happened: ", e.args)
            if mh.next_chapter():
                break
            print("the latest save path: ", mh.current_save_path)
        time.sleep(0.5)
