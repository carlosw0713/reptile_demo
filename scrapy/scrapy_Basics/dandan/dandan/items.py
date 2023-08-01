# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DandanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 下载内容的迭代器
    img = scrapy.Field()

    price=scrapy.Field()

    name=scrapy.Field()
