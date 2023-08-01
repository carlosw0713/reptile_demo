# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 11:11
# @Author  : Carlos
import re
s = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋铁</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说八道</span></div>
"""

# (?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='(?P<class_name>.*?)'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>",re.S)  # re.S: 让.能匹配换行符

result = obj.finditer(s)#在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
for it in result:
    # print(it)
    print(f'姓名：{it.group("name")}')
    print(f'编号：{it.group("id")}')
    print(f'class编码：{it.group("class_name")}')