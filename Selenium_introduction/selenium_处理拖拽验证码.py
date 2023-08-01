# -*- coding: utf-8 -*-
# @Time    : 2022/10/12 15:59
# @Author  : Carlos

from selenium.webdriver import Edge
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

from chaojiying_Python.chaojiying import Chaojiying_Client
import time


# 2.处理被浏览器识别为自动化测试工具
option = Options()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument('--disable-blink-features=AutomationControlled')

web = Edge(options=option)

# 进入tomtoc 登陆界面
web.get("https://www.tomtoc.cn/login")
time.sleep(0.5)

# 选择用户名登录
web.find_element(By.XPATH,'//*[@id="loginBg"]/div[1]/div/div[1]/span[2]').click()
time.sleep(1)

# 输入用户名和密码
web.find_element(By.XPATH,'//*[@id="loginBg"]/div[1]/div/div[3]/input[1]').send_keys('Remi')
web.find_element(By.XPATH,'//*[@id="loginBg"]/div[1]/div/div[3]/input[2]').send_keys('whm13142392973')


# 拖拽验证码 先获取拖拽元素的位置
btn=web.find_element(By.XPATH,'//*[@id="nc_2_n1z"]')

ActionChains(web).drag_and_drop_by_offset(btn, 360, 0).perform()
# 拖拽完要等待加载
time.sleep(2)

# 点击登录
web.find_element(By.XPATH,'//*[@id="loginBg"]/div[1]/div/div[3]/div[4]/input').click()
time.sleep(5)



