# -*- coding: utf-8 -*-
# @Time    : 2022/9/27 17:32
# @Author  : Carlos

# 原理. 通过第三方的一个机器去发送请求
import asyncio
from concurrent.futures import ThreadPoolExecutor

import aiohttp
import requests
from bs4 import BeautifulSoup
from lxml import etree


def get_porxy(url_page):

    url=url_page
    header= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'}
    resp=requests.get(url=url,headers=header)

    return  resp.text

async def get_porxy_url(resp):
    connet_html = etree.HTML(resp)
    itmes = connet_html.xpath('//*[@id="list"]/table/tbody/tr')

    for itme in itmes:
        IP=itme.xpath('./td[1]/text()')
        # print(type(IP))
        PORT=itme.xpath('./td[2]/text()')
        porxy_url=f'http://{IP[0]}:{PORT[0]}'

        # await url_test(porxy_url)

        try:
            await url_test(porxy_url)


        except Exception as e:
            print(f'{porxy_url}  {e}')
            pass

async def url_test(url_porxy):
    url='http://httpbin.org/get'
    proxies = {
        "http": f'{url_porxy}'
    }
    header= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'}

    # try:
    #     resp = requests.get(url=url, headers=header,proxies=proxies)
    #     print(resp.text)
    # except:
    #     pass

    # async with aiohttp.ClientSession().get(url=url, headers=header) as resp:
    # print(resp.text)
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), trust_env=True) as session:

        async with session.get(url=url, headers=header,proxy=url_porxy, timeout=10) as response:

            # print(response.text) # 错误打印aiohttp文本方式

            page_text = await response.text() # 正确打印方式
            print('\n'+page_text)
            print(url_porxy, '  支持代理')
            # print('success'+'\n')

async def task():
    tasks=[]
    for i in range(1,5):
        url_page=f'https://www.kuaidaili.com/free/inha/{i}/'
        resp=get_porxy(url_page)
        task = asyncio.create_task(get_porxy_url(resp))
        tasks.append(task)
    await asyncio.wait(tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task())

