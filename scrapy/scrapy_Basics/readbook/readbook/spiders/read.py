import scrapy
from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from readbook.items import ReadbookItem


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['dushu.com']
    start_urls = ['https://dushu.com']

    # allow: 正则表达式或者正则表达式列表, 筛选出符合正则表达式的部分
    # follow: 布尔值, 它指定从response提取的链接是否需要跟进, 如果callback参数为none, follow默认设置为true, 否则false
    rules = (
        Rule(LinkExtractor(allow=r'/book/\d+\.html'),
             callback='parse_item',
             follow=False),
    )

    def parse_item(self, response):

        sel = Selector(response)

        # itmes = sel.xpath('/html/body/div[6]/div/div[2]/div[3]/div/a')

        # 传送第一页数据
        page1_url='https://www.dushu.com' + str(sel.xpath('/html/body/div[6]/div/div[2]/div[3]/div/a[1]/@href').get()).split('_')[0]+'.html'

        yield scrapy.Request(url=page1_url, callback=self.parse_item1)

        # for itme in itmes:

        # uri=itme.xpath('./@href').get()
        # url = 'https://www.dushu.com' + str(uri)

        for i in range(2,4):

            url=f'{page1_url.split(".html")[0]}_{i}.html'


            yield scrapy.Request(url=url, callback=self.parse_item1)


    def parse_item1(self, response):

        item = {}

        sel=Selector(response)

        title1=sel.xpath('/html/body/div[5]/div/a[3]/text()').get()
        title2 = sel.xpath('/html/body/div[5]/div/a[4]/text()').get()
        title3 = sel.xpath('/html/body/div[5]/div/a[5]/text()').get()

        if title2==None: #
            title3=''
            title2=''
        elif title3==None:
            title2 = '>' + str(title2)
            title3 = ''
        else:
            title3='>'+str(title3)

        title=f'{title1}{title2}{title3}'
        itmes=sel.xpath('/html/body/div[6]/div/div[2]/div[2]/ul/li/div')

        try:
            page=sel.xpath('/html/body/div[6]/div/div[2]/div[3]/div/span[1]/text()').get()
            page=int(page)
        except:
            page=sel.xpath('/html/body/div[6]/div/div[2]/div[3]/div/span[2]/text()').get()


        for itme in itmes:

            name=itme.xpath('./h3/a/@title').get()
            directory=f'{title}-第{page}页'
            name_list=f'{title}-第{page}页：{name}'

            # 注意页面 用了防盗链 直接打不开的
            src=itme.xpath('./div/a/img/@data-original').get()

            book = ReadbookItem(name=name,src=src,directory=directory)

            yield book

        return item
