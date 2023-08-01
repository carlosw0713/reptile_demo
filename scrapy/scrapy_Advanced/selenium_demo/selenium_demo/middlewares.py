# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


from selenium.webdriver import Edge
from scrapy.http import HtmlResponse

class SeleniumMiddleware(object):


    def __init__(self,):
        pass

    # 一定要用 process_request 否者调用不了
    def process_request(self,request,spider):

        # 调用spider对象
        edge=spider.edge

        url=request.url
        edge.get(url)
        # time.sleep(2)
        html=edge.page_source

        return HtmlResponse(url=url,body=html,request=request,encoding='utf-8')

