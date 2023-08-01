# -*- coding: utf-8 -*-
# @Time    : 2022/9/30 9:56
# @Author  : Carlos

# 百度小说 都市之帝尊归来
# 第一步：获取小说章节名、小说章节url
import asyncio

import aiohttp
import requests
import requests

# requests.get() 同步请求 ---转换为 aiohttp 异步请求
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import aiofiles

import json

url1='http://baidu8.cread.com/book/805001003/3.html?nrhz=4a3929508b876c34e2bbd5685a5ac211'

# uri参数


async def aiodownload(cid, b_id, title):
    data = {
        "book_id":b_id,
        "cid":f"{b_id}|{cid}",
        "need_bookinfo":1
    }
    data = json.dumps(data)
    url = f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    # print(url)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # print(resp.url)
            dic = await resp.json()

            async with aiofiles.open("小说/"+title, mode="w", encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])  # 把小说内容写出
                print(f'小说章节：{title}     下载成功')

            # print(dic['data']['novel']['content'])




async def get_url_task(book_id):

    tasks=[]

    data={
        'book_id': book_id
    }
    data=json.dumps(data)

    url =f"https://dushu.baidu.com/api/pc/getCatalog?data={data}"
    resp=requests.get(url)
    dic=resp.json()
    resp.close()
    # print(dic['data']['novel']['items'])

    x=1
    for items in dic['data']['novel']['items']:

        # 设置爬取章节次数
        x+=1
        if x==50:
            break

        cid=items["cid"]
        price_status=items["price_status"]
        title=items["title"]

        # print(f'小说章节：{title}')
        # print(f'cid编号：{cid}')

        task=asyncio.create_task(aiodownload(cid, book_id, title))
        tasks.append(task)
    await asyncio.wait(tasks)




if __name__ == '__main__':


    # RuntimeError: Event loop is closed解决办法 改为以下
    # asyncio.run(get_url_task())

    # url 百度小说 。
    'https: // dushu.baidu.com / pc / detail?gid = 4306170312'
    loop=asyncio.get_event_loop()
    loop.run_until_complete(get_url_task(4306170312))



print("运行成功")
