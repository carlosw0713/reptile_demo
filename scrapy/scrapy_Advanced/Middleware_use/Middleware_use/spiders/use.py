import scrapy


class UseSpider(scrapy.Spider):
    name = 'use'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):

        # print(response.meta)



        for i in range(5):

            url='http://httpbin.org/get'

            yield scrapy.Request(url=url,callback=self.use)

    def use(self,response):
        print(response.text)



