import datetime
import time

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

from search_info import EpidemicPrevention, increase_speed
import pandas as pd


import password as pw

pd.set_option('display.max_columns', None)

# 最大重试次数
MAX_RETRY = 3


def login_and_enter_search(ep: EpidemicPrevention):
    ep.get_url(pw.url)

    input_code = input("请输入验证码：")

    username = ep.find_element_by_name('username')
    ep.click(username, 0)
    ep.send_key_to_input(username, pw.username)

    password = ep.find_element_by_name('password')
    ep.click(password, 0)
    ep.send_key_to_input(password, pw.password)

    code = ep.find_element_by_name('code')
    ep.click(code, 0)
    ep.send_key_to_input(code, input_code)

    btn = ep.find_element_by_class_name('layui-btn')
    ep.click(btn)
    ep.switch_latest_handle()

    pic = ep.find_element_by_class_name('wrapper-content-cateAndlist-content-bottom-img')
    ep.click(pic)
    ep.switch_latest_handle()


def search_id_and_name(ep: EpidemicPrevention, name, id):
    # 重置
    clear_btn = ep.find_element_by_xpath_contains_text('span', '重置')
    ep.click(clear_btn)

    # 输入姓名
    _name = ep.find_element_by_xpath("//input[@placeholder='姓名']")
    ep.click(_name, 0)
    ep.send_key_to_input(_name, name)

    # 输入身份证号
    _id = ep.find_element_by_xpath("//input[@placeholder='身份证号']")
    ep.click(_id, 0)
    ep.send_key_to_input(_id, id)

    # 点击查询
    search_btn = ep.find_element_by_xpath_contains_text('span', '查询')
    ep.click(search_btn)

    # 解析html，获取列名
    area = ep.find_element_by_xpath("//div[@class='wrap-outer cssId17']")
    cells = area.find_elements_by_xpath(".//tr/th/div[@class='cell']")
    columns = []
    for cell in cells:
        columns.append(cell.text)

    # 获取数据
    rows = ep.find_elements_by_xpath("//tr/td/div[@class='cell']/../..")
    result = []
    count = 1
    for row in rows:
        cells = row.find_elements_by_xpath(".//td/div[@class='cell']")
        temp_list = []
        for cell in cells:
            v = cell.text
            temp_list.append(v)

        # 省级结果处理
        if len(temp_list) == 5:
            detection_time = temp_list[3]
            detection_result = temp_list[4]
            temp_list = [count, '', '', detection_time, '', '省接口', detection_result]

        # 市级/区级 结果处理
        elif len(temp_list) == 6:
            # 检查index为2的是不是时间
            try:
                pd.to_datetime(temp_list[2])
                flag = True
            except:
                flag = False

            if flag:
                # 市级
                detection_result = temp_list.pop(-1)
                temp_list = [count] + temp_list[1:] + ['市接口', detection_result]
            else:
                # 区级
                detection_result = temp_list[-1]
                detection_organization = temp_list[1]
                sample_organization = temp_list[2]
                sample_time = temp_list[3]
                detection_time = temp_list[4]
                temp_list = [count, detection_organization, sample_time, detection_time, sample_organization, '区接口',
                             detection_result]

        result.append(temp_list)
        count += 1

    df = pd.DataFrame(result, columns=columns)
    df.set_index('序号', inplace=True)
    df.sort_values(by='检测时间', inplace=True, ascending=False, axis=0)

    # 检测时间处理，去空值，去重
    detection_time = df['检测时间'].dropna().drop_duplicates()
    sample_time = df['采样时间'].dropna().drop_duplicates()
    # 如果检测时间有，就用检测时间，没有则用采样时间
    dt_list = []
    for x, y in zip(pd.to_datetime(detection_time), pd.to_datetime(sample_time)):
        if not pd.isna(x):
            dt_list.append(x)
        else:
            if not pd.isna(y):
                dt_list.append(y)
            else:
                ...
    detection_time = pd.Series(dt_list).sort_values(ascending=False)
    # 【重要】如果一顿操作之后，竟然一个时间数据都没有，直接返回全空值
    if len(detection_time) == 0:
        return ['一条数据也没有啊大哥'] + [''] * 5

    # 开始处理业务逻辑和数据处理
    latest_detection_date = detection_time.iloc[0]
    if_now_detection = datetime.datetime.now().strftime('%Y-%m-%d') == latest_detection_date.strftime('%Y-%m-%d')
    main_result = [if_now_detection, latest_detection_date.strftime('%Y-%m-%d %H:%M:%S'),
                   detection_time.iloc[-1].strftime('%Y-%m-%d %H:%M:%S')]

    # 检查最近14天数据，最长核酸间隔，单位为天，以最近核酸时间作为标准往前推14天
    day_of_two_week = latest_detection_date - datetime.timedelta(days=14)
    day_of_one_month = latest_detection_date - datetime.timedelta(days=30)
    max_stamp_two_week = 0
    max_stamp_one_month = 0
    max_stamp = 0
    count_of_two_week = 0

    for s1, s2 in zip(detection_time.iloc[:-1], detection_time.iloc[1:]):
        delta = s1 - s2
        delta_hours = round(delta.days + delta.components.hours / 24, 2)
        if delta_hours > max_stamp:
            max_stamp = delta_hours

            if s1 > day_of_two_week:
                max_stamp_two_week = delta_hours
                count_of_two_week += 1
            if s1 > day_of_one_month:
                max_stamp_one_month = delta_hours

    main_result = main_result + [max_stamp_two_week, count_of_two_week, max_stamp_one_month, max_stamp]

    return main_result


def main():
    global driver
    # chrome_driver_path = 'E:/6-下载资源/chromedriver.exe'
    driver = webdriver.Chrome()
    ep = EpidemicPrevention(driver)
    ep.maximize_window()
    login_and_enter_search(ep)

    file_path = './datas/temp.xlsx'
    df = pd.read_excel(file_path)

    columns = ['今天是否做核酸', '最近核酸时间', '最远核酸时间', '最近两周核酸最长间隔', '最近两周核酸次数', '最近一个月核酸最长间隔', '历史核酸最长间隔']
    data = []
    index = 1
    for i in range(df.shape[0]):
        name = df.iloc[i, 0]
        id_card = df.iloc[i, 1]
        print('{}. 正在查询：{}'.format(str(index), name), '...')
        index += 1

        count = 1
        main_result = ['老是报错啊大哥'] + [''] * 5
        while True:
            if count > MAX_RETRY:
                break
            count += 1

            try:
                main_result = search_id_and_name(ep, name, id_card)
                break
            except StaleElementReferenceException as e:
                print('搞错了，再运行一次吧...')

        print(pd.Series(main_result, index=columns))
        data.append(main_result)

    result = pd.DataFrame(data, columns=columns)
    result.to_excel(datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.xlsx')
    print(result)


def test():
    global driver
    # chrome_driver_path = 'E:/6-下载资源/chromedriver.exe'
    driver = webdriver.Chrome()
    ep = EpidemicPrevention(driver)
    ep.maximize_window()
    login_and_enter_search(ep)
    temp_columns, main_result = search_id_and_name(ep, '', '')
    print(main_result)


if __name__ == '__main__':
    main()
    # test()
