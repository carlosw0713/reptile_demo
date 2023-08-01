# -*- coding: utf-8 -*-
# @Time    : 2022/9/29 11:03
# @Author  : Carlos
import re
from concurrent.futures import ThreadPoolExecutor

import requests

# requests.get() 同步请求 ---转换为 aiohttp 异步请求
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import aiofiles

def get_soup(get_resp):
    page = BeautifulSoup(get_resp, "html.parser")
    # print("获取美丽汤对象成功")
    # wallpapers = page.find("div", class_="container").find_all("a", attrs={"class": "pic-list"})
    wallpapers = page.find("div", class_="pic-list").find_all("a")

    # 获取网页下载地址：
    wallpapers_url_list=[]
    for it in wallpapers:
        wallpapers_link=it.get("href")

        # 拼接网址
        x=str(wallpapers_link).rsplit("/",1)[1]
        y=x.split(".")[0]
        wallpapers_url=f"http://pic.bizhi360.com/bbpic/{y[-2:]}/{y}.jpg"
        wallpapers_url_list.append(wallpapers_url)

        # print(wallpapers_url)
    # print(wallpapers_url_list[1:])
    return wallpapers_url_list[1:]


def get_url(url):

    # async with aiohttp.ClientSession() as session:  # requests
    #     async with session.get(url) as resp:  # resp = requests.get()
    try:
        with requests.get(url) as resp:
            return resp

    except:
        print(f"该{url}没有下载地址")


async def download(url):

    # 返回的结果 - 通过resp调用
    resp1 = get_url(url)

    # 返回url下载地址列表 -通过美丽汤获取
    download_url = get_soup(resp1.text)

    for it in download_url:
        imgname=it.rsplit("/",1)[1]

        # resp=requests.get(it)
        # print(f"图片名称：{imgname}   下载成功")
        # with open("wallpaper/"+imgname,mode="wb") as f: #wallpaper/表示下级
        #     f.write(resp.content)

        try:
            async with aiohttp.ClientSession() as session:  # requests
                async with session.get(it) as resp:  # resp = requests.get()

                    with open("D:/Desktop/carlos的桌面壁纸/"+imgname, mode="wb") as f:  # 创建文件
                        f.write(await resp.content.read())  # 读取内容是异步的. 需要await挂起, resp.content.read() ==resp.content

                    # python 异步模式操作文件 aiofiles库 ！！！！ 代码还有问题
                    # async with aiofiles.open("D:/Desktop/carlos的桌面壁纸/"+imgname, mode="wb") as fp:
                    #     await fp.write(resp.content)

                    # print(f"图片名称：{imgname}  下载成功")
                    print(f"下载地址：{it}  下载成功" )
        except:

            print(f"下载地址：{it}  下载失败！！！")


async def main():

    tasks = []

    for i in range(2,20):

        if i == 0:
            url = "http://www.bizhi360.com/meinv/"
        else:
            url = f"http://www.bizhi360.com/meinv/list_{i + 1}.html"

        # 3.8之前会自动生成为Tasks对象
        # python3.8改版后，不支持一次性把协程对象都放到task里，需要自己创建task对象

        task=asyncio.create_task(download(url))

        tasks.append(task)

    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())