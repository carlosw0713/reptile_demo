import scrapy

from scrapy_Advanced.room_web.room_web.items import RoomWebItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['sh.lianjia.com']
    start_urls = ['http://sh.lianjia.com/']


    def start_requests(self):
        for page in range(1,5):

            url=f'https://sh.lianjia.com/zufang/jiading/pg{page}rp3rp4rp2rp1/#contentList'

            yield scrapy.Request(url=url,callback=self.parse)


    def parse(self,response):

        itmes=response.xpath('//*[@id="content"]/div[1]/div[1]/div')

        for itme in itmes:

            price_time=itme.xpath('./div/span[@class="content__list--item-price"]/text()').get()
            price_money=itme.xpath('./div/span[@class="content__list--item-price"]/em/text()').get()
            price=f'{price_money}{price_time}'

            locations_elements=itme.xpath('./div/p[@class="content__list--item--des"]/a')
            locations=[]
            for location_elements in locations_elements:
                location=location_elements.xpath('./text()').get()
                locations.append(str(location))

            huose_type=[]
            for i in range(5,8):
                huose_type1=itme.xpath(f'./div/p[@class="content__list--item--des"]/text()[{i}]').get()
                huose_type.append(str(huose_type1).strip())

            src='https://sh.lianjia.com'+itme.xpath('./a/@href').get()

            room= RoomWebItem(locations=locations,huose_type=huose_type,price=price, src=src)

            # print(price, locations, huose_type, src)

            yield room





