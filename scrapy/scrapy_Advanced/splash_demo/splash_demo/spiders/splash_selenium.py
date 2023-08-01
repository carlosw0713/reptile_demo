import scrapy


class SplashSeleniumSpider(scrapy.Spider):
    name = 'splash_selenium'
    allowed_domains = ['www.guazi.com']
    start_urls = ['https://www.guazi.com/buy']

    def parse(self, response):
        pass
