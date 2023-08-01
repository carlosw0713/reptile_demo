import scrapy
from bs4 import BeautifulSoup
from scrapy import signals
from selenium.webdriver import Edge


class SeleniumTestSpider(scrapy.Spider):
    name = 'selenium_test'
    allowed_domains = ['www.guazi.com']
    start_urls = ['https://www.guazi.com/buy']


    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):

        #'SeleniumTestSpider' # 父类class名称
        spider = super(SeleniumTestSpider, cls).from_crawler(crawler, *args, **kwargs)

        # 创建webdriver对象 用户中间件调度
        spider.edge=Edge()

        # signals.spider_closed 当莫信号成立时 关闭spider
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)

        return spider


    def spider_closed(self, spider, reason):

        spider.edge.quit()
        print('爬虫结束')

    def parse(self, response):
        # print(response.url)


        soup = BeautifulSoup(str(response.text), "html.parser")
        pictures = soup.find_all('div', class_='car-card content-item')

        for picture in pictures:
            src = str(picture.find('img').get('data-src')).split('?')[0]  # 提取高清图
            name = picture.find('img').get('alt')
            print(src, name)



