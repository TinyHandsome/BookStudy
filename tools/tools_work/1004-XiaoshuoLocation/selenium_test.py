"""
    1. selenium节点定位：https://blog.csdn.net/huilan_same/article/details/52541680
    2. Selenium自动化之JS增删改查操作元素的属性：https://blog.csdn.net/DansonC/article/details/99398096
"""


from system_hotkey import SystemHotkey
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from vscode_settings_tool import VSCODE
from xiaoshuo_locatoin import XiaoshuoLocation
from run_cmd import run_cmd
import time

from threading import Thread

CURRENT_PAGE_PARAM = "thiefBook.currPageNumber"
BOOK_PATH = "thiefBook.filePath"
PAGESIZE = "thiefBook.pageSize"


class SeleniumChrome:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option(
            "debuggerAddress", "127.0.0.1:9222")
        chrome_driver = "E:/6-下载资源/chromedriver.exe"
        self.driver = webdriver.Chrome(
            chrome_driver, chrome_options=chrome_options)

        # 获取目标节点
        tag_code = self.driver.find_element_by_xpath(
            "//*[@data-index='0']/code")
        self.class_operator = tag_code.find_element_by_class_name(
            'token.operator')

        # vscode工具
        self.vs = VSCODE()
        vscode_json_dict = self.vs.get_vscode_json_dict()
        # 当前页码
        self.current_page = int(vscode_json_dict.get(CURRENT_PAGE_PARAM))
        book_path = vscode_json_dict.get(BOOK_PATH)
        page_size = vscode_json_dict.get(PAGESIZE)

        # xs
        self.xs = XiaoshuoLocation(page_size, book_path)

    def insert_new_line(self, new_line):
        self.driver.execute_script(
            "arguments[0].innerText='';let a = document.createElement('label');a.innerText=arguments[1];" +
            # 设置字体没有作用啊马飞
            "a.style.fontSize='50px!important';" + 
            "arguments[0].appendChild(a);", self.class_operator, '+' + new_line + '+')

    def alert_str(self, ss):
        self.driver.execute_script(
            f"alert(arguments[0])", ss
        )

    def insert_new_line_by_page(self, page):
        line = self.xs.get_aim_line_info(page)
        self.insert_new_line(line)

    def close(self):
        # 更新vscode中配置的页码
        self.vs.update_param(CURRENT_PAGE_PARAM, self.current_page)
        self.driver.close()
        self.driver.quit()

    def start_read(self):
        self.insert_new_line_by_page(self.current_page)

    def next_page(self):
        self.current_page += 1
        self.insert_new_line_by_page(self.current_page)

    def previous_page(self):
        self.current_page -= 1
        self.insert_new_line_by_page(self.current_page)

    def hide(self):
        self.insert_new_line('+')


class KeyOperator:
    def __init__(self) -> None:
        self.sc = SeleniumChrome()
        self.sh = SystemHotkey()
        self.sh.register(('j',), callback=lambda e: self.sc.next_page())
        self.sh.register(('k',), callback=lambda e: self.sc.previous_page())
        self.sh.register(('l',), callback=lambda e: self.sc.start_read())
        self.sh.register(('h',), callback=lambda e: self.sc.hide())
        self.sh.register(('q',), callback=lambda e: self.close())

        self.flag = True

    def close(self):
        self.sc.hide()
        self.sc.close()
        self.flag = False


if __name__ == '__main__':
    # 获取当前工作目录路径
    current_path = os.getcwd()
    sys.path.append(current_path)

    def run1():
        print(1, 'start')
        run_cmd(
            r'E:/1-Work/3-Code/tools/tools_work/1004-XiaoshuoLocation/open_chrome.bat')
        print(1, 'end')

    def run2():
        print(2, 'start')
        ko = KeyOperator()
        ko.sc.alert_str('加载完毕')

        while ko.flag:
            # print(ko.flag)
            time.sleep(1)
        print(2, 'end')

    # 当一个线程设置为daemon线程时，主线程结束时，不会因为daemon线程还没有结束运行而阻塞
    t1 = Thread(target=run1, daemon=True)
    t2 = Thread(target=run2)
    t1.start()
    t2.start()
