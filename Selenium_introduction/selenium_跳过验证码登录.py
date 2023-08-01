# -*- coding: utf-8 -*-
# @Time    : 2022/10/13 10:43
# @Author  : Carlos
import time
from selenium.webdriver.chrome import options
# from selenium import webdriver

# # 1.获取浏览器cookies储存的路径 浏览器搜索 ”Edge//version/ “  C:\Users\carlos\AppData\Local\Microsoft\Edge\User Data\Default
# # 我们去掉后面的 \Default，然后在路径前加上「–user-data-dir=」就拼接出我们要的路径了。
# profile_directory = r'--user-data-dir=C:\Users\carlos\AppData\Local\Microsoft\Edge\User Data'
# opt=options
# opt.add_argument(profile_directory)
# driver = webdriver.Edge(options=opt)

# driver.get('https://www.tomtoc.cn/')

from selenium import webdriver



url='https://ys.endata.cn/BoxOffice/Movie'
def option_use(url):
    # 启动参数：
    profile_directory = (r" user-data-dir=C:\Users\carlos\AppData\Local\Google\Chrome\User Data")  # 把数据传入程序

    # ChromeOptions是chromedriver支持的浏览器启动选项。
    opt = webdriver.ChromeOptions()
    opt.add_argument(profile_directory)

    #设置为 headless 模式 无头浏览器
    # opt.add_argument('--headless')

    # 禁用GPU
    opt.add_argument('--disable-gpu')

    #设置窗口大小
    opt.add_argument("window-size=1024,768")

    # 彻底停用沙箱。
    opt.add_argument("--no-sandbox")

    opt.add_experimental_opt('excludeSwitches', ['enable-automation'])   # 防止网站发现我们使用模拟器

    driver = webdriver.Chrome(chrome_options=opt)

    driver.get('url')

    return driver


time.sleep(5)

option_use(url).quit()