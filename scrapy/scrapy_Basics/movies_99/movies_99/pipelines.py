# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib.request

from itemadapter import ItemAdapter


class Movies99Pipeline:

    # 必须要的方法
    def process_item(self, item, spider):

        url = item.get('img')
        name=item.get('name')


        filename = './movies_img/' + item.get('name') + '.jpg'
        # filename = './movies_img/' + item.get('name')

        urllib.request.urlretrieve(url=url, filename=filename)



        return item
