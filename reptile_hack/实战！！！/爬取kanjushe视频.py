# -*- coding: utf-8 -*-
# @Time    : 2022/10/9 15:09
# @Author  : Carlos

# 接口地址：https://cdn.zoubuting.com/20220929/eC0Fx2eR/index.m3u8
# frame框架内置地址：https://www.34kanju.xyz/11/?url=https://cdn.zoubuting.com/20220929/eC0Fx2eR/index.m3u8
# 1. 获取 frame里面的 视频源地址
import requests
from bs4 import BeautifulSoup
import re
import asyncio
import aiohttp
import aiofiles
from Crypto.Cipher import AES  # pycryptodome
import os

# 获取resp
def connet(url):

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
    }

    resp = requests.get(url, headers=header)

    resp.close()
    # print(resp.text)

    return  resp

# 1.通过 iframe框架的源代码 获取 下载 m3u8文件地址
def frame_url(url):

    page=connet(url).text
    # print(page)

    # (?P<???>) 生成迭代对象
    obj=re.compile(r'var now="(?P<url>.*?)";var',re.S)
    result=obj.finditer(page)
    for i in result:
        # print(i.group("url"))
        result1=i.group("url")


    return result1


# 2.根据视频源地址 获取文件
def get_m3u8(url):

    # 电影名称 正则抓取
    movies_name = re.findall(r"<script>var playn='(.*?)', playp", connet(url).text)[0]

    frist_mu38=f"{movies_name}--第一层mu38文件.txt"
    second_mu38=f"{movies_name}--第二层mu38文件.txt"

    # # 保存目标目录如果不存在则创建
    movies_name_dir=movies_name+"m3u8文件"
    if not os.path.exists(movies_name_dir):
        os.mkdir(movies_name_dir)


    # if not os.path.exists(movies_name/frist_mu38):
    #     os.mkdir(movies_name/frist_mu38)
    #
    # if not os.path.exists(movies_name/second_mu38):
    #     os.mkdir(movies_name/second_mu38)

    # 获取frame框架内的url
    fr_url1=frame_url(url)


    # 获取第一层的m3u8文件 写入到文本
    with open(f"{movies_name_dir}/{frist_mu38}",mode='wb') as f1:
        f1.write(connet(fr_url1).content)

    # 获取第一层m3u8文件 读取文本
    with open(f"{movies_name_dir}/{frist_mu38}",mode='r') as f2:
        for line in f2:

            if line.startswith("#"): # 去掉开头为#号的
                continue

            # line就是xxxxx.ts
            line = line.strip() # 去掉前后空格
            address1 =fr_url1.split(".com")[0]+".com"+line

        print(f"m3u8地址：{address1} 下载成功\n")

        # 获取第二层的m3u8文件 写入到文本
        with open(f"{movies_name_dir}/{second_mu38}", mode='wb') as f3:
            f3.write(connet(address1).content)

    return [fr_url1,movies_name_dir,second_mu38]

# 3.根据m3u8地址 下载源视频
async def download(movies_name,ts_url, name, session):

    movies_name_m3u8=f"{movies_name}_ts文件"

    # 文件下载地址
    # 保存目标目录如果不存在则创建
    if not os.path.exists(movies_name_m3u8):
        os.mkdir(movies_name_m3u8)

    async with session.get(ts_url) as resp:
        async with aiofiles.open(f"{movies_name_m3u8}/{name}", mode="wb") as f:
            await f.write(await resp.content.read())  # 把下载到的内容写入到文件中

    print(f"电影：{movies_name}--片段：{name}  下载完毕！")


# 4.运行下载任务
async def run_task(url):

    # 电影名称 正则抓取
    movies_name = re.findall(r"<script>var playn='(.*?)', playp", connet(url).text)[0]

    # 执行下载m3u8程序 并且 获取相关需要变量
    page=get_m3u8(url)

    second_mu38 = page[2]  # 存放m3u8文本
    movies_name_dir = page[1] # 存放m3u8文件
    fr_url=page[0]  # 下载m3u8地址的url

    # 创建运行的任务列表
    tasks = []

    '''
        ClientTimeout 可以支持的字段
        total 整个操作的最大秒数，包括建立连接、发送请求和读取响应。
        connect 如果超出池连接限制，则建立新连接或等待池中的空闲连接的最大秒数。
        sock_connect 为新连接连接到对等点的最大秒数，不是从池中给出的。
        sock_read 从对等点读取新数据部分之间允许的最大秒数。
    '''
    timeout=aiohttp.ClientTimeout(total=2500) #默认情况下，aiohttp使用总共300 秒（5 分钟）超时，这意味着整个操作应该在 5 分钟内完成。

    '''
       服务器可以限制可以从单个IP地址建立的并行TCP连接的数量。 默认情况下，
       aiohttp已经将并行连接的数量限制为100。 可以试着降低限制，看看是否能
       解决问题。 为此，您可以创建一个带有不同限值的自定义TCPConnector，并将其传递给ClientSession:
    '''
    connector = aiohttp.TCPConnector(limit=30)

    async with aiohttp.ClientSession(timeout=timeout,connector=connector) as session:  # 提前准备好session
        async with aiofiles.open(f"{movies_name_dir}/{second_mu38}", mode="r", encoding='utf-8') as f:

            name_number=1
            async for line in f:
                if line.startswith("#"):
                    continue

                # line就是xxxxx.ts
                line = line.strip()  # 去掉没用的空格和换行

                #文件名称name
                name=str(name_number)+"---"+str(line).split('/hls/')[1]
                name_number+=1

                # 因为有的m3u8文件中包含，有的不包含http 需要拼接
                if "http" not in line:

                    # 拼接真正的ts路径
                    ts_url =fr_url.split(".com")[0]+".com"+line

                else:
                    ts_url=line

                # print(ts_url)

                task = asyncio.create_task(download(movies_name,ts_url, name, session))  # 创建任务
                tasks.append(task)

            await asyncio.wait(tasks)  # 等待任务结束


# 4.合并m3u8的视频  还有问题！！！
def merge_src():

    movies_name = re.findall(r"<script>var playn='(.*?)', playp", connet(url).text)[0]
    movies_name_m3u8 = f"{movies_name}_ts文件"
    second_mu38 = f"{movies_name}--第二层mu38文件.txt"
    movies_name_dir = movies_name + "m3u8文件"

    cmd = f"copy /b {movies_name_m3u8}\* {movies_name}.mp4"
    print(f'cmd 命令  {cmd}')

    # 代码有问题！！！！！！ 未修改好 暂时建议直接用cmd命令

    # python(/)写路径  与  系统(\)写路径  格式不一样
    # os.system(f"copy /b {movies_name_m3u8}/* {movies_name}.mp4")
    # print("搞定!!!!!!!!!")



if __name__ == '__main__':

    # 百度秒播类型地址
    url='http://www.34kanju.com/play/38989-0-0.html'

    # 生成储存m3u8接口地址
    # frame_url(url)

    # 生成文件储存m3u8文件信息
    # get_m3u8(url)

    # # 运行并下载视频文件
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(run_task(url))

    merge_src()

