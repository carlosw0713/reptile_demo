# -*- coding: utf-8 -*-
# @Time    : 2022/10/31 17:40
# @Author  : Carlos


class ProxyMiddleware(object):
    def process_request(self,request,spider):
        #普通代理
        # request.meta['proxy']='http://ip:port'
        # # 独享代理
        # request.meta['proxy']='http//user:passsword@ip:port'
        request.meta['proxy']='http://58.20.184.187:9091'