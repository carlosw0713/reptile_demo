# -*- coding: utf-8 -*-
# @Time    : 2022/9/15 17:02
# @Author  : Carlos
import re

import requests
from selenium import webdriver
import time
#注意声明 BY
from selenium.webdriver.common.by import By

print("\n**************通过request爬取电影内容信息*************************")

# url1="https://movie.douban.com/j/chart/top_list"
#
# header={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
# }
#
# # 创建总的电影code
# movies_num=[]
#
# # 获取前300的电影接口信息
# for start_count in range(0,21,20):
#
#     # 将请求url的参数封装
#     body_data={
#     'type': '24',
#     'interval_id': '100:90',
#     'action': '',
#     'start': start_count,
#     'limit': '20'
#     }
#     # 发送请求
#     resp=requests.get(url=url1,headers=header,params=body_data)
#     # movie_link = re.findall(r"re")
#     movie_link_code = re.findall(r'subject\\/(.*?)\\/', resp.text)
#     movies_num+=movie_link_code
#
# print(f'总的movie_ode,数量：{len(movies_num)}  {movies_num}')

# print(f'文本信息：  {resp.text}')
# print(f"请求头:  {resp.request.headers}")
# print(f'请求url:  {resp.request.url}')

#关闭接口
# resp.close()

print(f'\n************selenium爬取电影名称************')

br=webdriver.Edge()
ht_url="https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7%E7%89%87&type=24&interval_id=100:90&action="
br.get(ht_url)

# 电影总名
movies_name=[]

for i in range(10):
    # 滑动到底部
    js = "var q=document.documentElement.scrollTop=100000"
    br.execute_script(js)
    time.sleep(1)
    NR = br.find_elements(By.XPATH, '//*[@class="movie-name-text"]')
    for i in NR:
        if i.text !="":
            movies_name.append(i.text)

print(f"总数：{len(movies_name)}\n电影名：{movies_name}")

# # 滑动到顶部
# js = "var q=document.documentElement.scrollTop=0"
# br.execute_script(js)


