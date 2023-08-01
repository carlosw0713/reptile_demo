# -*- coding: utf-8 -*-
# @Time    : 2022/9/20 10:26
# @Author  : Carlos
import requests
from lxml import etree


# 生成一个通过url获取源代码的方法
def connet(url):
    url1=url
    header= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'}
    resp=requests.get(url1,headers=header)
    resp.close()
    # print(resp.text)
    return resp.text

# 建立获取XPATH
# url="https://shanghai.zbj.com/search/service/?l=0&kw=3D%E5%8A%A8%E7%94%BB&r=1"
url='https://shanghai.zbj.com/search/service/?l=0&kw=%E6%BC%AB%E7%94%BB&r=2' # 漫画
connet_html=etree.HTML(connet(url))


# 获取相对信息
html_list_num=connet_html.xpath("//div[@class='search-result-list']")

for html_list in html_list_num:

    Vendor_name=html_list.xpath("//div[@class='shop-info text-overflow-line']/text()")
    Good_comments=html_list.xpath("//div[@class='el-tooltip comment item']/span[2]/text()")
    sales=html_list.xpath("//div[@class='el-tooltip sale item']/span[2]/text()")
    price=html_list.xpath("//div[@class='bot-content']/div/span/text()")
    # print(type(price))

'''特殊用法（字符串全为中文时）
	1.背景，因为中文补全的空格格式是英文格式，比中文格式要窄
	2.采用 
tp='{0:^5}\t{1:{2}^15}\t{2:{2}^15}'
tp.format(m[i],q[i],h[i],chr(12288))
chr(12288)表示一个中文占位长度
^表示居中对齐
{2}表示此时以第3个变量为基准
	3.但是如果字符串同时出现中文英文呢数字时 不能使用 '''
tp='{0:{3}<20}{1:{3}<10}\t{2:10}' #“\t”是指制表符，代表着四个空格，也就是一个tab。
for i in range(len(price)):

    list_zbj2=tp.format(str(Vendor_name[i]),str(Good_comments[i]),str(sales[i]),chr(12288))

    list_zbj=f"店铺名:{str(Vendor_name[i]):22s}好评:{str(Good_comments[i]):5s}销售量:{str(sales[i]):5s},价格:{str(price[i]):4s}"
    # print(list_zbj.format(chr(12288)))

    print(list_zbj2)
    # with open("zbj_3D动漫信息", mode="w",encoding="utf8") as f:
    #     f.write(list_zbj)
print("运行成功")