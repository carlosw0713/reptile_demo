# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 15:12
# @Author  : Carlos
from multiprocessing import Process # 线程类


def func(name):
    for i in range(20):
        print(f"{name}-子进程：{i}")


if __name__=="__main__":

    # 运行子进程 直接调用函数
    p = Process(target=func,args=("王",))
    p.start()

    p1 = Process(target=func,args=("黄",))
    p1.start()
    for i in range(20):
        print("主进程")