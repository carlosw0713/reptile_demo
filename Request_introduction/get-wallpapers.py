# -*- coding: utf-8 -*-
# @Time    : 2022/9/15 14:28
# @Author  : Carlos
import re

import requests


proxies = {
    "https": "https://218.60.8.83:3129"
}

url1 = "https://wallhaven.cc/hot?page=2"
header= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1345.33'}
resp=requests.get(url1,headers=header,proxies=proxies)

print(resp)
print(resp.text)
link=re.findall(r'href="(.*?)"',resp.text)
print(len(link),type(link),link)

#关闭接口
resp.close()

print("运行成功")