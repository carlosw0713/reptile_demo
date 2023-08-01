# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 11:41
# @Author  : Carlos
import re
import requests

# 新建一个文件
file=open(
        "douban_Top250.txt",#必需，文件路径（相对或者绝对路径）
      mode="a", # "w"从开头开始编辑，即原有内容会被删除,"a"新的内容将会被写入到已有内容之后
      encoding="utf8",# 打开方式，一般使用utf8
      errors=None, # 报错级别
      newline=None, # 区分换行符
      closefd=True, # 传入的file参数类型
      opener=None #设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。
          )

# 设置四个参数，依次添加。
def add_file(name,year,score,num):
    file.write(
       f"电影时间：{it.group('year').strip():<5},"
       f"电影评分：{it.group('score'):<4},"
       f"电影评论：{it.group('num'):<10},"
       f"电影名称：{it.group('name').strip():<10}\n"
        )

# 创建一个获取网页源代码的网址
def connet_resp(re_url):
    resp=requests.get(url=re_url,headers=header) # 获取网页源代码
    resp.close()  # 断开连接
    # print(resp.text) #输出网页源代码

    # 正则将将关键点做为一个迭代器。
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                     r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                     r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                     r'<span>(?P<num>.*?人评价)</span>', re.S)

    result = obj.finditer(resp.text)  # 将obj的迭代器返回成一个列表

    return result #返回正则后的信息

for pages in range(0,251,25):

    # 请求体，设备信息。
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33"
    }

    if pages==0:
        re_url = "https://movie.douban.com/top250"
    else:
        re_url=f"https://movie.douban.com/top250?start={pages}&filter="
        print(re_url)

    for it in connet_resp(re_url): # 调用 connet_resp返回的正则表达式迭代器列表

        # print(it.group()) #输出迭代器内容

        print(
           f"电影时间：{it.group('year').strip():<5},"
           f"电影评分：{it.group('score'):<4},"
           f"电影评论：{it.group('num'):<10},"
           f"电影名称：{it.group('name').strip():<10}",
            end="\n"
            )

        # 调用add——file方法，添加相关信息
        add_file(it.group('name'),it.group('year').strip(),it.group('score'),it.group('num'))

# 关闭文件
file.close()
