

import random

from fake_useragent import UserAgent
from scrapy import signals

from scrapy_Advanced.Middleware_use.Middleware_use.settings import PROXIES


# class ProxyMidde(object):
#     def process_request(self, request, spider):
#             proxy = random.choice(PROXIES)
#             request.meta['proxy']='http://'+proxy['ip']


class ProxyMidde(object):

    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        newip = random.choice(PROXIES)
        print('ip为：' + newip)
        request.meta["proxy"] =  newip  # 格式为 'http://121.13.252.62:41564'


"""设置随机UA"""
class UseAgentMiddleware(object):
    def __init__(self, user_agent=''):
        self.ua = UserAgent(verify_ssl=False)

    def process_request(self, request, spider):
        print("====UseAgentMiddleware process_request==")
        if self.ua:
            # 显示当前使用的useragent
            print("*************Current UserAgent:%s***************")
            custom_ua = self.ua.random
            print("custom_ua:", custom_ua)
            request.headers['User-Agent'] = custom_ua
