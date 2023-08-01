# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter


class RoomWebPipeline:

    def process_item(self, item, spider):
        return item


class room_web_mongodb:

    def open_spider(self,spider):
        self.conn = pymongo.MongoClient(host='localhost',
                           port=27017,
                           username='mongo',
                           password='123456')

        # 连接数据库
        self.db = self.conn.Carlos_test

        # 创建(获取)集合
        self.collection = self.db['lianjia_room_web']



    def process_item(self, item, spider):


        # 直接添加item不过要先转换未字典格式
        self.collection.insert_one(dict(item))


        return item

    def close_spider(self, spider):
        self.conn.close()

        pass