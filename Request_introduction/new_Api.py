# -*- coding: utf-8 -*-
# @Time    : 2022/8/23 10:14
# @Author  : Carlos
# 导入 requests 包
import requests
#登录
data1={'username': 'byhy','password': '88888888'}
url1="http://127.0.0.1/api/mgr/signin"
header1={'Content-Type':'application/x-www-form-urlencoded',
         'Cookie':'sessionid=jtmaj7unp5ig4yzk1ucukzitlwjfsnig'}

# data:字典。对应的默认body格式Content-Type:application/x-www-form-urlencoded
# json:字典。对应的默认body格式Content-Type:application/json
login=requests.post(url1,data=data1)

# 打印json的响应结果
print(login.json())

# 获取cookie
result=login.cookies

# 将cookie转换为字典格式
Cookie=result.get_dict()
print(Cookie)


url = "http://127.0.0.1/api/mgr/customers"
data ={"action":"add_customer","data":{"name":"123456","phonenumber":"13334567754","address":"1234567890"}}
headers = {'Content-Type':'application/json; charset=UTF-8'}
r = requests.post(url=url,json=data,headers=headers,cookies=Cookie)

print(f"直接把字典传给 requests.post() 的 json 参数:{r.json()}\n"
      f"返回http状态码:{r.status_code}\n"
      f"反应状态的描述:{r.reason}\n"
      f"返回编码:{r.apparent_encoding}\n"
      f"返回Cookies:{r.cookies}")

