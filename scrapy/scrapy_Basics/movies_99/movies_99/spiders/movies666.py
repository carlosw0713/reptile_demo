import scrapy
from scrapy import Selector

from movies_99.items import Movies99Item


class Movies666Spider(scrapy.Spider):
    name = 'movies666'
    allowed_domains = ['ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    def parse(self, response):

       sel = Selector(response)

       itmes=sel.xpath('//table//td[2]//a[2]')


       for itme in itmes:



           src=itme.xpath('./@href').extract_first()

           name=itme.xpath('./text()').extract_first()

           url='https://www.ygdy8.net/'+str(src)

           yield scrapy.Request(url=url,callback=self.src_prase,meta={'name':name})



    def src_prase(self, response):

        sel=Selector(response)

        img=sel.xpath('//*[@id="Zoom"]//img/@src').get()

        # 接收请求meta参数的值 注意meta不能用调度器Selector
        name=response.meta['name']

        movie=Movies99Item(img=img,name=name)

        # 返回管道
        yield movie
