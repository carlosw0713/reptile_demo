#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: carlos_mysql_use.py
@time: 2023/6/21  11:23
"""
import datetime

import pymysql

def connent_mysql(host, port, user, password, database):
    """
    连接数据库返回，游标得值
    :param host: 数据库主机名或 IP 地址
    :param port: 数据库端口号
    :param user: 数据库用户名
    :param password: 数据库密码
    :param database: 数据库名称
    :return: 查询结果的字典形式，其中键是字段名，值是字段值
    """
    # host, port, user, password, database='10.99.102.156', 3306, 'root', 'rootroot', 'eagoal-operation-uat'
    port =int(port)# 对port取整数
    # 连接数据库
    conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)

    return conn

def mysql_sel_dict(my_conn,sql):
    '''
    连接数据库查询单条数据，并将查询结果转化为字典形式
    :param my_conn: 数据库游标
    :param sql: 数据库查询语句
    :return: 查询结果的字典形式，其中键是字段名，值是字段值
    '''
    # 连接数据库
    conn=my_conn

    # 创建游标对象
    cursor = conn.cursor()

    # 执行查询语句
    cursor.execute(sql)

    # 获取查询结果
    result = cursor.fetchone()


    print sql

    # 将查询结果转化为字典形式
    if result:
        # 获取查询结果的字段列表
        fields = [i[0] for i in cursor.description]
        # 将字段和值一一对应，组成字典返回
        return dict(zip(fields, result))
    else:
        return None


def mysql_sel_data(my_conn,sql):
    '''
    连接数据库查询单条数据，并将查询结果转化为字典形式
    :param my_conn: 数据库游标
    :param sql: 数据库查询语句
    :return: 查询结果的字典形式，其中键是字段名，值是字段值
    '''
    # 连接数据库
    conn = my_conn

    # 创建游标对象
    cursor = conn.cursor()

    # 执行查询语句
    cursor.execute(sql)

    # 获取查询结果
    results = cursor.fetchall()


    # 将查询结果转化为列表返回
    results_list=[]
    for items in results:
        items=list(items)
        for itme in items:
            if isinstance(itme,str):
                item=itme.decode("utf-8")
        #         print (itme)
        # print (items)
        results_list.append(list(items))

    return  results_list




def execute_sql(my_conn, sql):
    '''
    连接数据库执行 SQL 语句
    :param my_conn: 数据库连接对象
    :param sql: 执行的 SQL 语句
    '''


    # 创建游标对象
    cursor = my_conn.cursor()

    # 执行 SQL 语句
    cursor.execute(sql)

    # 提交事务
    my_conn.commit()



def mysql_del(my_conn, SQL):
    '''
    连接数据库执行删除操作
    :param my_conn: 数据库连接对象
    :param SQL: 删除语句
    '''
    # 调用通用的 execute_sql 函数执行 SQL
    print SQL
    execute_sql(my_conn, SQL)

def mysql_update(my_conn, SQL):
    '''
    连接数据库执行更新操作
    :param my_conn: 数据库连接对象
    :param SQL: 更新语句
    '''
    # 调用通用的 execute_sql 函数执行 SQL
    execute_sql(my_conn, SQL)

def mysql_insert(my_conn, SQL):
    '''
    连接数据库执行插入操作
    :param my_conn: 数据库连接对象
    :param SQL: 插入语句
    '''
    # 调用通用的 execute_sql 函数执行 SQL
    execute_sql(my_conn, SQL)





if __name__=="__main__":

    myconn=connent_mysql('10.99.102.156', 3306, 'root', 'rootroot', 'eagoal-operation-uat')

    result = mysql_sel_dict(myconn, 'SELECT * FROM t_battery_picking_management WHERE id=176')

    # result =mysql_sel_data(myconn,'SELECT * FROM t_battery_picking_management WHERE id>176')

    print(result)

    # data = '\xe6\x8a\xa5\xe5\xba\x9f\xe5\x87\xba\xe5\xba\x93\xe7\x9a\x84\xe5\xb0\x8f\xe5\xbc\x9f'
    # decoded_data = data.decode('utf-8')
    # print(decoded_data)