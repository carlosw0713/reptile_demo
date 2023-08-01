# -*- coding: utf-8 -*-
# @Time    : 2022/11/8 10:19
# @Author  : Carlos
import urllib

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url='https://www.guazi.com/buy'

# 此接口用于获取JS渲染的页面 render.html获取HTML代码  render.png 渲染网页截图
way='render.html'
# way='render.png'

wait=1 # 加载时间
splash_url=f'http://localhost:8050/{way}?url={url}&wait={wait}&width=1000&height=700'

header={'User-Agent':UserAgent().random}

resp=requests.get(url=splash_url,headers=header)
# resp.encoding='utf-8'
# print(resp.text)

resp.close()

# 解析下载
soup = BeautifulSoup(resp.text,"html.parser")
pictures=soup.find_all('div',class_='car-card content-item')

for picture in pictures:

    src=str(picture.find('img').get('data-src')).split('?')[0] # 提取高清图
    name=picture.find('img').get('alt')
    print(src, name)

    # 下载 方式
    filename = 'picture1/' + name + '.jpg'
    urllib.request.urlretrieve(url=src, filename=filename)
    break