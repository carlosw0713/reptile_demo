import scrapy
from scrapy import Selector

from scrapy_Basics.begin_study.begin_study.items import BeginStudyItem


class DoubanSpider(scrapy.Spider):

    # 运行爬虫写的值 scrapy crawl douban
    name = 'douban'
    # 允许访问的域名
    allowed_domains = ['www.movie.douban.com']
    # 起始url地址
    start_urls = ['https://movie.douban.com/top250']

    # 执行 url后执行的脚本文件 response 先当与request 返回的对象
    def parse(self, response):

        '''
        scrapy的selector主要分为两类，第一类为xpath，第二类为css，
        同时夹杂着正则表达式等，xpath和css提取的原理都是一样的，只是
        表现形式不太一样。这里运行的代码都是在scrapy shell中运行的。
        '''
        response=Selector(response)

        print('开始学习scrapy框架')
        # print(f"设备名称：{response.headers}")
        # print(response.text) # 网页字符串
        # print(response.body) # 网页二进制数据

        names=response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        # print(names.extract())

        #get() 、getall() 是新版本的方法，extract() 、extract_first()是旧版本的方法
        #前者更好用，取不到就返回None，后者取不到就raise一个错误。
        for name in names:
            # //方式是定位整个页面文档中所有符合的元素，而 ./ 是在当前节点下面进行选择， .//方式也会将操作限制到当前节点
            data=name.xpath('./div/div[2]/div[1]/a/span[1]')

            movies_name1=data.extract_first() #extract()方法返回的是符合要求的所有的数据，存在一个列表里。
            movies_name2=data.get()

            movies=BeginStudyItem(movies_name1=movies_name1,movies_name2=movies_name2)

            yield movies


        # print(names.extract()[1]) #说明了extract_first()方法返回的hrefs 列表里的第一个数据。
        # print(names.getall()[1])



