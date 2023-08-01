import scrapy


class City1Spider(scrapy.Spider):
    name = 'city1'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
