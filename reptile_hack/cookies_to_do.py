# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 17:01
# @Author  : Carlos

# 会话
import requests

# requests.session()自动处理cookies，做状态保持 下一次请求会带上前一次的cookie
session = requests.session()

data = {
    "loginName": "13142392973",
    "password": "whm51921"
}

# 1. 登录
url = "https://passport.17k.com/ck/user/login"
session.post(url, data=data)

a=session.cookies.get_dict()
print(a)

# 2. 拿书架上的数据
# 刚才的那个session中是有cookie的

resp = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
a=session.cookies.get_dict()
print(a)


result=resp.json()["data"][0]["bookName"]

# 获取cookie

print(f"requests.session接口返回信息:\n{result}\n")


# 3.直接在请求头加cookie

# cookie=session.get("https://user.17k.com/inc/fragment/user/new.html").cookies.get_dict()
# print(cookie)

cookie={"Cookie": "GUID=5f612249-0e41-4cc0-94f5-ad7edc11c8d6; Hm_lvt_9793f42b498361373512340937deb2a0=1663837239; sajssdk_2015_cross_new_user=1; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F02%252F82%252F12%252F98141282.jpg-88x88%253Fv%253D1663837677148%26id%3D98141282%26nickname%3D%25E4%25B9%25A6%25E5%258F%258BfQ02798dg%26e%3D1679389677%26s%3D4eed773f68dfcce7; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2298141282%22%2C%22%24device_id%22%3A%22183646d7738194-0657807d0f457d-26021c51-1049088-183646d7739450%22%2C%22props%22%3A%7B%7D%2C%22first_id%22%3A%225f612249-0e41-4cc0-94f5-ad7edc11c8d6%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1663839355"}

resp1=requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919",headers=cookie)

# result1=resp1.json()["data"][0]["bookName"]
result1=resp1.json()["data"][1]["bookName"]
print(f"请求头添加cookie接口返回信息:\n{result1}\n")


