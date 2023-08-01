# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 15:52
# @Author  : Carlos

import mysql.connector

import pymysql

# 数据库连接
mydb = pymysql.connect\
    (
  host="127.0.0.1", # 数据库主机地址
  port=3306,
  user="root",    # 数据库用户名
  passwd="123456",# 数据库密码
  db="sys",
  charset="utf8"  # cursorclass=pymysql.cursors.DictCursor
    )



cursor=mydb.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# 使用预处理语句创建表
sql2= """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT, 
         SEX CHAR(1),
         INCOME FLOAT )"""
# cursor.execute(sql2)

# SQL 插入语句
sql1 = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   # cursor.execute(sql1)
   # 提交到数据库执行
   mydb.commit()
except:
   # 如果发生错误则回滚
   mydb.rollback()

# SQL 查询语句
sql = "SELECT * FROM sys_config where value=56"
# 执行SQL语句
select_list=cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
print(f"查询结果:{select_list}\n获取所有记录列表:{results}")


# 关闭数据库连接
mydb.close()

