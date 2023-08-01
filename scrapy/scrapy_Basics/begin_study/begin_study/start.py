# -*- coding: utf-8 -*-
# @Time    : 2022/11/23 10:01
# @Author  : Carlos

from scrapy.cmdline import execute

# 执行代码
# execute('scrapy carwl douban '.split())

# 保存json格式数据 -o 后面是导出文件名，-t 后面是导出类型 其余的同理
execute('scrapy crawl douban -o douban.json -t json  '.split())
execute('scrapy crawl douban -o douban.csv -t csv  '.split())
execute('scrapy crawl douban -o douban.xml -t xml  '.split())
