# -*- coding: utf-8 -*-
# @Time    : 2022/9/27 17:40
# @Author  : Carlos

# 1. 找到未加密的参数                       # window.arsea(参数, xxxx,xxx,xxx)
# 2. 想办法把参数进行加密(必须参考网易的逻辑), params  => encText, encSecKey => encSecKey
# 3. 请求到网易. 拿到评论信息

# 需要安装pycrypto:   pip install pycrypto
from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json

# 请求方式是POST
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1325905146",
    "threadId": "R_SO_4_1325905146"
}

# 服务于d的
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
e = "010001"
i = "d5bpgMn9byrHNtAh"  # 手动固定的. -> 人家函数中是随机的


def get_encSecKey():  # 由于i是固定的. 那么encSecText就是固定的.  c()函数的结果就是固定的
    return "1b5c4ad466aabcfb713940efed0c99a1030bce2456462c73d8383c60e751b069c24f82e60386186d4413e9d7f7a9c7cf89fb06e40e52f28b84b8786b476738a12b81ac60a3ff70e00b085c886a6600c012b61dbf418af84eb0be5b735988addafbd7221903c44d027b2696f1cd50c49917e515398bcc6080233c71142d226ebb"


# 把参数进行加密
def get_params(data):  # 默认这里接收到的是字符串
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second  # 返回的就是params


# 转化成16的倍数, 位下方的加密算法服务
def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


# 加密过程
def enc_params(data, key):
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode('utf-8'), mode=AES.MODE_CBC)  # 创建加密器
    bs = aes.encrypt(data.encode("utf-8"))  # 加密, 加密的内容的长度必须是16的倍数
    return str(b64encode(bs), "utf-8")  # 转化成字符串返回,


# 处理加密过程
"""
    function a(a = 16) {  # 随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)  # 循环16次
            e = Math.random() * b.length,  # 随机数 1.2345
            e = Math.floor(e),  # 取整  1 
            c += b.charAt(e);  # 去字符串中的xxx位置 b
        return c
    }
    function b(a, b) {  # a是要加密的内容, 
        var c = CryptoJS.enc.Utf8.parse(b) #  # b是秘钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)  # e是数据
          , f = CryptoJS.AES.encrypt(e, c, {  # c 加密的秘钥
            iv: d,  # 偏移量
            mode: CryptoJS.mode.CBC  # 模式: cbc
        });
        return f.toString()
    }
    function c(a, b, c) {   # c里面不产生随机数
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {  d: 数据,   e: 010001, f: 很长, g: 0CoJUm6Qyw8W8jud
        var h = {}  # 空对象
          , i = a(16);  # i就是一个16位的随机值, 把i设置成定值 
        h.encText = b(d, g)  # g秘钥
        h.encText = b(h.encText, i)  # 返回的就是params  i也是秘钥
        h.encSecKey = c(i, e, f)  # 得到的就是encSecKey, e和f是定死的 ,如果此时我把i固定, 得到的key一定是固定的
        return h
    }

    两次加密: 
    数据+g => b => 第一次加密+i => b = params
"""

# url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_475479888",
    "threadId": "R_SO_4_475479888"
}

body={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()
}

# 发送请求. 得到评论结果
resp = requests.post(url, data=body)

print(resp.json())

respdata=resp.json()

for it in respdata['data']['comments']:
    content=it['content']
    print(content)
