# -*- coding: utf-8 -*-
# @Time    : 2022/10/27 16:42
# @Author  : Carlos
import asyncio
import datetime
import time

import requests
from concurrent.futures import ThreadPoolExecutor

def DownLoad_OnePage():
    for i in range(5):
        time.sleep(2) # 表示遇到读写时阻塞等待时间
        print('开始执行多线程')

async def get():

    await asyncio.sleep(2) # 表示遇到读写时阻塞等待时间
    print('开始执行异步协程')

async def get_url_task():
    tasks=[]

    for x in range(5):
        for i in range(5):
            task=asyncio.create_task(get())
            tasks.append(task)

    await asyncio.wait(tasks)


if __name__=='__main__':
    b = datetime.datetime.now()
    with ThreadPoolExecutor(50) as T:
        for i in range(5):
            T.submit(DownLoad_OnePage)
    print('多线程爬取完毕')


    a=datetime.datetime.now()
    print(b - a)

    c=datetime.datetime.now()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_url_task())
    d=datetime.datetime.now()
    print(d-c)
    print('异步协程爬取完毕')

