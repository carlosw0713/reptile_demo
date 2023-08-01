# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 14:32
# @Author  : Carlos
import time
from threading import Thread # 线程类


def func(name):
    for i in range(200):
        # time.sleep(0.00000001)
        print(f"{name}子进程1")

def run():
    for i in range(200):
        print("子进程2")


if __name__=="__main__":

    # 运行子进程 直接调用函数 # args=给方法传参，必须是元组形式
    t1=Thread(target=func,args=("垃圾hk",))
    t1.start()

    t2 = Thread(target=run)
    t2.start()


    for i in range(20):
        print("主进程")