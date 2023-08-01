import json

import scrapy


class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    allowed_domains = ['fanyi.baidu.com']

    # post 请求 是需要参数的 所以satrt_url也没有意义 parse同样没有意义
    # start_urls = ['http://fanyi.baidu.com/']
    # def parse(self, response):
    #     pass

    def start_requests(self):
        x='girl'
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'}
        re_url = "https://fanyi.baidu.com/sug"
        re_data = {
            'kw': x
        }

        # 发送请求
        yield scrapy.FormRequest(url=re_url,formdata=re_data,callback=self.parse_result)


    def parse_result(self,response):

        obj=response.text

        # 转换格式！！！ \u65f6\u4e0d\u53e转中文
        obj1=obj.encode('utf-8').decode('unicode_escape')

        # 该方法 在python3.9后被弃用
        # obj2=json.loads(obj,encoding='utf-8')

        print(obj1)

