import scrapy


class CitySpider(scrapy.Spider):
    name = 'city'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
