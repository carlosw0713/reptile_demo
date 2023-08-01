# -*- coding: utf-8 -*-
# @Time    : 2022/9/19 16:21
# @Author  : Carlos
import asyncio
from time import time

import aiofiles
import aiohttp
import requests
from bs4 import BeautifulSoup
import time


# 1.创建连接获取源代码
def connet(url):

    # 添加代理  注意连接出问题时记得切换代理
    proxies = {
        "http": "58.20.184.187:9091"
    }

    header= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'}
    resp=requests.get(url,headers=header)
    resp.close()

    # 添加延迟
    time.sleep(0.1)

    # print("获取源代码成功")
    return resp.text


# 2.将源代码返回一个soup对象
def get_url(url,logs_download):

    # 获取 页面源代码
    resp=connet(url)

    # 获取 图片地址信息 soup
    page=BeautifulSoup(resp,"html.parser")

    wallpapers = page.find("section", class_="thumb-listing-page").find_all("a", attrs={"class": "preview"})

    wallpapers_list_url=[] # 建一个列表储存url

    # 记录下载总数的增加
    logs_download["total"] += len(wallpapers)

    # 通过遍历列表获取详细需要的信息
    for it in wallpapers:


        href = it.get('href')  # 获取图片网址的值的值
        # print(f"\n查看图片地址：{href}")

        try:

            # 获取图片下载地址信息
            soup2 = BeautifulSoup(connet(href),"html.parser")  # 赋值soup对象
            wallpaper = soup2.find("img", attrs={"id": "wallpaper"})
            src_url = wallpaper.get("src")  # 获取图片下载地址

            wallpapers_list_url.append(src_url) # 添加到列表

            print(f"\n图片地址: {href}")

        except:
            print(f"\n图片地址: {href}  美丽汤获取地址失败！！！")

            # 下载失败 成功数记录减1
            logs_download['fail'] += 1

    return wallpapers_list_url

async def download(url,logs_download):

    # 获取下载url地址合集
    wallpapers_list_url=get_url(url,logs_download)
    # print(f'下载地址列表：{wallpapers_list_url}')

    for it in wallpapers_list_url:

        # time.sleep(0.1) # 设置延迟

        img_name=str(it).split("-")[-1] # 给图片取名
        # print("successful!",img_name)

        # 获取下载图片链接
        # img_resp = requests.get(it)  # 下载图片

        # 下载到本地
        # with open("D:/Desktop/carlos的桌面壁纸/"+img_name,mode="wb") as f: # wb 用于用于非文本文件如图片，”wallpapers/“子目录，”+“命名
        #     f.write(img_resp.content) # 图片内容写入文件

        try:
            async with aiohttp.ClientSession() as session:  # requests
                async with session.get(it) as resp:  # resp = requests.get()

                    # with open("D:/Desktop/carlos的桌面壁纸/"+img_name, mode="wb") as f:  # 创建文件
                    #     f.write(await resp.content.read())  # 读取内容是异步的. 需要await挂起, resp.content.read() ==resp.content

                    # python 异步模式操作文件 aiofiles库
                    async with aiofiles.open("C:/Users/carlos/Desktop/carlos的桌面壁纸/赛博朋克/"+img_name, mode="wb") as f:
                        await f.write(await resp.content.read())  # 把小说内容写出

                    # print(f"图片名称：{img_name}  下载成功")

                    print(f"下载地址：{it}  下载成功!!!" )

                    # 下载成功 成功数记录加1
                    logs_download['successful'] += 1


        except:

            print(f"下载地址：{it}  下载失败！！！")

            # 下载失败 成功数记录减1
            logs_download['fail']+=1




async def run_task(type):

    tasks = []

    # 记录下载数 总数、成功、失败
    logs_download={'total':0,'successful':0,'fail':0}

    for i in range(2, 8):
        x_url = f'https://wallhaven.cc/{type}{i}'

        task = asyncio.create_task(download(x_url,logs_download))

        tasks.append(task)

    await asyncio.wait(tasks)

    print(f"总数:{logs_download['total']}  "
          f"下载成功：{logs_download['successful']}  "
          f"下载失败：{logs_download['fail']}")

if __name__ == '__main__':


    # asyncio.run(run_task())
    # RuntimeError: Event loop is closed解决办法 改为以下

    # # 随机3种类型！！！
    # list_wallpapers=["latest",'hot','toplist']
    # for type in list_wallpapers:
    #     # 拼接
    #     type=type+'?page='
    #     # 运行 协程对象
    #     loop = asyncio.get_event_loop()
    #     loop.run_until_complete(run_task(type))


    # 自主选择 输入关键词
    keyword=input("输入你的关键词")
    # 拼接
    type='search?q='+keyword+'&page='
    #运行协程对象
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_task(type))

    # 注意修改文件保存地址！！！！！