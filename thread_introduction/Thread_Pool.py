# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 15:55
# @Author  : Carlos

# 线程池: 一次性开辟一些线程. 我们用户直接给线程池子提交任务. 线程任务的调度交给线程池来完成
import time
from concurrent.futures import ThreadPoolExecutor
from pythonProject.MOS平台测试脚本.APP签到sql_语句.mysql_how_to_do import mysql_carlos

def fn(name):
    for i in range(10):
        print(name, i)

if __name__ == '__main__':

    # 创建线程池
    start1_time=time.time()
    with ThreadPoolExecutor(50) as t:
        for i in range(200):
            t.submit(mysql_carlos.get_time, time="now",count=100,x=1)
    end1_time=time.time()

    # 等待线程池中的任务全部执行完毕. 才继续执行(守护)
    print("线程池内容执行完毕")

    start2_time = time.time()
    for i in range(200):
        mysql_carlos.get_time("now",100,1)
    end2_time = time.time()

    print(f"线程池：执行时间{-start1_time + end1_time}")
    print(f"主进程：执行时间{-start2_time + end2_time}")



