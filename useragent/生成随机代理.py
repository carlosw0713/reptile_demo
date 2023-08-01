# -*- coding: utf-8 -*-
# @Time    : 2022/10/31 15:17
# @Author  : Carlos
# -*- coding: utf-8 -*-
# @Time    : 2022/9/27 17:32
# @Author  : Carlos

# 原理. 通过第三方的一个机器去发送请求
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

import aiofiles
import aiohttp
import requests
from bs4 import BeautifulSoup
from lxml import etree
from fake_useragent import UserAgent


def get_porxy(url_page,session):

    url = url_page

    ua = UserAgent(use_cache_server=False)
    header = {'User-Agent': ua.random} # 生成随机UA
    # header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'}

    resp=session.get(url=url,headers=header)

    # print(resp.url,resp.status_code)

    return resp.text

async def get_porxy_url(resp,list):

    connet_html = etree.HTML(resp)
    itmes = connet_html.xpath('//*[@id="list"]/table/tbody/tr')

    for itme in itmes:
        IP = itme.xpath('./td[1]/text()')
        # print(type(IP))
        PORT = itme.xpath('./td[2]/text()')
        porxy_url = f'http://{IP[0]}:{PORT[0]}'


        try:
            await url_test(porxy_url)

            if porxy_url not in list:
                # print(porxy_url)
                list.append(porxy_url)

        except Exception as e:
            # print(f'{porxy_url}:{e}')
            pass

    async with aiofiles.open('proxy', mode="w", encoding="utf-8") as f:
        await f.write(str(list))

async def url_test(url_porxy):
    url = 'http://httpbin.org/get'
    # url='http://www.baidu.com'
    # proxies = {
    #     "http": f'{url_porxy}'
    # }
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'}
    # resp = requests.get(url=url, headers=header)

    # async with aiohttp.ClientSession().get(url=url, headers=header) as resp:
    # print(resp.text)
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), trust_env=True) as session:
        async with session.get(url=url, headers=header, proxy=url_porxy, timeout=10) as response:
            pass

            # print(response.text) # 错误打印aiohttp文本方式

            page_text = await response.text() # 正确打印方式
            print(page_text)
            # print('success')


async def task():
    tasks = []

    session = requests.session()
    list = [] # 存放可以调用的代理
    for i in range(1, 10):
        url_page = f'https://www.kuaidaili.com/free/inha/{i}/'
        await asyncio.sleep(3) # 同时间访问 无法获取cookies
        resp = get_porxy(url_page, session)
        task = asyncio.create_task(get_porxy_url(resp,list))
        tasks.append(task)
    await asyncio.wait(tasks)


if __name__ == '__main__':

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(task())
    # print('获取代理完成')

    ua = UserAgent(use_cache_server=False)
    header = {'User-Agent': ua.random}  # 生成随机UA

    porxy={
        'http':'61.216.185.88:60808'
    }

    resp=requests.get('http://httpbin.org/get',headers=header,proxies=porxy)
    print(resp.text)

