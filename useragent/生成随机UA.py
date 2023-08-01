# -*- coding: utf-8 -*-
# @Time    : 2022/10/31 11:14
# @Author  : Carlos



# 第一步 github下载 fake_useragent.json文件  git clone https://github.com/Voccoo/useragent.git
# 第二步 将json文件存放在系统临时文件夹  路径：C:\Users\ADMINI~1\AppData\Local\Temp
# 第三步 如果下一次你们使用还是报错了，就要检查一下是不是已经将其清理掉了。

from fake_useragent import UserAgent
ua = UserAgent()
ua=UserAgent()

# print(ua.random)
for i in range(10):  # 随机生成十个User-Agent
    headers = {'User-Agent': ua.random}
    print(headers)

