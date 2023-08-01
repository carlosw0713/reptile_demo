# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Movies99Item(scrapy.Item):

    name=scrapy.Field()

    img=scrapy.Field()


