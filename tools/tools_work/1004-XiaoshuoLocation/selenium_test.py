"""
    1. selenium节点定位：https://blog.csdn.net/huilan_same/article/details/52541680
"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "E:/6-下载资源/chromedriver.exe" 
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

tag_code = driver.find_element_by_xpath("//*[@data-index='0']/code")
class_operator = tag_code.find_element_by_class_name('token.operator')
print(class_operator.text)


driver.quit()