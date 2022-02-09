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
        https://res99.shut123.com/image/view/2766078/9.webp
        1. [Max retries exceeded with url (Caused by NewConnectionError(urllib3.connection...)](https://blog.csdn.net/wangziyang777/article/details/106670320/)
        2. [OSError: encoder error -2 when writing image file](https://blog.csdn.net/kasagawa/article/details/7841935)
"""
import os
import warnings
from dataclasses import dataclass
from io import BytesIO

import requests
from PIL import Image
from PIL import ImageFile, UnidentifiedImageError

from djangoProject.settings import MY_TEMP_IMG_URL
from funcs.my_base_funcs.file_folder_funcs import if_path_not_exists_create_path

# 可能存在数据丢失的情况，报错：【OSError: image file is truncated】，这里设置加载截断的图片
from funcs.my_base_funcs.time_funcs import get_now_year_month_day, get_now_hour_minute_second, \
    sleep_random_and_base_pause_time

ImageFile.LOAD_TRUNCATED_IMAGES = True


@dataclass
class GetUrlPic:
    root_url: str
    save_path = None
    name = None
    format = 'png'

    # 每获取一个图片链接的暂停时间 1 + [0-1]
    every_pic_pause_second = 1

    def __post_init__(self):

        # 处理保存的名字
        if self.name is None:
            self.name = get_now_hour_minute_second()
        if self.save_path is None:
            self.save_path = os.path.join(MY_TEMP_IMG_URL, get_now_year_month_day())

    @staticmethod
    def generate_long_img(chapter_long_imgs):
        """垂直拼接图片，宽为所有图片最宽，长为所有图片长的和"""
        y = sum([img.size[1] for img in chapter_long_imgs])
        x = max([img.size[0] for img in chapter_long_imgs])
        long_img = Image.new('RGB', (x, y))

        current_loc = (0, 0)
        for img in chapter_long_imgs:
            long_img.paste(img, current_loc)
            current_loc = (current_loc[0], current_loc[1] + img.size[1])

        return long_img

    def save_img(self, img, suffix_name=''):
        """
        保存图片
        :param img: 图片
        :param name: 保存的图片名称，没有的话，默认为章节名称
        """

        # 检查路径是否存在，否则就创建路径
        if_path_not_exists_create_path(self.save_path)

        # 保存图片时，需要考虑设置MAXBLOCK，因为大图容易报错
        save_file_path = self.save_path + self.name + suffix_name + '.' + self.format
        img.save(save_file_path, optimize=True)
        return save_file_path

    def save_imgs(self, imgs):
        """
        【该方法已弃用】保存多个照片
        """
        warnings.warn('该方法已弃用，保存多个chapter的时候，每获取一个保存一个', DeprecationWarning)
        count = 1
        for img in imgs:
            self.save_img(img, '_' + str(count))
            count += 1
        return self.save_path

    def get_img(self, aim_chapter=None, aim_page=1, page_zero_fill=0, pic_format='jpg'):
        """获取路径的图片"""

        # 这里修复连接次数太多导致的达到最大重试次数，以至于无法连接的问题
        # 1. 请求头上加 headers = {'Connection':'close'}
        # 2. s = requests.session() s.keep_alive = False
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            'Connection': 'close',
        }

        if page_zero_fill == 0:
            real_page = str(aim_page)
        else:
            real_page = str(aim_page).zfill(page_zero_fill)

        if aim_chapter:
            url = self.root_url + str(aim_chapter) + '/' + real_page + '.' + pic_format
        else:
            url = self.root_url + real_page + '.' + pic_format

        # 这里需要加上请求头哦
        a = requests.get(
            url, headers=headers,
            # verify=False
        )
        s = requests.session()
        s.keep_alive = False

        # 404说明没有下一页啦
        if a.status_code == 404:
            return 404, url

        f = BytesIO(a.content)

        # 如果检测到图片无法识别，直接给一个空白页好了
        try:
            img = Image.open(f)
        except UnidentifiedImageError as e:
            img = Image.new('1', (256, 256), 1)

        if img.mode == 'P' or img.mode == 'RGBA':
            img = img.convert('RGB')
        a.close()

        # 每搞一次暂停1-2秒
        sleep_random_and_base_pause_time(self.every_pic_pause_second)

        return img, url

    def get_chapter(self, aim_chapter=None, start_page=1, end_page=None, page_zero_fill=0, pic_format='jpg'):
        """
        获取对应的章节，并组合保存到目标文件夹中
        """
        chapter_long_imgs = []
        while True:
            img, url = self.get_img(aim_chapter, start_page, page_zero_fill, pic_format)

            if img == 404 or start_page - 1 == end_page:
                # 没有搞到图片的话，就结束啦
                if not chapter_long_imgs:
                    return None
                else:
                    long_img = self.generate_long_img(chapter_long_imgs)

                    # 是否保存
                    save_file_path = self.save_img(long_img)
                    return long_img
            else:
                # 合成长图，并保存
                print(url)
                chapter_long_imgs.append(img)
                start_page += 1

    def get_chapters(self, start_chapter, start_page=1, end_page=None, page_zero_fill=0, pic_format='jpg',
                     pic_limit=None):
        """获取所有的chapter"""

        pic_count = 0
        while True:
            # 当前合成图片计数
            pic_count += 1
            if pic_limit is None:
                ...
            else:
                if pic_limit > 0:
                    pic_limit = pic_limit - 1
                else:
                    break

            long_img = self.get_chapter(start_chapter, end_page, start_page, page_zero_fill, pic_format)
            if long_img:
                self.save_img(long_img, suffix_name='_' + str(pic_count))
            else:
                # 如果long_img没有内容，即第一张图片也没搞到，说明该chapter的url无效，所以图片收集完了
                print('采集完毕...', '共采集了', pic_format, '个图...')
                return
            start_chapter += 1


if __name__ == '__main__':
    # 测试1
    root_url = 'https://filelearning.whchem.com/Moudle/NetLearning/upload/CWFile/6a8f87cc-fdc3-4f1a-8a90-1a0093d4f5e9/course/'
    gup = GetUrlPic(root_url)
    gup.get_chapter(None, 1, 1, 6)

    # 测试2
    # root_url = 'https://img.dongman.la/file/comicbook/s/slds/'
    # gup = GetUrlPic(root_url)
    # gup.get_chapters(1, 1, None, 4, 'jpg', 2)
