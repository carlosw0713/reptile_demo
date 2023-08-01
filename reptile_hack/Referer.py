# -*- coding: utf-8 -*-
# @Time    : 2022/9/27 13:34
# @Author  : Carlos

# 学习爬网站视频
# Referer防盗链 Referer是HTTP请求header
import re
from concurrent.futures.thread import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup
from lxml import etree

# 思路解析：1.获取video_id 2.通过接口信息获取伪url 3.替换拼接

# 建立方法
# 建立连接获取网页源代码
def connet(url,Referfer):

    header= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
        # Referer防盗链 Referer是HTTP请求header 的一部分，当浏览器（或者模拟浏览器行为）向web服务器发送请求的时候，头信息里有包含Referer
        'Referer': Referfer
            }
    resp=requests.get(url,headers=header)
    resp.close()
    # print(resp.text)
    return resp


# 将源代码返回一个soup对象
def get_soup(get_resp):
    page=BeautifulSoup(get_resp,"html.parser")
    # print("获取美丽汤对象成功")
    return page


# 通过video_id 获取视频下载地址
def get_video_url(video_id):
    # url 与防盗链
    url2 = f"https://www.pearvideo.com/videoStatus.jsp?contId={video_id}&mrd=0.03489233977787043"
    Referfer2 = f"https://www.pearvideo.com/video_{video_id}"  # 防盗链

    # 获取接口关键信息
    resp = connet(url2, Referfer2).json()
    srcUrl = resp["videoInfo"]["videos"]["srcUrl"]
    systemTime = resp["systemTime"]

    # print(resp)
    print(f"伪url：{srcUrl}")
    print(f"systemTime：{systemTime}")

    # 拼接，打印出url
    video_url = str(srcUrl).replace(systemTime, f"cont-{video_id}")
    print(f"视频下载链接：{video_url}\n")

# 通过网页源代码 获取get_video_id_list
def get_video_id_list(resp):

    soup1 = get_soup(resp)  # 赋值soup对象
    result1 = soup1.find("div", class_="search-result-wrap fix-center").find_all("div", class_="have-result")

    # 循环获取videoid 打印vedeo_id_list
    for it in result1:
        x = it("img")
        # print(x)
        # 正则提取
        vedeo_id_list = re.findall(r"cont-(.*?)-", str(x))
        print(f"获取的video_id_list:{vedeo_id_list}\n")

    return vedeo_id_list


# 整合
with ThreadPoolExecutor(50) as t:


    for i in range(0,201,10):

        # 根据接口不同替换防盗链信息
        if i ==0:
            url1=f"https://www.pearvideo.com/search.jsp?start=0&k=%E7%96%AB%E6%83%85"
            Referfer1='https: // www.pearvideo.com'
        else:
            url1 = f"https://www.pearvideo.com/search.jsp?start={i}&k=%E7%96%AB%E6%83%85"
            Referfer1 = "https://www.pearvideo.com/search.jsp?start=0&k=%E7%96%AB%E6%83%85"

        resp=connet(url1, Referfer1).text

        # 循环获取video_url
        for it in get_video_id_list(resp):

           t.submit(get_video_url,video_id=it)









