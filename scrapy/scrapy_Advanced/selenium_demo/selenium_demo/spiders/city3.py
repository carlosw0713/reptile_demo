import scrapy


class City3Spider(scrapy.Spider):
    name = 'city3'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
