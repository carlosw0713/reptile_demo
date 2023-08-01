# -*- coding: utf-8 -*-
# @Time    : 2022/11/8 10:19
# @Author  : Carlos

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url='https://www.guazi.com/buy'


'''return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har(),
  }
'''

lua_script='''
function main(splash, args)
  splash:go('{}')
  splash:wait(1)
  return splash:html()
end
'''.format(url)
# print(lua_script)


wait=1 # 加载时间
splash_url=f'http://localhost:8050/execute?lua_source={lua_script}'

header={'User-Agent':UserAgent().random}

resp=requests.get(url=splash_url,headers=header)
resp.encoding='utf-8'
# print(resp.text)

resp.close()

soup = BeautifulSoup(resp.text,"html.parser")
pictures=soup.find_all('div',class_='car-card content-item')

for picture in pictures:

    src=str(picture.find('img').get('data-src')).split('?')[0] # 提取高清图
    name=picture.find('img').get('alt')
    print(src, name)

    # 下载
    with requests.get(url=src) as resp_down:
        with open ('picture2/'+name+'.jpg',mode='wb') as file: # 输入的名字要以jpg结尾
            file.write(resp_down.content)
    break


