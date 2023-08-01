# -*- coding: utf-8 -*-
# @Time    : 2022/10/11 11:14
# @Author  : Carlos
import time
import webbrowser


from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Edge()

driver.get("https://www.lagou.com/")
time.sleep(0.5)
driver.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a').click()
driver.maximize_window() # 页面遮住了元素，得最大化才能找到 才能点击
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("软件测试")
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="search_button"]').click()

time.sleep(1)
list_xpath=driver.find_elements(By.XPATH,'//*[@id="jobList"]/div[1]/div/div[1]')

# 建议暂时不要用xapth去匹配，因为匹配出来的值全是默认第一个的值
for i in list_xpath:
    # print(i.text)
    position=i.find_element(By.TAG_NAME,'a').text
    # experience=
    # price=
    # loctio
    company=i.find_element(By.XPATH,'//*[@class="company__2EsC8"]').text
    people_umber=i.find_element(By.CLASS_NAME,'company__2EsC8').text
    print(f'  \n{people_umber}')