"""
    爬虫403解决：https://blog.csdn.net/weixin_51111267/article/details/129045633
    bs4：https://blog.csdn.net/IT_arookie/article/details/82824620
"""

import random
import time

from curl_cffi import requests
from bs4 import BeautifulSoup
from chapter import Chapter

home = 'https://wufangdao.com'
url = '/html/9/9071/241891.html'
book_url_chapter1 = home + url

uas = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
]
proxy_list = [
    '183.95.80.102:8080',
    '123.160.31.71:8080',
    '115.231.128.79:8080',
    '166.111.77.32:80',
    '43.240.138.31:8080',
    '218.201.98.196:3128'
]


def analyse_url(aim_url=book_url_chapter1):
    headers = {
        'user-agent': random.choice(uas),
        'authority': 'wufangdao.com',
        "method": "GET",
        "scheme": "https",
        "path": aim_url,
    }

    response = requests.get(book_url_chapter1, headers=headers, impersonate="chrome101")
    content = response.text

    soup = BeautifulSoup(content, 'lxml')

    title = soup.find(class_='title').get_text()
    content = soup.find(class_='content').get_text()
    next_chap_url = soup.find(text='下一页').parent.attrs['href']
    print(next_chap_url)

    chap = Chapter(home=home, title=title, content=content, next_chap_url=next_chap_url)
    return chap


def run():
    with open('temp.txt', 'w', encoding='utf-8') as f:
        chap = analyse_url()
        f.write(str(chap))

        while chap.has_next_page():
            next_url = chap.get_next_page_url()
            chap = analyse_url(aim_url=next_url)
            f.write(str(chap))
            time.sleep(1 + 2 * random.random())


if __name__ == '__main__':
    run()
