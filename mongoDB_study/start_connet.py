# -*- coding: utf-8 -*-
# @Time    : 2022/11/7 14:25
# @Author  : Carlos

# 安装该库后，这里才能导入
import pymongo
from pymongo import MongoClient

# 连接服务器
conn = MongoClient(host='localhost',port=27017,username='mongo',password='123456')

# 连接数据库
db = conn.Carlos_test

# 查看集合名称
db_list=db.list_collection_names()

# 创建(获取)集合
collection = db['information']

#  插入数据
list=[
    {"name": "abc1","age": 19,"gender": 1,"adress": "北京","isDelete": 0},
    {"name": "b2","age": 18,"gender": 1,"adress": "湖南","isDelete": 0},
    {"name": "carlos","age": 21,"gender": 1,"adress": "上海","isDelete": 0}
      ]

# collection.insert_many(list)

# 查询所有  正常打印都是<pymongo.cursor.Cursor object at 0x000001D38A346CC0>
res_all=collection.find()
for i in res_all:
    print(i)


# 条件查询
res=collection.find({"name": "abc1"})
print(res)



# 模糊查询 {"name": "/a/"} name中包含a的值  {"name": "/^a/"}name 中以a开头的字

# 统计个数
# res_count = collection.find().count()

# 升序排序
res_sort = collection.find().sort("age")

# 降序排序
res_Descending = collection.find().sort("age",pymongo.DESCENDING)

# 分页查询
res = collection.find().limit(3).skip(5)

# 断开连接【最后一步】
conn.close()
print('运行完成')