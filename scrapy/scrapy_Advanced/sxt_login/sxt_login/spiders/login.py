import re

import requests
import scrapy

from fake_useragent import UserAgent
from parsel import Selector

ua = UserAgent(use_cache_server=False)

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['www.bjsxt.com']
    # start_urls = ['https://www.bjsxt.com'] #start_requests是不已start_urls登录


    #通过表单登录
    def start_requests1(self):


        url='https://www.bjsxt.com/api.php'

        header={
            'Referer':'https://www.bjsxt.com/login.html',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent':f'{ua.random}'
        }


        data={
            'op':'user',
            'phone':'13142392973',
            'pass':'whm51921',
            'status':'checkpass',
        }

        yield scrapy.FormRequest(url=url,formdata=data,headers=header,callback=self.parse)

    # 通过cookies登录 在控制台中输入如下代码：console.log(document.cookie) 获取cookies (不一定有用)
    # 建议直接拿登录请求的响应cookies， 有多个set cookie 就合并一起。
    def start_requests(self):

        cookie_str = 'PHPSESSID=updmsm122q4h4fgc7vmkg6aj04; path=/; wordpress_3d1a75cf63f9491f67067e16eba72d33=13142392973%7C1668760698%7CidjXs0QqGxo4n6RBYLspgSZfmzjCDarqajHwox2PF8C%7C24df4175fa7287d693cbc536dac23bd634c04a9f98253bf34ba95435981549c2; expires=Fri, 18-Nov-2022 20:38:18 GMT; Max-Age=1252800; path=/wp-content/plugins; wordpress_3d1a75cf63f9491f67067e16eba72d33=13142392973%7C1668760698%7CidjXs0QqGxo4n6RBYLspgSZfmzjCDarqajHwox2PF8C%7C24df4175fa7287d693cbc536dac23bd634c04a9f98253bf34ba95435981549c2; expires=Fri, 18-Nov-2022 20:38:18 GMT; Max-Age=1252800; path=/; wordpress_logged_in_3d1a75cf63f9491f67067e16eba72d33=13142392973|1668760698|idjXs0QqGxo4n6RBYLspgSZfmzjCDarqajHwox2PF8C|8e4662e530b3db297dab03d57f994bf3e6e4ab5c25447d4c77c693d1b1214d46; expires=Fri, 18-Nov-2022 20:38:18 GMT; Max-Age=1252800 '

        cookie = {}

        for i in cookie_str.split(';'):
            key, values = i.split('=', 1)  # 以空格为分隔符，分隔成两部分
            cookie[key] = values

        url = 'https://www.bjsxt.com/download.html'

        yield scrapy.Request(url=url,cookies=cookie, callback=self.login_after)

    def parse(self, response):

        print(response.text)

        yield scrapy.Request('https://www.bjsxt.com/download.html',callback=self.login_after)

    def login_after(self,response):

        print(response.text)
        try:
            # 判断登录成功
            tishi=re.findall(r'action=logout">(.*?)</a></div>',response.text)


            if tishi[0] =='安全退出':
                print(f'登录成功')
            else:
                print(f'登录失败')
        except:
            print('登录失败')






