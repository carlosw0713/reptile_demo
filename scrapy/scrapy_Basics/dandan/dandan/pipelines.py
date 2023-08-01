# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib.request

from itemadapter import ItemAdapter


class DandanPipeline:


    def open_spider(self,spider):

        self.f=open('books.json','w',encoding='utf8') # 查看json文件小技巧 Ctrl+Alt+L 一键调整排版

    # item 就是yield后面的book对象
    def process_item(self, item, spider):

        # write 必须是一个字符串 这种写法会导致每次写入都重复打开关闭文档
        # with open('books.json','a',encoding='utf8') as f
        #     f.write(str(item))

        self.f.write(str(item))

        return item

    def close_spider(self,spider):

        self.f.close()

# 多条管道同时开启
# 1. 照着写 定义管道类
# 2. 在settings中开启管道 也是造着写
class Dandan_download_img:

    # 必须要的方法
    def process_item(self, item, spider):

        url='http:'+item.get('img')
        filename='./qianming_img/'+item.get('name')+'.jpg'


        '''
        将URL表示的网络对象复制到本地文件。如果URL指向本地文件，则对象将不会被复制，除非提供文件名。
        urlretrieve(url, filename=None, reporthook=None, data=None)
        参数filename指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
        参数reporthook是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，我们可以利用这个回调函数来显示当前的下载进度。
        参数data指post导服务器的数据，该方法返回一个包含两个元素的(filename, headers)
        元组，filename
        表示保存到本地的路径，header表示服务器的响应头
        '''
        urllib.request.urlretrieve(url=url,filename=filename)

        return item