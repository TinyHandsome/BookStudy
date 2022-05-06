#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: articleSpider.py
@time: 2022/5/5 8:26
@desc: 
"""

from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy import Spider
from wikiSpider.items import Article


class ArticleSpider(Spider):
    name = "article"
    allowed_domains = ["en.wikipedia.beta.wmflabs.org"]
    start_urls = [
        "https://en.wikipedia.beta.wmflabs.org/wiki/Main_Page",
        "https://en.wikipedia.beta.wmflabs.org/wiki/Python_%28programming_language%29"
    ]
    rules = [Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*$'),), callback="parse_item", follow=True)]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is: " + title)
        item['title'] = title
        return item
