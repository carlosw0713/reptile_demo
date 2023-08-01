# -*- coding: utf-8 -*-
# @Time    : 2022/10/11 14:12
# @Author  : Carlos
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()

# # 切换浏览器窗口
# driver.get("https://www.lagou.com/")
# time.sleep(0.5)
#
# driver.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a').click()
# driver.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("软件测试")
# driver.find_element(By.XPATH,'//*[@id="search_button"]').click()
# time.sleep(0.5)
#
# # 打开一个新窗口  职位详情
# driver.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
#
# # windows为所有窗口的列表，浏览器每打开一个窗口会在列表尾部添加一个窗口对象，所以index=-1就是切换至新打开的窗口
# driver.switch_to.window(driver.window_handles[-1])
# # 打印职位信息
# print(driver.find_element(By.XPATH,'//*[@id="job_detail"]/dd[2]/div').text)
#
# # 关闭当前窗口
# driver.close()
#
# # 回到初始窗口 打印公司信息
# driver.switch_to.window(driver.window_handles[0])
# print(driver.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[1]/div[1]').text.strip())

# 切换frame窗口

driver.get("http://www.34kanju.com/play/38989-0-0.html")
time.sleep(0.5)

# 切换frame    switch_to.frame(reference)  reference是传入的参数，
# 用来定位frame，可以传入索引(0,1,2) id、name、index以及selenium的WebElement对象

# 切换第一层 frame
driver.switch_to.frame('cciframe')
address1=driver.find_element(By.XPATH,'/html')
print(f"输入第一层的网址：{address1.get_attribute('xmlns')}")

# 切换第二层 *[@id="player"]的frame
driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="player"]/iframe'))
# # 获取第二层全部资源 driver.page_source
print(f"获取第二层全部资源：{driver.page_source}")
url=re.findall(r' url: "(.*?)"',driver.page_source)
print(f"第二层的网址{url}")


# 从frame2再切回frame1，这里selenium给我们提供了一个方法能够从子frame切回到父frame，而不用我们切回主文档再切进来。
driver.switch_to.parent_frame()  # 切换上一级 如果当前已是主文档，则无效果

# 通过 索引的方法进入 frame第一层的 frame[0]内
driver.switch_to.frame(0)
print(f"输入第二层frame(0)网址：{driver.page_source}")

# 切到frame中之后，我们便不能继续操作主文档的元素，这时如果想操作主文档内容，则需切回主文档。
driver.switch_to.default_content()
print(f"电影名称{driver.find_element(By.XPATH,'/html/body/div[2]').text}") #切换主文档


