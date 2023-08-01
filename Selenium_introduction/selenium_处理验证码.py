# -*- coding: utf-8 -*-
# @Time    : 2022/10/11 18:08
# @Author  : Carlos

# 1.图像识别
# 2.选择互联网的图像识别软件 代码等
import time

from selenium.webdriver.common.by import By

from chaojiying_Python.chaojiying import Chaojiying_Client

from selenium.webdriver import Edge
web = Edge()

web.get("http://www.chaojiying.com/user/login/")

# 处理验证码
img = web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png  # 这个是获取屏幕截图，保存的是二进制数据
chaojiying = Chaojiying_Client('13142392973', '13142392973', '914467')

# img 为二进制图片
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']

# 向页面中填入用户名, 密码, 验证码
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("13142392973")
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("13142392973")
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)

time.sleep(5)
# 点击登录
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()


time.sleep(2)
web.close()