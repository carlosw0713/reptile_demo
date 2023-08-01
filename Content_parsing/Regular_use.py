# -*- coding: utf-8 -*-
# @Time    : 2022/8/25 9:56
# @Author  : Carlos

import re

data='''001-苹果,5元 是绿色色色色色色色的
520橙子,是橙色色的
666香蕉,8元 是黄色的
oo7乌鸦,4dollars do是黑色的
99猴子,abcd'''

# . 表示要匹配除了 “换行符” 之外的任何 “单个” 字符。 . 的左右
regular1=re.findall(r',.',data)
regular2=re.findall(r"绿.",data)

# * 表示匹配前面的子表达式任意次，包括0次。所以整个表达式的意思就是在逗号后面的 所有字符，包括逗号。
regular3=re.findall(r",.*",data)
regular4=re.findall(r".色*",data)

# 你要从文本中，选择每行逗号后面的1个字符，也包括逗号本身。表示匹配1次或0次
regular5=re.findall(r",.?",data)

# 色{min,max}表示匹配字符”色“，至少min次，至多max次。
regular6=re.findall(r".色{2,4}",data)

file=open("time.log","r")
connet=file.read()
regular7=re.findall(".*> buy",connet)

'''反斜杠后面接一些字符，表示匹配 某种类型 的一个字符。
比如：
\d 匹配0-9之间任意一个数字字符，等价于表达式 [0-9]
\D 匹配任意一个不是0-9之间的数字字符，等价于表达式 [^0-9]
\s 匹配任意一个空白字符，包括 空格、tab、换行符等，等价于表达式 [\t\n\r\f\v]
\S 匹配任意一个非空白字符，等价于表达式 [^ \t\n\r\f\v]
\w 匹配任意一个文字字符，包括大小写字母、数字、下划线，等价于表达式 [a-zA-Z0-9_]
缺省情况也包括 Unicode文字字符，如果指定 ASCII 码标记，则只包括ASCII字母
\W 匹配任意一个非文字字符，等价于表达式 [^a-zA-Z0-9_]'''
regular8=re.findall(".*\d",data)
regular9=re.findall(".\w",data)

# [abc] 可以匹配 a, b, 或者 c 里面的任意"一个字符"。等价于 [a-c] 。
# [色是4,] 匹配 色 是 4 , 里面"任意一个字符"
# 如果在方括号中使用 ^ ， 表示 非 方括号里面的字符集合。
regular10=re.findall("[色是4,]",data)
regular11=re.findall("[^色]",data)

'''  ^ 表示匹配文本的 开头 位置。
正则表达式可以设定 单行模式 和 多行模式
如果是 单行模式 ，表示匹配 整个文本 的开头位置。
如果是 多行模式 ，表示匹配 文本每行 的开头位置。'''
regular12=re.findall("^\d+",data)

# 竖线 "|" 表示 匹配 其中之一 。
regular13=re.findall(".*绿|诚|猴",data)

# 把匹配值当作一个组，只展示（.*?）匹配值
regular14=re.findall("(.*?)> buy",connet)

#正则表达式里面的 split 方法
names = '关羽; 张飞, 赵云,马超, 黄忠  李逵'
namelist = re.split(r'[;,\s]\s*', names)

#正则表达式中的 sub 替换 用法
list1='1你是美女 我是帅哥 3你是弟弟 '
list2=re.sub("\d.","垃圾黄康",list1)

# 匹配字符串 match
# 替换函数，参数是 Match对象



print("运行成功")