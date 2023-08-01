# -*- coding: utf-8 -*-
# @Time    : 2022/9/15 15:21
# @Author  : Carlos
import re
import requests
from selenium import webdriver
import time
#注意声明 BY
from selenium.webdriver.common.by import By



# x=input("请输入你需要翻译的的单词或者汉字\n")
x="god"


print("********通过接口爬************")
header= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'}
re_url= "https://fanyi.baidu.com/sug"
re_data = {
    'kw':x
}
resp=requests.post(re_url,data=re_data)
print(resp.json())#将服务器的内容转为json
#关闭接口
resp.close()

print('************selenium获取源代码************')

# br=webdriver.Edge()
# ht_url="https://fanyi.baidu.com/#en/zh/"+x
# br.get(ht_url)
# # 设置强制等待
# time.sleep(2)
# NR=br.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[1]/div[3]/div/div[2]/div/div[1]')
#
# print(NR.text)
# # br.close()