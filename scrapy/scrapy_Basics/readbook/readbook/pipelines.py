# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
from pymongo import MongoClient
import pymongo

class ReadbookPipeline:
    def process_item(self, item, spider):
        return item

# 加载setting文件
from scrapy.utils.project import get_project_settings

class roodbook_mysql:

    def open_spider(self,spider):
        '''
        DB_HOST='localhost'
        DB_POST=3306
        DB_USER='root'
        DB_PASSWORD='123456'
        DB_NAME='Carlos1'
        DB_CHARSET='utf-8'
        '''
        setting=get_project_settings()
        self.host=setting['DB_HOST']
        self.port=setting['DB_POST']
        self.user=setting['DB_USER']
        self.password=setting['DB_PASSWORD']
        self.name=setting['DB_NAME']
        self.charset=setting['DB_CHARSET']

        self.coonnect()

    def coonnect(self):
        self.coon=pymysql.Connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )

        # 获取游标
        self.cursor = self.coon.cursor()


    def process_item(self, item, spider):

        name=item.get('name')
        src=item.get('src')
        directory=item['directory']

        sql=f'INSERT INTO readbook(name,src,directory)VALUES("{name}","{src}","{directory}")'
        self.cursor.execute(sql)
        self.coon.commit()

        return item

    def close_spider(self,spider):


        self.coon.close()

        pass

class roodbook_mongodb:

    def open_spider(self,spider):
        self.conn = pymongo.MongoClient(host='localhost',
                           port=27017,
                           username='mongo',
                           password='123456')

        # 连接数据库
        self.db = self.conn.Carlos_test

        # 创建(获取)集合
        self.collection = self.db['readbook']



    def process_item(self, item, spider):
        name = item.get('name')
        src = item.get('src')
        directory = item['directory']

        # 直接添加item不过要先转换未字典格式
        self.collection.insert_one(dict(item))

        # self.collection.insert_one({'dir':directory,'name':name,'src':src})

        return item

    def close_spider(self, spider):
        self.conn.close()

        pass