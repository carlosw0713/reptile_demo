import scrapy

# pip安装scrapy-splash库
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup


class SplashTestSpider(scrapy.Spider):
    name = 'splash_test'
    allowed_domains = ['guazi.com']
    start_urls = ['http://guazi.com/']

    # 直接访问
    def start_requests1(self):
        url='https://www.guazi.com/buy'

        yield SplashRequest(url=url,callback=self.parse,args={'wait':1}) # 等待一秒

    # 通过lua代码访问
    def start_requests(self):

        url = 'https://www.guazi.com/buy'

        lua='''
            function main(splash, args)
            assert (splash:go(args.url))
            assert (splash:wait(2))
            return splash:html()
            end
        '''

        # endpoint='execute',args={'lua_source':lua} 等价于  url + 'execute?lua_source=' + lua
        # yield SplashRequest(url=url,callback=self.parse,endpoint='execute',args={'lua_source':lua})

        splash_url = url + 'execute?lua_source=' + lua
        yield SplashRequest(url=splash_url,callback=self.parse)

    def parse(self, response):

        # print(response.text)

        soup = BeautifulSoup(str(response.text), "html.parser")
        pictures = soup.find_all('div', class_='car-card content-item')


        for picture in pictures:
            src = str(picture.find('img').get('data-src')).split('?')[0]  # 提取高清图
            name = picture.find('img').get('alt')
            print(src, name)

