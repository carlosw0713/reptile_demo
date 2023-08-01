import scrapy
from scrapy import Selector
from dandan.items import DandanItem


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'

    # 如果多页下载，一般要调整其页码 改为 仅含域名
    allowed_domains = ['search.dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=%C7%A9%C3%FB&act=input']

    page_url='http://search.dangdang.com/?key=%C7%A9%C3%FB&act=input'
    page = 2


    def parse(self, response):


        print('开始执行')

        sel = Selector(response)

        items = sel.xpath('//*[@id="component_59"]/li')

        a=0
        for item in items:




            name = item.xpath('./p[1]/a/@title').extract_first()
            price = item.xpath('./p[3]/span[@class="search_now_price"]/text()').extract_first()

            # 因为img[0]时 不存在 @data-original 所有 if img 为 false 输出else数据
            img = item.xpath('./a/img/@data-original').extract_first()
            if img:
                img = img
            else:
                img = item.xpath('./a/img/@src').extract_first()

            # 获取一个管道就交给管道 如果想使用管道就可以选择在settings 开启管道
            book = DandanItem(img=img, price=price, name=str(name).split('（')[0][0:10])

            # print(f"{img:25},{price:8},{str(name).split('（')[0]:10}")

            # yield 就是相当于return 获取一个对象就将对象传给管道
            yield book

        # 每一页的逻辑都是一样了  添加多页下载的方法
        # http://search.dangdang.com/?key=%C7%A9%C3%FB&act=input
        # http://search.dangdang.com/?key=%C7%A9%C3%FB&act=input&page_index=2
        # http://search.dangdang.com/?key=%C7%A9%C3%FB&act=input&page_index=3


        if self.page <= 10:
            self.page += 1
            url = f'{self.page_url}&page_index={self.page}'
            print(url)

            '''
            no more duplic ates will be shown (see DUPEFILTER_DEBUG to show all duplicates)
            原因:在爬虫出现了重复的链接,重复的请求,出现这个DEBUG或者是yield scrapy.Request(xxxurl,callback=self.xxxx)
            中有重复的请求其实scrapy自身是默认有过滤重复请求的让这个DEBUG不出现,可以有 dont_filter=True,在Request中添加可以解决

            '''
            # 注意parse不加()
            yield scrapy.Request(url=url, callback=self.parse,dont_filter=True)





